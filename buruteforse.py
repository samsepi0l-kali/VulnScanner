import requests

#POST METHOD ONLY


login_page = input('Enter the complete address: ')
login_id =input('Enter username : ')
#key = input('Enter key for post method : ')
dictionary = ['laoshjj' , 'ashish' ]
for i in dictionary:
    r = requests.post(login_page , {'email':login_id,'password': i})
#print(r)
#print(r.content)
    response = r.text    
    print(response)
    #print (r.content)
#out = open_new_tab(content)
#print(out)
#print(r.text)
#r.encoding = 'utf-8'
#print(r.encoding)
