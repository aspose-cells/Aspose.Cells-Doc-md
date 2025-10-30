---
title: C++ ile Stok Grafikler Nasıl Oluşturulur
linktitle: Hisse Senedi Grafikleri Nasıl Oluşturulur
description: Stok grafikler, işlem gören varlıkların fiyat değişikliklerini izlemek için kullanılan özel türde grafiklerdir.
keywords: Hisse Senedi Grafikleri, Aspose.Cells, Piyasa Verisi Görselleştirme, Hisse Senedi Analizi, Adım Adım Kılavuz.
type: docs
weight: 71
url: /tr/cpp/how-to-create-stock-charts/
---

{{% alert color="primary" %}}

Bu paragraf, HLC (Yüksek-Düşük-Kapanış), OHLC (Açık-Yüksek-Düşük-Kapanış), VHLC (Hacim-Yüksek-Düşük-Kapanış) ve VOHLC (Hacim-Açık-Yüksek-Düşük-Kapanış) olmak üzere dört türde hisse senedi grafiği nasıl oluşturacağınızı anlatacak.
- **HLC** – Yüksek-Düşük-Kapanış.
- **OHLC** – Açık-Yüksek-Düşük-Kapanış.
- **VHLC** – Hacim-Yüksek-Düşük-Kapanış.
- **VOHLC** – Hacim-Açık-Yüksek-Düşük-Kapanış.

{{% /alert %}}

## **Stok Grafiği Nedir?**

Stok grafikler, yatırım araçlarının fiyatlarındaki değişiklikleri takip etmek için kullanılan belirli grafik türleridir. Emtia, hisse senetleri ve kripto para birimleri gibi varlıklar. Bu grafikler, zaman içindeki yüksek ve düşük değerleri ile açılış ve kapanış değerlerini aynı grafikte görebilmenizi sağlar. Aspose.Cells, 4 stok grafiği sunar ve bunları kullanmak için doğru veri setlerine sahip olmalı ve sütunları doğru sırayla seçmelisiniz.

Aşağıdaki veri seti, bir hisse senedine ait günlük işlem bilgilerini gösterir. Bu verileri kullanarak dört tür stok grafiği oluşturacağız: Yüksek-Düşük-Kapanış (HLC), Açık-Yüksek-Düşük-Kapanış (OHLC), Hacim-Yüksek-Düşük-Kapanış (VHLC) ve Hacim-Açık-Yüksek-Düşük-Kapanış (VOHLC).

![todo:image_alt_text](stock.chart.data.png)
{{< app/cells/assistant language="cpp" >}}
