---
title: Grafik Biçimlendirme
type: docs
weight: 20
url: /tr/java/chart-formatting/
---

## **Grafik Görünümünü Ayarlama**

[Grafik Türleri](/cells/tr/java/chart-types/)'nde, Aspose.Cells tarafından sunulan grafik türleri ve grafik nesnelerine kısaca bir giriş yapmıştık.

Bu makalede, farklı özelliklerin ayarlanmasıyla grafiklerin görünümünün nasıl özelleştirileceğini tartışıyoruz:

- [Grafik alanını ayarlama](/cells/tr/java/chart-formatting/#setting-chart-area).
- [Grafik çizgilerini ayarlama](/cells/tr/java/chart-formatting/#setting-chart-lines).
- [Temalar uygulama](/cells/tr/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [Grafiklere ve ekselere başlık atama](/cells/tr/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [Izgaralarla çalışma](/cells/tr/java/chart-formatting/#setting-major-gridlines).
- [Arka ve yan duvarlar için sınırlar belirleme](/cells/tr/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **Grafik Alanını Ayarlama**

Bir grafikte farklı türde alanlar bulunmakta ve Aspose.Cells her bir alanın görünümünü değiştirme esnekliği sağlamaktadır. Geliştiriciler, bir alan üzerinde farklı biçimlendirme ayarları uygulayarak öncelikli renk, arka plan rengi ve doldurma formatı gibi özellikleri değiştirebilirler.

Aşağıdaki örnekte, bir grafikte farklı türde alanlara farklı biçimlendirme ayarları uyguladık. Bu alanlar şunları içerir:

- Plot alanı
- Grafik alanı
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) alanı
- Bir [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) içinde tek bir noktanın alanı

Örnek kodu çalıştırdıktan sonra aşağıdaki gibi bir sütun grafiği çalışma sayfasına eklenecektir:

**Renkli alanlara sahip sütun grafiği** 

![todo:image_alt_text](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **Grafik Çizgilerini Ayarlama**

Geliştiriciler, örnekte gösterildiği gibi [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) veya diğer grafik nesnelerinin çizgilerine veya veri işaretçilerine farklı stili uygulayabilirler. Örnek kodu çalıştırdıktan sonra çalışma sayfasına bir sütun grafiği eklenir:

**Çizgi stilleri uygulandıktan sonra sütun grafiği** 

![todo:image_alt_text](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Microsoft Excel 2007/2010 Temalarını Grafiklere Uygulama**

Geliştiriciler, aşağıdaki örnekte gösterildiği gibi [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) veya diğer grafik nesnelerine farklı Microsoft Excel temaları ve renkleri uygulayabilirler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **Grafiğin veya Eksenlerin Başlıklarını Ayarlama**

Grafik ve ekselerin başlıkları Excel'i kullanarak aşağıdaki gibi bir WYSIWYG ortamında ayarlanabilir.

**Grafik başlıklarının ve ekselertitslerinin Microsoft Excel kullanarak ayarlanması** 

![todo:image_alt_text](chart-formatting_3.png)

Aspose.Cells ayrıca geliştiricilere grafiklerin ve ekselerinin başlıklarını çalışma zamanında belirleme imkanı sağlar. Tüm grafiklerin ve ekselerinin bir [**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text) yöntemi bulunur ve bu yöntem örnekte gösterildiği gibi başlıklarını belirlemek için kullanılabilir. Örnek kodu çalıştırdıktan sonra çalışma sayfasına aşağıdaki gibi bir sütun grafiği eklenecektir:

**Başlık belirlendikten sonraki sütun grafiği** 

![todo:image_alt_text](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **Önemli Izgaraları Belirleme**

#### **Büyük Izgaraları Gizleme**

Geliştiriciler, [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line) nesnesinin [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) yöntemini kullanarak önemli izgaraların görünürlüğünü kontrol edebilirler. Önemli izgaraları gizledikten sonra çalışma sayfasına eklenen sütun grafiğinin aşağıdaki görünüme sahip olacaktır:

**Önemli izgaraları gizlenmiş sütun grafiği** 

![todo:image_alt_text](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **Büyük Izgaraların Ayarlarını Değiştirme**

Geliştiriciler sadece önemli izgaraların görünürlüğünü değil ayrıca rengi gibi diğer özelliklerini de ayarlayabilirler. Önemli izgaraların rengini ayarladıktan sonra çalışma sayfasına eklenen sütun grafiğinin aşağıdaki görünüme sahip olacağı:

**Renkli önemli izgaralı sütun grafiği** 

![todo:image_alt_text](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **Arka ve Yan Duvarlar için Sınırlar Belirleme**

Microsoft Excel 2007'nin piyasaya sürülmesinden beri, 3D grafiklerin duvarları ikiye bölünmüştür: yan duvar ve arka duvar, bu yüzden bunları ayrı ayrı temsil etmek için iki [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) nesnesi kullanmalı ve onlara erişmek için [**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) ve [**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall) kullanabilirsiniz.

Aşağıdaki örnek, yan duvarın kenarını farklı özellikleri kullanarak nasıl ayarlayacağınızı gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **Grafik Pozisyonunu ve Boyutunu Değiştirme**

Bazen, çalışma sayfası içindeki yeni veya mevcut grafiğin konumunu veya boyutunu değiştirmek isteyebilirsiniz. Aspose.Cells, bunu başarmak için [**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject) özelliğini sağlar. Yeni **yükseklik** ve **genişlik** ile grafik boyutunu veya yeni **X** ve **Y** koordinatları ile konumunu ayarlamak için alt özelliklerini kullanabilirsiniz.

### **Grafiğin Konumunu ve Boyutunu Değiştirme**

Grafiğin pozisyonunu (X, Y koordinatları) ve boyutunu (yükseklik, genişlik) değiştirmek için bu özellikleri kullanın:

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

Aşağıdaki örnek yukarıdaki özelliklerin kullanımını açıklar. İlk çalışma sayfasında bir grafiği içeren mevcut bir çalışma kitabını yükler. Ardından grafiği yeniden boyutlandırır ve konumlandırır ve çalışma kitabını kaydeder.

Örnek kodun yürütülmeden önce, kaynak dosya şu şekildedir:

**Örnek kodun yürütülmeden önce grafiğin boyutu ve konumu** 

![todo:image_alt_text](chart-formatting_7.png)

Yürütüldükten sonra, çıktı dosyası şu şekildedir:

**Örnek kodun yürütüldükten sonra grafiğin boyutu ve konumu** 

![todo:image_alt_text](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **Tasarımcı Grafikleri Manipüle Etmek**

Tasarım şablonu dosyalarınızda grafikleri manipüle etmeniz gereken bir zamandır. Aspose.Cells, içeriği ve öğeleriyle tasarım grafiklerini tamamen destekler. Veri, grafik içeriği, arka plan resmi ve biçimlendirme doğrulukla korunabilir.

### **Tasarım Şablonlarında Grafikleri Manipüle Etme**

Tasarım şablonu dosyasındaki grafikleri manipüle etmek için tüm grafikle ilgili API çağrılarını kullanın. Örneğin, mevcut grafikleri almak için [**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) özelliğini kullanın.

#### **Bir Grafik Oluşturma**

Aşağıdaki örnek, bir pasta grafiği oluşturmanın nasıl yapıldığını gösterir. Bu grafiği daha sonra manipüle edeceğiz. Aşağıdaki çıktı kod tarafından oluşturulmuştur.

**Giriş pasta grafiği** 

![todo:image_alt_text](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **Grafiği Manipüle Etmek**

Aşağıdaki örnek, mevcut grafiği nasıl manipüle edeceğinizi gösterir. Bu örnekte yukarıda oluşturulan grafiği değiştiriyoruz. Aşağıdaki çıktı kod tarafından oluşturulmuştur. Grafik başlığının renginin maviden siyaha değiştiğine dikkat edin ve 'England 30000' 'United Kingdom, 30K' olarak değiştirildi.

**Pasta grafiği değiştirildi** 

![todo:image_alt_text](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Tasarımcı Şablonunda Bir Çizgi Grafiği Manipüle Etmek**

Bu örnekte, bir çizgi grafiği manipüle edeceğiz. Mevcut grafiğe bazı veri serileri ekleyeceğiz ve bunların çizgi renklerini değiştireceğiz.

İlk olarak, tasarımcıdaki hat grafiğine bakın.

**Giriş hat grafiği** 

![todo:image_alt_text](chart-formatting_11.png)

Şimdi, aşağıdaki kodu kullanarak hat grafiğini manipüle ediyoruz (**linechart.xls** dosyasında bulunan). Aşağıdaki çıktı kod tarafından oluşturulmuştur.

**Manipüle edilen hat grafiği** 

![todo:image_alt_text](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **Sparklines Kullanma**

Microsoft Excel 2010, bilgileri daha önce hiç olmadığı kadar fazla şekilde analiz etmenizi sağlar. Kullanıcıların yeni veri analiz ve görselleştirme araçlarıyla önemli veri eğilimlerini takip etmesine ve vurgulamasına izin verir. Sparklines, veriyi ve tabloyu aynı anda görüntüleyebileceğiniz mini grafiklerdir. Sparklines uygun şekilde kullanıldığında, veri analizi daha hızlı ve daha anlaşılır olur. Ayrıca, aşırı kalabalık çalışma tablolarını çok fazla meşgul grafiklerle önler. Onlar, aynı tabloda veriyi görmek için basit bir görünüm sağlar. Ayrıca, Aspose.Cells, elektronik tablolardaki sparklines'ı manipüle etmek için bir API sağlar.

Aspose.Cells, elektronik tablolardaki sparklines'ları manipüle etmek için bir API sağlar.

### **Microsoft Excel'de Sparklines Kullanma**

Microsoft Excel 2010'da Sparklines eklemek için:

1. Sparklines'ların görünmesini istediğiniz hücreleri seçin. Onları görüntülemeyi kolaylaştırmak için, verinin yanındaki hücreleri seçin.
1. Menü şeridinde **Ekle**'yi tıklayın, ardından **Sparklines** grubunda **Sütun**'u seçin.

![todo:image_alt_text](chart-formatting_13.png)

1. Kaynak verileri içeren çalışma sayfasındaki hücrelerin aralığını seçin veya girin.
   Grafikler görünür.

Kıvılcım çizgileri, örneğin trendleri veya bir ​​beyzbol ligi için kazanma veya kaybetme kaydını görmeye yardımcı olur. Kıvılcım çizgileri, ligin her takımının tüm sezonunu hatta toplayabilir.

![todo:image_alt_text](chart-formatting_14.png)

### **Aspose.Cells, kullanıcıların verilen veri aralığı için özel grafikleri ekleyerek seçilen hücre alanlarına farklı tipte minik grafikler ekleyebilecekleri özgürlüğü sunar.**

Geliştiriciler, Aspose.Cells tarafından sağlanan API ile şablon dosyasındaki kıvılcım çizgilerini oluşturabilir, silebilir veya okuyabilir. Belirli bir veri aralığı için özel grafikler ekleyerek, geliştiriciler seçilen hücre alanlarına farklı tipte küçük grafikler eklemek için özgürlüğe sahiptir.

Aşağıdaki örnek, Sparklines özelliğini sergiler. Örnek, şunları gösterir:

1. Basit bir şablon dosyasını açın.
1. Bir çalışma sayfası için sparklines bilgilerini okuyun.
1. Belirli bir veri aralığı için yeni sparklines ekleyin.
1. Excel dosyasını diske kaydedin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **Grafiğe 3D Format Uygulama**

Senaryonuz için sadece sonuçları alabilmeniz için 3D grafik stili gerekebilir. Aspose.Cells API'leri, bu makalede gösterildiği gibi Microsoft Excel 2007 3D biçimlendirmesini uygulamak için ilgili API'yi sağlar.

### **Grafiğe 3D Format Ayarlama**

Microsoft Excel 2007 3D biçimlendirmesi uygulamak için aşağıda tam bir örnek verilmiştir. Yukarıdaki örnek kodu çalıştırdıktan sonra, aşağıda gösterildiği gibi bir sütun grafiği (3D efektlerle) çalışma sayfasına eklenecektir.

**3D biçimlendirmeli sütun grafiği**

![todo:image_alt_text](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

Desteklenen 2D ve 3D grafik türlerinin tam listesi için [Görüntüleme için desteklenen grafik türleri](/cells/tr/java/chart-rendering/#supported-chart-types-for-rendering) sayfasına bakın.

{{% /alert %}}

## **Gelişmiş Konular**
- [Grafikte Arka Plan Doldurma Olarak Resim Ayarlama](/cells/tr/java/set-picture-as-background-fill-in-the-chart/)
{{< app/cells/assistant language="java" >}}
