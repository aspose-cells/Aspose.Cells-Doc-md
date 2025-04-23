---
title: Hisse Senedi Grafikleri Nasıl Oluşturulur
type: docs
weight: 71
url: /tr/java/how-to-create-stock-charts/
description: Bir hisse senedi grafiği nasıl oluşturulur, nasıl bir hisse senedi grafiği eklenir, hisse senedi grafiği nasıl oluşturulur.
keywords: Hisse senedi grafiği ekle, hisse senedi grafiği oluştur, hisse senedi grafiği oluştur.
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

Aşağıdaki veri seti, bir hisse senedi için günlük işlem bilgilerini göstermektedir. Bu verileri kullanarak Aspose.Cells'te bulunan 4 hisse senedi grafiği her birini oluşturacağız. 

![todo:image_alt_text](stock.chart.data.png)
{{< app/cells/assistant language="java" >}}
