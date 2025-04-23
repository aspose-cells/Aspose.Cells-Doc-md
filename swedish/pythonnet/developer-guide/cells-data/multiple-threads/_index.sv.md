---
title: Läsa cellvärden i flera trådar samtidigt med Python.NET
linktitle: Flera trådar
type: docs
weight: 1800
url: /sv/python-net/reading-cell-values-in-multiple-threads-simultaneously/
description: Lär dig hur man läser cellvärden i flera trådar samtidigt med Aspose.Cells för Python via .NET API.
keywords: Läs cellvärden i flera trådar samtidigt, Aspose.Cells Python Flertal trådar, Läs data i flera trådar
---

{{% alert color="primary" %}}

Att behöva läsa cellvärden i flera trådar samtidigt är ett vanligt krav. Den här artikeln förklarar hur man använder Aspose.Cells för detta ändamål.

{{% /alert %}}

För att läsa cellvärden i mer än en tråd samtidigt, ange [**worksheet.cells.multi_thread_reading**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/multi_thread_reading/) till **True**. Om du inte gör det kan du få felaktiga cellvärden.

Följande kod:

1. Skapar en arbetsbok
1. Lägger till ett kalkylblad
1. Fyller kalkylbladet med strängvärden
1. Skapar två trådar som samtidigt läser värden från slumpmässiga celler
   Om de lästa värdena är korrekta händer ingenting. Om de lästa värdena är inkorrekta visas ett meddelande.

Om du kommenterar denna rad:

```python
test_workbook.worksheets[0].cells.multi_thread_reading = True
```

då utlöses följande meddelandekontroll:

```python
if s != f"R{row}C{col}":
    print("This message will show when cells read values are incorrect")
```

I annat fall körs programmet utan att visa något meddelande, vilket betyder att alla värden som läses från cellerna är korrekta.

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

