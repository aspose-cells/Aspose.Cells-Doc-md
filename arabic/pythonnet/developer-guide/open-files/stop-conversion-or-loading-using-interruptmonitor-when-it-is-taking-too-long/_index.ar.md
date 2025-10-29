---
title: إيقاف التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلًا مع Python.NET
linktitle: إيقاف التحويل أو التحميل باستخدام InterruptMonitor
type: docs
weight: 100
url: /ar/python-net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: تعلم كيفية إيقاف معالجة ملف إكسل في بايثون باستخدام مراقب المقاطعة الخاص بـ Aspose.Cells لإدارة الموارد بكفاءة خلال العمليات الطويلة.
---

## **سيناريوهات الاستخدام المحتملة**

يسمح Aspose.Cells لك بإيقاف تحويل دفتر العمل إلى صيغ مختلفة مثل PDF، HTML وغيرها باستخدام كائن [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) عندما يستغرق الأمر وقتًا طويلاً. غالبًا ما يكون عملية التحويل كثيفة لوحدة المعالجة المركزية والذاكرة، وغالبًا ما يكون من المفيد إيقافها عندما تكون الموارد محدودة. يمكنك استخدام [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) لإيقاف التحويل وكذلك لإيقاف تحميل دفاتر العمل الضخمة. يرجى استخدام الخاصية [**Workbook.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/interrupt_monitor/) لإيقاف التحويل والخاصية [**LoadOptions.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) لإيقاف تحميل دفاتر العمل الضخمة.

## **توقّف عن التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً**

يشرح الكود العينة التالي استخدام كائن [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor). يحول الكود ملف إكسل كبير إلى PDF. سيستغرق عدة ثوانٍ (أي *أكثر من 30 ثانية*) لتحويله بسبب هذه الأسطر من الكود.

```python
# Access cell J1000000 and add some text inside it.
cell = ws.cells.get("J1000000")
cell.put_value("This is text.")
```

كما ترى، **J1000000** هو بعد طويل في ملف XLSX. ومع ذلك، فإن طريقة **wait_for_while_and_then_interrupt()** توقف التحويل بعد 10 ثوانٍ وينتهي/ينقطع البرنامج. يرجى استخدام الكود التالي لتنفيذ الكود النموذجي.

```python
StopConversionOrLoadingUsingInterruptMonitor().test_run()
```

## **الكود المثالي**

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
