---
title: Python.NET kullanarak Noktayı Toplam olarak ayarlama nasıl yapılır
linktitle: Noktayı Toplam olarak ayarlama nasıl yapılır
type: docs
weight: 72
url: /tr/python-net/how-to-set-point-as-total/
description: Aspose.Cells for Python via .NET ile Excel su sıralı grafikte toplam noktaları yapılandırmayı adım adım anlatan bir kılavuz.
---

## **Excel Grafiklerinde "Set Point as Total" nedir**

Bazı Excel grafikleri, örneğin su sıralı grafiklerde, belirli veri noktaları önceki değerlerin toplamını temsil eder. Bu makale, Aspose.Cells kullanarak bu toplam noktalarını programatik olarak nasıl yapılandıracağınızı gösterecek.

## **Toplam Noktası Gerektiren Su Sıralı Grafik**

![todo:image_alt_text](set-as-total1.png)

Bu su sıralı grafik örneğinde, önceki değerleri toplayan dört "Toplam" veri noktası gösterilir. Vurgulanan "Toplam 2024" noktası, orijinal dosyada yapılandırılmamış toplam durumunu gösterir. Takip etmek için [örnek Excel dosyasını](SampleSheet.xlsx) indir.

## **Aspose.Cells for Python kullanarak Toplam Noktalarını Yapılandırma**

Aşağıdaki kod, uygun toplam nokta yapılandırmasını gösterir:

```python
import aspose.cells as cells
from aspose.cells.charts import ChartType

# Load sample workbook
workbook = cells.Workbook("SampleSheet.xlsx")

try:
    # Access first worksheet and chart
    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    # Verify chart type
    if chart.type == ChartType.WATERFALL:
        # Configure chart data range
        chart.set_data_range("A1:B8", True)

        # Customize series formatting
        chart.n_series.is_color_varied = True

        # Configure total points (0-based indices)
        total_points = [3, 5, 7]  # Points to mark as totals
        for i in total_points:
            point = chart.n_series.points[i]
            point.is_total = True

        # Save modified workbook
        workbook.save("output.xlsx")

except Exception as e:
    print(f"Error processing workbook: {str(e)}")
```

```python
import os
from aspose.cells import Workbook

file_path = ""
wb = Workbook(os.path.join(file_path, "SampleSheet.xlsx"))
worksheet = wb.worksheets[0]
chart = worksheet.charts.get("Graphiq5")

# Set some points as total column
# In this example, we set points 0, 4, 8, 12 as total
chart.n_series[0].layout_properties.subtotals = [0, 4, 8, 12]
wb.save(os.path.join(file_path, "output.xlsx"))
```

Düzeltilmiş [çıktı dosyası](output.xlsx) toplam noktalarını düzgün şekilde yapılandırır:

![todo:image_alt_text](set-as-total2.png)

Ana uygulama ayrıntıları:
- Veri noktaları için 0 tabanlı indeksler kullanın
- `is_total` özelliğini `ChartPoint` nesnelerine ayarlayın
- Uygun veri aralığı yapılandırmasını sağlayın
- Grafik türü doğrulamasını yönetin

Gelişmiş yapılandırma seçenekleri için [ChartPoint belgelerine](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/) bakın.
{{< app/cells/assistant language="python-net" >}}
