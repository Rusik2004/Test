def chop(lst):
    if len(lst) >= 2:
        del lst[0]
        del lst[-1]

def middle(lst):
    if len(lst) >= 2:
        return lst[1:-1]
    else:
        return []

my_list = [1, 2, 3, 4]

print("my list before calling chop function =>", my_list)
chop(my_list)
print("my list after calling chop function =>", my_list)
my_list = [1, 2, 3, 4]
print("\nmy list before calling middle function =>", my_list)
new_list = middle(my_list)
print("my list after calling middle function =>", my_list)
print("new list after calling middle function =>", new_list)