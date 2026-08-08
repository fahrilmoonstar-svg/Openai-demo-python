#include <iostream>
using namespace std;

int main()
{
    // We can use array with loop
    string cars [5] = {"BMW", "TOYOTA", "KIA", "ANGKOR", "ODD"};
    cout << "This is a array : " << cars[3] << endl;

    for (int i = 0; i <= 5; i++){
        cout << cars[i] << endl;
    }

    return 0;
}