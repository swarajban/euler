from typing import List, Dict, Optional
from collections import OrderedDict


def main():
    sieve = Sieve(2000000)
    primes = sieve.get_primes()
    sum_primes = sum(primes)
    print('Sum primes: {}'.format(sum_primes))


class Sieve:
    def __init__(self, max_prime: int):
        self.max_prime = max_prime  # type: int
        self.last_marked = None  # type: Optional[int]
        self.ints = OrderedDict()  # type: Dict[int, bool]
        for n in range(2, self.max_prime):
            self.ints[n] = False

    def get_primes(self) -> List[int]:
        self._mark_non_primes()
        primes = []  # type: List[int]
        for n, is_marked in self.ints.items():
            if not is_marked:
                primes.append(n)

        return primes

    def _mark_non_primes(self) -> None:
        p = 2
        while True:
            self._mark_p_intervals(p)
            p = self._next_unmarked(p)
            if p is None:
                break

    def _mark_p_intervals(self, p: int) -> None:
        for n in range(2 * p, self.max_prime, p):
            self.ints[n] = True

    def _next_unmarked(self, p: int) -> Optional[int]:
        if self.last_marked is None:
            self.last_marked = p
        # from last marked, go through ordered dict
        next_unmarked = self.last_marked + 1
        while next_unmarked < self.max_prime:
            if not self.ints[next_unmarked]:
                self.last_marked = next_unmarked
                return next_unmarked
            next_unmarked = next_unmarked + 1

        return None


if __name__ == '__main__':
    main()
