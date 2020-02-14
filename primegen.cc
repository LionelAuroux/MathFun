#include <iostream>
#include <vector>
#include <math.h>
#include <sys/time.h>

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
    char *ary = new char[maxval];
    vector<int64_t> prime_list;

    cout << "SQRT MAX:" << sqrt_max << endl;
    struct timeval  tv;
    suseconds_t usec;
    gettimeofday(&tv, NULL);
    usec = tv.tv_usec;
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
    gettimeofday(&tv, NULL);
    usec = tv.tv_usec - usec;
    cout << "list0 " << usec << endl;
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
    auto ary = new int64_t[maxval];
    auto prime_rest = new int64_t[maxval];

    ary[0] = 2;
    int64_t len = 1;
    prime_rest[0] = 1;
    int64_t cnt = 3;
    struct timeval  tv;
    suseconds_t usec;
    gettimeofday(&tv, NULL);
    usec = tv.tv_usec;
    while (true)
    {
        bool is_prime = true;
        int64_t idx = 0;
        cout << "compo:" << cnt << endl;
        uint64_t next = ~0;
        for (int64_t it = 0; it < len; it += 1)
        {
            prime_rest[idx] += 2; 
            if (prime_rest[idx] != 1 && prime_rest[idx] < next)
                next = prime_rest[idx];
            if (prime_rest[idx] >= ary[it])
                prime_rest[idx] -= ary[it];
            cout << ary[it] << ": " << prime_rest[idx];
            if (it + 1 < len)
                cout << ", ";
            if (!prime_rest[idx])
                is_prime = false;
            idx += 1;
        }
        cout << endl;
        if (is_prime)
        {
            cout << "next: " << (cnt + next) << endl;
            ary[len] = cnt;
            prime_rest[idx] = 0;
            len += 1;
        }
        if (cnt >= maxval)
            break;
        cnt += 2;
    }
    gettimeofday(&tv, NULL);
    usec = tv.tv_usec - usec;
    cout << "list1 " << usec << endl;
    for (int64_t i = 0; i < len; i += 1)
        prime_list.push_back(ary[i]);
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
