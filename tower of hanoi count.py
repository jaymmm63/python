count = 0
def move( n, src, dest, temp ):
    global count
    if n >= 1 :
        move( n - 1, src, temp, dest )
        print( "Move %d -> %d" % (src, dest))
        count = count+1
        move( n - 1, temp, dest, src )


move(3, 1, 2, 3)
print(count)
