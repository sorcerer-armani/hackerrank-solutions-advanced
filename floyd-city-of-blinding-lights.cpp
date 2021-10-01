#include <bits/stdc++.h>
#define INF 100000000

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

void solve() {
    int n, e, x, y, z;

    cin >> n >> e;
    vii graph[n];

    for(int i = 0; i < e; ++i) {
        cin >> x >> y >> z;
        
        bool flag = 0;
        for(int j = 0; j < graph[x - 1].size() && !flag; ++j) {
            if(graph[x - 1][j].first == y - 1)
                graph[x - 1][j].second = z;
        }
        
        if(!flag)
            graph[x - 1].push_back(make_pair(y - 1, z));
    }

    int distance[n][n];
    memset(&distance[0][0], INF, sizeof(distance));

    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            if(i == j) {
                distance[i][j] = 0;
                continue;
            }

            distance[i][j] = INF;

           // Search graph[i] if j is present there, if yes, distance[i][j] is the weight
           for(int k = 0; k < graph[i].size(); ++k) {
               if(graph[i][k].first == j) {
                   distance[i][j] = graph[i][k].second; 
                   break;
               }
           }
        }
    }

    // Floyd Warshall
    for(int k = 0; k < n; ++k) {
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]);
            }
        }
    }

    int q;
    cin >> q;
    for(int i = 0; i < q; ++i) {
        cin >> x >> y;
        if(distance[x - 1][y - 1] == INF)
            cout << -1 << "\n";
        else
            cout << distance[x - 1][y - 1] << "\n";
    }
}

int main() {
    solve();
    return 0;
}

