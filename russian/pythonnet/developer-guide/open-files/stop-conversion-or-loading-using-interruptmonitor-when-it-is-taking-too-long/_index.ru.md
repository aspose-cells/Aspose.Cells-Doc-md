---
title: Прекратить конвертацию или загрузку с помощью InterruptMonitor, когда процесс занимает слишком много времени с помощью Python.NET.
linktitle: Прекратить конвертацию или загрузку с помощью InterruptMonitor.
type: docs
weight: 100
url: /ru/python-net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Узнайте, как прервать обработку файла Excel в Python с помощью InterruptMonitor для эффективного управления ресурсами во время длительных операций.
---

## **Возможные сценарии использования**

Aspose.Cells позволяет остановить преобразование рабочей книги в различные форматы, такие как PDF, HTML и др., с помощью объекта [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor), когда оно занимает слишком много времени. Процесс преобразования часто требует много ресурсов CPU и памяти, и его можно приостановить при нехватке ресурсов. Можно использовать [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) для остановки преобразования и [**Workbook.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/interrupt_monitor/) для остановки загрузки больших рабочих книг.

## **Прекратите преобразование или загрузку с использованием объекта InterruptMonitor, если это занимает слишком много времени**

В следующем образце кода объясняется использование объекта [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor). Код преобразует довольно большой файл Excel в PDF. Это займет несколько секунд (т.е. *более 30 секунд*) для преобразования из-за этих строк кода.

```python
# Access cell J1000000 and add some text inside it.
cell = ws.cells.get("J1000000")
cell.put_value("This is text.")
```

Как вы видите, **J1000000** — довольно дальняя ячейка в XLSX-файле. Однако метод **wait_for_while_and_then_interrupt()** прерывает конвертацию через 10 секунд, и программа завершается. Используйте следующий код для выполнения примера.

```python
StopConversionOrLoadingUsingInterruptMonitor().test_run()
```

## **Образец кода**

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
