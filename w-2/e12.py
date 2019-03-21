#https://github.com/hacktiv8/phase-0-activities/blob/master/modules/challenge-konversi-menit.md

def konversiMenit(menit):
  return f"{int(menit/60):02d}:{int(menit % 60):02d}"

# TEST CASES
print(konversiMenit(63)) # 1:03
print(konversiMenit(124)) # 2:04
print(konversiMenit(53)) # 0:53
print(konversiMenit(88)) # 1:28
print(konversiMenit(120)) # 2:00