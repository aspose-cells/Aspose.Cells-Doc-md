---
title: Pasta Grafikte Özel Dilim veya Sektör Renkleri
type: docs
weight: 60
url: /tr/net/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

Bu makalede, pasta grafik dilimlerine/sektörlerine özel renklerin nasıl ekleneceği açıklanmaktadır. Pasta grafikler varsayılan olarak Microsoft Excel varsayılan şablonunu kullanır. Diğer renkleri kullanmak için tablodaki renkleri yeniden tanımlayın.

{{% /alert %}}

Bir pasta grafiğin ayrı dilimleri veya sektörleri için özel bir renk ayarlamak üzere:

1.  Erişmek[**Diziler**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) nesnenin[**Harita Noktası**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint).
1.  kullanarak istediğiniz rengi atayın.[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)Emlak.

Bu makale ayrıca şunların nasıl yapılacağını açıklar:

- Bir grafiğin kategori verileri.
- Bir hücreye bağlı grafik başlığı.
- Grafik başlığı yazı tipi ayarları.
- Efsanenin konumu.

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor) pasta grafiklere özgü değildir, ancak tüm grafik türleri için kullanılabilir.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
