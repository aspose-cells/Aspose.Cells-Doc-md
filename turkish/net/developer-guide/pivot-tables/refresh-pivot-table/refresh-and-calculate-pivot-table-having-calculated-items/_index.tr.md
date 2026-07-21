---
title: Yenileme ve Hesaplanmış Öğeleri Olan Özet Tabloyu Yenileme
type: docs
weight: 40
url: /tr/net/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells artık hesaplanmış öğeleri içeren pivot tablosunu yenileme ve hesaplama işlemini destekler. Bunun için bu işlemi gerçekleştirmek için değişkenleri [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) ve [**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) kullanmalısınız.

{{% /alert %}}

## **Hesaplanmış öğeleri olan özet tabloyu yenileme ve hesaplama**

Aşağıdaki örnek kod, içerisinde "add", "div" ve "div2" gibi üç hesaplanmış öğe bulunan bir pivot tablosunu içeren [kaynak excel dosyasını](5115238.xlsx) yükler. İlk olarak D2 hücresinin değerini 20 olarak değiştiririz ve sonra Aspose.Cells API'lerini kullanarak pivot tablosunu yeniler ve hesaplar, ardından sonucu PDF formatında kaydeder. [Çıktı PDF'indeki](5115229.pdf) sonuçlar, Aspose.Cells'in başarılı bir şekilde hesaplanmış öğeleri içeren pivot tablosunu yenilediğini ve hesaplama yaptığını göstermektedir. Bu durumu Microsoft Excel'i kullanarak manuel olarak D2 hücresine 20 değerini girerek ve sonra pivot tablosunu Alt+F5 kısayol tuşunu kullanarak veya pivot tablosu Yenile düğmesine tıklayarak doğrulayabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
