---
title: Grafikte hangi Eksenin bulunduğunu belirleyin
type: docs
weight: 140
url: /tr/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Bazen, kullanıcının Grafikte belirli bir eksen olup olmadığını bilmesi gerekir. Örneğin, grafiğin içinde bir İkincil Değer Ekseninin var olup olmadığını bilmek istiyor. Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Donut, DonutExploded, vb. gibi bazı grafiklerin ekseni yoktur.

 Aspose.Cells sağlar[**Chart.HasAxis(AxisType eksenTürü, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) Grafiğin belirli bir ekseni olup olmadığını belirleme yöntemi.

{{% /alert %}}

 Aşağıdaki örnek kod, kullanımını gösterir[**Chart.HasAxis(AxisType eksenTürü, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)örnek grafiğin Birincil ve İkincil Kategoriye ve Değer Eksenine sahip olup olmadığını belirlemek için.

## Grafikte hangi eksenin bulunduğunu belirlemek için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Örnek kod tarafından oluşturulan konsol çıktısı

Birincil Kategori ve Değer Ekseni için doğru ve İkincil Kategori ve Değer Ekseni için yanlış gösteren kodun konsol çıktısı aşağıda gösterilmiştir.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
