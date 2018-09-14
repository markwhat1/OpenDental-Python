import OpenDental
import pickle


def manual():
    def yorn(data):
        if lower(data) == 'y':
            return True
        elif lower(data) == 'n':
            return False
        else:
            print('Invalid Input!')
            return False

    print("Attempt to load previously saved configuration?")
    check = input('Y/N?')
    if yorn(check):
        if OpenDental.DatabaseConnection():
            return True

    def write(host, username, password, database, path):
        try:
            f = open(path, 'w')
            f.write(
                'Host = ' + host + '\nUsername = ' + username + '\nPassword = ' + password + '\nDatabase = ' + database)
            f.close()
            return True
        except Exception as ex:
            return False

    print("Please enter OpenDental database details.")
    host = input('Host?:')
    username = input('Username?')
    password = input('Password?')
    database = input('Database?')
    print("Save this configuration?")
    save = input('Y/N?')
    if yorn(save):
        import os
        path = os.path.dirname(__file__).replace('\\library.zip', "")
        path += '\OpenDentalDatabaseConfig.ini'
        if os.path.isfile(path):
            print("configuration already exists! Overwrite?")
            overwrite = input('Y/N?')
            if yorn(overwrite):
                if write(host, username, password, database, path):
                    print("Parameters updated successfully.")
                else:
                    print("Save failed.")
        else:
            if write(host, username, password, database, path):
                print("Data saved.")
            else:
                print("Save failed")

    else:
        print("Data not saved.")

    print('Attempting to connect to database')
    if OpenDental.DefineDatabase(host, username, password, database):
        print("connection successful")
        return True
    else:
        print("connection failed!")
        return False


manual()
x = 0
while True:
    print("Select patient by patient number: ")
    patientnum = input('Patient number: ')
    patient = OpenDental.GetPatientDetails(patientnum)
    f = open('patientnumber' + patientnum + '-' + str(x) + '-DUMP.txt', 'w')
    pickle.dump(patient, f)
    x += 1
    print(patient)


test_dict = {'PatNum': 'Sargent, Smith', 'LName': 'Sargent', 'FName': 'Smith', 'MiddleI': '', 'Preferred': '',
             'PatStatus': 'Patient', 'Gender': 'Female', 'Position': 'Single', 'Birthdate': '07/20/1971',
             'SSN': '4794319997', 'Address': '57023 Smith St', 'Address2': '', 'City': 'Lake Charles', 'State': 'LA',
             'Zip': '70605', 'HmPhone': '1(337)477-2651', 'WkPhone': '', 'WirelessPhone': '1(337)529-6872',
             'Guarantor': 'Sargent, Smith', 'CreditType': '', 'Email': 'donnarmetta@yahoo.com', 'Salutation': '',
             'EstBalance': 0, 'PriProv': 'SP', 'SecProv': '', 'FeeSched': '', 'BillingType': 'Standard Account',
             'ImageFolder': 'SargentDonna3587578', 'AddrNote': '', 'FamFinUrgNote': '', 'MedUrgNote': '',
             'ApptModNote': '', 'StudentStatus': '', 'SchoolName': '', 'ChartNumber': '', 'MedicaidID': '',
             'Bal_0_30': '0.00', 'Bal_31_60': '0.00', 'Bal_61_90': '0.00', 'BalOver90': '0.00', 'InsEst': '0.00',
             'BalTotal': '0.00', 'EmployerNum': 0, 'EmploymentNote': '', 'County': '', 'GradeLevel': 'Unknown',
             'Urgency': 'Unknown', 'DateFirstVisit': '09/05/2018', 'ClinicNum': 0, 'HasIns': '',
             'TrophyFolder': '57\x1d87578', 'PlannedIsDone': 0, 'Premed': 0, 'Ward': '', 'PreferConfirmMethod': 0,
             'PreferContactMethod': 0, 'PreferRecallMethod': 0, 'SchedBeforeTime': '00:00:00',
             'SchedAfterTime': '00:00:00', 'SchedDayOfWeek': 0, 'Language': '', 'AdmitDate': '01/01/0001 12:00:00 AM',
             'Title': '', 'PayPlanDue': 0, 'SiteNum': 0, 'DateTStamp': '09/13/2018', 'ResponsParty': 0,
             'CanadianEligibilityCode': 0, 'AskToArriveEarly': 0, 'PreferContactConfidential': 0, 'SuperFamily': 0,
             'TxtMsgOk': 0, 'SmokingSnoMed': 2, 'Country': '', 'DateTimeDeceased': '', 'BillingCycleDay': 1,
             'SecUserNumEntry': 65, 'SecDateEntry': '08/22/2018 12:00:00 AM', 'HasSuperBilling': 0,
             'PatNumCloneFrom': 0, 'DiscountPlanNum': 1}
