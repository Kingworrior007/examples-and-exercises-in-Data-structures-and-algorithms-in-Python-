

class LNode(object):
    # 单链表节点类
    def __init__(self, item, next = None):
        self.item = item
        self.next = next


class LinkedListUnderFlow(ValueError):
    # 自定义异常类
    pass


class LList(object):
    # 单链表类
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    # def prepend(self,item):
    #     new_node = LNode(item)
    #     new_node._next = self.head
    #     self.head = new_node
    def prepend(self, item):
        """头部添加节点"""
        self.head = LNode(item, self.head)

    def pop(self):
        """pop 头元素"""
        if self.is_empty():
            raise LinkedListUnderFlow('in pop')
        e = self.head.item
        self.head = self.head.next
        return e

    def append(self, item):
        """尾部添加节点"""
        new_node = LNode(item)
        if self.head is None:
            self.head = new_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node

    def pop_last(self):
        """pop 尾节点元素"""
        if self.head is None:
            raise LinkedListUnderFlow
        p = self.head
        if p.next is None:
            while p.next:
                p = p.next
            e = p.item
            self.head = None
            return e
        else:
            while p.next.next is not None:
                p = p.next
            e = p.next.item
            p.next = None
            return e

    def length(self):
        n = 0
        p = self.head
        while p is not None:
            p = p.next
            n += 1
        return n

    def insert(self, item, i):
        """插入元素到给定位置,重点理解"""
        if i <= 0:
            self.prepend(item)
        elif i >= self.length():
            self.append(item)
        else:
            p = self.head
            new_node = LNode(item)
            while p.next is not None and i > 1:
                p = p.next
                i -= 1
            new_node.next = p.next
            p.next = new_node

    def remove(self, item):
        """删除第一个给定元素"""
        if self.head.item == item:
            self.head = self.head.next
        else:
            pre = self.head
            p = self.head.next
            while p is not None:
                if p.item == item:
                    pre.next = p.next
                    break
                else:
                    pre = p
                    p = p.next

    def remove_all(self,item):
        """删除全部给定元素"""
        while self.head.item == item:
            self.head = self.head.next
        pre = self.head
        p = self.head.next
        while p is not None:
            while p is not None and p.item == item:
                p = p.next
            pre.next = p
            if p is not None:
                pre = p
                p = p.next

    def find(self,pred):
        """找到满足一定条件的（第一个）元素"""
        p = self.head
        while p is not None:
            if pred(p.item):
                return p.item
            p = p.next
        return -1

    def printall(self):
        """打印全部元素"""
        p = self.head
        while p is not None:
            if p.next is not None:
                print(p.item,end=' ')
            else:
                print(p.item)
            p = p.next

    def proc_all(self, proc):
        """表的遍历-->对全部元素执行操作"""
        p = self.head
        while p is not None:
            proc(p.item)
            p = p.next

    def elements(self):
        """表的遍历-->生成器"""
        p = self.head
        while p is not None:
            yield p.item
            p = p.next

    def filter(self, proc):
        """表的遍历-->筛选器"""
        p = self.head
        while p is not None:
            if proc(p.item):
                yield p.item
            p = p.next

    def reverse(self):
        """反转链表"""
        q = None
        while self.head is not None:
            p = self.head
            self.head = self.head.next
            p.next = q
            q = p
        self.head = q

    def _sort1(self):
        """单链表插入排序，继承到其他类需要修改"""
        if self.head is None:
            return
        cur = self.head.next
        while cur is not None:
            p = self.head
            x = cur.item
            while p is not cur and p.item < x:
                p = p.next
            while p is not cur:
                y = p.item
                p.item = x
                x = y
                p = p.next
            # 在循环开始前x里保存的是cur.item的值，循环结束后x是cur.item应该有的值，但是需要将这个值赋给cur.item
            cur.item = x
            cur = cur.next




if __name__ == '__main__':
    alist = LList()
    for i in range(10):
        alist.prepend(i)
    for i in range(10,20):
        alist.prepend(i)
    alist.printall()
    # a = 'a'
    # alist.insert(a, 0)
    # alist.insert(a, 0)
    # alist.insert(a, 5)
    # alist.insert(a, 5)
    # alist.insert(a, 5)
    # alist.insert(a, 20)
    # alist.insert(a, 20)
    # alist.insert(a, 20)
    # alist.printall()
    print('length:',alist.length())
    # for i in range(10):
    #     ret = alist.pop_last()
    #     print(ret)

    # alist.remove('a')
    # alist.remove_all('a')
    # alist.reverse()
    alist._sort1()
    alist.printall()
    print('length:', alist.length())



    # for i in alist.elements():
    #     print(i*2)

    # ret = alist.filter(lambda x:x%3 == 0)
    # for i in ret:
    #     print(i)

    # ret = alist.find(lambda x: x>3 and x % 2 == 0)
    # print(ret)









