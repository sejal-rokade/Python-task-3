# clear
d1={
    "fruit":'apple',
    'color':'red',
    'price':'34'
}
d1.clear()
print(d1)
print()
print('-----')
print()

# copy
d2={
     "fruit":'apple',
    'color':'red',
    'price':'34'
}
x=d2.copy()
print(x)
print()
print('-----')
print()

# fromkeys
x=('marks1','marks2','marks3',)
y=50
thisdict=dict.fromkeys(x,y)
print(thisdict)
print()
print('-----')
print()

# get
d3={
    'x':'x1',
    'y':'y1',
    'z':'z1'
}
x=d3.get('y')
print(x)
print()
print('-----')
print()

# items
d4={
    'x':'x1',
    'y':'y1',
    'z':'z1'
}
x=d4.items()
print(x)
print()
print('-----')
print()

# keys
d5={
     "fruit":'apple',
    'color':'red',
    'price':'34'
}
x=d5.keys()
print(x)
print()
print('-----')
print()

# values
d6={
     "fruit":'apple',
    'color':'red',
    'price':'34'
}
x=d6.values()
print(x)
print()
print('-----')
print()

# pop
d7={
    'stu':'Ram',
    'add':'add1',
    'sub':'math'
}
d7.pop('add')
print(d7)
print()
print('-----')
print()

# popitem
d7={
    'stu':'Ram',
    'add':'add1',
    'sub':'math'
}
d7.popitem()
print(d7)
print()
print('-----')
print()

# setdefault
d8={
     "fruit":'apple',
    'color':'red',
    'price':34
}
x=d8.setdefault('price',100)
print(x)
print()
print('-----')
print()

# update
d9={
     "fruit":'apple',
    'color':'red',
    'price':34
}
d9.update({'color':'green'})
print(d9)