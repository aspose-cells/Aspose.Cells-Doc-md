---
title: Hisse Senedi Grafikleri Nasıl Oluşturulur
description: Hisse senedi grafikleri, ticari varlıkların fiyatındaki değişiklikleri izlemek için kullanılan belirli bir grafik türüdür. Bu bölümde, Aspose.Cells API lerini kullanarak farklı türde hisse senedi grafiklerini nasıl kolayca oluşturacağınızı göstereceğiz. 
keywords: Hisse Senedi Grafikleri, Aspose.Cells, Piyasa Verisi Görselleştirme, Hisse Senedi Analizi, Adım Adım Kılavuz.
type: docs
weight: 71
url: /tr/net/how-to-create-stock-charts/
---

{{% alert color="primary" %}}

Bu paragraf, HLC (Yüksek-Düşük-Kapanış), OHLC (Açık-Yüksek-Düşük-Kapanış), VHLC (Hacim-Yüksek-Düşük-Kapanış) ve VOHLC (Hacim-Açık-Yüksek-Düşük-Kapanış) olmak üzere dört türde hisse senedi grafiği nasıl oluşturacağınızı anlatacak.
- **HLC** – Yüksek-Düşük-Kapanış.
- **OHLC** – Açık-Yüksek-Düşük-Kapanış.
- **VHLC** – Hacim-Yüksek-Düşük-Kapanış.
- **VOHLC** – Hacim-Açık-Yüksek-Düşük-Kapanış.

{{% /alert %}}

## **Hisse senedi grafiği nedir?**

Hisse senedi grafları, ticari varlıkların fiyatındaki değişiklikleri izlemek için kullanılan belirli bir grafiktir. Emtia, hisse senetleri ve kripto paralar gibi varlıkları içerir. Bu grafikler, zaman içinde yüksek ve düşük değerleri, açılış ve kapanış değerlerini aynı grafikte görmemizi sağlar. Aspose.Cells 4 hisse senedi grafiği sunar ve bunları kullanabilmek için uygun veri setlerine sahip olmanız ve sütunları doğru sırada seçmeniz gerekmektedir.

Aşağıdaki veri seti, bir hisse senedi için günlük ticaret bilgilerini gösterir. Bu veriyi kullanarak Yüksek-Düşük-Kapanış (HLC) hisse senedi grafiği, Açık-Yüksek-Düşük-Kapanış (OHLC) grafiği, Hacim-Yüksek-Düşük-Kapanış (VHLC) hisse senedi grafiği ve Hacim-Açık-Yüksek-Düşük-Kapanış (VOHLC) hisse senedi grafiği oluşturacağız. 

![todo:image_alt_text](stock.chart.data.png)
{{< app/cells/assistant language="csharp" >}}
