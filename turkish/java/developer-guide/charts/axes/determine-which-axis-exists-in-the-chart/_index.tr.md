---
title: Grafiğin hangi Eksenin varolduğunu belirle.
type: docs
weight: 130
url: /tr/java/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Bazen, kullanıcının belirli bir eksenin grafikte var olup olmadığını bilmeye ihtiyacı vardır. Örneğin, Grafik içinde İkinci Değer Ekseni var mı yok mu öğrenmek istiyor. Bazı grafik türleri, Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded vb. ekseni bulunmamaktadır.

Aspose.Cells, belirli bir eksenin grafikte var olup olmadığını belirlemek için [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-) methodunu sağlar.

{{% /alert %}}

## Grafiğe Hangi Eksenin Varolduğunu Belirle

Aşağıdaki ekran görüntüsü, yalnızca Birincil Kategori ve Değer Eksenine sahip bir grafiği gösterir. Herhangi bir İkincil Kategori ve Değer Ekseni bulunmamaktadır.

![todo:image_alt_text](determine-which-axis-exists-in-the-chart_1.png)

Aşağıdaki örnek kod, örnek grafiğin Birincil ve İkincil Kategori ve Değer Eksenine sahip olup olmadığını belirlemek için [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-) kullanımını gösterir. Kodun konsol çıktısı, aşağıda gösterilmiştir; Bu çıktı, Birincil Kategori ve Değer Ekseni için true ve İkincil Kategori ve Değer Ekseni için false değerlerini gösterir.

### Bir grafikte bulunan eksenleri belirlemek için Java kodu

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Örnek kod tarafından oluşturulan konsol çıktısı

Yukarıdaki Örnek Kodunun Konsol Çıktısı.

{{< highlight java >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
