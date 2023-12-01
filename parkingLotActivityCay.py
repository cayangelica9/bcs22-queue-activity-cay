class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.QList = [None] * capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.isFull():
            print("The parking lot is full. Cannot park more cars.")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.QList[self.rear] = item
        self.size = self.size + 1
        print("%s parked in the parking lot." % str(item))

    def dequeue(self):
        if self.isEmpty():
            print("Parking lot is empty. No cars to remove.")
            return None
        item = self.QList[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1
        print("%s left the parking lot." % str(item))
        return item

    def queueFront(self):
        if self.isEmpty():
            print("Parking lot is empty.")
        else:
            print("Front car in the parking lot is", self.QList[self.front])

    def queueRear(self):
        if self.isEmpty():
            print("Parking lot is empty.")
        else:
            print("Rear car in the parking lot is", self.QList[self.rear])

    def displayStatus(self):
        if self.isEmpty():
            print("Parking lot is empty.")
        else:
            print("Current parking lot status:")
            for i in range(self.front, self.front + self.size):
                print(self.QList[i % self.capacity], end=" ")
            print()

    def totalCapacity(self):
        return self.capacity


if __name__ == '__main__':
    capacity = int(input("Enter the capacity of the parking lot: "))
    queue = Queue(capacity)

    while True:
        print("\nMenu:")
        print("1. Park a car")
        print("2. Remove a car")
        print("3. Display front car")
        print("4. Display rear car")
        print("5. Display current status")
        print("6. Display total capacity")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ")

        if choice == "1":
            car = input("Enter the car to park: ")
            queue.enqueue(car)
        elif choice == "2":
            removed_item = queue.dequeue()
            if removed_item is not None:
                print("Removed item:", removed_item)
        elif choice == "3":
            queue.queueFront()
        elif choice == "4":
            queue.queueRear()
        elif choice == "5":
            queue.displayStatus()
        elif choice == "6":
            print("Total parking capacity:", queue.totalCapacity())
        elif choice == "0":
            print("Exiting the parking lot simulation. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")
