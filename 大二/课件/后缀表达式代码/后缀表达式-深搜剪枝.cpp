#include <iostream>
#include <stack>
#include <string>

using namespace std;

int n = 0;

static bool isOperator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

static float calPostfix(string postfix) {
    n++;
    stack<float> stack;

    for (char c : postfix) {
        if (isdigit(c) || c == '.') {
            stack.push((float)(c - '0'));
        } else if (isOperator(c)) {
            if (stack.empty())
            {
                throw std::runtime_error("");
            }
            
            float operand2 = stack.top();
            stack.pop();
            if (stack.empty())
            {
                throw std::runtime_error("");
            }
            float operand1 = stack.top();
            stack.pop();
            switch (c) {
                case '+':
                    stack.push(operand1 + operand2);
                    break;
                case '-':
                    stack.push(operand1 - operand2);
                    break;
                case '*':
                    stack.push(operand1 * operand2);
                    break;
                case '/':
                    if (operand2 == 0)
                        throw std::runtime_error("Division by zero");
                    stack.push(operand1 / operand2);
                    break;
            }
        }
    }

    return stack.top();
}


void dfs(string str, float k, int opts, int nums,int & sum) {
    try {
        if (str.length() == 7 && abs(calPostfix(str) - k) < 1e-4) {
            sum++;
        }
    } catch (const exception &e) {
        return;
    }

    if (nums < 4) {
        for (int i = 0; i < 10; i++)
            dfs(str + to_string(i), k, opts, nums + 1,sum);
    }

    if (str.length() >= 2 && opts < 3 && nums>opts) {
        dfs(str + "+", k, opts + 1, nums,sum);
        dfs(str + "-", k, opts + 1, nums,sum);
        dfs(str + "*", k, opts + 1, nums,sum);
        dfs(str + "/", k, opts + 1, nums,sum);
    }
}

int search(float k) {
    int sum = 0;
    dfs("", k, 0, 0,sum);
    return sum;
}
// 判断是否是运算符


int main() {
    int sum = 0;
    cout<<search(-6)<<endl;
    cout<<n<<endl;
    return 0;
}
