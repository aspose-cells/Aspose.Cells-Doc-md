---
title: قراءة قيم الخلايا في عدة خيوط بالتوازي باستخدام Python.NET
linktitle: الخيوط المتعددة
type: docs
weight: 1800
url: /ar/python-net/reading-cell-values-in-multiple-threads-simultaneously/
description: تعلم كيفية قراءة قيم الخلايا في عدة خيوط بالتزامن باستخدام Aspose.Cells لـ Python via .NET API.
keywords: قراءة قيم الخلايا في عدة خيوط بالتوازي، Aspose.Cells Python خيوط متعددة، قراءة البيانات في خيوط متعددة
---

{{% alert color="primary" %}}

من الضروري قراءة قيم الخلية في خيوط متعددة بشكل متزامن ، وهو متطلب شائع. يشرح هذا المقال كيفية استخدام Aspose.Cells لهذا الغرض.

{{% /alert %}}

للقراءة المتزامنة لقيم الخلايا في أكثر من خيط واحد في نفس الوقت، قم بضبط [**worksheet.cells.multi_thread_reading**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/multi_thread_reading/) إلى **True**. إذا لم تفعل ذلك، قد تحصل على قيم خلايا غير صحيحة.

الكود التالي:

1. إنشاء دفتر عمل
1. إضافة ورقة عمل
1. ملء ورقة العمل بقيم نصية
1. إنشاء خيوطين يقرآن القيم من خلايا عشوائية بشكل متزامن
   إذا كانت القيم المقروءة صحيحة، لا يحدث شيء. إذا كانت القيم المقروءة غير صحيحة، يتم عرض رسالة.

إذا قمت بتعليق هذا السطر:

```python
test_workbook.worksheets[0].cells.multi_thread_reading = True
```

ثم ستحدث الرسالة التالية:

```python
if s != f"R{row}C{col}":
    print("This message will show when cells read values are incorrect")
```

وإلا، يعمل البرنامج بدون عرض أي رسالة مما يعني أن جميع القيم المقروءة من الخلايا صحيحة.

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
