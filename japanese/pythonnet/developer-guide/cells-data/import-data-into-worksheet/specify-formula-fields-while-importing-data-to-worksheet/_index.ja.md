---
title: Excelにインポートするデータの数式フィールドを指定する方法[Python via .NET API]
linktitle: ワークシートへのデータインポート時に式フィールドを指定
type: docs
weight: 300
url: /ja/python-net/specify-formula-fields-while-importing-data-to-worksheet/
description: Aspose.Cells for Python via .NETを使用して、データをインポートする際に数式フィールドを指定する方法を学びます。
keywords: Pythonでデータインポート時に数式フィールドを指定、Pythonでインポート時に数式列を設定、Aspose.Cells Python数式インポート
---

## **可能な使用シナリオ**

[**ImportTableOptions.is_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells/importtableoptions/is_formulas/)プロパティを使ってワークシートにデータをインポートする際に数式フィールドを指定できます。このプロパティはブール値のリストを取り、値が**True**の場合、そのフィールドは数式です。例えば、3番目のフィールドが数式フィールドの場合、リストの3番目の要素は**True**になります。

## **データインポート時に数式フィールドを指定する**

以下の例は、データをインポートする際に数式フィールドを指定する方法を示しています。生成された[出力Excelファイル](61767838.xlsx)と結果を示すスクリーンショットを参照してください。

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **サンプルコード**

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
