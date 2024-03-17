import unittest
import pandas as pd
import app.io.input as scanner


class TestFileInput(unittest.TestCase):
    def test_read_file(self):
        expected_data = "Some unique test data"
        test_file_name = "test_data/unique_test_file.txt"
        with open(test_file_name, "w") as file:
            file.write(expected_data)

        actual_data = scanner.read_from_file(test_file_name)
        self.assertEqual(actual_data, expected_data)

    def test_read_nonexistent_file(self):
        non_existent_file_name = "test_data/file_that_cannot_exists.txt"
        expected_data = f"File '{non_existent_file_name}' not found"

        actual_data = scanner.read_from_file(non_existent_file_name)
        self.assertEqual(actual_data, expected_data)

    def test_read_empty_file(self):
        empty_file_name = "test_data/empty_file.txt"
        with open(empty_file_name, "w") as file:
            pass

        actual_data = scanner.read_from_file(empty_file_name)
        self.assertEqual(actual_data, "")


class TestPandasFileInput(unittest.TestCase):
    def test_pandas_read_file(self):
        expected_data = "  Name  Id\n0  hot  90"
        test_file_name = "test_data/unique_pandas_test_file.csv"
        with open(test_file_name, "w") as file:
            file.write("Name,Id\nhot,90")

        actual_data = scanner.read_from_csv_file_with_pandas(test_file_name)
        self.assertEqual(actual_data, expected_data)

    def test_pandas_read_nonexistent_file(self):
        non_existent_file_name = "test_data/pandas_file_that_cannot_exists.csv"
        expected_data = f"File '{non_existent_file_name}' not found"

        actual_data = scanner.read_from_csv_file_with_pandas(non_existent_file_name)
        self.assertEqual(actual_data, expected_data)

    def test_pandas_read_empty_file(self):
        empty_file_name = "test_data/empty_pandas_file.csv"
        with open(empty_file_name, "w") as file:
            pass

        self.assertRaises(pd.errors.EmptyDataError, scanner.read_from_csv_file_with_pandas, empty_file_name)


if __name__ == "__main__":
    unittest.main()
