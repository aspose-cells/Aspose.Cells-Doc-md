---
title: Pasta Grafiğinde Özel Dilim veya Sektör Renkleri
type: docs
weight: 30
url: /tr/java/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

Bu makale, pasta grafik dilimlerine/ sektörlerine özel renkler eklemenin nasıl yapılacağını açıklar. Varsayılan olarak, pasta grafikleri Microsoft Excel'in varsayılan şablonunu kullanır. Diğer renkleri kullanmak için grafikte renkleri yeniden tanımlamak mümkündür.

{{% /alert %}}

Pasta grafiğinin bireysel dilimleri veya sektörleri için özel renk ayarlamak için:

1. [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) nesnesinin [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)ına erişin.
1. [**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) methodını kullanarak istediğiniz rengi atayın.

Bu makale ayrıca nasıl kurulacağını da açıklar:

- Bir grafik kategorisi verisi.
- Bir hücreye bağlı grafik başlığı.
- Grafik başlık font ayarları.
- Açıklamanın konumu.

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) sadece pasta grafikleri için değil, tüm grafik türleri için kullanılabilir.

{{% /alert %}}

**Pasta grafiğinde özel dilim renkleri**

![todo:image_alt_text](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
