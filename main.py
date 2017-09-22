import csv


class DataInfo:
    name = None
    email = None
    mobile = None
    university = None
    major = None

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setMobile(self, mobile):
        self.mobile = mobile

    def getMobile(self):
        return self.mobile

    def setUniversity(self, university):
        self.university = university

    def getUniversity(self):
        return self.university

    def setMajor(self, major):
        self.major = major

    def getMajor(self):
        return self.major


print('Please enter data')

nb = None
dataInfo = [DataInfo()]

while (nb != 'stop'):
    data1 = DataInfo()
    nb = input('Enter name: ')
    data1.setName(nb)
    nb = input('Enter email: ')
    data1.setEmail(nb)
    nb = input('Enter mobile: ')
    data1.setMobile(nb)
    nb = input('Enter university: ')
    data1.setUniversity(nb)
    nb = input('Enter major: ')
    data1.setMajor(nb)
    dataInfo.append(data1)
    nb = input('If you want to exit enter stop, if not enter anything to add new data: ')

with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Email', 'Mobile', 'University', 'Major']
    writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=fieldnames)
    writer.writeheader()

    for data2 in dataInfo:
        writer.writerow({'Name': data2.getName(), 'Email': data2.getEmail(), 'Mobile': data2.getMobile(),
                         'University': data2.getUniversity(), 'Major': data2.getMajor()})

print('Done')
