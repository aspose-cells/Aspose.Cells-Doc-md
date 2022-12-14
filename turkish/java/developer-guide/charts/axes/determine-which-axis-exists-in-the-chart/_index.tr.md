---
title: Grafikte hangi Eksenin bulunduğunu belirleyin
type: docs
weight: 130
url: /tr/java/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Bazen, kullanıcının Grafikte belirli bir eksen olup olmadığını bilmesi gerekir. Örneğin, grafiğin içinde bir İkincil Değer Ekseninin var olup olmadığını bilmek istiyor. Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Donut, DonutExploded vb. gibi bazı grafiklerin ekseni yoktur.

 Aspose.Cells sağlar[**Chart.hasAxis(int eksenTürü, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)) grafiğin belirli bir ekseni olup olmadığını belirleme yöntemi.

{{% /alert %}}

## Grafikte hangi Eksenin bulunduğunu belirleyin

Aşağıdaki ekran görüntüsü, yalnızca Birincil Kategori ve Değer Eksenine sahip bir grafiği göstermektedir. Herhangi bir İkincil Kategorisi ve Değer Ekseni yoktur.

![yapılacaklar:resim_alternatif_Metin](determine-which-axis-exists-in-the-chart_1.png)

 Aşağıdaki örnek kod, kullanımını gösterir[**Chart.hasAxis(int eksenTürü, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)örnek grafiğin Birincil ve İkincil Kategori ve Değer Ekseni olup olmadığını belirlemek için. Birincil Kategori ve Değer Ekseni için doğru ve İkincil Kategori ve Değer Ekseni için yanlış gösteren kodun konsol çıktısı aşağıda gösterilmiştir.

### Grafikte hangi eksenin bulunduğunu belirlemek için Java kodu

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Örnek kod tarafından oluşturulan konsol çıktısı

İşte yukarıdaki Örnek Kodun Konsol Çıktısı.

{{< highlight "java" >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
