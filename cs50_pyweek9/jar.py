class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._number = 0

    def __str__(self):
        cookies = "🍪" * self._number
        return f"The jar has {cookies} cookies."
    
    def deposit(self, n):
        if self._number + n > self._capacity:
            raise ValueError("Too many cookies!")
        self._number += n

    def withdraw(self, n):
        if n > self.number:
            raise ValueError("Not enough cookies!")
        self._number -= n

    @property
    def capacity(self):
        return self._capacity
    
    @property
    def number(self):
        return self._number
    
def main():
    jar = Jar()
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(3)
    print(jar)
    jar.deposit(2)
    print(jar)
    print(jar.capacity)
    print(jar.number)

if __name__ == "__main__":
    main()

