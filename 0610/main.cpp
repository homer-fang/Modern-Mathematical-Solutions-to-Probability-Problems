#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e5 + 10;

double E1[MAXN];
double E2[MAXN];
double ans[MAXN];

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    E1[0] = E2[0] = ans[0] = 0.0;

    for (int i = 1; i <= n; i++) {
        double p;
        cin >> p;

        ans[i ] = ans[i - 1] + p * (3 * E2[i - 1] + 3 * E1[i - 1] + 1);
        
        E1[i] = p * (E1[i - 1] + 1);
        
        E2[i] = p * (E2[i - 1] + 2 * E1[i - 1] + 1);
    }
    cout << fixed << setprecision(1) << ans[n] << "\n";

    return 0;
}