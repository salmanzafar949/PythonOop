class Language:
    def SayHello(self):
        raise NotImplementedError('Please use SayHello Function in Child Class')


class French(Language):
    def SayHello(self):
        print('Bonjour')


class Chinese(Language):
    def SayHello(self):
        print('你好')


def Intro(lang):
     lang.SayHello()


fr = French()
ch = Chinese()
Intro(fr)
Intro(ch)
