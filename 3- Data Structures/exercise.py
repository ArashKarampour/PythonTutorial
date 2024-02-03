# find the most repeated charachter in this sentence:
sentence = "This is a common interview question"

# my Solution
# d = {'x':3,'y': 2, 'a':10}
# print(max(d,key=lambda x:d[x]))

# my code:
# dic = dict(a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,k=0,l=0,m=0,n=0,o=0,p=0,q=0,r=0,s=0,t=0,u=0,v=0,w=0,x=0,y=0,z=0)
# dic[' '] = 0
# print(dic)

# for i in sentence.lower():
#     dic[i] = dic[i] + 1

# optimized way of the above code:
char_freq = {}
for char in sentence:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

dic = char_freq
print(dic)

print(max(dic,key= lambda x:dic[x])) # find the maximum that have the max value. it returns the key of the max value

# see also video 23 for mosh solution but actually my solution was better :)).