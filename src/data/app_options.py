# Eventually will move to DB.
appOptions = [
  { 
    'tech': 'python',
    'name': 'Python 2.7 - Interactive command line app',
    'supporteddVersions': ['2.7'],
  },
  {
    'tech': 'angularjs',
    'name': 'Simple web site',
    'supporteddVersions': ['1.6'],
  }
]

def getAppOptionsText():
  """"""

  appOptionsTextArr = ['Select the type of desired project:\n']
  for index, appOption in enumerate(appOptions):
    appOptionsTextArr.append(str(index + 1) + '. ' + appOption.get('name'))
  return '\n'.join(appOptionsTextArr)
