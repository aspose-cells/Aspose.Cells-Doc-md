---
title: Lider Çizgilerle Pasta Grafiği Oluşturma
description: Aspose.Cells for Python via .NET kullanarak, Microsoft Excel de lider çizgileri olan pasta grafik oluşturmayı öğrenin. Kılavuzumuz, veri noktalarını sembollerle bağlayan lider çizgileri eklemeyi ve grafiklerin genel netliğini artırmayı gösterecek.
keywords: Aspose.Cells for Python via .NET, Pasta Grafiği, Lider Çizgileri, Microsoft Excel, Veri Görselleştirme, Grafik Özelleştirme.
linktitle: Pasta Grafiği
type: docs
weight: 45
url: /tr/python-net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Bu makale, Aspose.Cells for Python via .NET API kullanarak sıfırdan lider çizgili pasta grafik oluşturma yöntemini açıklar. Excel’de, 'Lider çizgilerini göster' seçeneği varsayılan olarak ayarlanmıştır, bu nedenle Excel’de pasta grafik oluşturduğunuzda lider çizgileri gösterilir. Ancak, Aspose.Cells for Python via .NET API'leriyle benzer bir grafik oluştururken, [**Series.has_leader_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/has_leader_lines) özelliğini açıkça ayarlamanız gerekir.

{{% /alert %}}

Aspose.Cells for Python via .NET API kullanarak lider çizgili bir pasta grafik oluşturmak için ilk olarak yeni bir [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) oluşturacağız ve serilerin veri kaynağı olacak verileri gireceğiz. Veri hazır olduktan sonra, koleksiyona [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) nesnesi ekleyecek ve istediğiniz görünüm elde etmek için farklı yönlerini ayarlayacağız.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateWorkbook.py" >}}

Şimdiye kadar bir pasta grafiği oluşturduk ve farklı yönlerini ayarladık. Şimdi grafiğin lider çizgilerini açmaya hazırlanıyoruz. Lütfen unutmayın, lider çizgileri göstermek için veri etiketlerini biraz hareket ettirmemiz gerekiyor.

Aşağıdaki kod parçası lider çizgileri açar, grafiği yeniler ve ardından veri etiketlerinin konumlarını uygun şekilde hareket ettirir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TurnOnLeaderLines.py" >}}

Son olarak, aşağıdaki kod çizgiyi görüntü formatında ve çalışma kitabını XLSX formatında kaydeder.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SaveChartInImageAndWorkbookInXLSX.py" >}}

**Sonuçta Oluşan Pasta Grafiği**
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Gelişmiş Konular**
- [Pasta Grafiğinde Özel Dilim veya Sektör Renkleri](/cells/tr/python-net/custom-slice-or-sector-colors-in-pie-chart/)
- [Bir Pasta-grafik veya Çubuk-grafikte Veri Noktalarının İkinci Pasta'nın veya Pasta'nın Çubuğu'nun Üzerinde Olup Olmadığını Bulma](/cells/tr/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## İlgili Makaleler

- [Grafikler Oluşturma](/cells/tr/python-net/creating-charts/)
- [Grafikleri Özelleştirme](/cells/tr/python-net/customizing-charts/)
- [Grafiklerde Veri Biçimlendirme](/cells/tr/python-net/data-formatting-in-charts/)
- [Grafik Görünümünü Ayarlama](/cells/tr/python-net/setting-chart-appearance/)

{{< app/cells/assistant language="python-net" >}}
