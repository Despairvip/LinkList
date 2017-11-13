class Node(object):
    def __init__(self, item):
        self.item = item

class SingleLinkList(object):
    def __init__(self):
        self.__head = None


    def is_empty(self):
        '''
        链表是否为空
        :return:
        '''
        return self.__head is None


    def length(self):
        '''
        长度查询
        :return:
        '''
        cur = self.__head
        content = 0
        while cur is not None:
            content += 1
            cur = cur.next
        return content

    def travel(self):
        '''
        遍历
        :return:
        '''
        # 创建游标　指向下一个数
        cur = self.__head
        while cur is not None:
            # 输出当前节点的内容
            print(cur.item, end=' ')
            cur = cur.next
        print()

    def add(self, item):
        '''
        从头部添加数据
        :param item: 用户输入的数据
        :return:
        '''
        # 1、创建新节点
        node = Node(item)
        # 2、让新节点的next指向老节点
        node.next = self.__head
        # 3、让头节点指向新节点
        self.__head = node

    def append(self, item):
        '''
        从尾部添加数据
        :param item:用户输入
        :return:
        '''
        # 判断是否有数据
        if self.is_empty():
            self.add(item)
        else:
            # 获取最后一个节点
            cur = self.__head
            while cur is not None:
                cur = cur.next
            node = Node(item)
            cur.next = node

    def insert(self, pos, item):
        '''
        指定位置添加元素
        :param pos: 指定位置的下标
        :param item: 用户输入
        :return:
        '''
        # 判断输入位置的正负
        if pos < 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            # 插入到中间节点
            # 找出当前节点的前一个节点
            cur = self.__head
            index = 0
            while index < (pos - 1):
                cur = cur.next
                index += 1
            node = Node(item)
            # 让新节点的ｎｅｘｔ指向老节点所指的对象
            node.next = cur.next
            # 让原来指向老节点的对象指向新的节点
            cur.next = node

    def remove(self, item):
        '''
        删除节点
        :param item: 用户输入
        :return:
        '''
        # 遍历链表，找到要删除的节点，
        # 找到要删除节点的前一个节点
        cur = self.__head
        # 前一个节点对象
        pre = None
        while cur is not Node:
            # 判断当前数据是否是匹配需要删除的数据
            if cur .item == item:
                # 判断pre是否为Ｎｏｎｅ，如果是，就说明删除的是首节点
                if pre == None:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
            pre = cur
            cur = cur.next


    def search(self, item):
        '''
        搜索数据是否在链表中
        :param item: 用户输入
        :return:
        '''
        # 循环查找
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__ == '__main__':
    c = SingleLinkList()
    c.add(1)
    print(c.is_empty())
    print(c.travel())

