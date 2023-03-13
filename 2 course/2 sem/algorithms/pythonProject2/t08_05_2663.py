"""
// https://www.eolymp.com/uk/submissions/13200187

#include "iostream"

using namespace std;
typedef long long int ll;

void solve()
{
	int n;
	cin >> n;
	int v[1002];
	for (int i = 0; i < n; i++)
		cin >> v[i];

	int count = 0;
	for (int i = 1; i < n; i++)
		for (int r = 0; r < n - i; r++)
			if (v[r] > v[r + 1]) {
				int t = v[r];
				v[r] = v[r + 1];
				v[r + 1] = t;
				count++;
			}
	cout << count;
}

int main()
{
	solve();
	return 0;
}
"""