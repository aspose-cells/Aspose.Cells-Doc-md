---
title: Python ile Çalışma Sayfasına Veri İçe Aktarırken Formül Alanlarını Belirtme via .NET
linktitle: Çalışma Sayfasına Veri İçeri Aktarırken Formül Alanları Belirt
type: docs
weight: 300
url: /tr/python-net/specify-formula-fields-while-importing-data-to-worksheet/
description: Aspose.Cells for Python API kullanarak verileri çalışma sayfasına ithal ederken formül alanlarını nasıl belirteceğinizi öğrenin via .NET.
keywords: Python ile veri içe aktarımında formül alanlarını belirtme, Python ile formül sütunlarını ayarlama, Aspose.Cells Python formül ithalatı
---

## **Olası Kullanım Senaryoları**

Veri ithalatı sırasında [**ImportTableOptions.is_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells/importtableoptions/is_formulas/) özelliği kullanılarak formül alanlarını belirtebilirsiniz. Bu özellik, alanın formül olduğunu belirtmek için **True** olan boolean listesini kabul eder. Örneğin, üçüncü alan formül alanıysa, listenin üçüncü öğesi **True** olur.

## **Veri İçe Aktarma sırasında Formül Alanlarını Belirtme**

Aşağıdaki örnek, veri içe aktarırken formül alanlarını nasıl belirteceğinizi gösterir. Oluşturulan [çıkış Excel dosyasını](61767838.xlsx) ve sonuçları gösteren ekran görüntüsünü inceleyin.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Örnek Kod**

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
