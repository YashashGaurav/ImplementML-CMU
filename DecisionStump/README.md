# Decision Stump

## Algorithm and problem statement

This simple algorithm acts as a precursor to the Decision Tree.

A Decision Stump is simply a decision tree of depth one (it predicts a class label for the input instance based on testing just one of the instance’s attributes). You may assume that the attribute to be tested by your Decision Stump is provided as input to your program (on the command line). Your algorithm should partition the provided training data based on that attribute. You may assume that the attributes are always binary and that the output class label is always binary. As such, the left branch of your trained decision stump should assign a class label corresponding the majority label among the training examples that sort down that branch. The right branch should do likewise for the other value of the attribute. The training procedure should store the decision stump data structure for use at test time. In case of a tie in majority vote, you may output either of the two values or pick randomly between them.
At test time, each example should be passed down through the stump. Its label becomes the label (i.e. the stored majority vote) of the corresponding branch in which it lands.

## The Datasets

The input contains three datasets. Each one contains attributes and labels and is already split into training and testing data. The first line of each .tsv file contains the name of each attribute, and the class label is always the last column.

- small: including small_train.tsv and small_test.tsv — a small, purely for demonstration version of the actual datasets, with sample attributes.s

## Command Line Arguments

python3 decisionStump.py [args...]

Where above [args...] is a placeholder for six command-line arguments: <train_input_path> <test_input_path> <spltting_index> <train_output_path> <test_output_path> <metrics_output_path>:
1. <train_input_path>: path to the training input .tsv file
2. <test_input_path>: path to the test input .tsv file
3. <spltting_index>: the index of feature at which we split the dataset. The first column has index 0, the second column index 1, and so on.
4. <train_output_path>: path of output .labels file to which the predictions on the training data should be written
5. <test_output_path>: path of output .labels file to which the predictions on the test data should be written
6. <metrics_output_path>: path of the output .txt file to which metrics such as train and test error should be written

## Output: Labels Files

Your program should write two output .labels files containing the predictions of your model on training data and test data. Each should contain the predicted labels for each example printed on a new line. Use ’\n’ to create a new line.

## Output: Metrics File

Generate another file where you should report the training error and testing error. This file should be written to the path specified by the command line argument <metrics_output_path>. Your reported numbers should be within 0.01 of the reference solution. The file should be formatted as follows:
    
    error(train): 0.241611
    error(test): 0.228916
