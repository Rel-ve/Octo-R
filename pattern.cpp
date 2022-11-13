#include <iostream>
using namespace std;

int main(){
    int row;
    cout<<"Enter how many rows are to be printed: ";
    cin>>row;
    int y = 1;
    while(row>=y){
        int num = (row+1)-y;
        int i = 0;
        while(num){
            i++;
            cout<<i;
            num--;
        }
        if(y>1){
            int space = 1;
            while(space!=y){
                cout<<"**";
                space++;
            }
        }
        num = (row+1)-y;
        while(num){
            cout<<i;
            i--;
            num--;
        }
        cout<<endl;
        y++;
    }
    y = 1;
    while(row>y){
        int num_ = 0;
        int j = 0;
        while(num_<=y){
            j++;
            num_++;
            cout<<j;
        
        }
        if(y<row-1){
            int space = row-y-1;
            while(space){
                cout<<"**";
                space--;
            }
        }
        num_ = 0;
        j++;
        while(num_<=y){
            j--;
            num_++;
            cout<<j;
        
        }
        cout<<endl;
        y++;
    }
    return 0;
}
