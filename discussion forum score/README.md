# Discussion Forum Final Score

This function includes how do we generate final score for discusssion forum attendence.

# How do we get the result:

## Get comment information and comment id from database:
1. importsql.py: Load id, body from commentthread, output AndroidBody1 and JavaBody1.
2. AndroidBody1.txt: Contain id, body for android
3. JavaBody1.txt: Contain id, body for java

## Match keyword with comment body

1. MatchingKeyWord.py: Find matched comment and output comment id
2. keyword_tableJava.txt: Contain matched comment id for java
3. keyword_tableAndroid.txt: Contain matched comment id for android

## Compute staff reply ratio within comments comtaining keywords

1. GetCommentID.py: Get all comments with both staff reply and keywords containing
2. staffcomment102_1x_4T2015.txt & staffcomment107x_1T2016_c.txt will also be used in this section, the detail description for these two files can be found in StaffAttend file
