---
title: Detener la conversión o carga usando InterruptMonitor cuando toma demasiado tiempo con Python.NET
linktitle: Detener la conversión o carga usando InterruptMonitor
type: docs
weight: 100
url: /es/python-net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Aprende cómo interrumpir el procesamiento de archivos Excel en Python usando InterruptMonitor de Aspose.Cells para una gestión eficiente de recursos durante operaciones largas.
---

## **Escenarios de uso posibles**

Aspose.Cells te permite detener la conversión de libro de trabajo a varios formatos como PDF, HTML, etc., usando el objeto [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) cuando lleva demasiado tiempo. El proceso de conversión suele ser intensivo tanto en CPU como en memoria y a menudo es útil detenerlo cuando los recursos son limitados. Puedes usar [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) tanto para detener la conversión como para detener la carga de libros de trabajo grandes. Por favor, usa la propiedad [**Workbook.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/interrupt_monitor/) para detener la conversión y la propiedad [**LoadOptions.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) para cargar libros de trabajo grandes.

## **Detener la conversión o carga utilizando InterruptMonitor cuando está tardando demasiado**

El siguiente código de muestra explica el uso del objeto [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor). El código convierte un archivo de Excel bastante grande a PDF. Tomará varios segundos (es decir, *más de 30 segundos*) en convertirse debido a estas líneas de código.

```python
# Access cell J1000000 and add some text inside it.
cell = ws.cells.get("J1000000")
cell.put_value("This is text.")
```

Como puedes ver, **J1000000** está bastante lejos en la celda del archivo XLSX. Sin embargo, el método **wait_for_while_and_then_interrupt()** interrumpe la conversión después de 10 segundos y el programa termina/cesa. Por favor, usa el siguiente código para ejecutar el código de ejemplo.

```python
StopConversionOrLoadingUsingInterruptMonitor().test_run()
```

## **Código de muestra**

```python
import os
import threading
import time
from aspose.cells import Workbook, Worksheet, CellsException, ExceptionType
from aspose.cells import InterruptMonitor

class StopConversionOrLoadingUsingInterruptMonitor:
    # Output directory
    output_dir = None  # Will be set using GetOutputDirectory()

    def __init__(self):
        # Create InterruptMonitor object
        self.im = InterruptMonitor()
        self.output_dir = self.get_output_directory()

    @staticmethod
    def get_output_directory():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, "output")

    def create_workbook_and_convert_to_pdf(self, monitor_thread):
        # Create a workbook object
        wb = Workbook()
        # Assign InterruptMonitor object
        wb.interrupt_monitor = self.im

        # Access first worksheet
        ws = wb.worksheets[0]

        # Access cell J1000000 and add text
        cell = ws.cells.get("J1000000")
        cell.put_value("This is text.")

        try:
            # Save to PDF
            output_path = os.path.join(self.output_dir, "output_InterruptMonitor.pdf")
            wb.save(output_path)
            print("Excel to PDF - Successful Conversion")
            # Interrupt monitor thread
            monitor_thread.interrupt()
        except CellsException as ex:
            if ex.code == ExceptionType.INTERRUPTED:
                print(f"Conversion process interrupted - Message: {ex.message}")
            else:
                raise

    def wait_and_interrupt(self):
        try:
            time.sleep(10)
            self.im.interrupt()
        except KeyboardInterrupt as e:
            print(f"Monitor thread interrupted - Message: {e}")

    def test_run(self):
        monitor_thread = threading.Thread(target=self.wait_and_interrupt)
        conversion_thread = threading.Thread(
            target=self.create_workbook_and_convert_to_pdf,
            args=(monitor_thread,)
        )

        monitor_thread.start()
        conversion_thread.start()

        monitor_thread.join()
        conversion_thread.join()

    @classmethod
    def run(cls):
        converter = cls()
        converter.test_run()
        print("StopConversionOrLoadingUsingInterruptMonitor executed successfully.")
```
{{< app/cells/assistant language="python-net" >}}
