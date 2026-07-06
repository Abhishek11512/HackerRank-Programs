#Text_Alignment

thick = int(input().strip())
c = "H"

for i in range(thick):
    cb = (c*i).rjust(i) + c + (c*i).ljust(i)
    print (cb.center(thick * 2))
for i in range(thick + 1):
    print(
        (c * thick).center(thick * 2)
        + (c * thick).center(thick * 6)
    )
for i in range((thick + 1) // 2):
    print((c * thick * 5).center(thick * 6))

for i in range(thick + 1):
    print((c * thick).center(thick * 2) + (c * thick).center(thick * 6))

for i in range(thick):
    cb = (c * (thick - i - 1)).rjust(thick) + c + (c * (thick - i - 1)).ljust(thick)
    print(cb.rjust(thick * 6))

#Its really frustrating and complex to do for beginners.... feels bad to say but had to use suggestions myself to crack this one.  