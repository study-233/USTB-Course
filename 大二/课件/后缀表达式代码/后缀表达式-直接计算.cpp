#include <iostream>
#include <cmath>

using namespace std;

int n;
// 运算符计算函数，o==0表示加法，o==1表示减法，o==2表示乘法，o==3表示除法，数字表示符合方便后续循环遍历
float cal(int o, float a, float b)
{
    if (o == 0)
    {
        return a + b;
    }
    if (o == 1)
    {
        return a - b;
    }
    if (o == 2)
    {
        return a * b;
    }
    if (o == 3)
    {
        if (abs(b - 0) < 1e-4)
        {
            throw std::runtime_error("Division by zero");
        }

        return a / b;
    }
    return -1;
}

// 后缀表达式前两位必定是数字，后5位中不考虑顺序符号与数字的排列种数为C52=10种，其中5种为非法表达式，剩下5种排列如下
// 1代表数字的位置，2代表符号的位置，数字与符号的位置确定后缀表达式的计算顺序，可以直接转化为一般表达式计算
// nums表示数字数组(size=4)，opts代表符号数组(size=3)
// int[][] postfixArray = new int[][] {{ 1, 1, 1, 1, 2, 2, 2 },    opts[2](nums[0],opts[1](nums[1],opts[0](nums[2],nums[3])))
//                                     { 1, 1, 1, 2, 1, 2, 2 },    opts[2](nums[0],opts[1](opts[0](nums[1],nums[2]),nums[3]))
//                                     { 1, 1, 1, 2, 2, 1, 2 },    opts[2](opts[1](nums[0],opts[0](nums[1],nums[2])),nums[3])
//                                     { 1, 1, 2, 1, 1, 2, 2 },    opts[2](opts[0](nums[0],nums[1]),opts[1](nums[2],nums[3]))
//                                     { 1, 1, 2, 1, 2, 1, 2 }};   opts[2](opts[1](opts[0](nums[0],nums[1]),nums[2]),nums[3])

// 5种顺序计算函数
float calPostfix1(int nums[], int opts[])
{
    n++;
    return cal(opts[2], nums[0], cal(opts[1], nums[1], cal(opts[0], nums[2], nums[3])));
}

float calPostfix2(int nums[], int opts[])
{
    n++;
    return cal(opts[2], nums[0], cal(opts[1], cal(opts[0], nums[1], nums[2]), nums[3]));
}

float calPostfix3(int nums[], int opts[])
{
    n++;
    return cal(opts[2], cal(opts[1], nums[0], cal(opts[0], nums[1], nums[2])), nums[3]);
}

float calPostfix4(int nums[], int opts[])
{
    n++;
    return cal(opts[2], cal(opts[0], nums[0], nums[1]), cal(opts[1], nums[2], nums[3]));
}

float calPostfix5(int nums[], int opts[])
{
    n++;
    return cal(opts[2], cal(opts[1], cal(opts[0], nums[0], nums[1]), nums[2]), nums[3]);
}

// 循环写法
// 分别递归5种计算顺序和4个位置的10种数及3个位置的4种符号，总计4+3层循环，迭代次数10^4*4^3*5 = 320W
int search_loop(int k)
{
    int nums[4] = {0};
    int opts[3] = {0};
    int sum = 0;
    for (int i0 = 0; i0 < 10; ++i0)
        for (int i1 = 0; i1 < 10; ++i1)
            for (int i2 = 0; i2 < 10; ++i2)
                for (int i3 = 0; i3 < 10; ++i3)
                    for (int j0 = 0; j0 < 4; ++j0)
                        for (int j1 = 0; j1 < 4; ++j1)
                            for (int j2 = 0; j2 < 4; ++j2)
                            {
                                int nums[4] = {i0, i1, i2, i3};
                                int opts[3] = {j0, j1, j2};
                                try
                                {
                                    if (abs(calPostfix1(nums, opts) - (float)k) < 1e-4)
                                    {
                                        sum++;
                                    }
                                }
                                catch (const std::runtime_error &e)
                                {
                                }

                                try
                                {
                                    if (abs(calPostfix2(nums, opts) - (float)k) < 1e-4)
                                    {
                                        sum++;
                                    }
                                }
                                catch (const std::runtime_error &e)
                                {
                                }

                                try
                                {
                                    if (abs(calPostfix3(nums, opts) - (float)k) < 1e-4)
                                    {
                                        sum++;
                                    }
                                }
                                catch (const std::runtime_error &e)
                                {
                                }

                                try
                                {
                                    if (abs(calPostfix4(nums, opts) - (float)k) < 1e-4)
                                    {
                                        sum++;
                                    }
                                }
                                catch (const std::runtime_error &e)
                                {
                                }

                                try
                                {
                                    if (abs(calPostfix5(nums, opts) - (float)k) < 1e-4)
                                    {
                                        sum++;
                                    }
                                }
                                catch (const std::runtime_error &e)
                                {
                                }
                            }
    return sum;
}

// int dfs2(int nums[], int opts[], int loop, int k)
// {
//     int sum = 0;
//     opts[loop] = 0;
//     while (opts[loop] < 4)
//     {
//         if (loop < 2)
//         {
//             sum += dfs2(nums, opts, loop + 1, k);
//         }
//         if (loop == 2)
//         {
//             if (abs(calPostfix1(nums, opts) - (float)k) < 1e-4)
//             {
//                 sum++;
//             }
//             if (abs(calPostfix2(nums, opts) - (float)k) < 1e-4)
//             {
//                 sum++;
//             }
//             if (abs(calPostfix3(nums, opts) - (float)k) < 1e-4)
//             {
//                 sum++;
//             }
//             if (abs(calPostfix4(nums, opts) - (float)k) < 1e-4)
//             {
//                 sum++;
//             }
//             if (abs(calPostfix5(nums, opts) - (float)k) < 1e-4)
//             {
//                 sum++;
//             }
//         }
//         ++opts[loop];
//     }
//     return sum;
// }

// int dfs(int nums[], int loop, int k)
// {
//     int sum = 0;
//     nums[loop] = 0;
//     while (nums[loop] < 10)
//     {
//         if (loop < 3)
//         {
//             sum += dfs(nums, loop + 1, k);
//         }
//         if (loop == 3)
//         {
//             int opts[] = {0,0,0};
//             sum += dfs2(nums, opts, 0, k);
//         }
//         ++nums[loop];
//     }
//     return sum;
// }

// int search_dfs(int k)
// {
//     int nums[4] = {0};
//     return dfs(nums, 0, k);
// }

int main()
{
    cout<<search_loop(24)<<endl;
    cout<<n<<endl;
    return 0;
}