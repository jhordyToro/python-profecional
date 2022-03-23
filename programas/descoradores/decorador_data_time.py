from datetime import datetime

def time(func):
    def date(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        secuns = end_time - start_time
        print(f'el programa tardo {secuns.total_seconds()} segundos')
    return date
@time
def main():
    for _ in range(1000000000):
        pass

main()