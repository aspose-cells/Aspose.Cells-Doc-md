---
title: Stop conversion or loading using InterruptMonitor when it is taking too long with Python.NET
linktitle: Stop Conversion or Loading Using InterruptMonitor
type: docs
weight: 100
url: /python-net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Learn how to interrupt Excel file processing in Python using Aspere.Cells' InterruptMonitor for efficient resource management during long operations.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells allows you to stop the conversion of a Workbook to various formats like PDF, HTML, etc., using the [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) object when it is taking too long. The conversion process is often both CPU and memory intensive, and it is useful to halt it when resources are limited. You can use [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) both for stopping conversion and for stopping the loading of huge workbooks. Please use the [**Workbook.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/interrupt_monitor/) property for stopping conversion and the [**LoadOptions.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) property for loading huge workbooks.

## **Stop conversion or loading using InterruptMonitor when it is taking too long**

The following sample code explains the usage of [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) object. The code converts a fairly large Excel file to PDF. It will take several seconds (i.e., *more than 30 seconds*) to convert because of these lines of code.

```python
# Access cell J1000000 and add some text.
cell = ws.cells.get("J1000000")
cell.put_value("This is text.")
```

As you can see, **J1000000** is a much farther cell in the XLSX file. However, the **wait_and_interrupt()** method interrupts the conversion after 10 seconds and the program terminates. Please use the following code to execute the sample code.

```python
StopConversionOrLoadingUsingInterruptMonitor().test_run()
```

## **Sample Code**

```python
import os
import threading
import time
from aspose.cells import Workbook, Worksheet, CellsException, ExceptionType
from aspose.cells import InterruptMonitor

class StopConversionOrLoadingUsingInterruptMonitor:
    # Output directory
    output_dir = None  # Will be set using get_output_directory()

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
