def load_classes():
    import cPickle
    path = 'cifar-10-batches-py/'
    file = 'batches.meta'
    
    f = open(path+file, 'rb')
    dict = cPickle.load(f)
    return dict['label_names']

def print_classes(classes):
    for i in range(0, 10):
        print str(i) + " : " + classes[i] + "  "

ln = load_classes()
print_classes(ln)