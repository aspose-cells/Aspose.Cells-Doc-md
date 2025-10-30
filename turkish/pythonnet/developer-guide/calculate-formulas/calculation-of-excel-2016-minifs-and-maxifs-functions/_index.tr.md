---
title: Excel 2016 MINIFS ve MAXIFS fonksiyonlarının Python.NET ile hesaplanması
linktitle: Excel 2016 MINIFS ve MAXIFS İşlevlerini Hesaplama
type: docs
weight: 300
url: /tr/python-net/calculation-of-excel-2016-minifs-and-maxifs-functions/
description: Aspose.Cells for Python via .NET API kullanarak Excel 2016 MINIFS ve MAXIFS fonksiyonlarının nasıl hesaplanacağını kod örnekleriyle öğrenin.
keywords: python excel, minifs maxifs, formül hesaplama, aspose.cells
---

## **Olası Kullanım Senaryoları**
Microsoft Excel 2016, MINIFS ve MAXIFS fonksiyonlarını destekler. Bu fonksiyonlar Excel 2013 veya daha eski sürümlerinde desteklenmemektedir. Aspose.Cells da bu fonksiyonların hesaplamasını destekler. Aşağıdaki ekran görüntüsü, bu fonksiyonların kullanımını göstermektedir. Lütfen ekran görüntüsündeki kırmızı yorumları okuyarak bu fonksiyonların nasıl çalıştığını anlayın.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Excel 2016 MINIFS ve MAXIFS işlevlerinin hesaplanması**
Aşağıdaki örnek kod, [örnek excel dosyasını](5115149.xlsx) yükler ve [workbook.calculate_formula()](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) yöntemiyle formülleri Aspose.Cells kullanarak hesaplar ve sonuçları [çıktı PDF'sine](5115154.pdf) kaydeder.


```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")

# Load your source workbook containing MINIFS and MAXIFS functions
workbook = Workbook(os.path.join(source_dir, "sampleMINIFSAndMAXIFS.xlsx"))

# Perform Aspose.Cells formula calculation
workbook.calculate_formula()

# Save the calculations result in pdf format
options = PdfSaveOptions()
options.one_page_per_sheet = True

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "outputMINIFSAndMAXIFS.pdf"), options)
```
{{< app/cells/assistant language="python-net" >}}
