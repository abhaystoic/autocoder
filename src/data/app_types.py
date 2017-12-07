# Eventually will move to DB.
appTypes = [
  {
    'type': 'input-output',
    'name': 'Simple I/O',
  },
  {
    'type': 'hello-world',
    'name': 'Hello World',
  },
  {
    'type': 'fibonacci',
    'name': 'Fibonacci',
  },
  {
    'type': 'math',
    'name': 'All math operations',
  },
]

def getAppTypesText():
  """"""

  appTypeTextArr = ['Select a project:\n']
  for index, appType in enumerate(appTypes):
    appTypeTextArr.append(str(index + 1) + '. ' + appType.get('name'))
  return '\n'.join(appTypeTextArr)
