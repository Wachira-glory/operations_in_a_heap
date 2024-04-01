import heapq

#create an empty heap
heap = []

#inserting items into the heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)

print("Heap after inserting items:",heap)

#delete items drom the heap
print ("Heap before deletion:", heap)
item_deleted = heapq.heappop(heap)
print("Deleted item:", item_deleted)
print("Heap after deletion:", heap)

#accesssing the smallest item in the heap
smallest_item = heap[0]
print("smallest item in the heap;",smallest_item)
