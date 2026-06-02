arr = [1,2,5,6,2,1];

i = 1;

while True:
    if ( arr[i-1]< arr[i] and arr[i]<arr[i+1] ) or ( arr[i-1]> arr[i] and arr[i]>arr[i+1]) :
        if i < len(arr)-2 :
         i+=1
    else:
       break;

def checkForIncOrDec(li):
    li_sorted = sorted(li);
    li_sorted_rev = sorted(li, reverse=True);

    if li_sorted == li:
       print("Increasing");
    elif li_sorted_rev == li:
       print("Decreasing");
    else:
       print("Neither");

print(arr[i-1], arr[i], arr[i+1]);


ar1= [1,2,2,4];
ar2=[4,3,2,3];

checkForIncOrDec(ar1);
checkForIncOrDec(ar2);