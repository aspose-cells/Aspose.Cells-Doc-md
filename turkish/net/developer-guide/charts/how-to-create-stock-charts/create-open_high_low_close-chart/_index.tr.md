---
title: Açık-Yüksek-Düşük-Kapanış(OHLC) Hisse Senedi Tablosu Oluştur
description: Aspose.Cells for .NET numaralı telefonu kullanarak açılış-yüksek-düşük-kapanış hisse senedi grafiğini nasıl oluşturacağınızı öğrenin. Kılavuzumuz, daha iyi analiz ve görselleştirme için açılış, yüksek, düşük ve kapanış fiyatları da dahil olmak üzere borsa verilerinin bir grafiğe nasıl çizileceğini gösterecektir.
keywords: Aspose.Cells for .NET, Open-High-Low-Close Stock Chart, Stock Market Data, Analysis, Visualization.
type: docs
weight: 182
url: /tr/net/create-open-high-low-close-stock-chart/
---
##  **Olası Kullanım Senaryoları**
Açık-Yüksek-Düşük-Kapanış (OHLC) grafiği sırayla beş veri sütunu kullanır: kategori, açılış, yüksek, düşük ve kapanış. Her kategorideki fiyat aralığı yine dikey bir çizgiyle gösterilirken, açılış ve kapanış arasındaki aralık daha geniş bir kayan çubukla gösterilir; kategoride fiyat artarsa (kapanış açılıştan yüksekse) çubuk bir renkle doldurulur, fiyat düşerse çubuk başka bir renkle doldurulur. Bu tür grafiklere genellikle mum grafiği denir.

![yapılacak şey:image_alt_text](data.png)

![yapılacak şey:image_alt_text](sample.png)
##  **Grafikteki görünürlük iyileştirmeleri**
Artan ve azalan fiyatları belirtmek için genellikle siyah beyaz yerine renkleri kullanırız. Aşağıdaki ilk mum çubuklarında kırmızı, artan fiyatları, yeşil ise azalan fiyatları gösterir.

![yapılacak şey:image_alt_text](sample2.png)
##  **Basit kod**
 Aşağıdaki örnek kod,[örnek Excel dosyası](Open-High-Low-Close.xlsx) ve üretir[Excel dosyasının çıktısı](out.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-open-high-low-close-stock-chart.cs" >}}
