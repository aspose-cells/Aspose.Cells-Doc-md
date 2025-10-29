---
title: تحديد صيغة الحقول أثناء استيراد البيانات إلى ورقة عمل باستخدام Python via .NET
linktitle: تحديد حقول الصيغة أثناء استيراد البيانات إلى الورقة العمل
type: docs
weight: 300
url: /ar/python-net/specify-formula-fields-while-importing-data-to-worksheet/
description: تعلم كيفية تحديد صيغة الحقول عند استيراد البيانات إلى أوراق العمل باستخدام Aspose.Cells for Python via .NET API.
keywords: التحديد برمجياً في بايثون لصيغة العمود أثناء استيراد البيانات، إعداد عمود الصيغة عند استيراد البيانات باستخدام بايثون، استيراد الصيغة باستخدام Aspose.Cells Python
---

## **سيناريوهات الاستخدام المحتملة**

 يمكنك تحديد حقول الصيغ عند استيراد البيانات إلى ورقة العمل الخاصة بك باستخدام خاصية [**ImportTableOptions.is_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells/importtableoptions/is_formulas/). تأخذ هذه الخاصية قائمة منطقية حيث يشير **True** إلى أن الحقل هو صيغة. على سبيل المثال، إذا كان الحقل الثالث هو حقل صيغة، سيكون العنصر الثالث في القائمة هو **True**.

## **تحديد حقول الصيغ أثناء استيراد البيانات**

يوضح المثال التالي كيفية تحديد حقول الصيغ أثناء استيراد البيانات. راجع ملف إكسل الناتج ولقطة الشاشة التي تظهر النتائج.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **الكود المثالي**

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
