'''
CarbonEmission.py
- A class to handle the carbon emission data

AnnualTemperature.py
- A class to handle the global annual temperature data

Database.py
- Stores the Carbon Emission and Annual Temperature data
- Internally the database uses NamedTuples

Interface.py
- Read and store the data
- Uses data processing functions in the Process.py
- Outputs the processed data

Process.py
- Design a set of classes/functions process the data
- Store the data in the DataBased for both the CO2 and Temperature data
- NOTE: the + or - on the data indicate the temperature difference from the base average between 1960 and
        1990. The base average is not given. For example, +0.5 is the amount above the average and -0.5 is
        the amount below average.


'''
class InterfaceTemp:
    def __init__(self, filename):
        lines = []
        medians = []

        with open(filename, "r") as a_file:
            for line in a_file:
                stripped_line = line.strip()
                lines.append(stripped_line)

        # THIS PART OF THE PROGRAM WILL BE THE DATA PARSER

        lines = lines[5:-1]

        originalYears = []
        for curr in lines:
            originalYears.append(curr[15:19])

            medians_line = curr[28:]
            medians_carrot_index = medians_line.index('<')
            medians_line = curr[28:28 + medians_carrot_index]
            medians.append(medians_line)

        #string to float (to remove num nuder 1959
        years = list(map(int, originalYears))
        medians = list(map(float, medians))
        newYears = []
        newMedian = []
        for num in years:
            if num >= int(1959):
                newYears.append(num)

        for x in range(len(medians)):
            if x >= 109 and x <= 169:
                newMedian.append(medians[x])

        self.newYears = newYears
        self.newMedian = newMedian

    def temperature_years(self):
        return self.newYears

    def temperature_medians(self):
        return self.newMedian
#-----------------------------------------------------------------------------

class InterfaceCO2:

    def __init__(self, filename):

        CO2lines = []
        CO2years = []
        CO2month = []
        CO2average = []

        with open(filename, "r") as a_file:
            for line in a_file:
                stripped_line = line.strip()
                CO2lines.append(stripped_line)

        CO2lines = CO2lines[4:-1]

        for curr in CO2lines:
            CO2years.append(curr[15:19])

            CO2month_line = curr[28:]
            CO2month_carrot_index = CO2month_line.index('<')
            CO2month_line = curr[28:28 + CO2month_carrot_index]
            CO2month.append(CO2month_line)

            CO2average_line = curr[28 + CO2month_carrot_index + 26:]
            CO2average_carrot_index = CO2average_line.index('<')
            CO2average_line = curr[28 + CO2month_carrot_index + 26:28 + CO2month_carrot_index + 26 + 
                                                                   CO2average_carrot_index]
            CO2average.append(CO2average_line)

        #string to float number
        CO2average = list(map(float, CO2average))

        # new data values list -> organized
        CO2newYear = []
        CO2newAverage = []

        # Take one one year value from the list
        for x in CO2years:
            if x not in CO2newYear:
                CO2newYear.append(x)
        if CO2newYear[-1] == '2019':
            CO2newYear.pop()
        CO2newYear = list(map(int, CO2newYear))

        #finding yearly average
        CO2average = [CO2average[i:i + 12] for i in range(0, len(CO2average), 12)]

        #Divide all values by 12 (nasted list)
        for x in range(len(CO2average)-1):
            sum = 0
            for y in range(12):
                sum = sum + CO2average[x][y]
            CO2newAverage.append(sum)

        for x in range(len(CO2newAverage)):
            CO2newAverage[x] = round(CO2newAverage[x]/12, 2)

        self.CO2newYear = CO2newYear
        self.CO2newAverage = CO2newAverage

    def CO2_years(self):
        return self.CO2newYear

    def CO2_average(self):
        return self.CO2newAverage

#==================================================================================

class Database:
    def __init__(self, CO2years,average, tempYears,  median):
        self.CO2years = CO2years
        self.tempYears = tempYears
        self.average = average
        self.median = median

    def CO2dict(self):
        CO2dict = {
            'CO2_years': self.CO2years,
            'CO2_average': self.average,
            }
        return CO2dict

    def tempDict(self):
        tempDict = {
            'temperature_years': self.tempYears,
            'temperature_median': self.median,
            }
        return tempDict

class Parser:
    def __init__(self,average, median):
        self.average = list(map(float, average))
        self.median = list(map(float, median))
        self.averageMedian = []

    def average_times_median(self, average, median):
        average = list(map(float, average))
        median = list(map(float, median))
        self.averageMedian = [x * y for x, y in zip(average, median)]
        for i in range(len(self.averageMedian)):
            self.averageMedian[i] = round(self.averageMedian[i], 4)
        return self.averageMedian

    def squared_average(self):
        self.average = [i * i for i in self.average]
        for i in range(len(self.average)):
            self.average[i] = round(self.average[i], 2)
        return self.average

    def squared_median(self):
        self.median = [i * i for i in self.median]
        for i in range(len(self.median)):
            self.median[i] = round(self.median[i], 6)
        return self.median

class Output:
    def __init__(self, co2_filename, temperature_filename):
        self.co2 = InterfaceCO2(co2_filename)
        self.temp = InterfaceTemp(temperature_filename)

    def process(self):
        co2years = self.co2.CO2_years()
        co2average = self.co2.CO2_average()
        tempYears = self.temp.temperature_years()
        tempMedian = self.temp.temperature_medians()
        database = Database(co2years,co2average,tempYears,tempMedian)
        CO2_data = database.CO2dict()
        temp_data = database.tempDict()
        parser = Parser(co2average, tempMedian)
        squrt_av = parser.squared_average()
        squrt_med = parser.squared_median()
        av_med = parser.average_times_median(co2average, tempMedian)
        xy = sum(av_med)
        x = sum(co2average)
        y = sum(tempMedian)
        x2 = sum(squrt_av)
        xouter2 = x**2
        n = 60

        b = (60 * xy - (x * y)) / ((60 * x2) - xouter2)

        return b

def main():
    myOutput = Output('Co2.html', 'Temperature.html')
    result = myOutput.process()
    print(result)

main()