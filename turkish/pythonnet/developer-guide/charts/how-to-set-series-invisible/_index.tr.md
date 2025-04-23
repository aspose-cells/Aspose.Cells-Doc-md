---
title: Python.NET kullanarak Seriyi görünmez yapma
linktitle: Seriyi görünmez yapma
type: docs
weight: 74
url: /tr/python-net/how-to-set-series-invisible/
description: Aspose.Cells for Python via .NET kullanarak Excel de grafik serilerini gizlemeyi adım adım öğrenin.
keywords: python excel grafik, seriyi gizle, is_filtered özelliği, Aspose.Cells Python
---

## **Excel Grafiklerinde seriyi nasıl görünmez yapabilirim**

Bir Excel grafiğinde, grafiğe sağ tıklayabilir, "Veri Seç"e tıklayabilir ve açılır pencerede, serinin görünür olup olmadığını işaretleyerek veya işareti kaldırarak ayarlayabilirsiniz.
Aşağıdaki [örnek dosyayı](SeriesFiltered.xlsx) indirebilir ve şekilde gösterildiği gibi Excel'de kullanarak bu fonksiyonu gerçekleştirebilirsiniz. Daha sonra, Aspose.Cells for Python via .NET kütüphanesini kullanarak bunu nasıl yapacağınızı göstereceğiz.

![todo:image_alt_text](series-invisible.png)

## **Aspose.Cells kullanarak seriyi görünmez yapma**

Aşağıdaki kodu kullanarak Aspose.Cells for Python via .NET ile seriyi görünmez yapabilirsiniz:

```python
import os
from aspose.cells import Workbook

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Load sample workbook
workbook = Workbook(os.path.join(data_dir, "SeriesFiltered.xlsx"))

# Access charts from first worksheet
charts = workbook.worksheets[0].charts
chart = charts.get("Chart 1")

# Get series collections
n_series_filtered = chart.filtered_n_series
n_series = chart.n_series

# Filter series by marking them as filtered
n_series[1].is_filtered = True
n_series[0].is_filtered = True

# Save modified workbook
workbook.save(os.path.join(data_dir, "output.xlsx"))
```

Aşağıdaki [girdi dosyasını](SeriesFiltered.xlsx) ve [çıktı dosyasını](output.xlsx) edinebilirsiniz.

Aşağıdaki şekildeki gibi, başlangıçta görünür olan ilk iki seri çıktı dosyasında görünmez hale geldi.
![todo:image_alt_text](output.png)
