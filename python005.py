# linking the nodes

class lintnode:
    def _init_(self,data):
        self.data = data
        self.next = None
        
        class linkedlist:
    def _init_(self):
        self._start = None
        
        def insert(self,data):
    next_node = listnode(data)
    
    if self.start is None:
        self._current = next_node
        self._start = next_node
    else:
            self._current.next = next_node
            self._curent = next_node
            
            my_list = linkedlist()
            my_list.insert(25)
            
            my_list._start.data
my_list.insert(35)
my_list._start.next.data

def pretty_print(self):
    out_str = '['
    _cur = self._start
    while _cur is not None:
        out_str+=str(_cur.data)+","
        _cur = +cur.next
        return out_str.strip(',')+']'
        
        linkedlist.pretty_print = pretty_print  # dynamically adding a bound method to a class
        my_list = linkedlist()
        
        my_list.inser(5)
my_list.inser(7)
my_list.inser(8)

print my_list.preety print()

# call backs 
# we want to call a function on all the nodes

def print_square(node_x):
    print (node_x.data,"x",node_x.data,"=")
    print (node_x.data*node_x.data)
    print_square(my_list._start)
    
    def call_func(self,fn):
    _cur = self._start
    while _cur is not None:
        fn(_cur)
        _cur = _cur.next
        linklist.call_func = call_func
        
        my_list = linkedlist()
        
        my_list.inser(5)
my_list.inser(7)
my_list.inser(8)

print (my_list)

my_list.call_func(print_square)

def call_func(self,fn):
    _cur = self._start
    while _cur is not None:
        fn(_cur)
        _cur = _cur.next
        linklist.call_func = call_func
