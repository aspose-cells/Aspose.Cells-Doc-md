---
title: Uzun süre alıyorsa, çekmek veya yüklemeyi durdurmak için InterruptMonitor kullanarak dönüştürmeyi durdurun.
linktitle: Dönüştürmeyi veya Yüklemeyi InterruptMonitor kullanarak durdurun
type: docs
weight: 100
url: /tr/python-net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Aspose.Cells ın uzun süren işlemler sırasında kaynak yönetimi için Python da Excel dosyası işlemeyi nasıl durduracağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) nesnesini kullanarak uzun sürdüğünde yayın dönüştürmesini PDF, HTML vb. gibi durdurmanıza olanak tanır. Dönüştürme işlemi hem CPU hem de Bellek açısından yoğundur ve kaynaklar sınırlıysa durdurmak faydalı olur. Hem dönüştürmeyi durdurmak hem de büyük çalışma kitaplarını yüklemeyi durdurmak için [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) ve [**Workbook.interrupt_monitor**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/interrupt_monitor/) kullanabilirsiniz.

## **Çok uzun sürüyorsa, Duraklatma İzleyiciyi kullanarak dönüşümü veya yüklemeyi durdurun**

Aşağıdaki örnek kod, [**InterruptMonitor**](https://reference.aspose.com/cells/python-net/aspose.cells/interruptmonitor) nesnesinin kullanımını açıklar. Kod, oldukça büyük bir Excel dosyasını PDF'e dönüştürür. Bu kod satırları nedeniyle dönüştürülmesi birkaç saniye (yani, *30 saniyeden fazla*) sürecektir.

```python
# Access cell J1000000 and add some text inside it.
cell = ws.cells.get("J1000000")
cell.put_value("This is text.")
```

Görüldüğü gibi **J1000000** oldukça uzak bir hücrede. Ancak, **wait_for_while_and_then_interrupt()** yöntemi dönüşümü 10 saniye sonra durdurur ve program sonlanır/sonlandırılır. Lütfen örnek kodu çalıştırmak için aşağıdaki kodu kullanın.

```python
StopConversionOrLoadingUsingInterruptMonitor().test_run()
```

## **Örnek Kod**

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
