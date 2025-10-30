---
title: Açık Yüksek Düşük Kapalı (OHLC) Hisse Senedi Grafiği Oluştur
description: Aspose.Cells for Python via .NET kullanarak açık yüksek düşük kapanış hisse senedi grafiği nasıl oluşturulur öğrenin. Kılavuzumuz, hisse senedi verilerini, açık, yüksek, düşük ve kapanış fiyatlarını grafik üzerine yerleştirme adımlarını gösterir.
keywords: Aspose.Cells for Python via .NET, Açık Yüksek Düşük Kapanış Hisse Senedi Grafiği, Hisse Senedi Verileri, Analiz, Görselleştirme.
type: docs
weight: 182
url: /tr/python-net/create-open-high-low-close-stock-chart/
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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-open-high-low-close-stock-chart.py" >}}
{{< app/cells/assistant language="python-net" >}}
