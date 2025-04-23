---
title: Beenden der Konvertierung oder des Ladens mit InterruptMonitor, wenn es zu lange dauert, mit Python.NET
linktitle: Beenden der Konvertierung oder des Ladevorgangs mit InterruptMonitor
type: docs
weight: 100
url: /de/python-net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Lernen, wie man die Excel Dateibearbeitung in Python mit Aspose.Cells InterruptMonitor bei längeren Vorgängen effizient unterbricht.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es, die Konvertierung eines Arbeitsbuchs in verschiedene Formate wie PDF, HTML etc. mit dem [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor)-Objekt zu stoppen, wenn sie zu lange dauert. Der Konvertierungsprozess ist oft sowohl CPU- als auch speicherintensiv, daher ist es oft sinnvoll, ihn bei begrenzten Ressourcen abzubrechen. Sie können [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) sowohl zum Stoppen der Konvertierung als auch zum Anhalten großer Arbeitsbücher verwenden. Bitte verwenden Sie [**Workbook.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/interrupt_monitor/)-Eigenschaft zum Stoppen der Konvertierung und [**LoadOptions.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/)-Eigenschaft zum Laden großer Arbeitsbücher.

## ** Konvertierung oder Laden mit InterruptMonitor stoppen, wenn es zu lange dauert**

Der folgende Beispielscode erläutert die Verwendung des [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor)-Objekts. Der Code konvertiert eine ziemlich große Excel-Datei in PDF. Es dauert einige Sekunden (d.h. *mehr als 30 Sekunden*), um sie zu konvertieren, aufgrund dieser Codezeilen.

```python
# Access cell J1000000 and add some text inside it.
cell = ws.cells.get("J1000000")
cell.put_value("This is text.")
```

Wie Sie sehen, ist **J1000000** eine ziemlich weit entfernte Zelle in der XLSX-Datei. Die Methode **wait_for_while_and_then_interrupt()** unterbricht die Konvertierung nach 10 Sekunden und das Programm endet/terminiert. Verwenden Sie den folgenden Code, um das Beispiel auszuführen.

```python
StopConversionOrLoadingUsingInterruptMonitor().test_run()
```

## **Beispielcode**

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
