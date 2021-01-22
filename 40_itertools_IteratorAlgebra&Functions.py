'''Itertools functions operate on iterators to produce more complex iterators
1. zip(): Takes any number of iterables as arguments while returning an iterator over tuple 
of their respective elements.'''

zipUtility = list(zip([1, 2, 3], ['a', 'b', 'c']))
print(zipUtility)


''' 2. map() is another built in function that works by returning an iterator object when called
on an iterable (second argument) and advances this iterator with next() until iterator gets exhausted. '''

mapUtility = list(map(len, ['abc', 'de', 'fghi']))
print(mapUtility)

'''iter() Returns iterator object for that iterable'''

iterUtility = iter([1, 2, 3, 4])
print(iterUtility)

