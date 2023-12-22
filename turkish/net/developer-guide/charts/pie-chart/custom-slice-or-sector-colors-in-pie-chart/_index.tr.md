---
title: Pasta Grafiğinde Özel Dilim veya Sektör Renkleri
description: Pasta grafiğindeki dilim ve sektör renklerini özelleştirmek için Aspose.Cells for .NET'i nasıl kullanacağınızı öğrenin. Kılavuzumuz, gelişmiş görsel çekicilik ve veri temsili için her dilime, sektöre veya lejyona benzersiz renklerin nasıl atanacağını gösterecektir.
keywords: Aspose.Cells for .NET, Pie Chart, Custom Slice Colors, Custom Sector Colors, Visual Appeal, Data Representation.
type: docs
weight: 60
url: /tr/net/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

Bu makalede, pasta grafik dilimlerine/sektörlerine özel renklerin nasıl ekleneceği açıklanmaktadır. Pasta grafikleri varsayılan olarak Microsoft Excel varsayılan şablonunu kullanır. Diğer renkleri kullanmak için grafikteki renkleri yeniden tanımlayın.

{{% /alert %}}

Pasta grafiğinin ayrı dilimleri veya sektörleri için özel bir renk ayarlamak üzere:

1.  Erişmek[**Seri**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) nesnenin[**Harita Noktası**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint).
1. kullanarak istediğiniz rengi atayın.[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)mülk.

Bu makalede ayrıca aşağıdakilerin nasıl yapılacağı açıklanmaktadır:

- Bir grafiğin kategori verileri.
- Bir hücreye bağlı grafik başlığı.
- Grafik başlığı yazı tipi ayarları.
- Efsanenin konumu.

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor) pasta grafiklere özel değildir ancak tüm grafik türleri için kullanılabilir.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
