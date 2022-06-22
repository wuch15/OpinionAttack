def sentitocate(x):
    if x<=-0.6:
        return 0
    elif x>-0.6 and x<=-0.2:
        return 1
    elif x>-0.2 and x<0.2:
        return 2
    elif x>=0.2 and x<0.6:
        return 3
    elif x>=0.6:
        return 4

def special_entity(x):
    feat_vec=[0]*7 # only 6 elements are used, the rest one is reserved for future entities
    if 'facebook'  in x.lower():
        feat_vec[0]=1
    if 'google'  in x.lower():
        feat_vec[1]=1
    if 'Trump' in x:
        feat_vec[2]=1
    if 'Biden' in x:
        feat_vec[3]=1
    if 'Republica' in x:
        feat_vec[4]=1
    if 'Democrat' in x:
        feat_vec[5]=1
    return feat_vec