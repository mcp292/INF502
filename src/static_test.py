class Counter():
    count = 0
    
    def __init__(self):
        Counter.count += 1
    

# main()
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()

print(counter3.count)  # 3
print(Counter.count)   # 3
        
