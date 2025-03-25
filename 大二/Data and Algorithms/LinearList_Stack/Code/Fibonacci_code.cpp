/**
  * @author         : Andy Tao
  * @brief          : 斐波那契编码
  * @date           : 25-3-21 下午8:33
  */
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    // 生成斐波那契数列，直到超过 n
    vector<int> fib = {1, 2};
    while (true) {
        int next = fib.back() + fib[fib.size()-2];
        if (next > n) break;
        fib.push_back(next);
    }

    // 确定最大可用斐波那契数的索引
    int max_idx = fib.size()-1;
    for (int i = 0; i < fib.size(); ++i) {
        if (fib[i] <= n) max_idx = i; // 记录最大有效索引
    }

    // 标记选中的斐波那契数（贪心算法：从大到小选择）
    vector<bool> selected(max_idx+1, false);
    int remaining = n;
    for (int i = max_idx; i >= 0; --i) {
        if (fib[i] <= remaining) {
            selected[i] = true;
            remaining -= fib[i]; // 减去已选数值
        }
    }

    // 生成二进制编码并添加终止符 1
    string code;
    for (bool used : selected) {
        code += used ? '1' : '0';
    }
    code += '1'; // 添加终止符 1

    cout << code << endl;
    return 0;
}