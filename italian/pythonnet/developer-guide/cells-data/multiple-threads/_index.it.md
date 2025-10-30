---
title: Lettura dei valori delle celle in più thread contemporaneamente con Python.NET
linktitle: Thread multipli
type: docs
weight: 1800
url: /it/python-net/reading-cell-values-in-multiple-threads-simultaneously/
description: Impara a leggere i valori delle celle in più thread contemporaneamente usando Aspose.Cells per Python API via .NET.
keywords: Leggi i valori delle celle in più thread simultaneamente, Aspose.Cells Python più thread, Leggi i dati in più thread
---

{{% alert color="primary" %}}

La necessità di leggere i valori delle celle in thread multipli contemporaneamente è una richiesta comune. Questo articolo spiega come utilizzare Aspose.Cells per questo scopo.

{{% /alert %}}

Per leggere i valori delle celle in più di un thread contemporaneamente, imposta [**worksheet.cells.multi_thread_reading**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/multi_thread_reading/) su **True**. Se non lo fai, potresti ottenere valori di cella errati.

Il seguente codice:

1. Crea una cartella di lavoro
1. Aggiunge un foglio di lavoro
1. Popola il foglio di lavoro con valori stringa
1. Crea due thread che leggono contemporaneamente valori da celle casuali
   Se i valori letti sono corretti, non succede nulla. Se i valori letti non sono corretti, viene visualizzato un messaggio.

Se si commenta questa riga:

```python
test_workbook.worksheets[0].cells.multi_thread_reading = True
```

quindi il controllo del messaggio seguente verrà attivato:

```python
if s != f"R{row}C{col}":
    print("This message will show when cells read values are incorrect")
```

In caso contrario, il programma viene eseguito senza mostrare alcun messaggio, il che significa che tutti i valori letti dalle celle sono corretti.

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
