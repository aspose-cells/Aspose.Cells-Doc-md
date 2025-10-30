---
title: Pie Grafiğinde Özel Dilim veya Sektör Renkleri Golang ile C++ kullanarak
linktitle: Pasta Grafiğinde Özel Dilim veya Sektör Renkleri
description: Pasta grafikte dilim ve sektör renklerini özelleştirmek için Aspose.Cells for C++ nasıl kullanılır öğrenin. Rehberimiz, her dilim, sektör veya lejyon için benzersiz renkler atamanızı gösterecek, görsel çekiciliği ve veri sunumunu geliştirecektir.
keywords: Aspose.Cells for C++, Pasta Grafiği, Özelleştirilmiş Dilim Renkleri, Özelleştirilmiş Sektör Renkleri, Görsel Çekicilik, Veri Sunumu.
type: docs
weight: 60
url: /tr/go-cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

Bu makale, pasta grafiğine özel renkler eklemenin nasıl olduğunu açıklar. Varsayılan olarak, pasta grafikleri Microsoft Excel'in varsayılan şablonunu kullanır. Diğer renkleri kullanmak için, grafikte renkleri yeniden tanımlayın.

{{% /alert %}}

Pasta grafiğinin bireysel dilimleri veya sektörleri için özel bir renk ayarlamak için:

1. [**Series**](https://reference.aspose.com/cells/go-cpp/series/) nesnesinin [**ChartPoint**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/)ına erişin.
Renk seçeneğiniz [**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/go-cpp/area/getforegroundcolor/) özelliğini kullanarak atayın.

Bu makale ayrıca şunları açıklar:

- Bir grafik kategorisi verisi.
- Bir hücreye bağlı grafik başlığı.
- Grafik başlık font ayarları.
- Açıklamanın konumu.

{{% alert color="primary" %}}

[**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/go-cpp/area/getforegroundcolor/) sadece pasta grafikleri için özgü değil, tüm grafik türleri için kullanılabilir.

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomSliceOrSectorColorsInPieChart.go" >}}
