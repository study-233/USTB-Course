/**
  * @author         : Andy Tao
  * @brief          : 后缀表达式2025
  * @date           : 25-3-22 下午10:10
  */
#include <iostream>
#include <vector>
using namespace std;

const char ops_list[5] = {'+', '-', '*', '/', '%'};
int K;

// 验证运算符位置是否构成合法后缀表达式
bool is_valid(const vector<int>& pos) {
    vector<bool> is_op(7, false);
    for (int p : pos) is_op[p] = true;

    int stack_size = 0;
    for (int i = 0; i < 7; i++) {
        if (is_op[i]) {
            if (stack_size < 2) return false;
            stack_size--;
        } else {
            stack_size++;
        }
    }
    return stack_size == 1;
}

int main() {
    cin >> K;

    vector<vector<int>> valid_positions;

    // 生成所有合法的运算符位置组合（3个运算符的位置）
    for (int a = 0; a < 7; a++) {
        for (int b = a + 1; b < 7; b++) {
            for (int c = b + 1; c < 7; c++) {
                vector<int> pos = {a, b, c};
                if (is_valid(pos)) {
                    valid_positions.push_back(pos);
                }
            }
        }
    }

    int cnt = 0;

    // 遍历所有合法位置组合
    for (const auto& valid_pos : valid_positions) {
        vector<bool> is_op(7, false);
        for (int p : valid_pos) is_op[p] = true;

        // 预处理数字位置映射
        vector<int> digits_pos, digit_map(7, -1);
        for (int i = 0; i < 7; i++) {
            if (!is_op[i]) {
                digits_pos.push_back(i);
                digit_map[i] = digits_pos.size() - 1;
            }
        }

        // 预处理运算符索引
        vector<int> op_indices(7, -1);
        for (int k = 0; k < 3; k++) {
            op_indices[valid_pos[k]] = k;
        }

        // 遍历所有运算符组合（5^3=125种）
        for (int op_num = 0; op_num < 125; op_num++) {
            vector<char> ops = {
                    ops_list[op_num / 25],
                    ops_list[(op_num % 25) / 5],
                    ops_list[op_num % 5]
            };

            // 遍历所有4位数字组合（0-9999）
            for (int num = 0; num < 10000; num++) {
                vector<int> digits = {
                        num / 1000,
                        (num / 100) % 10,
                        (num / 10) % 10,
                        num % 10
                };

                // 模拟后缀表达式计算
                bool valid = true;
                int stack[7], sp = 0;

                for (int i = 0; i < 7 && valid; i++) {
                    if (op_indices[i] != -1) { // 处理运算符
                        if (sp < 2) { valid = false; continue; }
                        int a = stack[sp-2], b = stack[sp-1];
                        sp -= 2;
                        char op = ops[op_indices[i]];

                        if ((op == '/' || op == '%') && b == 0) {
                            valid = false;
                            continue;
                        }

                        int res;
                        switch(op) {
                            case '+': res = a + b; break;
                            case '-': res = a - b; break;
                            case '*': res = a * b; break;
                            case '/': res = a / b; break;
                            case '%': res = a % b; break;
                        }
                        stack[sp++] = res;
                    } else { // 处理数字
                        stack[sp++] = digits[digit_map[i]];
                    }
                }

                // 检查结果是否符合
                if (valid && sp == 1 && stack[0] == K) {
                    cnt++;
                }
            }
        }
    }

    cout << cnt << endl;
    return 0;
}