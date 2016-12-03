def find_missing(firstList, secondList):
    extraList = []
    lesserList = []
    if len(firstList) > len(secondList):
        extraList = firstList
        lesserList = secondList
    else:
        extraList = secondList
        lesserList = firstList
    extraNumber = [x for x in extraList if x not in lesserList]
    if len(extraNumber) == 0:
        return 0
    return extraNumber.pop()
