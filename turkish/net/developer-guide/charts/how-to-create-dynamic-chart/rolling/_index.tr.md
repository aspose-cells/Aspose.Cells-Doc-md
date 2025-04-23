---
title: Dinamik Dolan Grafiği Nasıl Oluşturulur
description: Aspose.Cells for .NET kullanarak dinamik dolan grafiği nasıl oluşturulacağını öğrenin. Kılavuzumuz, grafikte sürüksek veri geçişlerini ve sürekli güncellenen görüntüyü uygulamanın nasıl gerçekleştirileceğini gösterecektir.
keywords: Aspose.Cells for .NET, Dinamik Dolan Grafiği, Veri Geçişleri, Düz Aritmik Ortalamalar, Sürekli Görüntü, Güncellenen Görselleştirme.
type: docs
weight: 74
url: /tr/net/create-dynamic-rolling-chart/
---

## **Olası Kullanım Senaryoları**
Dinamik dolan grafiği, sürekli olarak kayan ve güncellenen veri noktalarını gösteren görsel bir temsilidir. Bu tür bir grafik, sürekli olarak kendini güncelleyen, en yeni veri noktalarının yanı sıra eski veri noktalarını yeni veriler geldikçe atarak bir ilerleme penceresi gösteren bir türdür.

Dinamik dolan grafikler, gerçek zamanlı veya akış verilerindeki trendleri ve desenleri görselleştirmek için yaygın olarak kullanılır. Özellikle zamanla değişen zamanla ilgili unsurların kritik olduğu senaryolarda, örneğin hisse senedi piyasası analizi, hava durumu izleme veya canlı performans takip etme gibi senaryolarda oldukça kullanışlıdır.

Bu grafikler genellikle en güncel bilgilerin her zaman sunulmasını sağlamak için animasyon veya otomatik kaydırma mekanizmalarından yararlanırlar. Kayan pencerenin uzunluğu, son bir saat, gün veya hafta gibi belirli bir zaman dilimini göstermek üzere özelleştirilebilir.

Özetle, dinamik dolan grafiği, en son veri noktalarını sürekli olarak güncelleyen ve eski verileri atarak kullanıcılara gerçek zamanlı trendleri ve desenleri gözlemleme imkanı tanıyan bir şekilde devamlı güncellenen bir görsel temsilidir.

## **Aspose Cells'i kullanarak Dinamik Dolan Grafiği oluşturmak**
Sonraki paragraflarda, Aspose.Cells'i kullanarak Dinamik Dolan Grafiği nasıl oluşturulacağını göstereceğiz. Size örneğin kodunu ve bu kodla oluşturulan Excel dosyasını göstereceğiz.

## **Örnek Kod**
Aşağıdaki örnek kod, [Dinamik Dolan Grafiği Dosyasını](DynamicRollingChart.xlsx) oluşturacaktır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-rolling-chart.cs" >}}

## **Notlar**
Oluşturulan dosyada, A ve B sütunlarına sürekli veri eklemeye devam edebilirken grafik sürekli olarak en son 5 veri setini sayacaktır. Bu, örneğin kodundaki 'OFFSET' formülü kullanılarak gerçekleşir:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Formüldeki "-5" değerini "-10" olarak değiştirmeyi deneyin ve dinamik grafik en son 10 veri setini sayacaktır. Aspose.Cells'i kullanarak başarılı bir şekilde dinamik dolan bir grafik oluşturduk.
{{< app/cells/assistant language="csharp" >}}
