#include <bits/stdc++.h>
using namespace std;

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long double P, Q;

    cin >> n >> m >> P >> Q;

    long double p = P / Q;
    long double q = 1.0L - p;

    vector<pair<int, int>> edges;
    vector<int> deg(n + 1);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
        deg[u]++;
        deg[v]++;
    }

    vector<vector<long double>> a(n + 1, vector<long double>(n + 2, 0));

    for (int i = 1; i <= n; i++) {
        a[i][i] = 1.0L;
    }

    a[1][n + 1] = 1.0L;

    for (auto [u, v] : edges) {
        a[v][u] -= q /deg[u];
        a[u][v] -= q /deg[v];
    }


    const long double EPS = 1e-18L;

    for (int col = 1; col <= n; col++) {
        int pivot = col;

        for (int row = col + 1; row <= n; row++) {
            if (fabsl(a[row][col]) > fabsl(a[pivot][col])) {
                pivot = row;
            }
        }
        swap(a[col], a[pivot]);


        if (fabsl(a[col][col]) < EPS) {
            continue;
        }

        long double div = a[col][col];

        for (int j = col; j <= n + 1; j++) {
            a[col][j] /= div;
        }

        for (int row = 1; row <= n; row++) {
            if (row == col) {
                continue;
            }

            long double factor = a[row][col];

            if (fabsl(factor) < EPS) continue;

            for (int j = col; j <= n + 1; j++) {
                a[row][j] -= factor * a[col][j];
            }
        }
    }

    vector<long double> x(n + 1);

    for (int i = 1; i <= n ;i++) {
        x[i] = a[i][n + 1];
    }

    cout << fixed << setprecision(10);

    for (int i = 1; i <= n; i++) {
        long double ans = p * x[i];
        cout << (double)ans << "\n";
    }
    return 0;
}