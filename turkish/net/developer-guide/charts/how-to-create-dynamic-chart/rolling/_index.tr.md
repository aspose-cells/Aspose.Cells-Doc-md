---
title: Dinamik Dönen Grafik nasıl oluşturulur?
description: Aspose.Cells for .NET'i kullanarak dinamik hareketli grafiğin nasıl oluşturulacağını öğrenin. Kılavuzumuz, sürekli ve güncel bir görüntü için grafiğinizde düzgün veri geçişlerini ve hareketli ortalamaları nasıl uygulayacağınızı gösterecektir.
keywords: Aspose.Cells for .NET, Dynamic Rolling Chart, Data Transitions, Smooth Averages, Continuous Display, Updating Visualization.
type: docs
weight: 74
url: /tr/net/create-dynamic-rolling-chart/
---
##  **Olası Kullanım Senaryoları**
Dinamik yuvarlanan grafik, zaman içinde sürekli değişen ve güncellenen veri noktalarını görüntüleyen grafiksel bir temsili ifade eder. Kendini sürekli güncelleyen, en yeni veri noktalarının değişen bir penceresini sergileyen ve yenileri geldikçe eski veri noktalarını atan bir grafik türüdür.

Dinamik yuvarlanan grafikler, gerçek zamanlı veya akış verilerindeki eğilimleri ve modelleri görselleştirmek için yaygın olarak kullanılır. Borsa analizi, hava durumu izleme veya canlı performans takibi gibi zamansal hususların ve zaman içindeki değişikliklerin kritik olduğu senaryolarda özellikle faydalıdırlar.

Bu grafiklerde, her zaman en güncel bilgilerin sunulmasını sağlamak için genellikle animasyon veya otomatik kaydırma mekanizmaları kullanılır. Kayan pencerenin uzunluğu, son saat, gün veya hafta gibi belirli bir zaman dilimini gösterecek şekilde özelleştirilebilir.

Özetle, dinamik bir hareketli grafik, eski veri noktalarını atarken en yeni veri noktalarını görüntüleyen ve kullanıcıların gerçek zamanlı eğilimleri ve modelleri gözlemlemesine olanak tanıyan, sürekli güncellenen bir grafik temsilidir.

##  **Dinamik Dönen Grafik oluşturmak için Aspose Cells'i kullanın**
Sonraki paragraflarda Aspose.Cells kullanarak Dinamik Dönen Grafiğin nasıl oluşturulacağını göstereceğiz. Size örneğin kodunu ve bu kodla oluşturulan Excel dosyasını göstereceğiz.

##  **Basit kod**
 Aşağıdaki örnek kod,[Dinamik Dönen Grafik Dosyası](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-rolling-chart.cs" >}}

##  **Notlar**
Oluşturulan dosyada, grafik en son 5 veri kümesini dinamik olarak sayarken, A ve B sütunlarına veri eklemeye devam edebilirsiniz. Bu, örnek koddaki "OFFSET" formülü kullanılarak yapılır:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Formüldeki "-5" sayısını "-10" olarak değiştirmeyi deneyebilirsiniz; dinamik grafik en son 10 veri kümesini sayar. Artık Aspose.Cells'i başarıyla kullanarak dinamik bir hareketli grafik oluşturduk.
