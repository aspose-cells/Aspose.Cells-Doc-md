---
title: Yenileme ve Hesaplanmış Öğeleri Olan Özet Tabloyu Yenileme
type: docs
weight: 130
url: /tr/java/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells artık hesaplanmış öğeleri olan özet tablonun yenilenmesini ve hesaplanmasını destekler. Bu işlemi gerçekleştirmek için bu fonksiyonu normalde olduğu gibi [**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) ve [**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) kullanın.

{{% /alert %}}

## **Hesaplanmış öğeleri olan özet tabloyu yenileme ve hesaplama**

Aşağıdaki örnek kod, "ekle", "böl" ve "böl2" gibi üç hesaplanmış öğeye sahip bir özet tablo içeren [kaynak excel dosyasını](5473428.xlsx) yükler. İlk olarak D2 hücresinin değerini 20 olarak değiştirir, ardından Aspose.Cells API'leri kullanılarak özet tablonun yenilenmesi ve hesaplanması yapılır ve çalışma kitabı PDF formatında kaydedilir. [Çıktı PDF](5473431.pdf) sonuçları, Aspose.Cells'ın başarılı bir şekilde hesaplanmış öğeleri olan özet tabloyu yenilediğini ve hesapladığını gösterir. Bu durumu, Microsoft Excel'in Alt+F5 kısayol tuşunu kullanarak veya özet tablo Yenileme düğmesine tıklayarak manuel olarak D2 hücresine 20 değerini yerleştirerek doğrulayabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
