---
title: Yenileme ve Hesaplanmış Öğeleri Olan Özet Tabloyu Yenileme
type: docs
weight: 40
url: /tr/nodejs-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ artık hesaplanmış öğelerin bulunduğu pivot tabloları yenileme ve hesaplama desteği sağlar. Lütfen bu fonksiyonu gerçekleştirmek için [**PivotTable.refreshData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#refreshdata--) ve [**PivotTable.calculateData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#calculatedata--) kullanın.

{{% /alert %}}

## **Hesaplanmış öğeleri olan özet tabloyu yenileme ve hesaplama**

Aşağıdaki örnek kod, üç hesaplanmış öğe içeren bir pivot tabloyu içeren [kaynak excel dosyasını](5115238.xlsx) yükler. Öncelikle D2 hücresinin değerini 20 yapıyoruz ve ardından Aspose.Cells for Node.js via C++ API'leri kullanarak pivot tabloyu yeniliyor ve hesaplıyoruz, ve çalışma kitabını PDF formatında kaydediyoruz. Sonuçlar, [çıktı PDF'sinde](5115229.pdf) Aspose.Cells for Node.js via C++'ün hesaplanan öğeleri içeren pivot tabloyu başarıyla yenilediğini ve hesapladığını gösterir. Bunu doğrulamak için, Microsoft Excel kullanarak D2 hücresine manuel olarak 20 değerini koyabilir ve ardından Alt+F5 kısayolu veya Pivot Tablo Yenile düğmesine tıklayarak pivot tabloyu yenileyebilirsiniz.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTable-RefreshAndCalculateItems-1.js" >}}

