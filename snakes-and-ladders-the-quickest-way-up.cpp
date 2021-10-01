#include <bits/stdc++.h>

#define MOD ((int)1e9 + 7)
#define INF (int)1e7
#define DEB(x) cout << #x << ": " << x << "\n";
#define PDEB(p) cout << #p << ": " << p.first << " " << p.second << "\n";
#define VDEB(arr)                                                              \
    cout << #arr << ": ";                                                      \
    for (auto &a : arr)                                                        \
        cout << a << " ";                                                      \
    cout << "\n";

using namespace std;

typedef unsigned long long ull;
// #define int ull
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<vi> vii;

int dijikstra(vi graph[]) {
    priority_queue<int> pq;
    vi dist(101, INF);

    pq.push(1);
    dist[1] = 0;

    while (pq.size()) {
        int u = pq.top();
        pq.pop();

        for (int i = 0; i < graph[u].size(); ++i) {
            int v = graph[u][i];

            if (dist[v] > dist[u] + 1) {
                dist[v] = dist[u] + 1;
                pq.push(v);
            }
        }
    }

    return dist[100] == INF ? -1 : dist[100];
}

int solve() {
    int l, s;
    vi graph[101];

    int u, v;
    cin >> l;
    while (l--) {
        cin >> u >> v;
        graph[u].push_back(v);
    }

    cin >> s;
    while (s--) {
        cin >> u >> v;
        graph[u].push_back(v);
    }

    for (int i = 1; i <= 100; ++i) {
        for (int j = 1; j <= 6; ++j) {
            if (i + j <= 100) {
                if (graph[i + j].size())
                    graph[i].push_back(graph[i + j][0]);
                else
                    graph[i].push_back(i + j);
            }
        }
    }

    return dijikstra(graph);
}

int32_t main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--)
        cout << solve() << "\n";

    return 0;
}

