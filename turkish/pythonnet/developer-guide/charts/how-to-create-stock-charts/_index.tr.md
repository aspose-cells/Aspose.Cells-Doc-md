---
title: Hisse Senedi Grafikleri Nasıl Oluşturulur
description: Hisse grafikleri, işlem gören varlıkların fiyat değişikliklerini takip etmek için kullanılan belirli bir grafik türüdür. Bu bölümde, Aspose.Cells for Python via .NET API leri kullanarak farklı türde hisse grafiklerinin nasıl kolayca oluşturulacağını göstereceğiz. Özellikle, aşağıdaki hisse grafik türlerini ele alacağız Yüksek Düşük Kapanış (HLC) hisse grafiği,Açık Yüksek Düşük Kapanış (OHLC) grafiği,Hacim Yüksek Düşük Kapanış (VHLC) hisse grafiği ve Hacim Açık Yüksek Düşük Kapanış (VOHLC) hisse grafiği. 
keywords: Hisse Grafikleri Oluşturma, Aspose.Cells for Python via .NET, Piyasa Verisi Görselleştirme, Borsa Analizi, Adım Adım Kılavuz.
type: docs
weight: 71
url: /tr/python-net/how-to-create-stock-charts/
---

{{% alert color="primary" %}}

Bu paragraf, HLC (Yüksek-Düşük-Kapanış), OHLC (Açık-Yüksek-Düşük-Kapanış), VHLC (Hacim-Yüksek-Düşük-Kapanış) ve VOHLC (Hacim-Açık-Yüksek-Düşük-Kapanış) olmak üzere dört türde hisse senedi grafiği nasıl oluşturacağınızı anlatacak.
- **HLC** – Yüksek-Düşük-Kapanış.
- **OHLC** – Açık-Yüksek-Düşük-Kapanış.
- **VHLC** – Hacim-Yüksek-Düşük-Kapanış.
- **VOHLC** – Hacim-Açık-Yüksek-Düşük-Kapanış.

{{% /alert %}}

## **Hisse senedi grafiği nedir?**

Hisse grafikleri, işlem gören varlıkların fiyat değişikliklerini takip etmek için kullanılan belirli bir grafiktir.  Varlıklar örneğin, emtialar, hisseler ve kripto paralar olabilir.  Bu grafikler, zaman içindeki yüksek ve düşük değerleri, aynı zamanda açılış ve kapanış değerlerini tek bir grafikte görmenizi sağlar.  Aspose.Cells for Python via .NET, 4 farklı hisse grafikleri sunar ve bunları kullanmak için doğru veri setlerine sahip olmalı ve doğru sıralamayla sütunları seçmelisiniz.

Aşağıdaki veri seti, bir hisse senedi için günlük ticaret bilgilerini gösterir. Bu veriyi kullanarak Yüksek-Düşük-Kapanış (HLC) hisse senedi grafiği, Açık-Yüksek-Düşük-Kapanış (OHLC) grafiği, Hacim-Yüksek-Düşük-Kapanış (VHLC) hisse senedi grafiği ve Hacim-Açık-Yüksek-Düşük-Kapanış (VOHLC) hisse senedi grafiği oluşturacağız. 

![todo:image_alt_text](stock.chart.data.png)
