---
title: Pasta Grafikte Özel Dilim veya Sektör Renkleri
type: docs
weight: 30
url: /tr/java/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

Bu makalede, pasta grafik dilimlerine/sektörlerine özel renklerin nasıl ekleneceği açıklanmaktadır. Pasta grafikler varsayılan olarak Microsoft Excel varsayılan şablonunu kullanır. Diğer renkleri kullanmak için tablodaki renkleri yeniden tanımlamak mümkündür.

{{% /alert %}}

Bir pasta grafiğin ayrı dilimleri veya sektörleri için özel renk ayarlamak üzere:

1.  Erişmek[**Dizi**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) nesnenin[**Harita Noktası**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1.  kullanarak istediğiniz rengi atayın.[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)yöntem.

Bu makalede ayrıca aşağıdakilerin nasıl ayarlanacağı açıklanmaktadır:

- Bir grafiğin kategori verileri.
- Bir hücreye bağlı grafik başlığı.
- Grafik başlığı yazı tipi ayarları.
- Efsanenin konumu.

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) pasta grafiklere özgü değildir, ancak tüm grafik türleri için kullanılabilir.

{{% /alert %}}

**Pasta grafikte özel dilim renkleri**

![yapılacaklar:resim_alternatif_metin](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
