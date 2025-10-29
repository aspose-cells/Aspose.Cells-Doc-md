---
title: Добавить ячейки в окно слежения за формулами Microsoft Excel с помощью Python.NET
linktitle: Добавить ячейки в окно наблюдения формул
type: docs
weight: 60
url: /ru/python-net/add-cells-to-microsoft-excel-formula-watch-window/
description: Узнайте, как мониторить ячейки в окне слежения за формулами в Excel, используя Aspose.Cells для Python via .NET. Включает примеры кода и справочные материалы API.
keywords: python excel, окно слежения за формулами, мониторинг ячеек, aspose.cells, python.net
---

## **Возможные сценарии использования**

Окно слежения в Microsoft Excel — удобный инструмент для контроля значений ячеек и формул в отдельном окне. Вы можете открыть *Окно слежения* в Microsoft Excel, перейдя в *Формулы > Окно слежения*. Кнопка *Добавить наблюдение* позволяет добавлять ячейки для проверки. Аналогично, вы можете использовать метод [**Worksheet.cell_watches.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/cellwatchcollection/add/) для программного добавления ячеек в Окно слежения с помощью API Aspose.Cells.

## **Добавление ячеек в окно наблюдения формул Microsoft Excel**

Следующий пример кода устанавливает формулы для ячеек C1 и E1, затем добавляет их оба в Окно слежения. Он сохраняет рабочую книгу как [выходной Excel-файл](67338481.xlsx). При открытии файла в Excel оба ячейки появятся в Окне слежения, как показано:

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Образец кода**

```python
from aspose.cells import Workbook, SaveFormat

# Create empty workbook.
wb = Workbook()

# Access first worksheet.
ws = wb.worksheets[0]

# Put some integer values in cell A1 and A2.
ws.cells.get("A1").put_value(10)
ws.cells.get("A2").put_value(30)

# Access cell C1 and set its formula.
c1 = ws.cells.get("C1")
c1.formula = "=Sum(A1,A2)"

# Add cell C1 into cell watches by name.
ws.cell_watches.add(c1.name)

# Access cell E1 and set its formula.
e1 = ws.cells.get("E1")
e1.formula = "=A2*A1"

# Add cell E1 into cell watches by its row and column indices.
ws.cell_watches.add(e1.row, e1.column)

# Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat.XLSX)
```
{{< app/cells/assistant language="python-net" >}}
