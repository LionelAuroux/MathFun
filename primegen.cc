#include <iostream>
#include <vector>
#include <math.h>

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
            prime_list.push_back(cnt);
            prod *= cnt;
        }
        cnt += 2;
    }
    return prime_list;
}

vector<int64_t> get_prime_list0(int64_t maxval)
{
    int64_t sqrt_max = (int64_t) sqrt((double)maxval) + 1;
    int64_t msize = maxval;
    char *ary = new char[msize];
    vector<int64_t> prime_list;

    cout << "SQRT MAX:" << sqrt_max << endl;
    for (int64_t i = 3; i < sqrt_max; i += 2)
    {
        if (!ary[i])
        {
            int64_t j = i * 2;
            while (j < maxval)
            {
                ary[j] = 1;
                j += i;
            }
        }
    }
    prime_list.push_back(2);
    for (int64_t i = 3; i < maxval; i += 2)
    {
        if (!ary[i])
            prime_list.push_back(i);
    }
    return prime_list;
}

vector<int64_t> get_prime_list2(int64_t maxval)
{
    vector<int64_t> prime_list;
    vector<int64_t> prime_rest;

    prime_list.push_back(2);
    prime_rest.push_back(1);
    int64_t cnt = 3;
    while (true)
    {
        bool is_prime = true;
        int64_t idx = 0;
        for (auto it: prime_list)
        {
            prime_rest[idx] += 2; 
            if (prime_rest[idx] >= it)
                prime_rest[idx] -= it;
            if (!prime_rest[idx])
                is_prime = false;
            idx += 1;
        }
        if (is_prime)
        {
            prime_list.push_back(cnt);
            prime_rest.push_back(0);
        }
        if (cnt >= maxval)
            break;
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
    int64_t maxval = 1000000;
    if (ac >= 2)
        maxval = atoi(av[1]);
    auto ls1 = get_prime_list0(maxval);
    auto ls2 = get_prime_list2(maxval);
    int64_t idx = 0;
    for (auto it: ls1)
    {
        cout << it << " -- " << ls2[idx] << endl;
        idx += 1;
    }
    return 0;
}
