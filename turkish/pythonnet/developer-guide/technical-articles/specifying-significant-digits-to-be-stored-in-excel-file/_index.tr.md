---
title: Python.NET ile Excel Dosyasına Kaydedilecek Önemli Basamak Sayısı Belirtme
linktitle: Önemli Basamakların Belirtilmesi
type: docs
weight: 30
url: /tr/python-net/specifying-significant-digits-to-be-stored-in-excel-file/
description: Aspose.Cells for Python via .NET API kullanarak Excel dosyasında saklanan önemli basamak sayılarını nasıl kontrol edeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Varsayılan olarak, Aspose.Cells, Excel dosyası içinde ondalık sayıların 17 önemli basamağını saklar, MS-Excel ise sadece 15 önemli basamağı saklar. Bu davranışı [**CellsHelper.significant_digits**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/significant_digits/) özniteliği kullanarak 17’den 15’e değiştirebilirsiniz.

## **Excel dosyasında saklanacak anlamlı basamakları belirtme**

Aşağıdaki örnek kod, Aspose.Cells'un ondalık sayılarını saklarken 15 önemli basamağı kullanmasını zorlar. Lütfen [çıktı excel dosyasını](22774105.xlsx) kontrol edin (uzantıyı .zip'e değiştirerek saklanan değerleri inceleyebilirsiniz). Aşağıdaki ekran görüntüsü, bu ayarın saklanan değerleri nasıl etkilediğini gösterir.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Örnek Kod**

```python
from aspose.cells import Workbook, CellsHelper
import aspose.cells
import os
import pytest

# Set significant digits to 15
CellsHelper.set_significant_digits(15)

# Create new workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set value with extended precision
cell = worksheet.cells.get("A1")
cell.put_value(1234567890123456.001234567890123456)

# Save modified workbook
workbook.save("output.xlsx")
```

```python
import os
from aspose.cells import Workbook, CellsHelper

# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Set significant digits to 15 like MS-Excel
CellsHelper.set_significant_digits(15)

# Create workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Access cell A1
c = worksheet.cells.get("A1")

# Put double value with 15 significant digits
c.put_value(1234567890.123451711)

# Save the workbook
output_dir = os.path.join(current_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "out_SignificantDigits.xlsx"))
```
