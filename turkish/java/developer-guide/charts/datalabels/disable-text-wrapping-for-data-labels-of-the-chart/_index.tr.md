---
title: Grafiğin Veri Etiketlerinin Metin Sarılmasını Devre Dışı Bırakma
type: docs
weight: 60
url: /tr/java/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013, bir grafiğin veri etiketlerinin metnini sarmaya veya sarmamaya izin verir. Varsayılan olarak, veri etiketi metni sarmalanmıştır.

{{% /alert %}}

Aspose.Cells, [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) metodunu sağlar. Metin sarmalamayı etkinleştirmek veya devre dışı bırakmak için **True** veya **False** olarak ayarlayın.

Benzer şekilde, bir veri etiketinin zaten sarılı olup olmadığını bulmak için [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) metodunu kullanın.

Bu ekran görüntüsü, Microsoft Excel 2013 içeren bir örnek Excel dosyasını gösterir, içinde veri etiketlerinin metni sarılmıştır. Görebileceğiniz gibi, Microsoft Excel 2013'ün Format Datalabels panelinin ALIGNMENT bölümünde **Şeklin içinde metni sarma** seçeneğini kontrol edip temizleyebilirsiniz.

**Veri etiketlerini sarma**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

Aşağıdaki örnek kod, Aspose.Cells kullanarak örnek Microsoft Excel dosyasını yükler ve [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) yöntemini kullanarak veri etiketi metin sarmasını devre dışı bırakır. Kod çalıştırıldığında, grafik şu şekilde görünecektir. Önceden sarmalanmış metin artık sarmalanmamıştır.

**Veri etiketlerini yalnızca bir satırda gösterme**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
{{< app/cells/assistant language="java" >}}
