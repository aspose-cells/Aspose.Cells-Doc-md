---
title: Yenileme ve Hesaplanmış Öğeleri Olan Özet Tabloyu Yenileme
type: docs
weight: 40
url: /tr/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: Hesaplanmış Öğeler Bulunan Pivot Tablosunun Nasıl Yenileneceği ve Hesaplanacağı Aspose.Cells for Python via .NET ile nasıl yapılır.
keywords: Aspose.Cells, Python için Excel, Excel Python kütüphanesi, Hesaplanmış Öğeler İçeren Özet Tablonun Yenilenmesi ve Hesaplanması
---

{{% alert color="primary" %}}

Python için Aspose.Cells via .NET artık hesaplanmış öğeleri olan özet tabloyu yenileme ve hesaplama işlemini gerçekleştirmek için genellikle [**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) ve [**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) kullanmanızı desteklemektedir.

{{% /alert %}}

## **Hesaplanmış öğeleri olan özet tabloyu yenileme ve hesaplama**

Aşağıdaki örnek kod, 'add', 'div', 'div2' gibi üç hesaplanmış öğesi olan bir özet tabloyu içeren [kaynak excel dosyasını](5115238.xlsx) yükler. Önce D2 hücresinin değerini 20 olarak değiştirir ve ardından Aspose.Cells için Python via .NET API'leri kullanarak özet tabloyu yeniler ve hesaplar, ve çalışma kitabını PDF formatında kaydeder. Sonuçlar [çıktı PDF'inde](5115229.pdf) gösterilmektedir. Aspose.Cells için Python via .NET'nin hesaplanmış öğeleri olan özet tabloyu başarıyla yenilediğini ve hesapladığını kontrol etmek için manuel olarak D2 hücresine 20 değerini yerleştirerek ve ardından alt+F5 kısayol tuşu ile veya özet tabloyu tıklatarak yenileyebilirsiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
