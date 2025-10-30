---
title: Dinamik Dolan Grafiği Nasıl Oluşturulur
description: Aspose.Cells for Python via .NET kullanarak dinamik kaydırmalı grafik nasıl oluşturulur öğrenin. Kılavuzumuz, grafiklerinizde düzgün veri geçişleri ve kayan ortalamalar uygulayarak sürekli ve güncellenen bir görüntü sağlar.
keywords: Aspose.Cells for Python via .NET, Dinamik Kaydırmalı Grafik, Veri Geçişleri, Düzgün Ortalamalar, Sürekli Gösterim, Güncellenen Görselleştirme.
type: docs
weight: 74
url: /tr/python-net/create-dynamic-rolling-chart/
---

## **Olası Kullanım Senaryoları**
Dinamik dolan grafiği, sürekli olarak kayan ve güncellenen veri noktalarını gösteren görsel bir temsilidir. Bu tür bir grafik, sürekli olarak kendini güncelleyen, en yeni veri noktalarının yanı sıra eski veri noktalarını yeni veriler geldikçe atarak bir ilerleme penceresi gösteren bir türdür.

Dinamik dolan grafikler, gerçek zamanlı veya akış verilerindeki trendleri ve desenleri görselleştirmek için yaygın olarak kullanılır. Özellikle zamanla değişen zamanla ilgili unsurların kritik olduğu senaryolarda, örneğin hisse senedi piyasası analizi, hava durumu izleme veya canlı performans takip etme gibi senaryolarda oldukça kullanışlıdır.

Bu grafikler genellikle en güncel bilgilerin her zaman sunulmasını sağlamak için animasyon veya otomatik kaydırma mekanizmalarından yararlanırlar. Kayan pencerenin uzunluğu, son bir saat, gün veya hafta gibi belirli bir zaman dilimini göstermek üzere özelleştirilebilir.

Özetle, dinamik dolan grafiği, en son veri noktalarını sürekli olarak güncelleyen ve eski verileri atarak kullanıcılara gerçek zamanlı trendleri ve desenleri gözlemleme imkanı tanıyan bir şekilde devamlı güncellenen bir görsel temsilidir.

## **Aspose.Cells for Python via .NET kullanarak Dinamik Kaydırmalı Grafik oluştur**
Aşağıdaki paragrafarda, Aspose.Cells for Python via .NET kullanarak Dinamik Kaydırmalı Grafik nasıl oluşturulur göstereceğiz. Örneğin kodunu ve bu kodla oluşturulan Excel dosyasını da göstereceğiz.

## **Örnek Kod**
Aşağıdaki örnek kod, [Dinamik Dolan Grafiği Dosyasını](DynamicRollingChart.xlsx) oluşturacaktır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-dynamic-rolling-chart.py" >}}

## **Notlar**
Oluşturulan dosyada, A ve B sütunlarına sürekli veri eklemeye devam edebilirken grafik sürekli olarak en son 5 veri setini sayacaktır. Bu, örneğin kodundaki 'OFFSET' formülü kullanılarak gerçekleşir:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Formülde "-5" sayısını "-10" olarak değiştirmeyi deneyebilirsiniz ve dinamik grafik en son 10 veri setini sayacaktır. Şimdi Aspose.Cells for Python via .NET kullanarak başarıyla bir dinamik kaydırmalı grafik oluşturduk.
{{< app/cells/assistant language="python-net" >}}
