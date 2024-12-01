# mutable parameters

def fn(l = []):

    #print(id(l))
    
    if len(l) == 0:
        l = list()

    print(l)
    
    l.append("###")

    return l

fn()
fn()
fn()