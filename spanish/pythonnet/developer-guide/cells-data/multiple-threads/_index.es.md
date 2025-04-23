---
title: Lectura de valores de celda en múltiples hilos simultáneamente con Python.NET
linktitle: Hilos múltiples
type: docs
weight: 1800
url: /es/python-net/reading-cell-values-in-multiple-threads-simultaneously/
description: Aprenda cómo leer valores de celdas en múltiples hilos simultáneamente usando la API Aspose.Cells para Python via .NET.
keywords: Leer valores de celdas en múltiples hilos simultáneamente, Aspose.Cells Python Múltiples Hilos, leer datos en múltiples hilos
---

{{% alert color="primary" %}}

Necesitar leer valores de celda en múltiples hilos simultáneamente es un requisito común. Este artículo explica cómo usar Aspose.Cells para este propósito.

{{% /alert %}}

Para leer valores de celdas en más de un hilo simultáneamente, configure [**worksheet.cells.multi_thread_reading**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/multi_thread_reading/) a **True**. Si no lo hace, podría obtener valores incorrectos de las celdas.

El siguiente código:

1. Crear un libro de trabajo
1. Agrega una hoja de cálculo
1. Llena la hoja con valores de cadenas
1. Crea dos hilos que leen simultáneamente valores de celdas aleatorias
   Si los valores leídos son correctos, no sucede nada. Si los valores leídos son incorrectos, se muestra un mensaje.

Si comentas esta línea:

```python
test_workbook.worksheets[0].cells.multi_thread_reading = True
```

entonces, la siguiente verificación de mensaje se activará:

```python
if s != f"R{row}C{col}":
    print("This message will show when cells read values are incorrect")
```

De lo contrario, el programa se ejecuta sin mostrar ningún mensaje, lo que significa que todos los valores leídos de las celdas son correctos.

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

