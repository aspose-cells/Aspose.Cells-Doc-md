---
title: Ayar Tablosu Görünümü
linktitle: Grafik Formatı
type: docs
weight: 20
url: /tr/net/setting-chart-appearance/
---
## **Ayar Tablosu Görünümü**
Grafik Nasıl Oluşturulur'da, Aspose.Cells tarafından sunulan grafik türleri ve grafik nesneleri hakkında kısa bir giriş yaptık ve nasıl oluşturulacağını açıkladık. Bu makalede, özelliklerini ayarlayarak grafiklerin görünümünün nasıl özelleştirileceği anlatılmaktadır:

- Grafik alanını ayarlama.
- Grafik çizgilerini ayarlama.
- Temalar uygulanıyor.
- Başlıkları grafiklere ve eksenlere ayarlama.
- Kılavuz çizgileriyle çalışma.
### **Ayar Tablosu Alanı**
Bir grafikte farklı türde alanlar vardır ve Aspose.Cells, her alanın görünümünü değiştirme esnekliği sağlar. Geliştiriciler, ön plan rengini, arka plan rengini ve dolgu biçimini vb. değiştirerek bir alana farklı biçimlendirme ayarları uygulayabilir.

Aşağıda verilen örnekte, grafiğin farklı alanlarına farklı biçimlendirme ayarları uyguladık. Bu alanlar şunları içerir:

- Arsa alanı
- Grafik alanı
- SeriToplama alanı
- SeriesCollection'daki tek bir noktanın alanı

Aşağıdaki kod parçacığı, grafik alanının nasıl ayarlanacağını gösterir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **Grafik Çizgilerini Ayarlama**
 Geliştiriciler ayrıca satırlara veya veri işaretçilerine farklı türde stiller uygulayabilir.[Seri Koleksiyonu](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). Aşağıdaki kod parçacığı, Aspose.Cells API kullanılarak grafik çizgilerinin nasıl ayarlanacağını gösterir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **Microsoft Excel 2007/2010 Temalarını Grafiklere Uygulama**
 Geliştiriciler, farklı Microsoft Excel temalarını/renklerini[Seri Koleksiyonu](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)veya aşağıdaki örnekte gösterildiği gibi diğer grafik nesneleri.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **Grafiklerin veya Eksenlerin Başlıklarını Ayarlama**
WYSIWYG ortamında bir grafiğin başlıklarını ve eksenlerini ayarlamak için Microsoft Excel'i kullanabilirsiniz. Aspose.Cells, geliştiricilerin çalışma zamanında bir grafiğin başlıklarını ve eksenlerini ayarlamasına da olanak tanır. Tüm çizelgeler ve eksenleri bir[Başlık](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)başlıklarını aşağıda bir örnekte gösterildiği gibi ayarlamak için kullanılabilecek özellik.

Aşağıdaki kod parçacığı, başlıkların grafiklere ve eksenlere nasıl ayarlanacağını gösterir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **Büyük Kılavuz Çizgilerle Çalışma**
Ana kılavuz çizgilerinin görünümünü özelleştirmek mümkündür. Kılavuz çizgilerini gizleyin veya gösterin ya da renklerini ve diğer ayarlarını tanımlayın. Aşağıda, kılavuz çizgilerinin nasıl gizleneceğini ve renklerinin nasıl değiştirileceğini gösteriyoruz.
#### **Büyük Kılavuz Çizgilerini Gizleme**
Geliştiriciler, ana kılavuz çizgilerinin görünürlüğünü ayarlayarak kontrol edebilir.[Görünür](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) mülkiyeti[Astar](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) itiraz etmek**doğru** veya**yanlış**.

Aşağıdaki kod parçacığı, ana kılavuz çizgilerinin nasıl gizleneceğini gösterir. Ana kılavuz çizgilerini gizledikten sonra, kılavuz çizgileri olmayacak çalışma sayfasına bir sütun grafiği eklenecektir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **Ana Kılavuz Çizgileri Ayarlarını Değiştirme**
Geliştiriciler yalnızca ana kılavuz çizgilerinin görünürlüğünü değil, aynı zamanda rengi gibi diğer özellikleri de kontrol edebilir.

Aşağıdaki kod parçacığı, ana kılavuz çizgilerinin renginin nasıl değiştirileceğini gösterir. Ana kılavuz çizgilerinin rengini ayarladıktan sonra, çalışma sayfasına değiştirilmiş kılavuz çizgileriyle bir sütun grafiği eklenecektir.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **ileri konular**
- [Grafik Serisinin Değer Biçim Kodunu Ayarlayın](/cells/tr/net/set-the-values-format-code-of-chart-series/)
- [Grafiği Arka Plan Dolgusu Olarak Ayarla](/cells/tr/net/set-picture-as-background-fill-in-the-chart/)
