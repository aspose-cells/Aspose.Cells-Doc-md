---
title: Microsoft Excel formül izleme penceresine Hücreler ekleme Python.NET ile
linktitle: Formül İzleme Penceresine Hücreler Ekleyin
type: docs
weight: 60
url: /tr/python-net/add-cells-to-microsoft-excel-formula-watch-window/
description: Aspose.Cells for Python via .NET kullanarak Excel in Formül İzleme Penceresindeki hücreleri nasıl izleyebileceğinizi öğrenin. Kod örnekleri ve API referansları içerir.
keywords: python excel, formül izleme penceresi, hücre izleme, aspose.cells, python.net
---

## **Olası Kullanım Senaryoları**

Microsoft Excel İzleme Penceresi, hücre değerlerini ve formülleri kolayca izlemek için kullanışlı bir araçtır. *İzleme Penceresi*ni açmak için Microsoft Excel'de *Formüller > İzleme Penceresi* sekmesine gidin. *İzleme Ekle* düğmesi, hücreleri denetlemek için eklemenizi sağlar. Aynı zamanda, Aspose.Cells API'sini kullanarak programlı olarak hücreleri İzleme Penceresine eklemek için [**Worksheet.cell_watches.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/cellwatchcollection/add/) metodunu kullanabilirsiniz.

## **Microsoft Excel Formül İzleme Penceresine Hücreler Ekleme**

Aşağıdaki örnek kod, C1 ve E1 hücreleri için formüller ayarlar ve her ikisini de İzleme Penceresine ekler. Bu işlemi yaptıktan sonra çalışma kitabını [çıktı Excel dosyası](67338481.xlsx) olarak kaydeder. Excel'de açıldığında, her iki hücre de gösterilen gibi İzleme Penceresinde görünecektir:

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Örnek Kod**

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
