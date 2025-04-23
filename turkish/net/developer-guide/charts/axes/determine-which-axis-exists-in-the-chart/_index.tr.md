---
title: Grafiğin hangi Eksenin varolduğunu belirle.
description: Aspose.Cells for .NET kullanarak oluşturulan bir grafikte hangi ekseni belirlemenin nasıl yapılacağını öğrenin. Rehberimiz, kategori, değer ve ikincil eksenler de dahil olmak üzere bir grafikte farklı ekseni tanımlamanıza ve erişmenize yardımcı olacaktır.
keywords: Aspose.Cells for .NET, grafik, eksen, varlık, kategori, değer, ikincil.
type: docs
weight: 140
url: /tr/net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Bazı durumlarda kullanıcı, belirli bir eksenin grafikte var olup olmadığını bilmek isteyebilir. Örneğin, grafikte İkincil Değer Ekseni'nin var olup olmadığını bilmek isteyebilir. Bazı grafikler (Pasta, Patlamış Pasta, PastaPasta, PastaBar, Pasta3D, Patlamış Pasta3D, Donut, Patlamış Donut vb.) ekseni bulundurmaz.

Aspose.Cells, belirli bir eksenin grafikte var olup olmadığını belirlemek için [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) methodunu sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, örnek grafikte Birincil ve İkincil Kategori ve Değer Ekseni'nin olup olmadığını belirlemek için [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)'nin kullanımını göstermektedir.

## Grafikte hangi eksenin varolduğunu belirlemek için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Örnek Kod Tarafından Oluşturulan Konsol Çıktısı

Kodun konsol çıktısı aşağıda gösterilmiştir, Birincil Kategori ve Değer Eksenleri için true ve İkincil Kategori ve Değer Eksenleri için false göstermektedir.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
