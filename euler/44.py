from typing import Dict
import math


def main():
    n = 1
    found = False
    while not found:
        pj = pent(n)
        for k in reversed(range(1, n)):
            pk = pent(k)
            p_sum = pj + pk
            is_sum_pent = is_pent(p_sum)
            if is_sum_pent:
                p_diff = pj - pk
                is_diff_pent = is_pent(p_diff)
                if is_diff_pent:
                    print('j: {}, pj: {}, k: {}, pk: {}, diff: {}'.format(n, pj, k, pk, p_diff))
                    found = True
                    break
        n = n + 1

    print('done')


def is_pent(x: int) -> bool:
    n = (math.sqrt(24 * x + 1) + 1) / 6
    return n.is_integer()


PENT_MAP = {}  # type: Dict[int, int]


def pent(n: int) -> int:
    if n in PENT_MAP:
        return PENT_MAP[n]
    else:
        pent_n = int(n * (3 * n - 1) / 2)
        PENT_MAP[n] = pent_n
        return pent_n


if __name__ == '__main__':
    main()
