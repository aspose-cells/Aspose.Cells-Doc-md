---
title: Расчет массивных формул таблиц данных с помощью Python.NET
linktitle: Вычисление массивной формулы таблиц данных
type: docs
weight: 70
url: /ru/python-net/calculation-of-array-formula-of-data-tables/
description: Узнайте, как вычислять массивные формулы для таблиц данных Excel с помощью API Aspose.Cells для Python via .NET. Модифицируйте и сохраняйте таблицы программно.
keywords: Таблицы данных Excel на Python, Формулы массивов Python, Aspose.Cells Python, Расчет таблиц данных Python, Автоматизация Excel на Python
---

{{% alert color="primary" %}}

Вы можете создавать таблицы данных в Microsoft Excel через меню Данные > Анализ гипотез > Таблица данных... Aspose.Cells для Python via .NET позволяет выполнять расчет формул массива таблицы данных. Пожалуйста, используйте [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) как обычно для расчета любых формул.

{{% /alert %}}

В следующем примере используется исходный файл Excel (5115535.xlsx). Если изменить значение ячейки B1 на 100, значения таблицы данных (выделены желтым) обновятся до 120, как показано на скриншотах ниже. Этот Python-код генерирует этот [выходной PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Ниже представлен Python-обзор, демонстрирующий, как сгенерировать [выходной PDF](5115538.pdf) из исходного файла Excel (5115535.xlsx):

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create workbook from source excel file
workbook = Workbook(os.path.join(data_dir, "DataTable.xlsx"))

# Access first worksheet
worksheet = workbook.worksheets[0]

# When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.cells.get("B1").put_value(100)

# Calculate formula, now it also calculates Data Table array formula
workbook.calculate_formula()

# Save the workbook in pdf format
workbook.save(os.path.join(data_dir, "output_out.pdf"))
```

**Объяснение кода на Python:**
```python
import aspose.cells as ac

# Load source workbook
workbook = ac.Workbook("5115535.xlsx")

# Calculate formulas using Python.NET API
workbook.calculate_formula()

# Save the workbook in PDF format
workbook.save("5115538.pdf", ac.SaveFormat.PDF)
```
