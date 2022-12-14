---
title: Hesaplanan Öğelere Sahip Pivot Tabloyu Yenileyin ve Hesaplayın
type: docs
weight: 130
url: /tr/java/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells artık hesaplanan öğelere sahip pivot tablonun yenilenmesini ve hesaplanmasını destekliyor. Lütfen kullan[**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) ve[**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData()) bu işlevi gerçekleştirmek için her zamanki gibi.

{{% /alert %}}

## **Hesaplanan Öğelere Sahip Pivot Tabloyu Yenileyin ve Hesaplayın**

 Aşağıdaki örnek kod,[kaynak excel dosyası](5473428.xlsx)"add", "div", "div2" gibi hesaplanan üç öğeye sahip bir pivot tablo içerir. Önce D2 hücresinin değerini 20 olarak değiştiriyoruz ve ardından Aspose.Cells API'leri kullanarak pivot tabloyu yenileyip hesaplıyor ve çalışma kitabını PDF formatında kaydediyoruz. Sonuçlar[çıktı PDF](5473431.pdf) Aspose.Cells'in öğeleri başarıyla hesaplayarak pivot tabloyu yenilediğini ve hesapladığını gösterir. Microsoft Excel kullanarak, D2 hücresine 20 değerini manuel olarak koyarak ve ardından Alt+F5 kısayol tuşuyla veya pivot tablo Yenile düğmesine tıklayarak pivot tabloyu yenileyerek doğrulayabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
