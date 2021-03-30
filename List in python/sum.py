
s=input("enter string\n")
p=int(input("enter length\n"))
a=s[0]
l=len(s)
c=1
res=''+str(a)
if(p==0):
  res=""
else:
      for i in range(1,l):
          if(a==s[i] and c<p):
              res=res+str(s[i])
              c+=1
          elif(a==s[i]):
              pass
          else:
              c=1
              a=s[i]
              res=res+str(s[i])
print(res)

