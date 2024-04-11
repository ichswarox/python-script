from PIL import ImageGrab
import time
# rename
import os
from datetime import datetime
import time

from win10toast import ToastNotifier


def rename_file_with_date(old_filename):
    """Renames a file with the current date appended to its name.

    Args:
      old_filename: The path to the file to be renamed.

    Returns:
      The new filename with the date appended.
    """

    # Get the current date in the desired format
    date_str = datetime.now().strftime("%Y-%m-%d-%H%M%S")  # YYYY-MM-DD format

    # Get the filename and extension
    filename, extension = os.path.splitext(old_filename)

    # Create the new filename with date appended
    new_filename = f"{filename}_{date_str}{extension}"

    # Rename the file using os.rename
    os.rename(old_filename, new_filename)

    return new_filename


im = ImageGrab.grabclipboard()
im.save('C:\downloads\#\#tex.png', 'PNG')


# time.sleep(2.5)
# Example usage
old_file = "C:\downloads\#\#tex.png"
new_file = rename_file_with_date(old_file)
print(f"Old filename: {old_file}")
print(f"New filename: {new_file}")


def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)


if __name__ == "__main__":
    title = "Notice"
    message = "Saved"
    show_notification(title, message)
