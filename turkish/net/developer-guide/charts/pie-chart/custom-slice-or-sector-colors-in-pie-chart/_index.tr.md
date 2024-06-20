---
title: Pasta Grafiğinde Özel Dilim veya Sektör Renkleri
description: Aspose.Cells for .NET kullanarak pasta grafiğinde dilim ve sektör renklerini özelleştirme öğrenin. Kılavuzumuz, her dilim, sektör veya lejyon için benzersiz renkler atamak için pasta grafiğine nasıl daha iyi görsel çekicilik ve veri temsili sağlayacağını gösterecektir.
keywords: Aspose.Cells for .NET, Pasta Grafiği, Özel Dilim Renkleri, Özel Sektör Renkleri, Görsel Çekicilik, Veri Temsili.
type: docs
weight: 60
url: /tr/net/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

Bu makale, pasta grafiğine özel renkler eklemenin nasıl olduğunu açıklar. Varsayılan olarak, pasta grafikleri Microsoft Excel'in varsayılan şablonunu kullanır. Diğer renkleri kullanmak için, grafikte renkleri yeniden tanımlayın.

{{% /alert %}}

Pasta grafiğinin bireysel dilimleri veya sektörleri için özel bir renk ayarlamak için:

1. [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) nesnesinin [**ChartPoint**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint)ına erişin.
Renk seçeneğiniz [**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor) özelliğini kullanarak atayın.

Bu makale ayrıca şunları açıklar:

- Bir grafik kategorisi verisi.
- Bir hücreye bağlı grafik başlığı.
- Grafik başlık font ayarları.
- Açıklamanın konumu.

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor) sadece pasta grafikleri için özgü değil, tüm grafik türleri için kullanılabilir.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
