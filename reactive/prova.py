from reactivex import Observable
import rx
import rx.operators as ops

# creates an observable from a list
source = rx.from_iterable([1,2,3,4,5])

# now we create a computational graph composed by 2 operators
observable = source.pipe(
    # decrements every item by one
    ops.map(lambda i : i-1),
    # take only the even items
    ops.filter(lambda i : i % 2 == 0)
)

# The pipe operator allows to chain together operators
# map and filter take functions as parameters

# until we subscribe to the Observable nothing will happen
# We can do so by calling the method subscribe and passing 
# the callbacks that will be called at different times(on_next,on_completed,on_error)

disposable = observable.subscribe(
    on_next = lambda i : print("items: {}".format(i)),
    on_completed = lambda : print("completed"),
    on_error = lambda e : print("error:{}".format(e))
)
