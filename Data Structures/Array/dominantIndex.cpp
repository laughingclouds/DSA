#include <vector>

class Solution {
    public:
        int dominantIndex(std::vector<int>& arr) {
            int maxIndex, m = 0;
            int n = arr.size();

            int temp;
            for (int i = 0; i < n; i++) {
                temp = arr[i];
                if (m < temp) {
                    m = temp;
                    maxIndex = i;
                }
            }            

            for (int i = 0; i < n; i++) {
                temp = arr[i];
                if (m != temp && m < 2 * temp) {
                    maxIndex = -1;
                    break;
                }
            }
            return maxIndex;
        }
};