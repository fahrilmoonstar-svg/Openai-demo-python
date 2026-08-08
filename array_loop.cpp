#include <iostream>
using namespace std;

int main()
{
    // Array dengan 5 elemen
    string cars[5] = {"BMW", "TOYOTA", "KIA", "ANGKOR", "ODD"}; 
    
    cout << "This is an array : " << cars[3] << endl; // Output: ANGKOR

    // Loop yang BENAR: i < 5 (berhenti di i=4)
    for (int i = 0; i < 5; i++) {
        cout << cars[i] << endl;
    }

    return 0;
}