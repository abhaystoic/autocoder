""""""

import sys

from data import app_options
from data import app_types
from data import constants


class Autocode():

  def __init__(self):
    self._diplayMessageOnConsole(constants.WELCOME_MSG)

  def main(self):
    appOption = self.getAppOptionsFromUser()
    appType = self.getAppTypeFromUser()
    print 'appOption=', appOption
    print 'appType=', appType

  def _diplayMessageOnConsole(self, msg):
    sys.stdout.write('\n')
    sys.stdout.write(msg)
    sys.stdout.write('\n')

  def getAppOptionsFromUser(self):
    self._diplayMessageOnConsole(app_options.getAppOptionsText())
    return raw_input(constants.USER_CHOICE_MSG)

  def getAppTypeFromUser(self):
    self._diplayMessageOnConsole(app_types.getAppTypesText())
    return raw_input(constants.USER_CHOICE_MSG)



if __name__ == '__main__':
  Autocode().main()
