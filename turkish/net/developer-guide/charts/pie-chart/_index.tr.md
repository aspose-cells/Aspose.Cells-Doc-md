---
title: Lider Çizgilerle Pasta Grafiği Oluşturma
linktitle: Yuvarlak diyagram
type: docs
weight: 45
url: /tr/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

 Bu makalede, Aspose.Cells for .NET API kullanılırken sıfırdan lider çizgileri olan bir pasta grafiğin nasıl oluşturulacağı açıklanmaktadır. Excel'de 'Lider çizgileri göster' seçeneği varsayılan olarak ayarlanmıştır, böylece Excel'de bir pasta grafiği oluşturduğunuzda lider çizgiler gösterilir. Ancak, Aspose.Cells API'leri ile benzer bir grafik oluştururken, açıkça ayarlamanız gerekir.[**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) Emlak.

{{% /alert %}}

Aspose.Cells for .NET API'in lider çizgileri olan bir pasta grafiği oluşturmak için kullanımını göstermek için önce yeni bir tane oluşturacağız.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ve seri veri kaynağı olarak hizmet edecek bazı verileri girin. Veriler yerleştirildikten sonra, bir ekleyeceğiz[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) tipi[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)grafik koleksiyonuna gidin ve istenen grafik görünümünü elde etmek için farklı yönlerini ayarlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Şimdiye kadar bir pasta grafiği oluşturduk ve farklı yönlerini belirledik. Şimdi grafik için lider çizgileri açacağız. Lütfen lider çizgileri göstermek için veri etiketlerini biraz hareket ettirmemiz gerektiğini unutmayın.

Aşağıdaki kod parçası öncü çizgileri açar, grafiği yeniler ve ardından veri etiketlerinin konumlarını uygun şekilde hareket ettirmek için hesaplar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Son olarak, aşağıdaki kod grafiği resim formatında ve çalışma kitabını XLSX formatında kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Sonuç Pasta Grafiği**|
|:- |
|![yapılacaklar:resim_alternatif_metin](creating-pie-chart-with-leader-lines_1.png)|

## **ileri konular**
- [Pasta Grafikte Özel Dilim veya Sektör Renkleri](/cells/tr/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Veri Noktalarının İkinci Pastada veya Pasta Pastası veya Pasta Çubuğu Grafiğindeki Çubukta olup olmadığını bulun](/cells/tr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## İlgili Makaleler

- [Grafik Oluşturma](/cells/tr/net/creating-charts/)
- [Grafikleri Özelleştirme](/cells/tr/net/customizing-charts/)
- [Grafiklerde Veri Biçimlendirme](/cells/tr/net/data-formatting-in-charts/)
- [Ayar Tablosu Görünümü](/cells/tr/net/setting-chart-appearance/)

