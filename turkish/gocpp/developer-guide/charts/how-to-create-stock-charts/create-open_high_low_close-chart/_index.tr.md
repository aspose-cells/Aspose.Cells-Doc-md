---
title: Açık Yüksek Düşük Kapalı (OHLC) Hisse Senedi Grafiği Oluşturma Golang ile C++ aracılığıyla
description: Aspose.Cells for C++ kullanarak açık yüksek düşük kapanış hisse senedi grafiği nasıl oluşturulur onu gösteriyoruz. Adım adım kılavuzumuz, hisse senedi verilerini, açık, yüksek, düşük ve kapanış fiyatlarını grafiğe yansıtmanıza yardımcı olacak.
keywords: Aspose.Cells for C++, Açık Yüksek Düşük Kapanış Hisse Senedi Grafiği, Hisse Senedi Verileri, Analiz, Görselleştirme.
type: docs
weight: 182
url: /tr/go-cpp/create-open-high-low-close-stock-chart/
---

## **Olası Kullanım Senaryoları**
Açık-Yüksek-Düşük-Kapalı (OHLC) grafiği beş veri sütununu kullanır: kategori, açılış, yüksek, düşük ve kapanış sırasıyla. Her kategori için fiyat aralığı yine dikey bir çizgi ile gösterilirken, açılış ve kapanış arasındaki aralık daha geniş bir kayan çubukla gösterilir; eğer fiyat kategoride artarsa (kapanış, açılıştan yüksekse), çubuk bir renkle doldurulur, fiyat azalırsa başka bir renkle doldurulur. Bu tür bir grafik sıklıkla mum grafik olarak adlandırılır.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Grafikte görünürlük iyileştirmeleri**
Fiyatların artış ve azalışını göstermek için sıkça renkler kullanırız, siyah-beyaz yerine. Aşağıdaki ilk mum çubuğu setinde kırmızı artışları, yeşil azalışları gösterir.

![todo:image_alt_text](sample2.png)

## **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](Open-High-Low-Close.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreateOpenHighLowCloseChart.go" >}}
