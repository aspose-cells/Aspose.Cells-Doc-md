---
title: Stoppa konvertering eller inläsning med InterruptMonitor när det tar för lång tid med Python.NET
linktitle: Stoppa konvertering eller inläsning med InterruptMonitor
type: docs
weight: 100
url: /sv/python-net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Lär dig hur man avbryter Excel filbearbetning i Python med Aspose.Cells InterruptMonitor för effektiv resursförvaltning under långa operationer.
---

## **Möjliga användningsscenario**

Aspose.Cells tillåter dig att stoppa konverteringen av arbetsboken till olika format som PDF, HTML etc. med objektet [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) när det tar för lång tid. Konverteringsprocessen är ofta både CPU- och minnesintensiv och det är ofta användbart att avbryta den när resurser är begränsade. Du kan använda [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) för att stoppa konverteringen samt att stoppa inläsning av stora arbetsböcker. Använd [**Workbook.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/interrupt_monitor/) för att stoppa konverteringen och [**LoadOptions.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) för att stoppa inläsningen av stora arbetsböcker.

## **Stoppa konvertering eller laddning med hjälp av InterruptMonitor när det tar för lång tid**

Följande kodexempel förklarar användningen av [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) -objektet. Koden konverterar en ganska stor Excel-fil till PDF. Det tar flera sekunder (det vill säga *mer än 30 sekunder*) att konvertera den på grund av dessa kodrader.

```python
# Access cell J1000000 and add some text inside it.
cell = ws.cells.get("J1000000")
cell.put_value("This is text.")
```

Som du ser är **J1000000** ganska långt bort i XLSX-filen. Dock avbryter **wait_for_while_and_then_interrupt()** metoden konverteringen efter 10 sekunder och programmet avslutas/avslutas. Använd gärna koden nedan för att köra exempelcode.

```python
StopConversionOrLoadingUsingInterruptMonitor().test_run()
```

## **Exempelkod**

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
