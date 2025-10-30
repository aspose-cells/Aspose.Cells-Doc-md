---
title: Dinamik Kaydırmalı Grafik Nasıl Oluşturulur
description: Aspose.Cells for Python via .NET kullanarak dinamik kaydırmalı grafik nasıl oluşturulur öğrenin. Adım adım kılavuzumuz, grafiklerinizde düzgün veri geçişleri ve otomatik kaydırma sağlayarak sürekli ve güncellenen görünüm sağlamanıza yardımcı olacak.
keywords: Aspose.Cells for Python via .NET, Dinamik Kaydırmalı Grafik, Veri Geçişleri, Düzgün Kaydırma, Sürekli Gösterim, Güncellenen Görselleştirme.
type: docs
weight: 75
url: /tr/python-net/create-dynamic-scrolling-chart/
---

## **Olası Kullanım Senaryoları**
Dinamik kaydırma grafiği, zamanla değişen verileri göstermek için kullanılan bir grafiksel temsil türüdür. Gerçek zamanlı veri görünümü sağlamak üzere tasarlanmıştır ve kullanıcılara sürekli güncellemeleri ve trendleri takip etme imkanı tanır. Grafik, yeni veri ekledikçe sürekli güncellenir ve en güncel bilgileri göstermek üzere otomatik olarak kaydırılır.

Dinamik kaydırma grafikleri genellikle finans, hisse senedi piyasası analizi, hava durumu takibi ve sosyal medya analitiği gibi çeşitli endüstrilerde kullanılır. Kullanıcıların veri desenlerini görselleştirmelerine ve analiz etmelerine olanak tanır ve gerçek zamanlı bilgilere dayalı bilinçli kararlar almalarını sağlar.

Bu grafikler genellikle etkileşimli olarak tasarlanır, kullanıcının yakınlaştırma yapmasına, tarihli veriler arasında kaydırmasına ve zaman aralıklarını ayarlamasına olanak tanır. Genellikle birden fazla veri serisini destekler, farklı metriklerin ve ilişkilerinin kapsamlı bir görünümünü sunar.

Genel olarak, dinamik kaydırma grafikleri, zaman serisi verilerinin izlenmesi ve analiz edilmesi için değerli araçlardır, gerçek zamanlı karar alma ve veri görselleştirme kapasitelerini geliştirmeye yardımcı olurlar.

## **Aspose.Cells for Python via .NET kullanarak Dinamik Kaydırmalı Grafik oluştur**
Aşağıdaki paragrafarda, Aspose.Cells for Python via .NET kullanarak Dinamik Kaydırmalı Grafik nasıl oluşturulur göstereceğiz. Örneğin kodunu ve bu kodla oluşturulan Excel dosyasını da göstereceğiz.

## **Örnek Kod**
Aşağıdaki örnek kod, [Dinamik Kaydırma Grafik Dosyasını](DynamicScrollingChart.xlsx) oluşturacaktır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-dynamic-scrolling-chart.py" >}}

## **Notlar**
Oluşturulan dosyada, kaydırma çubuğunu kullanabilir ve grafik dinamik olarak en son 10 veri kümesini sayar. Bu, örnek kod içinde "OFFSET" formülü kullanılarak yapılır:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

"Sheet1!$H$20" hücresinde "10" sayısını "15" olarak değiştirmeyi deneyebilirsiniz ve dinamik grafik en son 15 veri setini sayacaktır. Şimdi Aspose.Cells for Python via .NET kullanarak başarıyla bir dinamik kaydırmalı grafik oluşturduk.
{{< app/cells/assistant language="python-net" >}}
