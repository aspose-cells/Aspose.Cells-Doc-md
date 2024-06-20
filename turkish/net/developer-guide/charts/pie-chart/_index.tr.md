---
title: Lider Çizgilerle Pasta Grafiği Oluşturma
description: Microsoft Excel de lider çizgilerle bir pasta grafiği oluşturmak için Aspose.Cells for .NET yi nasıl kullanacağınızı öğrenin. Rehberimiz, veri noktalarını efsaneye bağlayan lider çizgileri eklemenin ve grafiğinizin genel netliğini artırmanın nasıl yapıldığını gösterecektir.
keywords: Aspose.Cells for .NET, Pasta Grafiği, Lider Çizgiler, Microsoft Excel, Veri Görselleştirme, Grafik Özelleştirme.
linktitle: Pasta Grafiği
type: docs
weight: 45
url: /tr/net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Bu makale, Aspose.Cells for .NET API'sını kullanarak baştan bir pasta grafiği nasıl oluşturacağınızı açıklar. Excel'de 'Lider çizgileri göster' seçeneği varsayılan olarak ayarlıdır, bu nedenle Excel'de bir pasta grafiği oluşturduğunuzda lider çizgiler gösterilir. Bununla birlikte, Aspose.Cells API'ları ile benzer bir grafik oluştururken, [**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) özelliğini açıkça ayarlamanız gerekir.

{{% /alert %}}

Aspose.Cells for .NET API'nın lider çizgilerle bir pasta grafiği oluşturmak için kullanımını göstermek için önce yeni bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) oluşturacağız ve seri veri kaynağı olarak hizmet edecek bazı verileri gireceğiz. Veri yerine geldiğinde, [**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) türünden bir [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) koleksiyonuna ekleyeceğiz ve istenen grafik görünümünü elde etmek için farklı yönlerini ayarlayacağız.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Şimdiye kadar bir pasta grafiği oluşturduk ve farklı yönlerini ayarladık. Şimdi grafiğin lider çizgilerini açmaya hazırlanıyoruz. Lütfen unutmayın, lider çizgileri göstermek için veri etiketlerini biraz hareket ettirmemiz gerekiyor.

Aşağıdaki kod parçası lider çizgileri açar, grafiği yeniler ve ardından veri etiketlerinin konumlarını uygun şekilde hareket ettirir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Son olarak, aşağıdaki kod çizgiyi görüntü formatında ve çalışma kitabını XLSX formatında kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

**Sonuçta Oluşan Pasta Grafiği**
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Gelişmiş Konular**
- [Pasta Grafiğinde Özel Dilim veya Sektör Renkleri](/cells/tr/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Bir Pasta-grafik veya Çubuk-grafikte Veri Noktalarının İkinci Pasta'nın veya Pasta'nın Çubuğu'nun Üzerinde Olup Olmadığını Bulma](/cells/tr/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## İlgili Makaleler

- [Grafikler Oluşturma](/cells/tr/net/creating-charts/)
- [Grafikleri Özelleştirme](/cells/tr/net/customizing-charts/)
- [Grafiklerde Veri Biçimlendirme](/cells/tr/net/data-formatting-in-charts/)
- [Grafik Görünümünü Ayarlama](/cells/tr/net/setting-chart-appearance/)

