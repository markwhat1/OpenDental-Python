row = {'PatNum': 'Sargent, Smith', 'LName': 'Sargent', 'FName': 'Smith', 'MiddleI': '', 'Preferred': '',
       'PatStatus': 'Patient', 'Gender': 'Female', 'Position': 'Single', 'Birthdate': '01/01/1900', 'SSN': '4794319997',
       'Address': '5700 Smith St', 'Address2': '', 'City': 'Lake Charles', 'State': 'LA', 'Zip': '70605',
       'HmPhone': '1(333)111-1111', 'WkPhone': '', 'WirelessPhone': '1(333)111-0000', 'Guarantor': 'Sargent, Smith',
       'CreditType': '', 'Email': 'testing@yahoo.com', 'Salutation': '', 'EstBalance': 0, 'PriProv': 'SP',
       'SecProv': '', 'FeeSched': '', 'BillingType': 'Standard Account', 'ImageFolder': 'SargentDonna3587578',
       'AddrNote': '', 'FamFinUrgNote': '', 'MedUrgNote': '', 'ApptModNote': '', 'StudentStatus': '', 'SchoolName': '',
       'ChartNumber': '', 'MedicaidID': '', 'Bal_0_30': '0.00', 'Bal_31_60': '0.00', 'Bal_61_90': '0.00',
       'BalOver90': '0.00', 'InsEst': '0.00', 'BalTotal': '0.00', 'EmployerNum': 0, 'EmploymentNote': '', 'County': '',
       'GradeLevel': 'Unknown', 'Urgency': 'Unknown', 'DateFirstVisit': '09/05/2018', 'ClinicNum': 0, 'HasIns': '',
       'TrophyFolder': '57\x1d99999', 'PlannedIsDone': 0, 'Premed': 0, 'Ward': '', 'PreferConfirmMethod': 0,
       'PreferContactMethod': 0, 'PreferRecallMethod': 0, 'SchedBeforeTime': '00:00:00', 'SchedAfterTime': '00:00:00',
       'SchedDayOfWeek': 0, 'Language': '', 'AdmitDate': '01/01/0001 12:00:00 AM', 'Title': '', 'PayPlanDue': 0,
       'SiteNum': 0, 'DateTStamp': '09/13/2018', 'ResponsParty': 0, 'CanadianEligibilityCode': 0, 'AskToArriveEarly': 0,
       'PreferContactConfidential': 0, 'SuperFamily': 0, 'TxtMsgOk': 0, 'SmokingSnoMed': 2, 'Country': '',
       'DateTimeDeceased': '', 'BillingCycleDay': 1, 'SecUserNumEntry': 65, 'SecDateEntry': '08/22/2018 12:00:00 AM',
       'HasSuperBilling': 0, 'PatNumCloneFrom': 0, 'DiscountPlanNum': 1}


def row_test(old_dict, new_dict, key):
       if old_dict.get(key):
              new_dict[key] = old_dict.get(key)
       else:
              new_dict[key] = False

PatData = {}
row_test(row, PatData, 'LName')
print(PatData)