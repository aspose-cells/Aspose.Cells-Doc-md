---
title: Grafik Görünümünü Ayarlama
description: Aspose.Cells for Python via .NET’de grafiklerin görünümünü nasıl yapılandıracağınızı öğrenin. Kılavuzumuz, grafik düzenlerini, renkleri, yazı tiplerini ve efektleri nasıl değiştireceğinizi göstererek istediğiniz görsel stili elde etmenize ve çalışma sayfelerinizi geliştirmeye yardımcı olur.
keywords: Aspose.Cells for Python via .NET, grafikler, grafik görünümü, düzenler, renkler, yazı tipleri, efektler, çalışma sayfaları.
linktitle: Grafik Formatı
type: docs
weight: 20
url: /tr/python-net/setting-chart-appearance/
---

## **Grafik Görünümünü Ayarlama**
Grafik Oluşturma Nasıl Yapılır başlığında, Aspose.Cells for Python via .NET tarafından sunulan grafik türleri ve grafik nesnelerine kısa bir giriş yapmış ve nasıl oluşturulacağını anlatmıştık. Bu makale, grafiklerin görünümünü aşağıdaki gibi özelleştirmeye odaklanmıştır:

- Grafik alanını ayarlama.
- Grafik çizgilerini ayarlama.
- Temalar uygulama.
- Grafiklere ve eksenlere başlıklar eklemek.
- Izgaralarla çalışma.
### **Grafik Alanını Ayarlama**
Bir grafikte farklı alanlar olabilir ve Aspose.Cells for Python via .NET, her alanın görünümünü değiştirme esnekliği sağlar. Geliştiriciler, alanın ön plan rengini, arka plan rengini ve doldurma ayarlarını değiştirerek farklı biçimlendirme uygulayabilirler.

Aşağıdaki örnekte, bir grafikte farklı türde alanlara farklı biçimlendirme ayarları uyguladık. Bu alanlar şunları içerir:

- Plot alanı
- Grafik alanı
- Seri koleksiyonu alanı
- Bir Seri Koleksiyonu içindeki tek bir noktanın alanı

Aşağıdaki kod parçası, grafik alanını nasıl ayarlayacağınızı göstermektedir.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartArea-1.py" >}}

### **Grafik Çizgilerini Ayarlama**
Geliştiriciler ayrıca [SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) üzerindeki çizgi veya veri işaretçilerine farklı stiller uygulayabilirler. Aşağıdaki kod örneği, Aspose.Cells for Python via .NET API kullanarak grafik çizgilerini nasıl ayarlayacağınızı gösterir.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartLines-1.py" >}}

### **Microsoft Excel 2007/2010 Temalarını Grafiklere Uygulama**
Geliştiriciler, aşağıdaki örnekte gösterildiği gibi [SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) veya diğer grafik nesnelerine farklı Microsoft Excel temaları/rengleri uygulayabilirler.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ApplyingThemes-1.py" >}}

### **Grafiğin veya Eksenlerin Başlıklarını Ayarlama**
Microsoft Excel kullanarak bir grafik ve eksenlerin başlıklarını WYSIWYG ortamında ayarlayabilirsiniz. Aspose.Cells for Python via .NET, geliştirilicilere grafik ve eksenlerin başlıklarını çalışma zamanında ayarlama imkanı da sağlar. Tüm grafikler ve eksenleri, aşağıdaki örnekte gösterildiği gibi, [Chart.title](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/title) özelliğine sahiptir.

Aşağıdaki kod parçacığı, grafikler ve eksenlerin başlıklarını nasıl ayarlayacağını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingTitlesAxes-1.py" >}}

### **Büyük Izgaralarla Çalışma**
Büyük ızgaraların görünümünü özelleştirmek mümkündür. Izgaraları gizlemek veya göstermek, renk ve diğer ayarları tanımlamak vb. aşağıda, ızgaraların nasıl gizleneceğini ve renginin nasıl değiştirileceğini gösteriyoruz.

#### **Büyük Izgaraları Gizleme**
Geliştiriciler, [Line](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line) nesnesinin [is_visible](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line/is_visible) özelliğini **true** veya **false** yaparak ana ızgara çizgilerinin görünürlüğünü kontrol edebilirler.

Aşağıdaki kod parçası, büyük ızgaraları nasıl gizleyeceğinizi göstermektedir. Büyük ızgaraları gizledikten sonra, bir sütun grafiği çalışma sayfasına eklenecek ve ızgaraları olmayacaktır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-MajorGridlines-1.py" >}}

#### **Büyük Izgaraların Ayarlarını Değiştirme**
Geliştiriciler, yalnızca büyük ızgaraların görünürlüğünü değil, aynı zamanda rengi gibi diğer özelliklerini de kontrol edebilirler.

Aşağıdaki kod parçası, büyük ızgaraların rengini nasıl değiştireceğinizi göstermektedir. Büyük ızgaraların rengini ayarladıktan sonra, bir sütun grafiği çalışma sayfasına değiştirilmiş ızgaralarla eklenecektir.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ChangingMajorGridlines-1.py" >}}

## **Gelişmiş Konular**
- [Grafik Serisinin Değer Biçim Kodunu Ayarlayın](/cells/tr/python-net/set-the-values-format-code-of-chart-series/)
- [Grafikte Arka Plan Doldurma Olarak Resim Ayarlama](/cells/tr/python-net/set-picture-as-background-fill-in-the-chart/)
{{< app/cells/assistant language="python-net" >}}
