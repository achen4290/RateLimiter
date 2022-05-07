from ratelimiter import RateLimiter
import time

RL = RateLimiter()
RL.create_event("upload", max_calls=1, unit_time=15)


def check(delay, user):
    time.sleep(delay)
    print(RL.valid_call("upload", user))


if __name__ == '__main__':
    # Tests
    check(0, "a")  # True
    check(2, "a")  # False
    check(0, "b")  # True
    check(15, "a")  # True
    check(0.1, "b")  # True
    check(10, "a")  # False
    check(0, "b")  # False
    check(0, "c")  # True
