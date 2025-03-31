#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

// �ṹ�����ڴ洢��ѯ���
class Text {
public:
    int page;       // ҳ��
    string chapter; // �½�
    string book;    // ����
    string content; // ����
};

vector <Text> text;
Text TempContent;

// ��ȡ�ļ����洢��text��
void readBooks(const vector<string>& filenames) {

    for (string filename : filenames) {
        TempContent.book = filename; // �����ļ�����Ϊ����
        TempContent.page = 1;
        TempContent.chapter = "Chapter Zero";


        ifstream file;
        file.open(filename+".txt");
        if (!file.is_open()) {
            cerr << "�޷����ļ���" << filename << endl;
            continue;
        }

        int page_num;
        string line;
        bool isChapter_begin = true;

        while (getline(file, line)) {
            if (line.substr(0,7) == "Chapter" || line.substr(0,7) == "CHAPTER") {
                TempContent.chapter = line;
            }
            else if ('0' < line[0] && line[0] <= '9' && line.size() < 4){
                istringstream ss(line);
                ss >> page_num;
                TempContent.page = page_num + 1;
            }
            else {
                TempContent.content = line;
                text.push_back(TempContent);
            }
        }
        file.close();
    }
}

// ����������������/�������ı��еĳ���λ�ò���¼�����Ϣ
void searchNameInBooks(string info, vector<int> & s)    //������Ϣ
{
    int all_len = text.size();
    string::size_type p;
    for (int i = 0; i < all_len; i++)
    {
        p = text[i].content.find(info);
        while (!(p == string::npos)){
            s.push_back(i);
            p = text[i].content.find(info,p+1);
        }

    }
}

// ����������ʾ��ѯ���
void displayResults(vector<int> s, string info) {
    cout << "���       ����/����       ҳ��       �½�       ����" << endl;
    for (int i = 0; i < s.size(); i++)
        cout << "  "
             << i + 1           << "\t"
             << info            << "\t"
             << text[s[i]].page       << "\t"
             << text[s[i]].chapter    << "\t"
             << text[s[i]].book   << endl;
}

int main() {
    // ��������ϵ���鼮�ļ���
    vector<string> filenames = {
            "HP2--Harry_Potter_and_the_Chamber_of_Secrets_Book_2_",
            "HP7--Harry_Potter_and_the_Deathly_Hallows_Book_7_",
            "J.K. Rowling - HP 0 - Harry Potter Prequel",
            "J.K. Rowling - HP 3 - Harry Potter and the Prisoner of Azkaban",
            "J.K. Rowling - HP 4 - Harry Potter and the Goblet of Fire",
            "J.K. Rowling - HP 6 - Harry Potter and the Half-Blood Prince",
            "J.K. Rowling - Quidditch Through the Ages",
            "J.K. Rowling - The Tales of Beedle the Bard"
    };

    // ��ȡ�ı��ļ�����
    readBooks(filenames);

    // �û�����Ҫ��ѯ������/����
    string info;
    cout << "������Ҫ��ѯ������/������";
    cin >> info;

    // ��������/����
    vector<int> search_Info;
    searchNameInBooks(info, search_Info);

    // ��ʾ��ѯ���
    if (!search_Info.empty())
    {
        displayResults(search_Info, info);
        cout << endl << "������Ҫ��ʾ�Ķ�������: " << endl;
        while (1)
        {
            int x = 1;
            cin >> x;
            if (x == 0)
                break;
            cout << endl << text[search_Info[x - 1]-1].content << endl << text[search_Info[x - 1]].content << endl;
            cout << endl << "��Ҫ������ʾ����������������ţ��������� 0:" << endl;
        }
    }
    else
        cout << "�޷���ѯ�� ! ! !" << endl;
    return 0;

}

