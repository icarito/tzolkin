from notify.all import *

def inform_of_frobnicator (frobnicator_type, num_tentacles):
    print ("A frobnicator of type '%s' with %d tentacles has arrived"
           % (frobnicator_type, num_tentacles))

total_tentacles = 0

def count_tentacles (frobnicator_type, num_tentacles):
    global total_tentacles
    total_tentacles += num_tentacles
    print 'Total tentacles so far: %s' % total_tentacles

def run_if_scary (frobnicator_type, num_tentacles):
    if frobnicator_type == 'Slimy':
        print 'I panic'
        import sys
        sys.exit ()

new_frobnicator = Signal ()
new_frobnicator.connect (inform_of_frobnicator)
new_frobnicator.connect (count_tentacles)
new_frobnicator.connect (run_if_scary)

new_frobnicator ('Friendly', 8)
new_frobnicator ('Sleepy',   4)
new_frobnicator ('Slimy',    12)
new_frobnicator ('Hungry',   6)
