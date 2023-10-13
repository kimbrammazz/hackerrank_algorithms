def breakingRecords(scores):
    # Write your code here
    lowestRecord = scores[0]
    highestRecord = scores[0]

    breakingHighestRecord = 0
    breakingLowestRecord = 0

    for score in scores:
        if score > highestRecord:
            highestRecord = score
            breakingHighestRecord += 1

        if score < lowestRecord:
            lowestRecord = score
            breakingLowestRecord += 1

    return breakingHighestRecord, breakingLowestRecord
