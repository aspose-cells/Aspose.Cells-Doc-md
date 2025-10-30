---
title: Lesen von Zellwerten in mehreren Threads gleichzeitig mit Python.NET
linktitle: Mehrere Threads.
type: docs
weight: 1800
url: /de/python-net/reading-cell-values-in-multiple-threads-simultaneously/
description: Erfahren Sie, wie man Zellwerte in mehreren Threads gleichzeitig mit der Aspose.Cells for Python via .NET API liest.
keywords: Lesen von Zellwerten in mehreren Threads gleichzeitig, Aspose.Cells Python Mehrfachtreading, Daten in mehreren Threads lesen
---

{{% alert color="primary" %}}

Es ist häufig erforderlich, Zellwerte gleichzeitig in mehreren Threads zu lesen. Dieser Artikel erläutert, wie Sie Aspose.Cells zu diesem Zweck verwenden.

{{% /alert %}}

Um Zellwerte gleichzeitig in mehreren Threads zu lesen, setzen Sie [**worksheet.cells.multi_thread_reading**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/multi_thread_reading/) auf **True**. Wenn Sie das nicht tun, erhalten Sie möglicherweise falsche Zellwerte.

Der folgende Code:

1. Ein Arbeitsbuch erstellen
1. Ein Arbeitsblatt hinzufügen
1. Füllt das Arbeitsblatt mit Zeichenkettenwerten
1. Erstellt zwei Threads, die gleichzeitig Werte aus zufälligen Zellen lesen
   Wenn die gelesenen Werte korrekt sind, passiert nichts. Wenn die gelesenen Werte inkorrekt sind, wird eine Meldung angezeigt.

Wenn Sie diese Zeile kommentieren:

```python
test_workbook.worksheets[0].cells.multi_thread_reading = True
```

dann wird die folgende Nachrichtenprüfung ausgelöst:

```python
if s != f"R{row}C{col}":
    print("This message will show when cells read values are incorrect")
```

Ansonsten läuft das Programm ohne Anzeige einer Meldung, was bedeutet, dass alle Werte, die aus den Zellen gelesen wurden, korrekt sind.

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
