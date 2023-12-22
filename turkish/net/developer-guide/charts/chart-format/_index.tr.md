---
title: Grafik Görünümünü Ayarlama
description: Aspose.Cells for .NET numaralı telefondan grafiklerin görünümünü nasıl yapılandıracağınızı öğrenin. Kılavuzumuz, istediğiniz görsel stili elde etmek ve çalışma sayfalarınızı geliştirmek için grafik düzenlerini, renklerini, yazı tiplerini ve efektlerini nasıl değiştireceğinizi gösterecektir.
keywords: Aspose.Cells for .NET, charting, chart appearance, layouts, colors, fonts, effects, worksheets.
linktitle: Grafik Formatı
type: docs
weight: 20
url: /tr/net/setting-chart-appearance/
---
##  **Grafik Görünümünü Ayarlama**
Grafik Nasıl Oluşturulur bölümünde, Aspose.Cells tarafından sunulan grafik türlerine ve grafik nesnelerine kısa bir giriş yaptık ve nasıl oluşturulacağını anlattık. Bu makalede, özelliklerini ayarlayarak grafiklerin görünümünün nasıl özelleştirileceği anlatılmaktadır:

- Grafik alanını ayarlama.
- Grafik çizgilerini ayarlama.
- Temaların uygulanması.
- Grafiklere ve eksenlere başlıklar ayarlama.
- Kılavuz çizgileriyle çalışma.
###  **Grafik Alanının Ayarlanması**
Bir grafikte farklı türde alanlar vardır ve Aspose.Cells, her alanın görünümünü değiştirme esnekliği sağlar. Geliştiriciler bir alanın ön plan rengini, arka plan rengini, dolgu formatını vb. değiştirerek o alana farklı formatlama ayarları uygulayabilir.

Aşağıda verilen örnekte, bir grafiğin farklı türdeki alanlarına farklı biçimlendirme ayarları uyguladık. Bu alanlar şunları içerir:

- Arsa alanı
- Grafik alanı
- SeriKoleksiyon alanı
- SeriesCollection'daki tek bir noktanın alanı

Aşağıdaki kod parçacığı grafik alanının nasıl ayarlanacağını gösterir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
###  **Grafik Çizgilerini Ayarlama**
 Geliştiriciler ayrıca çizgilerin veya veri işaretçilerinin üzerine farklı türde stiller uygulayabilirler.[SeriKoleksiyon](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). Aşağıdaki kod parçacığı, Aspose.Cells API kullanılarak grafik çizgilerinin nasıl ayarlanacağını gösterir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
###  **Microsoft Excel 2007/2010 Temalarını Grafiklere Uygulama**
 Geliştiriciler farklı Microsoft Excel temalarını/renklerini aşağıdakilere uygulayabilir:[SeriKoleksiyon](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)veya aşağıdaki örnekte gösterildiği gibi diğer grafik nesneleri.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
###  **Grafiklerin veya Eksenlerin Başlıklarını Ayarlama**
 WYSIWYG ortamında bir grafiğin başlıklarını ve eksenlerini ayarlamak için Microsoft Excel'i kullanabilirsiniz. Aspose.Cells ayrıca geliştiricilerin çalışma zamanında bir grafiğin başlıklarını ve eksenlerini ayarlamasına da olanak tanır. Tüm grafikler ve eksenleri bir[Başlık](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)Aşağıda bir örnekte gösterildiği gibi başlıklarını ayarlamak için kullanılabilecek özellik.

Aşağıdaki kod parçacığı, grafik ve eksenlere başlıkların nasıl ayarlanacağını gösterir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
###  **Ana Kılavuz Çizgileriyle Çalışmak**
Ana kılavuz çizgilerinin görünümünü özelleştirmek mümkündür. Kılavuz çizgilerini gizleyin veya gösterin ya da renklerini ve diğer ayarlarını tanımlayın. Aşağıda kılavuz çizgilerinin nasıl gizleneceğini ve renklerinin nasıl değiştirileceğini gösteriyoruz.
####  **Ana Kılavuz Çizgilerini Gizleme**
 Geliştiriciler, ana kılavuz çizgilerinin görünürlüğünü aşağıdaki ayarları yaparak kontrol edebilir:[Görünür](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) mülkiyeti[Astar](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) itiraz etmek**doğru** veya yanlış**.

Aşağıdaki kod parçacığında ana kılavuz çizgilerinin nasıl gizleneceği gösterilmektedir. Ana kılavuz çizgileri gizlendikten sonra, çalışma sayfasına kılavuz çizgileri olmayacak bir sütun grafiği eklenecektir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
####  **Ana Kılavuz Çizgisi Ayarlarını Değiştirme**
Geliştiriciler yalnızca ana kılavuz çizgilerinin görünürlüğünü kontrol edemez, aynı zamanda rengi vb. gibi diğer özellikleri de kontrol edebilir.

Aşağıdaki kod parçacığı, ana kılavuz çizgilerinin renginin nasıl değiştirileceğini gösterir. Ana kılavuz çizgilerinin rengini ayarladıktan sonra çalışma sayfasına değiştirilmiş kılavuz çizgileri içeren bir sütun grafiği eklenecektir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

##  **İleri konular**
- [Grafik Serisinin Değer Biçimi Kodunu Ayarlama](/cells/tr/net/set-the-values-format-code-of-chart-series/)
- [Resmi Grafikte Arka Plan Dolgusu Olarak Ayarla](/cells/tr/net/set-picture-as-background-fill-in-the-chart/)
