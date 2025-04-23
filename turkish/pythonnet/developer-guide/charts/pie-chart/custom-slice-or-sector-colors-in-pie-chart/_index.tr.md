---
title: Pasta Grafiğinde Özel Dilim veya Sektör Renkleri
description: Aspose.Cells for Python via .NET kullanarak, pasta grafiklerinde dilim ve sektör renkleri nasıl özelleştirilir gösteririz. Her dilim, sektör veya bölgeye benzersiz renkler atayarak görsel cazibe ve veri temsili iyileştirilir.
keywords: Aspose.Cells for Python via .NET, Pasta Grafiği, Özel Dilim ve Sektör Renkleri, Görsel Çekicilik, Veri Temsili.
type: docs
weight: 60
url: /tr/python-net/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

Bu makale, pasta grafiğine özel renkler eklemenin nasıl olduğunu açıklar. Varsayılan olarak, pasta grafikleri Microsoft Excel'in varsayılan şablonunu kullanır. Diğer renkleri kullanmak için, grafikte renkleri yeniden tanımlayın.

{{% /alert %}}

Pasta grafiğinin bireysel dilimleri veya sektörleri için özel bir renk ayarlamak için:

1. [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) nesnesinin [**ChartPoint**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint)ına erişin.
Renk seçeneğiniz [**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color) özelliğini kullanarak atayın.

Bu makale ayrıca şunları açıklar:

- Bir grafik kategorisi verisi.
- Bir hücreye bağlı grafik başlığı.
- Grafik başlık font ayarları.
- Açıklamanın konumu.

{{% alert color="primary" %}}

[**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color) sadece pasta grafikleri için özgü değil, tüm grafik türleri için kullanılabilir.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CustomSliceSectorColorsPieChart-1.py" >}}
