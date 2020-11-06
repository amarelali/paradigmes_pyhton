
def add_prefix( p, l):
     for list in l :
            for minilist in p:
                if minilist in list :
                    return [p ]+ l
                elif p in l:
                    return [p ]+ l           


print(add_prefix([1,2,5] , [[1,2,3],[5,2,6,4],[8,2,4]]))
