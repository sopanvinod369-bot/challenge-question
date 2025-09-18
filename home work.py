sub1=85
sub2=76
sub3=88
sub4=92
sub5=88

totalmark =(sub1+sub2+sub3+sub4+sub5)
print(totalmark,"total mark")
percentage= totalmark/500*100
print(percentage,"percentage")
if percentage<=60:
 print("grade,D")
elif percentage<=70:
 print("grade_c")
elif percentage<= 80:
 print("grade_b")
elif percentage<=100:
 print("grade_a")
else:
 print("fail")


