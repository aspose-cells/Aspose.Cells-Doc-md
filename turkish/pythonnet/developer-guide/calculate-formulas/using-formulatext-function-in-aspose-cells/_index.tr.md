---
title: Python.NET ile Aspose.Cells da FormülText Fonksiyonunu Kullanma
linktitle: FormülText Fonksiyonunu Kullanma
type: docs
weight: 60
url: /tr/python-net/using-formulatext-function-in-aspose-cells/
description: Aspose.Cells for Python via .NET kullanarak Excel in FORMULATEXT fonksiyonuyla nasıl çalışılacağını öğrenin. Hücre formüllerini programlı olarak alın ve ayarlayın, çalışma sayfası bütünlüğünü koruyarak.
keywords: Aspose.Cells, Python, Excel, FORMULATEXT, formül işleme, elektronik tablo otomasyonu
---

{{% alert color="primary" %}} 

FORMULATEXT, Excel 2013 ve sonrası sürümlerinde kullanılabilen bir fonksiyondur. Önceki sürümler, örneğin Excel 2010 veya 2007 tarafından desteklenmez. İsminin de belirttiği gibi, belirtilen hücredeki formül metnini gösterir. Bu makale, bu fonksiyonun Aspose.Cells for Python ile nasıl kullanılacağını gösterir via .NET.

{{% /alert %}} 

Aşağıdaki örnek kod, Aspose.Cells kullanarak FORMULATEXT'in nasıl kullanılacağını gösterir. Kod önce A1 hücresine bir formül yazar ve sonra A2 hücresinde FORMULATEXT kullanarak formül metnini gösterir.

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

## **Konsol Çıktısı**
İşte yukarıdaki örnek kodun konsol çıktısı:

{{< highlight python >}}
=SUM(B1:B10)
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
