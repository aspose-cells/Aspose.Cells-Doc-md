---
title: Reading Cell Values in Multiple Threads Simultaneously with Python.NET
linktitle: Multiple Threads
type: docs
weight: 1800
url: /python-net/reading-cell-values-in-multiple-threads-simultaneously/
description: Learn how to read cell values in multiple threads simultaneously using Aspose.Cells for Python via .NET API.
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells Python Multiple Threads, Read data in Multiple Threads
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Needing to read cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.

{{% /alert %}}

To read cell values in more than one thread simultaneously, set [**worksheet.cells.multi_thread_reading**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/multi_thread_reading/) to **True**. If you do not, you might get the wrong cell values.

The following code:

1. Creates a workbook
1. Adds a worksheet
1. Populates the worksheet with string values
1. Creates two threads that simultaneously read values from random cells
   If the values read are correct, nothing happens. If the values read are incorrect, then a message is displayed.

If you comment this line:

```python
test_workbook.worksheets[0].cells.multi_thread_reading = True
```

then the following message check will trigger:

```python
if s != f"R{row}C{col}":
    print("This message will show when cells read values are incorrect")
```

Otherwise, the program runs without showing any message which means all values read from cells are correct.

```python
import threading
import random
import time
from aspose.cells import Workbook

test_workbook = None

def thread_loop():
    rand = random.Random()
    while True:
        try:
            row = rand.randint(0, 9999)
            col = rand.randint(0, 99)
            s = test_workbook.worksheets[0].cells.get(row, col).string_value
            if s != f"R{row}C{col}":
                print("This message will show up when cells read values are incorrect.")
        except:
            pass

def test_multi_threading_read():
    global test_workbook
    test_workbook = Workbook()
    test_workbook.worksheets.clear()
    test_workbook.worksheets.add("Sheet1")

    for row in range(10000):
        for col in range(100):
            test_workbook.worksheets[0].cells.get(row, col).value = f"R{row}C{col}"

    # Commenting this line will show a pop-up message
    # test_workbook.worksheets[0].cells.multi_thread_reading = True

    my_thread1 = threading.Thread(target=thread_loop, daemon=True)
    my_thread1.start()

    my_thread2 = threading.Thread(target=thread_loop, daemon=True)
    my_thread2.start()

    time.sleep(5)  # Sleep for 5 seconds

if __name__ == "__main__":
    test_multi_threading_read()
```

{{< app/cells/assistant language="python-net" >}}
