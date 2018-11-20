import collections
import functools
import datetime
import os

def wrapped_test(test):

    @functools.wraps(test)
    def wrapper(self,*args,**kwargs):
        try:
            self.testResults = collections.OrderedDict([])
            test_start = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            test_name = test.__name__
            test_result = ''
            test_duration = ''
            test(self,*args,**kwargs)
            test_result = 'PASS'
            test_end = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            test_duration = datetime.datetime.strptime(test_end,"%y-%m-%d %H:%M:%S") - datetime.datetime.strptime(test_start,"%y-%m-%d %H:%M:%S")
            test_duration = str(test_duration)

            try:
                #Grabbing screenshot of the failed screen
                screenshot_filename = os.path.join(self.executionFolderPath,test_name + '_' + datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S") + '.png')
                screenshot_filename_rel = '.' + '/' + screenshot_filename.split("/")[-1]
                self.driver.save_screenshot(screenshot_filename)
            except Exception as exp:
                print "Error capturing screenshot! {}".format(exp)
            
            self.testResults[test_name] = {'result': test_result, 
                                            'duration': test_duration,
                                            'start': test_start,
                                            'end':test_end,
                                            'screenshot':screenshot_filename_rel,
                                            'message':''}
        except Exception as exp:
            test_result = 'FAIL'
            message = exp.message
            try:
                #Grabbing screenshot of the failed screen
                screenshot_filename = os.path.join(self.executionFolderPath,test_name + '_' + datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S") + '.png')
                screenshot_filename_rel = '.' + '/' + screenshot_filename.split("/")[-1]
                self.driver.save_screenshot(screenshot_filename)
            except Exception as exp:
                print "Error capturing screenshot! {}".format(exp)

            test_end = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            test_duration = datetime.datetime.strptime(test_end,"%y-%m-%d %H:%M:%S") - datetime.datetime.strptime(test_start,"%y-%m-%d %H:%M:%S")
            test_duration = str(test_duration)
            self.testResults[test_name] = {'result': test_result, 
                                            'duration': test_duration,
                                            'start': test_start,
                                            'end':test_end,
                                            'screenshot':screenshot_filename_rel,
                                            'message':message}
            raise

    return wrapper