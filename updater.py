version = requests.get('https://raw.githubusercontent.com/secretoolmaker/WendigoToolkit/refs/heads/main/version.txt')
  if version.status_code == 200:
      c = version.text
      ola = c.strip()
  if Version == ola:
      print('[~] No versions available.')
      m = input('[~] Press enter to continue...')
  else:
      print('[~] A new version is available: {ola}')
      m = input('[~] Press enter to continue...')
