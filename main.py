class Worker:
    def __init__(self, worker_id, head_id, name):
        self.id = worker_id
        self.name = name
        self.head_id = head_id
        self.slaves = []

    def append_slave(self, slave):
        self.slaves.append(slave)

    def __repr__(self):
        return self.name


def get_root_and_connect_workers(workers: dict):
    root = None

    for worker in workers.values():
        worker_head = workers.get(worker.head_id)
        if worker_head is not None:
            worker_head.append_slave(worker)
        else:
            root = worker

    return root


def print_tree(root):
    print(root.name)
    if root.slaves is not None:
        _print_slaves(slaves=root.slaves, nesting=0)


def _print_slaves(slaves, nesting):
    if slaves is not None:
        nesting += 1
        for slave in slaves:
            print("{indent} {worker_name}".format(indent="---" * nesting, worker_name=slave.name))
            _print_slaves(slave.slaves, nesting)
    else:
        nesting += -1

# Парсим файл в список, где каждый работник представлен в виде [id, head_id, name]
workers_parsed_data = [
    text.rstrip('\n').split('|') for text in open('1.txt', encoding='utf-8-sig', mode='r')
    ]

workers_by_id = {worker_id: Worker(worker_id, head_id, name) for worker_id, head_id, name in workers_parsed_data}

tree_root = get_root_and_connect_workers(workers_by_id)

print_tree(tree_root)
