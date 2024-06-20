---
title: Grafik Eğrisi Eğilimi Denklem Metnini Alın
linktitle: Trendline
type: docs
weight: 90
url: /tr/java/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak Grafik Eğilim Çizgisinin Denklem Metnini alabilirsiniz. Aspose.Cells, eğilim çizgisinin denklem metnini döndüren [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) özelliğini sağlar. Bu özelliği kullanmak için öncelikle [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) yöntemini çağırmanız gerekecektir.

{{% /alert %}}

## **Örnek**

Aşağıdaki ekran görüntüsü eğilim çizgisi olan Grafiği ve Denklem Metnini Kırmızı renkte göstermektedir. Bu metni aşağıdaki örnek kodda [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) özelliğini kullanarak alacağız.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

### Grafik trend çizgisinin denklem metnini almak için Java kodu

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### Örnek kod tarafından üretilen çıktı

Yukarıdaki örnek kodun konsol çıktısı budur.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
