---
title: Lider Çizgilerle Pasta Grafiği Oluşturma
description: Microsoft Excel'de öncü çizgileri olan bir pasta grafiği oluşturmak için Aspose.Cells for .NET'i nasıl kullanacağınızı öğrenin. Kılavuzumuz, veri noktalarını göstergeye bağlayan ve grafiğinizin genel netliğini artıran öncü çizgilerin nasıl ekleneceğini gösterecektir.
keywords: Aspose.Cells for .NET, Pie Chart, Leader Lines, Microsoft Excel, Data Visualization, Chart Customization.
linktitle: Yuvarlak diyagram
type: docs
weight: 45
url: /tr/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

Bu makalede, Aspose.Cells for .NET API'i kullanarak sıfırdan lider çizgileri olan bir pasta grafiğinin nasıl oluşturulacağı açıklanmaktadır. Excel'de, 'Öncü çizgilerini göster' seçeneği varsayılan olarak ayarlıdır, böylece Excel'de bir pasta grafiği oluşturduğunuzda öncü çizgiler gösterilir. Ancak Aspose.Cells API'leri ile benzer bir grafik oluştururken, açık bir şekilde ayarlamanız gerekir.[**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) mülk.

{{% /alert %}}

 Lider çizgileri olan bir pasta grafiği oluşturmak için Aspose.Cells for .NET API'in kullanımını göstermek için önce yeni bir pasta grafiği oluşturacağız.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ve seri veri kaynağı olarak görev yapacak bazı verileri girin. Veriler yerleştirildikten sonra bir ekleyeceğiz[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) türün[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)İstediğiniz grafik görünümünü elde etmek için grafik koleksiyonuna gidin ve farklı yönlerini ayarlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Şu ana kadar bir pasta grafiği oluşturduk ve farklı yönlerini belirledik. Şimdi grafik için lider çizgilerini açacağız. Lider çizgileri göstermek için veri etiketlerini biraz hareket ettirmemiz gerektiğini lütfen unutmayın.

Aşağıdaki kod parçası öncü çizgileri açar, grafiği yeniler ve ardından veri etiketlerinin konumlarını uygun şekilde taşımak için hesaplar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Son olarak aşağıdaki kod, grafiği resim formatında ve çalışma kitabını XLSX formatında kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Sonuç Pasta Grafiği**|
| :- |
|![yapılacak şey:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

##  **İleri konular**
- [Pasta Grafiğinde Özel Dilim veya Sektör Renkleri](/cells/tr/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Veri Noktalarının Pasta Pastası veya Pasta Çubuğu Grafiğindeki İkinci Pasta veya Çubukta olup olmadığını bulma](/cells/tr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

##  İlgili Makaleler

- [Grafik Oluşturma](/cells/tr/net/creating-charts/)
- [Grafikleri Özelleştirme](/cells/tr/net/customizing-charts/)
- [Grafiklerde Veri Formatlama](/cells/tr/net/data-formatting-in-charts/)
- [Grafik Görünümünü Ayarlama](/cells/tr/net/setting-chart-appearance/)

