---
title: Grafiğin hangi Eksenin varolduğunu belirle.
description: Aspose.Cells for Python via .NET kullanılarak oluşturulan bir grafikte hangi eksenin olduğunu belirlemeyi öğrenin. Rehberimiz, kategoriler, değerler ve ikincil eksenler dahil olmak üzere grafikte farklı eksenleri tanımlama ve erişme konusunda size yardımcı olacaktır.
keywords: Aspose.Cells for Python via .NET, grafik, eksen, varlığı, kategori, değer, ikincil.
type: docs
weight: 140
url: /tr/python-net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Bazı durumlarda kullanıcı, belirli bir eksenin grafikte var olup olmadığını bilmek isteyebilir. Örneğin, grafikte İkincil Değer Ekseni'nin var olup olmadığını bilmek isteyebilir. Bazı grafikler (Pasta, Patlamış Pasta, PastaPasta, PastaBar, Pasta3D, Patlamış Pasta3D, Donut, Patlamış Donut vb.) ekseni bulundurmaz.

Aspose.Cells for Python via .NET, grafik, eksen, varlık durumu, belirli bir eksen olup olmadığını belirlemek için [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) yöntemini sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, örnek grafikte Birincil ve İkincil Kategori ve Değer Ekseni'nin olup olmadığını belirlemek için [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis)'nin kullanımını göstermektedir.

## Grafikte hangi eksenin varolduğunu belirlemek için C# kodu

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DetermineAxisInChart.py" >}}

## Örnek Kod Tarafından Oluşturulan Konsol Çıktısı

Kodun konsol çıktısı aşağıda gösterilmiştir, Birincil Kategori ve Değer Eksenleri için true ve İkincil Kategori ve Değer Eksenleri için false göstermektedir.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
