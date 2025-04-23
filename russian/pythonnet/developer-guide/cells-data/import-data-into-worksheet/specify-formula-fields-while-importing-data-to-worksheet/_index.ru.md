---
title: Укажите поля формул при импорте данных в лист с помощью Python via .NET
linktitle: Указание формульных полей при импорте данных в рабочий лист
type: docs
weight: 300
url: /ru/python-net/specify-formula-fields-while-importing-data-to-worksheet/
description: Узнайте, как указывать поля формул при импорте данных в листы с помощью API Aspose.Cells for Python via .NET.
keywords: Python указывает поля формул во время импорта данных, Python задает столбцы с формулой при импорте данных, Aspose.Cells Python формула импорт
---

## **Возможные сценарии использования**

Вы можете указать поля формул при импорте данных в ваш лист с помощью свойства [**ImportTableOptions.is_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells/importtableoptions/is_formulas/). Это свойство принимает логический список, где значение **True** указывает, что поле является формулой. Например, если третье поле — это формула, третий элемент списка будет **True**.

## **Указать поля формул при импорте данных**

Следующий пример демонстрирует, как указывать поля формул при импорте данных. См. сгенерированный [выходной файл Excel](61767838.xlsx) и скриншот, показывающий результаты.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Образец кода**

```python
import os
from dataclasses import dataclass
from aspose.cells import Workbook, ImportTableOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

@dataclass
class DataItems:
    number1: int
    number2: int
    formula1: str
    formula2: str

def run():
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(output_dir, exist_ok=True)

    dis = []
    dis.append(DataItems(2002, 3502, "=SUM(A2,B2)", "=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")"))
    dis.append(DataItems(2003, 3503, "=SUM(A3,B3)", "=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")"))
    dis.append(DataItems(2004, 3504, "=SUM(A4,B4)", "=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")"))
    dis.append(DataItems(2005, 3505, "=SUM(A5,B5)", "=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")"))

    wb = Workbook()
    ws = wb.worksheets[0]

    opts = ImportTableOptions()
    opts.is_formulas = [False, False, True, True]

    ws.cells.import_custom_objects(dis, 0, 0, opts)

    wb.calculate_formula()
    ws.auto_fit_columns()

    output_path = os.path.join(output_dir, "outputSpecifyFormulaFieldsWhileImportingDataToWorksheet.xlsx")
    wb.save(output_path)

    print("SpecifyFormulaFieldsWhileImportingDataToWorksheet executed successfully.")

if __name__ == "__main__":
    run()
```
