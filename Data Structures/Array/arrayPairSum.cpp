#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int arrayPairSum(vector<int> &v)
    {
        int s = 0, n = v.size();
        sort(v.begin(), v.end());

        for (int i = 0; i < n; i += 2) {
            s += v[i];
        }
        return s;
    }
};