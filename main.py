class FileUtils:
    @classmethod
    def count_lines(cls, file_path):
        try:
            with open(file_path, 'r') as file:
                line_count = sum(1 for line in file)
            return line_count
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return -1
        except Exception as e:
            print(f"An error occurred: {e}")
            return -1