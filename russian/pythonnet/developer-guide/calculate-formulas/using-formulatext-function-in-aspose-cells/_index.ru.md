---
title: Использование функции FormulaText в Aspose.Cells с Python.NET
linktitle: Использование функции FormulaText
type: docs
weight: 60
url: /ru/python-net/using-formulatext-function-in-aspose-cells/
description: Узнайте, как работать с функцией FORMULATEXT Excel в Aspose.Cells для Python via .NET. Получайте и задавайте формулы ячеек программно, сохраняя целостность таблицы.
keywords: Aspose.Cells, Python, Excel, FORMULATEXT, обработка формул, автоматизация таблиц
---

{{% alert color="primary" %}} 

FORMULATEXT — это функция Excel 2013 и новее. Она не поддерживается предыдущими версиями, такими как Excel 2010 или 2007. Как следует из названия, она отображает текст формулы, содержащейся в указанной ячейке. В этой статье показано, как использовать эту функцию с Aspose.Cells для Python via .NET.

{{% /alert %}} 

Следующий пример кода демонстрирует использование FORMULATEXT с Aspose.Cells. В коде сначала записывается формула в ячейке A1, а затем текст формулы отображается с помощью FORMULATEXT в ячейке A2.

```python
from aspose.cells import Workbook

# Create a workbook object
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Put some formula in cell A1
cell_a1 = worksheet.cells.get("A1")
cell_a1.formula = "=Sum(B1:B10)"

# Get the text of the formula in cell A2 using FORMULATEXT function
cell_a2 = worksheet.cells.get("A2")
cell_a2.formula = "=FormulaText(A1)"

# Calculate the workbook
workbook.calculate_formula()

# Print the results of A2, It will now print the text of the formula inside cell A1
print(cell_a2.string_value)
```

## **Вывод в консоль**
Вот вывод консоли для приведенного выше примера кода:

{{< highlight python >}}
=SUM(B1:B10)
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
