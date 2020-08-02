#------------------
# Reverse a String
#------------------

class revStrings:

    def rev_string1(self,string,lo,hi):

        s1 = string

        while (lo<hi):
            s1[lo],s1[hi] = s1[hi],s1[lo]
            lo = lo+1
            hi = hi-1


        str_o = ''.join(s1)

        return str_o

    def rev_string2(self,string,lo,hi):

        if(len(string)==0):
            return string

        return self.rev_string2(string[1:],0,len(string)-1)+list(string[0])


    def rev_string3(self,string):

        return string[::-1]

    def reverse(self,s):
        if len(s) == 0:
            return s
        else:
            return self.reverse(s[1:]) + s[0]

def main():
    r = revStrings()
    l = list("Suman")

    print("len-",len(l))
    print("str-",l[1:])
    revs = r.rev_string1(l,0,4)
    print(revs)

    revs = r.rev_string2(l, 0, 4)
    print('2-',''.join(revs))

    revs = r.rev_string3(l)
    print('3-',''.join(revs))

    l = ("Suman")
    print("string-", l[1:])
    revs = r.reverse(l)
    print('4-', ''.join(revs))

if __name__ == '__main__':
    main()
