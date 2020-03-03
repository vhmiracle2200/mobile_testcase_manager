'''
Main file is using to init and running scripts

'''
from TestCases.FastHub.EditSubjectAndDescription import EditSubjectAndDescription
from TestCases.FastHub.SignInBasicAuthentication import SignInBasicAuthentication


if __name__ == '__main__':
    '''
    Main module is first state that we are instantiate all Test Case scenarios.
    '''
    testcase_scenarios = [SignInBasicAuthentication(), EditSubjectAndDescription()]
    for scenario in testcase_scenarios:
        print("######################## {} ########################".format(type(scenario).__name__))
        scenario.preparation()
        scenario.teststeps()
        scenario.finilizing()
