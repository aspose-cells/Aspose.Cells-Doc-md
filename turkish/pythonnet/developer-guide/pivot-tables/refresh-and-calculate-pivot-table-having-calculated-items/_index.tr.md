---
title: Hesaplanan Öğelere Sahip Pivot Tabloyu Yenileyin ve Hesaplayın
type: docs
weight: 40
url: /tr/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: Bu makalede, Aspose.Cells for Python via .NET ile Hesaplanan Öğelere Sahip Pivot Tablonun nasıl Yenileneceği ve Hesaplanacağı gösterilmektedir.
keywords: Refresh and Calculate Pivot Table with Calculated Items
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET artık hesaplanan öğelere sahip pivot tablonun yenilenmesini ve hesaplanmasını destekliyor. Lütfen şunu kullanın:[**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) Ve[**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) Bu işlevi gerçekleştirmek için her zamanki gibi.

{{% /alert %}}

##  **Hesaplanan Öğelere Sahip Pivot Tabloyu Yenileyin ve Hesaplayın**

 Aşağıdaki örnek kod,[kaynak excel dosyası](5115238.xlsx)"add", "div", "div2" gibi hesaplanmış üç öğeye sahip bir pivot tablo içeren. Önce D2 hücresinin değerini 20 olarak değiştiriyoruz ve ardından Aspose.Cells for Python via .NET API'lerini kullanarak pivot tabloyu yenileyip hesaplıyoruz ve çalışma kitabını PDF formatında kaydediyoruz. Sonuçlar[çıkış PDF](5115229.pdf) Aspose.Cells for Python via .NET'in öğeleri başarıyla hesaplayan pivot tabloyu yenilediğini ve hesapladığını gösterir. Microsoft Excel'i kullanarak, D2 hücresine 20 değerini manuel olarak koyarak ve ardından Alt+F5 kısayol tuşuyla pivot tabloyu yenileyerek veya pivot tablo Yenile düğmesini tıklatarak bunu doğrulayabilirsiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
