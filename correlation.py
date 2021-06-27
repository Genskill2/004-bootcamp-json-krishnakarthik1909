import json
import math
def load_journal(fname):
    f=open(fname,'r')
    outpt=json.load(f)
    f.close()
    return outpt
def compute_phi(fname,event):
    lst=load_journal(fname)
    n11=0
    n00=0
    n10=0
    n01=0
    n1_=0
    n0_=0
    n_1=0
    n_0=0
    
    for item in lst:
        if (event in item['events']) and (item['squirrel'] is True):
            n11+=1
        if (event not in item['events']) and (item['squirrel'] is False):
            n00+=1
        if (event in item['events']) and (item['squirrel'] is False):
            n10+=1
        if (event not in item['events']) and (item['squirrel'] is True):
            n01+=1
        if event in item['events']:
            n1_+=1
        if event not in item['events']:
            n0_+=1
        if item['squirrel'] is True:
            n_1+=1
        if item['squirrel'] is False:
            n_0+=1
    phi=(n11*n00-n10*n01)/math.sqrt(n1_*n0_*n_1*n_0)
    return phi
def compute_correlations(fname):
    d=load_journal(fname)
    event_names=[]
    ans={}
    for item in d:
        for event in item['events']:
            if event not in event_names:
                event_names.append(event)
    print (event_names)
    for event in range(len(event_names)):
        print(event_names[event])
        cor=compute_phi(fname,event_names[event])
        ans[event_names[event]]=cor
    return ans
def diagnose(fname):
    ans=compute_correlations(fname)
    max_event = max(ans,key=ans.get)
    min_event = min(ans,key=ans.get)
    return max_event,min_event    
def main():
    compute_correlations("journal.json")
if __name__=="__main__":
    main()
# Add the functions in this file
