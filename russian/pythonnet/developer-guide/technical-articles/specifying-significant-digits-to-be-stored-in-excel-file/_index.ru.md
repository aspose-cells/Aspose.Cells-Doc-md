---
title: Указание значимых цифр, сохраняемых в файле Excel с помощью Python.NET
linktitle: Указание значительных цифр
type: docs
weight: 30
url: /ru/python-net/specifying-significant-digits-to-be-stored-in-excel-file/
description: Узнайте, как управлять значимостью цифр, сохраненных в файлах Excel, с помощью API Aspose.Cells for Python via .NET.
---

## **Возможные сценарии использования**

По умолчанию Aspose.Cells сохраняет 17 значимых цифр для значений double внутри файла Excel, в отличие от MS-Excel, который сохраняет только 15 значимых цифр. Вы можете изменить это поведение с 17 до 15 значимых цифр, используя атрибут [**CellsHelper.significant_digits**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/significant_digits/).

## **Указание значащих разрядов для хранения в файле Excel**

Следующий пример кода заставляет Aspose.Cells использовать 15 значимых цифр при сохранении значений double. Проверьте [выходной файл Excel](22774105.xlsx) (измените расширение на .zip, чтобы проверить сохраненные значения). Ниже показан снимок экрана, как это влияет на сохраненные значения:

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Образец кода**

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
{{< app/cells/assistant language="python-net" >}}
