---
title: Golang ile C++ kullanarak Hesaplanan Öğeler içeren Pivot Tablo yu Yenile ve Hesapla
linktitle: Yenileme ve Hesaplanmış Öğeleri Olan Özet Tabloyu Yenileme
type: docs
weight: 40
url: /tr/go-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Aspose.Cells kullanarak Golang ile C++ üzerinden hesaplanan öğeleri içeren Pivot Tablo yu yenile ve hesapla
---

{{% alert color="primary" %}}

Aspose.Cells artık hesaplanmış öğeleri içeren pivot tablosunu yenileme ve hesaplama işlemini destekler. Bunun için bu işlemi gerçekleştirmek için değişkenleri [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/go-cpp/pivottable/refreshdata/) ve [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) kullanmalısınız.

{{% /alert %}}

## **Hesaplanmış öğeleri olan özet tabloyu yenileme ve hesaplama**

 Aşağıdaki örnek kod, üç hesaplanan öğe içeren pivot tabloyu ("add", "div", "div2") içeren [kaynak excel dosyasını](5115238.xlsx) yükler. İlk olarak D2 hücresinin değerini 20 yapar, ardından Aspose.Cells API'leri kullanarak pivot tabloyu yeniler ve hesaplar ve çalışma kitabını PDF formatında kaydeder. [Çıktı PDF'sinde](5115229.pdf) Aspose.Cells'in pivot tabloyu başarıyla yenilediği ve hesapladığı görülür. Bunu, Microsoft Excel’de D2 hücresine manuel olarak 20 değerini koyup Alt+F5 kısayolu veya Pivot Tabloyu Yenile düğmesine tıklayarak doğrulayabilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshAndCalculatePivotTableHavingCalculatedItems.go" >}}
