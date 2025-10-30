---
title: Dinamik Kaydırmalı Grafik Nasıl Oluşturulur Golang ile C++ aracılığıyla
linktitle: Dinamik Dolan Grafiği Nasıl Oluşturulur
description: Aspose.Cells for C++ kullanarak dinamik dönen grafik oluşturmayı öğrenin. Kılavuzumuz, grafiklerinizde düzgün veri geçişleri ve dönen ortalamaları uygulamanıza nasıl yardımcı olacağını gösterecek.
keywords: Aspose.Cells for C++, Dinamik Dönen Grafik, Veri Geçişleri, Pürüzsüz Ortalamalar, Sürekli Gösterim, Güncellenen Görselleştirme.
type: docs
weight: 74
url: /tr/go-cpp/create-dynamic-rolling-chart/
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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Rolling.go" >}}
## **Notlar**
Oluşturulan dosyada, A ve B sütunlarına sürekli veri eklemeye devam edebilirken grafik sürekli olarak en son 5 veri setini sayacaktır. Bu, örneğin kodundaki 'OFFSET' formülü kullanılarak gerçekleşir:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Rolling-1.go" >}}
Formüldeki "-5" değerini "-10" olarak değiştirmeyi deneyin ve dinamik grafik en son 10 veri setini sayacaktır. Aspose.Cells'i kullanarak başarılı bir şekilde dinamik dolan bir grafik oluşturduk.
