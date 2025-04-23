---
title: C++ kullanarak Node.js ile Borsa Grafikleri nasıl oluşturulur
linktitle: Hisse Senedi Grafikleri Nasıl Oluşturulur
description: Aspose.Cells API lerini kullanarak HLC, OHLC, VHLC ve VOHLC dahil olmak üzere farklı türlerde borsa grafiklerinin nasıl oluşturulacağını öğrenin. 
keywords: Node.js ile C++ kullanarak Borsa Grafikleri oluşturma, Market Veri Görselleştirme, Borsa Analizi, Adım Adım Kılavuz.
type: docs
weight: 71
url: /tr/nodejs-cpp/how-to-create-stock-charts/
---

{{% alert color="primary" %}}

Bu paragraf, HLC (Yüksek-Düşük-Kapanış), OHLC (Açık-Yüksek-Düşük-Kapanış), VHLC (Hacim-Yüksek-Düşük-Kapanış) ve VOHLC (Hacim-Açık-Yüksek-Düşük-Kapanış) olmak üzere dört türde hisse senedi grafiği nasıl oluşturacağınızı anlatacak.
- **HLC** – Yüksek-Düşük-Kapanış.
- **OHLC** – Açık-Yüksek-Düşük-Kapanış.
- **VHLC** – Hacim-Yüksek-Düşük-Kapanış.
- **VOHLC** – Hacim-Açık-Yüksek-Düşük-Kapanış.

{{% /alert %}}

## **Hisse senedi grafiği nedir?**

Borsa grafikleri, emtia, hisse senedi ve kripto para gibi işlem gören varlıkların fiyat değişikliklerini takip etmek için kullanılan özel grafiklerdir. Bu grafikler, zaman içindeki en yüksek ve en düşük değerleri, açılış ve kapanış değerleriyle birlikte göstermenize olanak sağlar. Aspose.Cells for Node.js via C++, dört farklı borsa grafiği sunar ve bunları kullanmak için doğru veri setlerine sahip olmanız ve kolonları doğru sırayla seçmeniz gerekir.

Aşağıdaki veri seti, bir hisse senedine ait günlük işlem bilgilerini gösterir. Bu verileri kullanarak dört tür stok grafiği oluşturacağız: Yüksek-Düşük-Kapanış (HLC), Açık-Yüksek-Düşük-Kapanış (OHLC), Hacim-Yüksek-Düşük-Kapanış (VHLC) ve Hacim-Açık-Yüksek-Düşük-Kapanış (VOHLC).

![todo:image_alt_text](stock.chart.data.png)
