class dog:
    attr1="mammel"
def __init__(self,name):
    self.name=name    

rodger=dog("rodger")
tommy=dog("tommy")
print("rodger is a{}".format(rodger.__class.attr1))
print ("tommy is also{}".format(tommy.__class.__attr1))

print("my name is {}".format(rodger.name))
print("my name is {}".format(tommy.name))


