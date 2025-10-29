---
title: 使用Python.NET在多线程中同时读取单元格值
linktitle: 多线程
type: docs
weight: 1800
url: /zh/python-net/reading-cell-values-in-multiple-threads-simultaneously/
description: 了解如何使用Aspose.Cells for Python via .NET API在多个线程中同时读取单元格值。
keywords: 在多个线程中同时读取单元格值，Aspose.Cells Python多线程，读取多线程中的数据
---

{{% alert color="primary" %}}

需要同时在多个线程中读取单元格值是一个常见的需求。本文解释了如何使用Aspose.Cells来实现这一目的。

{{% /alert %}}

要在多个线程中同时读取单元格值，请将 [**worksheet.cells.multi_thread_reading**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/multi_thread_reading/) 设置为 **True**。否则，可能会得到错误的单元格值。

以下代码：

1. 创建工作簿
1. 添加工作表
1. 用字符串值填充工作表
1. 创建两个线程，分别同时读取随机单元格的值
   如果读取的值是正确的，则不会发生任何事情。如果读取的值不正确，则会显示一条消息。

如果您注释掉这一行：

```python
test_workbook.worksheets[0].cells.multi_thread_reading = True
```

然后会触发以下消息检查：

```python
if s != f"R{row}C{col}":
    print("This message will show when cells read values are incorrect")
```

否则，程序将在不显示任何消息的情况下运行，这意味着从单元格中读取的所有值都是正确的。

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
