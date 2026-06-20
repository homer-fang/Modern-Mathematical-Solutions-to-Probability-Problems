#include <bits/stdc++.h>
using namespace std;

using ll = long long;

bool check_one_query(int n, int S, int k, ll y) {
    ll D = 1LL * S * S - 4LL * y;
    if (D < 0) return false;

    ll r = sqrtl((long double)D);
    while (r * r < D) r++;
    while (r * r > D) r--;

    if (r * r != D) return false;

    auto valid_x = [&](ll x) -> bool {
        if (x < 0 || x > S) return false;
        if (x > k) return false;
        if (S - x > n - k) return false;
        return x * (S - x) == y;
    };

    if ((S + r) % 2 == 0) {
        ll x = (S + r) / 2;
        if (valid_x(x)) return true;
    }

    if ((S - r) % 2 == 0) {
        ll x = (S - r) / 2;
        if (valid_x(x)) return true;
    }

    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n == 1) {
        cout << "! 1" << endl;
        return 0;
    }

    mt19937 rng(
        chrono::steady_clock::now().time_since_epoch().count()
    );
    uniform_int_distribution<int> bit(0, 1);

    vector<pair<int, ll>> queries;
    queries.reserve(17);

    for (int t = 0; t < 17; t++) {
        vector<int> idx;

        for (int i = 1; i <= n; i++) {
            if (bit(rng)) {
                idx.push_back(i);
            }
        }
        // 空集或全集的返回值必然为 0；不必真正询问，但仍计作一次随机样本并记录约束。
        if (idx.empty() || (int)idx.size() == n) {
            queries.push_back({(int)idx.size(), 0});
            continue;
        }
        cout << "? " << idx.size();
        for (int x : idx) {
            cout << ' ' << x;
        }
        cout << endl;

        ll y;
        if (!(cin >> y) || y < 0) return 0;

        queries.push_back({(int)idx.size(), y});
    }

    int answer = -1;

    for (int S = 1; S <= n; S++) {
        bool ok = true;

        for (auto [k, y] : queries) {
            if (!check_one_query(n, S, k, y)) {
                ok = false;
                break;
            }
        }

        if (ok) {
            answer = S;
            break;
        }
    }

    if (answer == -1) return 0;
    cout << "! " << answer << endl;

    return 0;
}