---
title: Grafik Görünümünü Ayarlama
description: Grafik görünümünü Aspose.Cells for .NET. içinde nasıl yapılandıracağınızı öğrenin. Rehberimiz, istenen görsel stili elde etmek ve çalışma tablolarınızı geliştirmek için grafik düzenleri, renkler, fontlar ve efektleri nasıl değiştireceğinizi gösterecektir.
keywords: Aspose.Cells for .NET, grafik, grafik görünümü, düzenler, renkler, fontlar, efektler, çalışma tabloları.
linktitle: Grafik Formatı
type: docs
weight: 20
url: /tr/net/setting-chart-appearance/
---

## **Grafik Görünümünü Ayarlama**
Bir Grafik Oluşturma Nasıl Konusunda Aspose.Cells tarafından sunulan grafik türleri ve grafik nesnelerinin kısa bir tanıtımını ve bir tanesini nasıl oluşturacağınızı açıklamıştık. Bu makale, özelliklerini ayarlayarak grafiklerin görünümünü özelleştirmenin nasıl yapılacağını tartışıyor:

- Grafik alanını ayarlama.
- Grafik çizgilerini ayarlama.
- Temalar uygulama.
- Grafiklere ve eksenlere başlıklar eklemek.
- Izgaralarla çalışma.
### **Grafik Alanını Ayarlama**
Bir grafikte farklı türde alanlar bulunmakta ve Aspose.Cells her bir alanın görünümünü değiştirme esnekliği sağlar. Geliştiriciler, bir alan üzerinde farklı biçimlendirme ayarları uygulayarak ön plan rengi, arka plan rengi ve doldurma biçimi gibi farklı biçimlendirme ayarlarını uygulayabilir.

Aşağıdaki örnekte, bir grafikte farklı türde alanlara farklı biçimlendirme ayarları uyguladık. Bu alanlar şunları içerir:

- Plot alanı
- Grafik alanı
- Seri koleksiyonu alanı
- Bir Seri Koleksiyonu içindeki tek bir noktanın alanı

Aşağıdaki kod parçası, grafik alanını nasıl ayarlayacağınızı göstermektedir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **Grafik Çizgilerini Ayarlama**
Geliştiriciler ayrıca [SeriKoleksiyonu](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)'ndaki çizgilerin veya veri işaretçilerinin farklı türlerini de uygulayabilir. Aşağıdaki kod parçası, Aspose.Cells API'sını kullanarak grafik çizgilerini nasıl ayarlayacağınızı göstermektedir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **Microsoft Excel 2007/2010 Temalarını Grafiklere Uygulama**
Geliştiriciler, [SeriKoleksiyonu](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) veya diğer grafik nesnelerine farklı Microsoft Excel temaları/renkleri uygulayabilir, aşağıdaki örnekte gösterildiği gibi.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **Grafiğin veya Eksenlerin Başlıklarını Ayarlama**
Microsoft Excel'ı kullanarak Bir bakma yerim var ve eksenlerin başlıklarını NIsabetsiz Bir Ortamda AYARLAYABİLİRSİNİZ. Aspose.Cells ayrıca geliştiricilere grafiğin ve eksenlerinin başlıklarını çalışma zamanında ayarlamaları için olanak sağlar. Tüm grafikler ve eksenleri, aşağıdaki örnekte gösterildiği gibi başlıklarını ayarlamak için kullanılabilecek bir [Title](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title) özelliğine sahiptir.

Aşağıdaki kod parçacığı, grafikler ve eksenlerin başlıklarını nasıl ayarlayacağını göstermektedir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **Büyük Izgaralarla Çalışma**
Büyük ızgaraların görünümünü özelleştirmek mümkündür. Izgaraları gizlemek veya göstermek, renk ve diğer ayarları tanımlamak vb. aşağıda, ızgaraların nasıl gizleneceğini ve renginin nasıl değiştirileceğini gösteriyoruz.
#### **Büyük Izgaraları Gizleme**
Geliştiriciler, büyük ızgaraların görünürlüğünü [IsVisible](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) özelliğini **true** veya **false** olarak ayarlayarak kontrol edebilirler.

Aşağıdaki kod parçası, büyük ızgaraları nasıl gizleyeceğinizi göstermektedir. Büyük ızgaraları gizledikten sonra, bir sütun grafiği çalışma sayfasına eklenecek ve ızgaraları olmayacaktır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **Büyük Izgaraların Ayarlarını Değiştirme**
Geliştiriciler, yalnızca büyük ızgaraların görünürlüğünü değil, aynı zamanda rengi gibi diğer özelliklerini de kontrol edebilirler.

Aşağıdaki kod parçası, büyük ızgaraların rengini nasıl değiştireceğinizi göstermektedir. Büyük ızgaraların rengini ayarladıktan sonra, bir sütun grafiği çalışma sayfasına değiştirilmiş ızgaralarla eklenecektir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **Gelişmiş Konular**
- [Grafik Serisinin Değer Biçim Kodunu Ayarlayın](/cells/tr/net/set-the-values-format-code-of-chart-series/)
- [Grafikte Arka Plan Doldurma Olarak Resim Ayarlama](/cells/tr/net/set-picture-as-background-fill-in-the-chart/)
