---
title: 在导入数据到工作表时指定公式字段，使用Python via .NET
linktitle: 在导入数据到工作表时指定公式字段
type: docs
weight: 300
url: /zh/python-net/specify-formula-fields-while-importing-data-to-worksheet/
description: 学习如何在使用Aspose.Cells for Python via .NET API导入数据到工作表时指定公式字段。
keywords: Python在导入数据时指定公式字段，设置导入数据时的公式列，Aspose.Cells Python公式导入
---

## **可能的使用场景**

 使用[**ImportTableOptions.is_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells/importtableoptions/is_formulas/)属性在导入数据时指定公式字段。此属性接受一个布尔值列表，值为**True**代表该字段是公式。例如，如果第三个字段是公式字段，则列表中的第三个元素为**True**。

## ** 在导入数据时指定公式字段**

 以下示例演示如何在导入数据时指定公式字段。请查看生成的[输出Excel文件](61767838.xlsx)及显示结果的截图。

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **示例代码**

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
{{< app/cells/assistant language="python-net" >}}
