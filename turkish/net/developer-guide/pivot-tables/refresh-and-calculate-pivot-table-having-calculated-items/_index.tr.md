---
title: Hesaplanan Öğelere Sahip Pivot Tabloyu Yenileyin ve Hesaplayın
type: docs
weight: 40
url: /tr/net/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells artık hesaplanan öğelere sahip pivot tablonun yenilenmesini ve hesaplanmasını destekliyor. lütfen[**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) ve[**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) Bu işlevi gerçekleştirmek için her zamanki gibi.

{{% /alert %}}

## **Hesaplanan Öğelere Sahip Pivot Tabloyu Yenileyin ve Hesaplayın**

 Aşağıdaki örnek kod,[kaynak excel dosyası](5115238.xlsx)"add", "div", "div2" gibi hesaplanan üç öğeye sahip bir pivot tablo içerir. Önce D2 hücresinin değerini 20 olarak değiştiriyoruz ve ardından Aspose.Cells API'leri kullanarak pivot tabloyu yenileyip hesaplıyor ve çalışma kitabını PDF formatında kaydediyoruz. Sonuçlar[çıkış PDF](5115229.pdf) Aspose.Cells'in öğeleri başarıyla hesaplayarak pivot tabloyu yenilediğini ve hesapladığını gösterir. Microsoft Excel kullanarak, D2 hücresine 20 değerini manuel olarak koyarak ve ardından Alt+F5 kısayol tuşuyla veya pivot tablo Yenile düğmesine tıklayarak pivot tabloyu yenileyerek doğrulayabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
