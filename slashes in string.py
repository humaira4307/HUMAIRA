A='''mango city triple single qts'''

B="""mango city triple double qts"""

C="mango city double qts"

D='mango city single qts'

E="mango's city - use single qts inside double qts"

F='mango"s city - use single qts inside double qts'

G='mango\'s city - use slash single qts inside double qts'

H="mango\"s city - use slash double qts inside double qts"

I="mango\s city - use slash inside double qts"

J="mango\n s city - use new line inside double qts"

K="mango\t s city - use tab space inside double qts"

l="mango\b s city - use backspace inside double qts"

m="mango\\ s city - use double slashes inside double qts"



n='''mangos \
city - use \
single qts \
inside double qts'''


o='''mangos 
city - use 
single qts 
inside double qts'''

p="mango\\ s city - use double slashes inside double qts"
print(p)

p="mango\\\\ s city - use double slashes inside double qts"
print(p)

p="mango\\\\\\ s city - use double slashes inside double qts"
print(p)

p="mango\\\\\\\\ s city - use double slashes inside double qts"
print(p)




ui=input('enter the string')
print([w for w in ui.split() if 's' in w])


