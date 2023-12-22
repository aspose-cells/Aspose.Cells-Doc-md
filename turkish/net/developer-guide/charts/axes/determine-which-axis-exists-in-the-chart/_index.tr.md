---
title: Grafikte hangi Eksenin bulunduğunu belirleyin
description: Aspose.Cells for .NET kullanılarak oluşturulan bir grafikte hangi eksenin bulunduğunu nasıl belirleyeceğinizi öğrenin. Kılavuzumuz, kategori, değer ve ikincil eksenler dahil olmak üzere bir grafikteki farklı eksenleri nasıl tanımlayacağınızı ve bunlara nasıl erişeceğinizi anlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for .NET, chart, axis, existence, category, value, secondary.
type: docs
weight: 140
url: /tr/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Bazen kullanıcının Grafikte belirli bir eksenin mevcut olup olmadığını bilmesi gerekir. Örneğin grafikte İkincil Değer Ekseninin var olup olmadığını bilmek istiyor. Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded vb. gibi bazı grafiklerin ekseni yoktur.

 Aspose.Cells sağlar[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) Grafiğin belirli bir eksene sahip olup olmadığını belirleme yöntemi.

{{% /alert %}}

 Aşağıdaki örnek kod kullanımını göstermektedir:[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)Örnek grafiğin Birincil ve İkincil Kategori ve Değer Eksenine sahip olup olmadığını belirlemek için.

##  Grafikte hangi eksenin bulunduğunu belirlemek için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Örnek kod tarafından oluşturulan konsol çıktısı

Kodun Birincil Kategori ve Değer Ekseni için doğru, İkincil Kategori ve Değer Ekseni için yanlış değerini gösteren konsol çıktısı aşağıda gösterilmiştir.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
