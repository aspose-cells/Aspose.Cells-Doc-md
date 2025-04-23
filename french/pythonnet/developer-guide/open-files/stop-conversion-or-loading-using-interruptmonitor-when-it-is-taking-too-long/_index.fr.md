---
title: Arrêtez la conversion ou le chargement en utilisant InterruptMonitor lorsque cela prend trop de temps avec Python.NET
linktitle: Arrêtez la conversion ou le chargement en utilisant InterruptMonitor
type: docs
weight: 100
url: /fr/python-net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Découvrez comment interrompre le traitement des fichiers Excel en Python en utilisant l’InterruptMonitor d’Aspose.Cells pour une gestion efficace des ressources durant les longues opérations.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet d’arrêter la conversion du classeur dans divers formats comme PDF, HTML, etc., en utilisant l’objet [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) lorsque cela prend trop de temps. Le processus de conversion est souvent exigeant en CPU et en mémoire, il est donc utile de l’arrêter lorsque les ressources sont limitées. Vous pouvez utiliser [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) à la fois pour arrêter la conversion et pour arrêter le chargement de grands classeurs. Veuillez utiliser la propriété [**Workbook.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/interrupt_monitor/) pour arrêter la conversion et [**LoadOptions.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) pour le chargement de grands classeurs.

## **Arrêter la conversion ou le chargement à l'aide de InterruptMonitor lorsqu'il prend trop de temps**

Le code d'exemple suivant explique l'utilisation de l'objet [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor). Le code convertit un fichier Excel assez volumineux en PDF. Cela prendra plusieurs secondes (c'est-à-dire *plus de 30 secondes*) pour le convertir en raison de ces lignes de code.

```python
# Access cell J1000000 and add some text inside it.
cell = ws.cells.get("J1000000")
cell.put_value("This is text.")
```

Comme vous pouvez le voir, **J1000000** est une cellule assez éloignée dans le fichier XLSX. Cependant, la méthode **wait_for_while_and_then_interrupt()** interrompt la conversion après 10 secondes, et le programme se termine/immobilise. Utilisez le code suivant pour exécuter l’exemple de code.

```python
StopConversionOrLoadingUsingInterruptMonitor().test_run()
```

## **Code d'exemple**

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
