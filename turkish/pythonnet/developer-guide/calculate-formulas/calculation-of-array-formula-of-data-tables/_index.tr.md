---
title: Python.NET ile Veri Tablosu Dizisi Formülü Hesaplaması
linktitle: Veri Tablolarının Dizilerini Hesaplama
type: docs
weight: 70
url: /tr/python-net/calculation-of-array-formula-of-data-tables/
description: Aspose.Cells for Python via .NET API kullanarak Excel veri tabloları için dizi formüllerinin nasıl hesaplanacağı öğrenin. Elektronik tabloları programatik olarak değiştirin ve kaydedin.
keywords: Python Excel Veri Tabloları, Python Dizi Formülleri, Aspose.Cells Python, Veri Tablosu Hesaplama Python, Excel Otomasyonu Python
---

{{% alert color="primary" %}}

Microsoft Excel'de Data > What-If Analysis > Data Table.... Aspose.Cells for Python via .NET kullanarak veri tabloları için dizi formülü oluşturabilirsiniz. Lütfen herhangi bir formül türünü hesaplamak için [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) kullanın.

{{% /alert %}}

Aşağıdaki örnekte, [kaynak excel dosyası](5115535.xlsx) kullanılır. B1 hücresinin değerini 100 yaparsanız, Dosya Tablosunun değerleri (sarıyla vurgulanmıştır) ekran görüntülerinde gösterildiği gibi 120'ye güncellenecektir. Python kodu bu [çıktı PDF'sini](5115538.pdf) oluşturur.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Aşağıda, [kaynak excel dosyasından](5115535.xlsx) [çıktı PDF'sini](5115538.pdf) üretmenin Python uygulaması gösterilmektedir:

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

**Python Kod Açıklaması:**
```python
import aspose.cells as ac

# Load source workbook
workbook = ac.Workbook("5115535.xlsx")

# Calculate formulas using Python.NET API
workbook.calculate_formula()

# Save the workbook in PDF format
workbook.save("5115538.pdf", ac.SaveFormat.PDF)
```
