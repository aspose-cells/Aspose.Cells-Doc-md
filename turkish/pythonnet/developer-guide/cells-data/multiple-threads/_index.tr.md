---
title: Python.NET ile Çok İş parçacığında Hücre Değerlerini Okuma
linktitle: Çoklu İş Parçacıkları
type: docs
weight: 1800
url: /tr/python-net/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for Python via .NET API kullanarak çoklu iş parçacığında hücre değerlerini nasıl okuyacağınızı öğrenin.
keywords: Çoklu iş parçacığında Hücre Değerlerini Okuma, Aspose.Cells Python Çoklu İş Parçacığı, Çoklu İş Parçacığında Veri Okuma
---

{{% alert color="primary" %}}

Aynı Anda Birden Fazla İş Parçacığında hücre değerlerini okuma ihtiyacı yaygın bir gereksinimdir. Bu makale bu amaçla Aspose.Cells'in nasıl kullanılacağını açıklar.

{{% /alert %}}

Birden fazla iş parçacığında aynı anda hücre değerlerini okumak için [**worksheet.cells.multi_thread_reading**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/multi_thread_reading/) to **True** olarak ayarlayın. Aksi takdirde, yanlış hücre değerleri alabilirsiniz.

Aşağıdaki kod:

1. Bir çalışma kitabı oluşturur
1. Bir çalışma sayfası ekler
1. Çalışma sayfasını string değerlerle doldurur
1. Rastgele hücrelerden aynı anda değerler okuyan iki iş parçacığı oluşturur
   Okunan değerler doğru ise hiçbir şey olmaz. Okunan değerler yanlışsa bir mesaj görüntülenir.

Eğer bu satırı yorumlarsanız:

```python
test_workbook.worksheets[0].cells.multi_thread_reading = True
```

sonra aşağıdaki mesaj kontrolü tetiklenecek:

```python
if s != f"R{row}C{col}":
    print("This message will show when cells read values are incorrect")
```

Aksi takdirde, program herhangi bir mesaj göstermeden çalışır, bu da demek olur ki tüm hücrelerden okunan değerler doğrudur.

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
