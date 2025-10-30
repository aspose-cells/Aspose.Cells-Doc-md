---
title: Interrompi la conversione o il caricamento usando InterruptMonitor quando impiega troppo tempo con Python.NET.
linktitle: Interrompi la conversione o il caricamento usando InterruptMonitor.
type: docs
weight: 100
url: /it/python-net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Scopri come interrompere l elaborazione dei file Excel in Python utilizzando l’InterruptMonitor di Aspose.Cells per un efficiente gestione delle risorse durante operazioni lunghe.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells ti consente di fermare la conversione di un Workbook in vari formati come PDF, HTML ecc., usando l'oggetto [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) quando richiede troppo tempo. Il processo di conversione è spesso intensivo sia in CPU che in memoria e spesso è utile interromperlo quando le risorse sono limitate. Puoi usare [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) sia per fermare la conversione che per bloccare il caricamento di grandi workbook. Usa la proprietà [**Workbook.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/interrupt_monitor/) per fermare la conversione e la proprietà [**LoadOptions.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) per bloccare il caricamento di grandi workbook.

## **Interrompere la conversione o il caricamento utilizzando InterruptMonitor quando sta impiegando troppo tempo**

Il seguente codice di esempio illustra l'uso dell'oggetto [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor). Il codice converte un file Excel abbastanza grande in PDF. Ci vorranno diversi secondi (più di 30 secondi) per completare la conversione a causa di queste righe di codice.

```python
# Access cell J1000000 and add some text inside it.
cell = ws.cells.get("J1000000")
cell.put_value("This is text.")
```

Come puoi vedere, **J1000000** è una cella molto distante nel file XLSX. Tuttavia, il metodo **wait_for_while_and_then_interrupt()** interrompe la conversione dopo 10 secondi e il programma si termina. Usa il seguente codice per eseguire l'esempio.

```python
StopConversionOrLoadingUsingInterruptMonitor().test_run()
```

## **Codice di Esempio**

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
