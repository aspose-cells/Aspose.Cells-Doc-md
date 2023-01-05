---
title: Grafik Biçimlendirme
type: docs
weight: 20
url: /tr/java/chart-formatting/
---
## **Ayar Tablosu Görünümü**

 İçinde[Grafik Türleri](/cells/tr/java/chart-types/), Aspose.Cells tarafından sunulan harita türlerine ve harita nesnelerine kısa bir giriş yaptık.

Bu makalede, bir dizi farklı özellik ayarlayarak grafiklerin görünümünün nasıl özelleştirileceğini tartışıyoruz:

- [Grafik alanını ayarlama](/cells/tr/java/chart-formatting/#setting-chart-area).
- [Grafik çizgilerini ayarlama](/cells/tr/java/chart-formatting/#setting-chart-lines).
- [temaları uygulama](/cells/tr/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [Başlıkları grafiklere ve eksenlere ayarlama](/cells/tr/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [Kılavuz çizgileriyle çalışma](/cells/tr/java/chart-formatting/#setting-major-gridlines).
- [Arka ve yan duvarlar için sınır belirleme](/cells/tr/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **Ayar Tablosu Alanı**

Bir çizelgede farklı türde alanlar vardır ve Aspose.Cells, her alanın görünümünü değiştirme esnekliği sağlar. Geliştiriciler, ön plan rengini, arka plan rengini ve dolgu biçimini vb. değiştirerek bir alana farklı biçimlendirme ayarları uygulayabilir.

Aşağıda verilen örnekte, grafiğin farklı alanlarına farklı biçimlendirme ayarları uyguladık. Bu alanlar şunları içerir:

- Arsa alanı
- Grafik alanı
- [**Seri Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) alan
- Bir noktadaki tek bir noktanın alanı[**Seri Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

Örnek kodu çalıştırdıktan sonra, çalışma sayfasına aşağıda gösterildiği gibi bir sütun grafiği eklenecektir:

**Alanları doldurulmuş bir sütun grafiği** 

![yapılacaklar:resim_alternatif_metin](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **Grafik Çizgilerini Ayarlama**

 Geliştiriciler ayrıca satırlara veya veri işaretçilerine farklı türde stiller uygulayabilir.[**Seri Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)aşağıdaki örnekte gösterildiği gibi. Örnek kodu çalıştırmak, aşağıda gösterildiği gibi çalışma sayfasına bir sütun grafiği ekler:

**Çizgi stilleri uygulandıktan sonra sütun grafiği** 

![yapılacaklar:resim_alternatif_metin](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Microsoft Excel 2007/2010 Temalarını Grafiklere Uygulama**

Geliştiriciler, farklı Microsoft Excel temaları ve renkleri uygulayabilir.[**Seri Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)veya aşağıdaki örnekte gösterildiği gibi diğer grafik nesneleri.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **Grafiklerin veya Eksenlerin Başlıklarını Ayarlama**

Aşağıda gösterildiği gibi bir WYSIWYG ortamında grafiğin başlıklarını ve eksenlerini ayarlamak için Microsoft Excel'i kullanabilirsiniz.

**Microsoft Excel kullanarak bir grafiğin ve eksenlerinin başlıklarını ayarlama** 

![yapılacaklar:resim_alternatif_metin](chart-formatting_3.png)

 Aspose.Cells, geliştiricilerin çalışma zamanında bir grafiğin başlıklarını ve eksenlerini ayarlamasına da olanak tanır. Tüm çizelgeler ve eksenleri bir[**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text)aşağıda bir örnekte gösterildiği gibi başlıklarını ayarlamak için kullanılabilecek bir yöntem. Örnek kodu çalıştırdıktan sonra, çalışma sayfasına aşağıda gösterildiği gibi bir sütun grafiği eklenecektir:

**Başlıkları ayarladıktan sonra sütun grafiği** 

![yapılacaklar:resim_alternatif_metin](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **Ana Kılavuz Çizgilerini Ayarlama**

#### **Büyük Kılavuz Çizgilerini Gizleme**

 Geliştiriciler, ana kılavuz çizgilerinin görünürlüğünü aşağıdakileri kullanarak kontrol edebilir:[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) yöntemi[**Astar**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)nesne. Ana kılavuz çizgilerini gizledikten sonra, çalışma sayfasına eklenen bir sütun grafiği aşağıdaki görünüme sahip olur:

**Gizli ana kılavuz çizgileri olan bir sütun grafiği** 

![yapılacaklar:resim_alternatif_metin](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **Ana Kılavuz Çizgileri Ayarlarını Değiştirme**

Geliştiriciler yalnızca ana kılavuz çizgilerinin görünürlüğünü değil, aynı zamanda rengi gibi diğer özellikleri de kontrol edebilir. Ana kılavuz çizgilerinin rengini ayarladıktan sonra, çalışma sayfasına eklenen bir sütun grafiği aşağıdaki görünüme sahip olacaktır:

**Renkli ana kılavuz çizgileri olan sütun grafiği** 

![yapılacaklar:resim_alternatif_metin](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **Arka ve Yan Duvarlar İçin Kenarlık Ayarlama**

 Microsoft Excel 2007'nin piyasaya sürülmesinden bu yana, bir 3B grafiğin duvarları iki bölüme ayrılmıştır: yan duvar ve arka duvar, bu nedenle iki parça kullanmak zorundayız[**Duvarlar**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) nesneleri ayrı ayrı temsil edebilir ve bunları kullanarak erişebilirsiniz.[**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) ve[**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

Aşağıda verilen örnek, farklı nitelikler kullanılarak yan duvarın sınırının nasıl ayarlanacağını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **Grafik Konumunu ve Boyutunu Değiştirme**

 Bazen, çalışma sayfasındaki yeni veya mevcut grafiğin konumunu veya boyutunu değiştirmek istersiniz. Aspose.Cells şunları sağlar:[**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject)Bunu başarmak için mülkiyet. Grafiği yenisiyle yeniden boyutlandırmak için alt özelliklerini kullanabilirsiniz.**boy uzunluğu** ve**Genişlik** veya yenisiyle yeniden konumlandırın** X** ve**Y** koordinatları.

### **Grafiğin Konumunu ve Boyutunu Değiştirme**

Grafiğin konumunu (X, Y koordinatları) ve boyutunu (yükseklik, genişlik) değiştirmek için şu özellikleri kullanın:

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

Aşağıdaki örnek, yukarıdaki özelliklerin kullanımını açıklamaktadır. İlk çalışma sayfasında bir grafik içeren mevcut çalışma kitabını yükler. Ardından grafiği yeniden boyutlandırır ve yeniden konumlandırır ve çalışma kitabını kaydeder.

Örnek kodun yürütülmesinden önce, kaynak dosya şöyle görünür:

**Örnek kodun yürütülmesinden önceki grafik boyutu ve konumu** 

![yapılacaklar:resim_alternatif_metin](chart-formatting_7.png)

Yürütmeden sonra çıktı dosyası şöyle görünür:

**Örnek kodun yürütülmesinden sonraki grafik boyutu ve konumu** 

![yapılacaklar:resim_alternatif_metin](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **Tasarımcı Grafiklerini Değiştirme**

Tasarımcı şablon dosyalarınızdaki grafikleri manipüle etmeniz veya değiştirmeniz gereken zamanlar olabilir. Aspose.Cells, içeriği ve öğeleriyle tasarımcı grafiklerini işlemeyi tamamen destekler. Veriler, grafik içerikleri, arka plan görüntüsü ve biçimlendirme doğrulukla korunabilir.

### **Şablon Dosyalarında Tasarımcı Grafiklerini Değiştirme**

 Bir şablon dosyasındaki tasarımcı grafiklerini değiştirmek için tüm grafikle ilgili API çağrılarını kullanın. Örneğin, kullan[**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) şablon dosyasındaki mevcut grafikler koleksiyonunu almak için özelliği.

#### **Grafik Oluşturma**

Aşağıdaki örnek, pasta grafiğin nasıl oluşturulacağını gösterir. Bu tabloyu daha sonra manipüle edeceğiz. Aşağıdaki çıktı kod tarafından üretilir.

**Giriş pasta grafiği** 

![yapılacaklar:resim_alternatif_metin](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **Grafiği Manipüle Etme**

Aşağıdaki örnek, mevcut grafiğin nasıl değiştirileceğini gösterir. Bu örnekte, yukarıda oluşturulan grafiği değiştiriyoruz. Aşağıdaki çıktı kod tarafından üretilir. Grafik başlığının renginin maviden siyaha ve 'İngiltere 30000'in' Birleşik Krallık, 30K' olarak değiştirildiğine dikkat edin.

**Pasta grafik değiştirildi** 

![yapılacaklar:resim_alternatif_metin](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Tasarımcı Şablonunda Çizgi Grafiği Değiştirme**

Bu örnekte, bir çizgi grafiğini işleyeceğiz. Mevcut grafiğe bazı veri serileri ekleyeceğiz ve çizgi renklerini değiştireceğiz.

İlk olarak, tasarımcı çizgi grafiğine bir göz atın.

**Giriş çizgisi grafiği** 

![yapılacaklar:resim_alternatif_metin](chart-formatting_11.png)

 Şimdi (içinde bulunan) çizgi grafiğini manipüle ediyoruz.**çizgi grafiği.xls** dosya) aşağıdaki kodu kullanarak. Aşağıdaki çıktı kod tarafından üretilir.

**Manipüle edilmiş çizgi grafiği** 

![yapılacaklar:resim_alternatif_metin](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **Mini Grafikleri Kullanma**

Microsoft Excel 2010, bilgileri her zamankinden daha fazla yöntemle analiz edebilir. Kullanıcıların, yeni veri analizi ve görselleştirme araçlarıyla önemli veri trendlerini izlemesine ve vurgulamasına olanak tanır. Mini grafikler, verileri ve grafiği aynı tabloda görüntüleyebilmeniz için hücrelerin içine yerleştirebileceğiniz mini grafiklerdir. Küçük grafikler düzgün kullanıldığında, veri analizi daha hızlı ve isabetlidir. Ayrıca, birçok meşgul çizelge içeren aşırı kalabalık çalışma sayfalarından kaçınarak basit bir bilgi görünümü sağlarlar.

Aspose.Cells, elektronik tablolardaki mini grafikleri işlemek için bir API sağlar.

### **Microsoft Excel'deki Mini Grafikler**

Microsoft Excel 2010'da minik grafikler eklemek için:

1. Mini grafiklerin görünmesini istediğiniz hücreleri seçin. Görüntülenmelerini kolaylaştırmak için verilerin yan tarafındaki hücreleri seçin.
1.  Tıklamak**Sokmak** şeritte ve ardından seçin**kolon** içinde**mini grafikler** grup.

![yapılacaklar:resim_alternatif_metin](chart-formatting_13.png)

1. Çalışma sayfasında kaynak verileri içeren hücre aralığını seçin veya girin.
 Grafikler görünür.

Mini grafikler, örneğin trendleri veya bir softbol liginin galibiyet veya mağlubiyet rekorunu görmenize yardımcı olur. Mini grafikler, ligdeki her takımın tüm sezonunu bile özetleyebilir.

![yapılacaklar:resim_alternatif_metin](chart-formatting_14.png)

### **Aspose.Cells kullanan mini grafikler**

Geliştiriciler, Aspose.Cells tarafından sağlanan API'i kullanarak küçük grafikler (şablon dosyasında) oluşturabilir, silebilir veya okuyabilir. Geliştiriciler, belirli bir veri aralığı için özel grafikler ekleyerek, seçilen hücre alanlarına farklı türde küçük grafikler ekleme özgürlüğüne sahip olurlar.

Aşağıdaki örnek Mini Grafikler özelliğini göstermektedir. Örnek, aşağıdakilerin nasıl yapılacağını gösterir:

1. Basit bir şablon dosyası açın.
1. Bir çalışma sayfası için mini grafik bilgilerini okuyun.
1. Belirli bir veri aralığı için bir hücre alanına yeni mini grafikler ekleyin.
1. Excel dosyasını diske kaydeder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **Grafiğe 3B Format Uygulama**

Yalnızca senaryonuz için sonuçları alabilmek için 3B grafik stillerine ihtiyacınız olabilir. Aspose.Cells API'leri, bu makalede gösterildiği gibi Microsoft Excel 2007 3B biçimlendirmesini uygulamak için ilgili API'i sağlar.

### **3D Formatını Grafiğe Ayarlama**

Bir grafiğin nasıl oluşturulacağını ve Microsoft Excel 2007 3B biçimlendirmesinin nasıl uygulanacağını gösteren eksiksiz bir örnek aşağıda verilmiştir. Yukarıdaki örnek kodu çalıştırdıktan sonra, aşağıda gösterildiği gibi çalışma sayfasına bir sütun grafiği (3B efektlerle) eklenecektir.

**3B biçimlendirmeli bir sütun grafiği**

![yapılacaklar:resim_alternatif_metin](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

 Hangi 2B ve 3B grafiklerin desteklendiğinin tam listesi için bkz.[İşleme için desteklenen grafik türleri](/cells/tr/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **ileri konular**
- [Grafiği Arka Plan Dolgusu Olarak Ayarla](/cells/tr/java/set-picture-as-background-fill-in-the-chart/)
