
class Student:
    __indexNo = ''
    __firstname = ''
    __lastname = ''
    __yearOfExam = ''
    __school_code = ''

    def __init__(self,indexNo,firstName,lastName,yearOfExam,school_code):
        self.indexNo = indexNo
        self.firstName = firstName
        self.lastName = lastName
        self.yearOfExam = yearOfExam
        self.school_code = school_code


    #
    #  PROPERTIES
    #
    @property
    def indexNo(self):
        return self.__indexNo

    @indexNo.setter
    def indexNo(self, new_indexno):
        self.__indexNo = new_indexno

    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, new_firstName):
        self.__firstName = new_firstName

    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, new_lastName):
        self.__lastName = new_lastName

    @property
    def yearOfExam(self):
        return self.__yearOfExam

    @yearOfExam.setter
    def yearOfExam(self, new_yearOfExam):
        self.__yearOfExam = new_yearOfExam

    @property
    def school_code(self):
        return self.__school_code

    @school_code.setter
    def school_code(self, new_school_code):
        self.__school_code = new_school_code

    def getStudentResults(self):
        results = Marks.getMarks(self,self.school_code, self.yearOfExam, 5)
        print(results)
        print('marks for {} {} {} {} {}'.format(self.indexNo,self.lastName, self.firstName,self.yearOfExam, self.school_code))
        print('Maths = {}'.format(results[0]))
        print('English = {}'.format(results[1]))
        print('Kiswahili = {}'.format(results[2]))
        print('Science = {}'.format(results[3]))
        print('Social Studies = {}'.format(results[4]))


    def getSchoolResults(self):

        results = Marks.getMarks(self, self.school_code, self.yearOfExam)










class Marks(Student):

    def __init__(self):
        super(). __init__(self)

        self.mathsScore = 0
        self.englishScore = 0
        self.kiswahiliScore = 0
        self.scienceScore = 0
        self.socialScore = 0

    def getMarks(self, indexNo, Year):

        self.index = indexNo
        self.year = Year
        if indexNo == '508101121001' and Year == '2016' :
            self.mathsScore = 90
            self.kiswahiliScore = 85
            self.englishScore = 87
            self.scienceScore = 96
            self.socialScore = 78
            result = []
            result = [self.mathsScore, self.englishScore,self.kiswahiliScore,self.scienceScore, self.socialScore]
            return result
        else:
            return []

    def getMarks(self,school_code, Year, number):

        self.school_code = school_code
        self.year = Year

        if school_code == '508121' and Year == '2016':
            self.mathsScore = 90
            self.kiswahiliScore = 85
            self.englishScore = 87
            self.scienceScore = 96
            self.socialScore = 78
            result = []
            result = [self.mathsScore, self.englishScore, self.kiswahiliScore, self.scienceScore, self.socialScore]
            return result
        else:
            return []


p = Student('508101121001','Denis','deng','2016','508121')

p.getStudentResults()














