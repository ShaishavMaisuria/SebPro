
name= r'<td nowrap="" rel="Johnson, Jr., Eddie"><a href="/player/Eddie-Johnson-Jr/Summary/51360">Eddie Johnson, Jr.</a></td>' +"\n" +'<td nowrap="" rel="dohnson, dr., Eddie"><a href="/player/Eddie-Johnson-Jr/Summary/51360">Eddie Johnson, Jr.</a></td>'

fame=name


identify='href="'
finish='">'
endofString="</td>"
s = name
'''
def find_between( s, first, last ):

        if s.__contains__(first):
            return ""

        else:
            start = s.index(first) + len(first)
            end = s.index(last, start)
            str = s[start:end]
            data = find_between(s[end:], start, end) + str
            return data
for first in name:
    if(name.index(first)==1):
        find_between( s, start, end )
    else:
        find_between_r( s, "123", "abc" )
        return break
        data = find_between(s[end:], start, end) + str
        return data

print(find_between( s, start, end ))  '''

print("-------------------------------------------------------------------------------------")


def find_between(s, first, last):
        if not(s.__contains__(first)):
            return ""
        else:
            start = s.index(first) + len(first)
            end = s.index(last, start)
            str = s[start:end]

        return find_between(s[end + 1:], identify, finish) + " \n" +str



ne=find_between(s, identify, finish)
print("--dd " +ne)
