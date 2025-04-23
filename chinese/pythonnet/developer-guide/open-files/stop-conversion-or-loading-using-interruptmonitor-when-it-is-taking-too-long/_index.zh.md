---
title: 在 Python.NET 中使用 InterruptMonitor 在转换或加载过慢时停止操作
linktitle: 使用 InterruptMonitor 停止转换或加载
type: docs
weight: 100
url: /zh/python-net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: 学习如何在 Python 中使用 Aspose.Cells 的 InterruptMonitor 中断 Excel 文件处理，以在长时间操作中高效管理资源。
---

## **可能的使用场景**

当转换时间过长时，Aspose.Cells 允许你使用 [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) 对象停止工作簿转换为 PDF、HTML 等多种格式。该转换过程通常占用大量 CPU 和内存，资源有限时停止非常有用。你可以使用 [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) 来停止转换，也可以停止加载大工作簿。请使用 [**Workbook.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/interrupt_monitor/) 属性停止转换，使用 [**LoadOptions.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) 属性停止加载大工作簿。

## **在转换或加载花费太长时间时使用InterruptMonitor停止转换或加载**

以下示例代码解释了使用 [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) 对象的用法。该代码将大型Excel文件转换为PDF。由于这些代码行的原因，转换需要几秒钟（即*超过30秒*）。

```python
# Access cell J1000000 and add some text inside it.
cell = ws.cells.get("J1000000")
cell.put_value("This is text.")
```

如你所见，**J1000000** 是 XLSX 文件中的较远单元格。然而，**wait_for_while_and_then_interrupt()** 方法在10秒后中断转换并结束/终止程序。请使用以下代码执行示例。

```python
StopConversionOrLoadingUsingInterruptMonitor().test_run()
```

## **示例代码**

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
