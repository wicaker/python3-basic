# https://github.com/hacktiv8/phase-0-activities/blob/master/modules/challenge-bandingkan-angka.md

def bandingkanAngka(angka1, angka2):
  if(angka1>angka2):
    return False
  elif(angka1<angka2):
    return True
  else:
    return -1

# TEST CASES
print(bandingkanAngka(5, 8))# true
print(bandingkanAngka(5, 3))# false
print(bandingkanAngka(4, 4))# -1
print(bandingkanAngka(3, 3))# -1
print(bandingkanAngka(17, 2))# false