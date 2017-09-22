import csv

class DataInfo:
    name = None
    email = None
    mobile = None
    university = None
    major = None

    def __init__(self):
        name = ""
        email = ""
        mobile = ""
        university = ""
        major = ""



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


print('Please enter data, to stop enter stop')

nb = None
dataInfo = [DataInfo()]

while (nb != 'stop'):
    data1 = DataInfo()
    nb = input('Enter name: ')
    if (nb == 'stop'):
        nb = ''
        data1.setMajor(nb)
        dataInfo.append(data1)
        break

    data1.setName(nb)
    nb = input('Enter email: ')
    if (nb == 'stop'):
        nb = ''
        data1.setMajor(nb)
        dataInfo.append(data1)
        break
    data1.setEmail(nb)
    nb = input('Enter mobile: ')
    if (nb == 'stop'):
        nb = ''
        data1.setMajor(nb)
        dataInfo.append(data1)
        break
    data1.setMobile(nb)
    nb = input('Enter university: ')
    if (nb == 'stop'):
        nb = ''
        data1.setMajor(nb)
        dataInfo.append(data1)
        break
    data1.setUniversity(nb)
    nb = input('Enter major: ')
    if (nb == 'stop'):
        nb = ''
        data1.setMajor(nb)
        dataInfo.append(data1)
        break
    data1.setMajor(nb)
    dataInfo.append(data1)




with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Email', 'Mobile', 'University', 'Major']
    writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=fieldnames)
    writer.writeheader()

    for data2 in dataInfo:
        writer.writerow({'Name': data2.getName(), 'Email': data2.getEmail(), 'Mobile': data2.getMobile(),
                         'University': data2.getUniversity(), 'Major': data2.getMajor()})

print('Done')
