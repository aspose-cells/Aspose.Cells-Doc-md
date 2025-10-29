---
title: Чтение значений ячеек в нескольких потоках одновременно с помощью Python.NET
linktitle: Несколько потоков
type: docs
weight: 1800
url: /ru/python-net/reading-cell-values-in-multiple-threads-simultaneously/
description: Узнайте, как считывать значения ячеек в нескольких потоках одновременно с помощью API Aspose.Cells для Python via .NET.
keywords: Чтение значений ячеек в нескольких потоках одновременно, Aspose.Cells Python Многопоточное чтение данных
---

{{% alert color="primary" %}}

Необходимость чтения значений ячеек в нескольких потоках одновременно - это распространенная потребность. В этой статье объясняется, как использовать Aspose.Cells для этой цели.

{{% /alert %}}

Чтобы читать значения ячеек в нескольких потоках одновременно, установите [**worksheet.cells.multi_thread_reading**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/multi_thread_reading/) в значение **True**. Если этого не сделать, вы можете получить неправильные значения ячеек.

Следующий код:

1. Создает рабочую книгу
1. Добавляет лист
1. Заполняет лист строковыми значениями
1. Создает два потока, которые одновременно читают значения из случайных ячеек
   Если прочитанные значения правильные, ничего не происходит. Если прочитанные значения неправильные, то отображается сообщение.

Если вы закомментируете эту строку:

```python
test_workbook.worksheets[0].cells.multi_thread_reading = True
```

затем сработает следующее сообщение:

```python
if s != f"R{row}C{col}":
    print("This message will show when cells read values are incorrect")
```

В противном случае программа работает без отображения любого сообщения, что означает, что все значения, считываемые из ячеек, являются правильными.

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
