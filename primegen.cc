#include <iostream>
#include <vector>

using namespace std;

bool isrelatprime(int64_t prod, int64_t cnt)
{
    int64_t res = prod % cnt;
    if (res == 1)
        return true;
    if (res == 0)
        return false;
    return isrelatprime(cnt, res);
}

vector<int64_t> get_prime_list(int64_t maxval)
{
    vector<int64_t> prime_list;

    prime_list.push_back(2);
    prime_list.push_back(3);
    int64_t prod = 2 * 3;
    int64_t cnt = 5;
    while (true)
    {
        if (cnt >= maxval)
            break;
        if (isrelatprime(prod, cnt))
        {
            cout << cnt << endl;
            prime_list.push_back(cnt);
            prod *= cnt;
        }
        cnt += 2;
    }
    return prime_list;
}

ostream &operator<<(ostream &o, vector<int64_t> &ls)
{
    for (auto it: ls)
    {
        o << it << endl;
    }
    return o;
}

int main(int ac, char *av[])
{
    int64_t maxval = 1000;
    if (ac >= 2)
        maxval = atoi(av[1]);
    auto ls = get_prime_list(maxval);
    //cout << ls << endl;
    return 0;
}
