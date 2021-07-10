#include <vector>
// using namespace std;

class Solution {
    public:
        int pivotIndex(std::vector<int>& arr) {
            int left = 0, n = arr.size();
            int right = 0;

            for (int i = 1; i < n; i++) right += arr[i];

            int i = 0;

            while (left != right && i < n) {
                left += arr[i];
                right -= arr[i + 1];
                i++;
            }
            return left == right ? i : -1;
        }
};