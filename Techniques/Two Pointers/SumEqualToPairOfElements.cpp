#include<iostream>
using namespace std;


inline bool isPairSum(int arr[], int n, int x)
{
	int i, j; 
	i = 0; j = n - 1;

	int current_sum = 0;
	while(i < j)
	{
		current_sum = arr[i] + arr[j];
		if(current_sum == x)
			return true;

		if(current_sum < x)
			i++;
		else
			j--;
	}
	return false;
}


int main()
{
	int n; cin >> n;
	int arr[n];

	for(int i=0; i<n; ++i)
		cin >> arr[i];

	int x; cin >> x;

	cout << isPairSum(arr, n, x) << endl;
	return 0;
}
