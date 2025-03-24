/**
  * @author         : Andy Tao
  * @brief          : 线性表编程实验2025
  * @date           : 25-3-22 下午9:21
  */
#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

int main() {
    vector<int> list;  // 存储当前元素的列表
    string line;       // 用于读取输入行

    // 处理初始化命令C，格式：C m（创建包含0到m-1的列表）
    getline(cin, line);
    istringstream iss(line);
    string cmd;
    iss >> cmd;
    if (cmd != "C") {
        cout << "X" << endl;  // 首命令非C则报错
        return 0;
    }
    int m;
    iss >> m;
    list.clear();
    for (int i = 0; i < m; ++i) {
        list.push_back(i);  // 初始化0,1,...,m-1
    }

    bool terminated = false;
    while (!terminated && getline(cin, line)) {
        istringstream iss(line);
        iss >> cmd;

        if (cmd == "C") {  // 重复C命令视为错误
            cout << "X" << endl;
            return 0;
        }

        // 处理插入命令I，格式：I x y（在位置x插入y）
        if (cmd == "I") {
            int x, y;
            iss >> x >> y;
            if (x < 0 || x > list.size()) {  // 检查x有效性
                cout << "X" << endl;
                return 0;
            }
            list.insert(list.begin() + x, y);
        }

        // 处理删除命令D，格式：D x（删除位置x的元素）
        else if (cmd == "D") {
            int x;
            iss >> x;
            if (x < 0 || x >= list.size()) {
                cout << "X" << endl;
                return 0;
            }
            list.erase(list.begin() + x);
        }

        // 处理范围删除命令E，格式：E x y（删除x到y的元素）
        else if (cmd == "E") {
            int x, y;
            iss >> x >> y;
            if (x < 0 || y >= list.size() || x > y) {  // 检查范围有效性
                cout << "X" << endl;
                return 0;
            }
            list.erase(list.begin() + x, list.begin() + y + 1);
        }

        // 处理清空命令CLR
        else if (cmd == "CLR") {
            list.clear();
        }

        // 处理长度查询命令LEN（终止程序）
        else if (cmd == "LEN") {
            cout << list.size() << endl;
            terminated = true;
        }

        // 处理元素获取命令GET，格式：GET pos（输出指定位置元素）
        else if (cmd == "GET") {
            int pos;
            iss >> pos;
            if (pos < 0 || pos >= list.size()) {
                cout << "X" << endl;
                return 0;
            }
            cout << list[pos] << endl;
            terminated = true;
        }

        // 处理打印命令P（输出所有元素）
        else if (cmd == "P") {
            if (list.empty()) {
                cout << "EMPTY" << endl;
            } else {
                for (size_t i = 0; i < list.size(); ++i) {
                    if (i > 0) cout << " ";
                    cout << list[i];
                }
                cout << endl;
            }
            terminated = true;
        }

        // 无效命令处理
        else {
            cout << "X" << endl;
            return 0;
        }
    }

    return 0;
}