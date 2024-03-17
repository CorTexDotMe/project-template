import app.io.input
import app.io.output


def main():
    console_text = app.io.input.read_from_console()
    file_text = app.io.input.read_from_file("data/input.txt")
    pandas_file_text = app.io.input.read_from_file_with_pandas("data/input.txt")

    app.io.output.write_to_console(f"From console: {console_text}")
    app.io.output.write_to_console(f"From file: {file_text}")
    app.io.output.write_to_console(f"From file with pandas: {pandas_file_text}")

    app.io.output.write_to_file(console_text, "data/output_console_text.txt")
    app.io.output.write_to_file(file_text, "data/output_file_text.txt")
    app.io.output.write_to_file(pandas_file_text, "data/output_pandas_file_text.txt")


if __name__ == '__main__':
    main()
