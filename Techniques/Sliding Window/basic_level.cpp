#include <iostream>
#include <algorithm>
using namespace std;

int maxSum(int arr[], int k) {
    int n = sizeof(arr) / sizeof(arr[0]);

    int ma = -1, su = 0;

    for (int i = 0; i < n; i ++) {
        su += arr[i];

        if (i >= k) {
            su -= arr[i - k];
        }
        
        if (i >= k - 1) {
            ma = max(ma, su);
        }
    }
    return ma;
}