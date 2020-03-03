'''
Main file is using to init and running scripts

'''
from TestCases.FastHub.Edit_Subject_And_Description import EditSubjectAndDescription
from TestCases.FastHub.SignIn_Basic_Authentication import SignInBasicAuthentication

if __name__ == '__main__':
    '''
    Main module is first state that we are instantiate all Test Case scenarios.
    '''

    adb_device_name = 'R58M575Q2AW'
    remote_url = 'http://0.0.0.0:4723/wd/hub'
    testcase_scenarios = [SignInBasicAuthentication(adb_device_name, remote_url),
                          EditSubjectAndDescription(adb_device_name, remote_url)]
    for scenario in testcase_scenarios:
        print("######################## {} ########################".format(type(scenario).__name__))
        scenario.preparation()
        scenario.teststeps()
        scenario.finilizing()
