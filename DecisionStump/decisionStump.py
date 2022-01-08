import sys
import csv
import random


class DTree:
    def __init__(
        self,
        train_input_path,
        test_input_path,
        split_index,
        train_output_path,
        test_output_path,
        metrics_output_path,
    ):
        self.train_input_path = train_input_pat
        self.test_input_path = test_input_path
        self.split_feature_index = int(split_index)
        self.train_output_path = train_output_path
        self.test_output_path = test_output_path
        self.metrics_output_path = metrics_output_path
        self.train_matrix = []
        self.test_matrix = []
        self.confusion_matrix = [[0, 0], [0, 0]]
        self.feature_space = []
        self.class_space = []

    def read_input_files(self):
        with open(self.train_input_path) as f:
            train_reader = csv.reader(f, delimiter="\t")
            for row in train_reader:
                self.train_matrix.append(row)

        with open(self.test_input_path) as f:
            test_reader = csv.reader(f, delimiter="\t")
            for row in test_reader:
                self.test_matrix.append(row)

    def generate_confusion_matrix(self):
        self.identify_feature_space()

        for index, row in enumerate(self.train_matrix[1:]):
            if (
                row[self.split_feature_index] == self.feature_space[0]
                and row[len(row) - 1] == self.class_space[0]
            ):
                self.confusion_matrix[0][0] += 1
            elif (
                row[self.split_feature_index] == self.feature_space[1]
                and row[len(row) - 1] == self.class_space[0]
            ):
                self.confusion_matrix[1][0] += 1
            elif (
                row[self.split_feature_index] == self.feature_space[0]
                and row[len(row) - 1] == self.class_space[1]
            ):
                self.confusion_matrix[0][1] += 1
            elif (
                row[self.split_feature_index] == self.feature_space[1]
                and row[len(row) - 1] == self.class_space[1]
            ):
                self.confusion_matrix[1][1] += 1

    def identify_feature_space(self):
        for row in self.train_matrix[1:]:
            self.feature_space.append(row[self.split_feature_index])
            self.class_space.append(row[len(row) - 1])

        self.feature_space = list(set(self.feature_space))
        self.class_space = list(set(self.class_space))

    def classify_datasets(self):
        train_prediction_labels, training_error_rate = self.classify(
            self.train_matrix[1:]
        )
        self.print_labels(self.train_output_path, train_prediction_labels)
        test_prediction_labels, test_error_rate = self.classify(
            self.test_matrix[1:]
        )
        self.print_labels(self.test_output_path, test_prediction_labels)
        self.print_metrics(training_error_rate, test_error_rate)

    def print_metrics(self, training_error_rate, test_error_rate):
        with open(self.metrics_output_path, "w") as f:
            f.write(
                "error(train): " + "{0:.6f}".format(training_error_rate) + "\n"
            )
            f.write("error(test): " + "{0:.6f}".format(test_error_rate))

    def classify(self, dataset):
        resultant_labels = []
        errors = 0
        for row in dataset:
            feature_space_index = self.feature_space.index(
                row[self.split_feature_index]
            )
            if (
                self.confusion_matrix[feature_space_index][0]
                > self.confusion_matrix[feature_space_index][1]
            ):
                prediction = self.class_space[0]
            elif (
                self.confusion_matrix[feature_space_index][0]
                < self.confusion_matrix[feature_space_index][1]
            ):
                prediction = self.class_space[1]
            else:
                prediction = random.choice(self.class_space)
            if prediction != row[len(row) - 1]:
                errors += 1
            resultant_labels.append(prediction)

        return resultant_labels, errors / len(dataset)

    def print_labels(self, file_path, labels):
        with open(file_path, "w") as f:
            for label in labels:
                f.write(label + "\n")


if __name__ == "__main__":

    d_tree = DTree(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4],
        sys.argv[5],
        sys.argv[6],
    )

    d_tree.read_input_files()
    d_tree.generate_confusion_matrix()
    d_tree.classify_datasets()
