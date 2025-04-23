---
title: Açık Yüksek Düşük Kapalı (OHLC) Hisse Senedi Grafiği Oluştur
description: Aspose.Cells for .NET kullanarak açık yüksek düşük kapalı hisse senedi grafiği oluşturmayı öğrenin. Rehberimiz, hisse senedi piyasası verilerini, açık, yüksek, düşük ve kapanış fiyatlarını grafik üzerine plotlamayı, daha iyi analiz ve görselleştirme için nasıl yapılacağını gösterecektir.
keywords: Aspose.Cells for .NET, Açık Yüksek Düşük Kapalı Hisse Senedi Grafiği, Hisse Senedi Piyasa Verileri, Analiz, Görselleştirme.
type: docs
weight: 182
url: /tr/net/create-open-high-low-close-stock-chart/
---

## **Olası Kullanım Senaryoları**
Açık-Yüksek-Düşük-Kapalı (OHLC) grafiği beş veri sütununu kullanır: kategori, açılış, yüksek, düşük ve kapanış sırasıyla. Her kategori için fiyat aralığı yine dikey bir çizgi ile gösterilirken, açılış ve kapanış arasındaki aralık daha geniş bir kayan çubukla gösterilir; eğer fiyat kategoride artarsa (kapanış, açılıştan yüksekse), çubuk bir renkle doldurulur, fiyat azalırsa başka bir renkle doldurulur. Bu tür bir grafik sıklıkla mum grafik olarak adlandırılır.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Grafikte görünürlük iyileştirmeleri**
Sıklıkla artan ve azalan fiyatları göstermek için siyah-beyaz yerine renkler kullanırız. Aşağıdaki mum grafiklerinin ilk setinde, kırmızı artışı, yeşil azalışı gösterir.

![todo:image_alt_text](sample2.png)
## **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](Open-High-Low-Close.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-open-high-low-close-stock-chart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
