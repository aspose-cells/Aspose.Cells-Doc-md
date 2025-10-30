---
title: Golang ve C++ kullanarak Grafik Görünümünü Ayarlama
linktitle: Grafik Formatı
description: Aspose.Cells for C++ te grafiklerin görünümünü nasıl yapılandıracağınızı öğrenin. Rehberimiz, grafik düzenlerini, renkleri, yazı tiplerini ve efektleri değiştirme yollarını gösterecek ve arzu edilen görsel tarzı elde etmenize ve çalışma sayfalarınızı geliştirmeye yardımcı olacak.
keywords: Aspose.Cells for C++, grafik oluşturma, grafik görünümü, düzenler, renkler, yazı tipleri, efektler, çalışma sayfaları.
type: docs
weight: 20
url: /tr/go-cpp/setting-chart-appearance/
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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat.go" >}}
### **Grafik Çizgilerini Ayarlama**
Geliştiriciler ayrıca [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/) çizgileri veya veri işaretçileri üzerinde farklı türlerde stiller uygulayabilir. Aşağıdaki kod parçası Aspose.Cells API kullanarak grafik çizgilerini nasıl ayarlayacağınızı gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-1.go" >}}
### **Microsoft Excel 2007/2010 Temalarını Grafiklere Uygulama**
Geliştiriciler ayrıca aşağıdaki örnekte gösterildiği gibi [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/) veya diğer grafik nesnelerine farklı Microsoft Excel temaları/renkleri uygulayabilir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-2.go" >}}
### **Grafiğin veya Eksenlerin Başlıklarını Ayarlama**
Microsoft Excel kullanarak bir grafiğin ve eksenlerinin başlıklarını WYSIWYG ortamında ayarlayabilirsiniz. Aspose.Cells ayrıca geliştirilicilere grafik ve eksenlerin başlıklarını çalışma zamanında ayarlama olanağı sağlar. Tüm grafikler ve eksenleri bir [Title](https://reference.aspose.com/cells/go-cpp/title/) özelliği içerir ve bu özellik kullanılarak başlıklar ayarlanabilir. Aşağıda bir örnek gösterilmektedir.

Aşağıdaki kod parçacığı, grafikler ve eksenlerin başlıklarını nasıl ayarlayacağını göstermektedir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-3.go" >}}
### **Büyük Izgaralarla Çalışma**
Büyük ızgaraların görünümünü özelleştirmek mümkündür. Izgaraları gizlemek veya göstermek, renk ve diğer ayarları tanımlamak vb. aşağıda, ızgaraların nasıl gizleneceğini ve renginin nasıl değiştirileceğini gösteriyoruz.

#### **Büyük Izgaraları Gizleme**
Geliştiriciler, ana ızgara çizgilerinin görünürlüğünü [Line](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/) nesnesinin [IsVisible](https://reference.aspose.com/cells/go-cpp/line/isvisible/) özelliğini **true** veya **false** olarak ayarlayarak kontrol edebilirler.

Aşağıdaki kod parçası, büyük ızgaraları nasıl gizleyeceğinizi göstermektedir. Büyük ızgaraları gizledikten sonra, bir sütun grafiği çalışma sayfasına eklenecek ve ızgaraları olmayacaktır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-4.go" >}}
#### **Büyük Izgaraların Ayarlarını Değiştirme**
Geliştiriciler, yalnızca büyük ızgaraların görünürlüğünü değil, aynı zamanda rengi gibi diğer özelliklerini de kontrol edebilirler.

Aşağıdaki kod parçası, büyük ızgaraların rengini nasıl değiştireceğinizi göstermektedir. Büyük ızgaraların rengini ayarladıktan sonra, bir sütun grafiği çalışma sayfasına değiştirilmiş ızgaralarla eklenecektir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-5.go" >}}
## **Gelişmiş Konular**
- [Grafik Serisinin Değer Biçim Kodunu Ayarlayın](/cells/tr/cpp/set-the-values-format-code-of-chart-series/)
- [Grafikte Arka Plan Doldurma Olarak Resim Ayarlama](/cells/tr/cpp/set-picture-as-background-fill-in-the-chart/)
