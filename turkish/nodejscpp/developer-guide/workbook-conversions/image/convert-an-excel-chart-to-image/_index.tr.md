---  
title: Node.js ve C++ kullanarak Excel grafiğini görsele dönüştürme  
linktitle: Bir Excel Grafikini Görüntüye Dönüştür  
type: docs  
weight: 20  
url: /tr/nodejs-cpp/convert-an-excel-chart-to-image/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel grafiklerini görsele dönüştürmeyi öğrenin.  
---  

{{% alert color="primary" %}}  

Grafikler görsel olarak çekicidir ve kullanıcıların verilerdeki karşılaştırmaları, desenleri ve trendleri görmesini kolaylaştırır. Örneğin, çalışsayfa numaralarını analiz etmek yerine, bir grafik, satışların düşüp düşmediğini veya yükseldiğini veya gerçek satışların projeksiyonlanmış satışlarla nasıl karşılaştırıldığını hemen gösterir. İnsanlar genellikle istatistiksel ve grafiksel bilgileri anlaşılması ve bakımı kolay bir şekilde sunmaları istenir. Bir resim yardımcı olur.  

Bazen, uygulama veya web sayfalarında grafiklere ihtiyaç duyulur. Veya bir Word belgesi, PDF dosyası, PowerPoint sunumu veya başka bir uygulama için gerekebilir. Her durumda, grafiği başka yerlerde kullanabilmek için bir görsel olarak render etmek istersiniz.  

{{% /alert %}}  

## **Grafikleri Görüntüye Dönüştürme**  

Buradaki örneklerde, bir pasta grafiği ve bir sütun grafiği resimlere dönüştürülmüştür.  

### **Bir Dilim Grafiğini Bir Görüntü Dosyasına Dönüştürme**  

İlk olarak, Microsoft Excel'de bir pasta grafiği oluşturun ve sonra Aspose.Cells for Node.js via C++ kullanarak görsel dosyasına dönüştürün. Bu örnekteki kod, şablon Microsoft Excel dosyasındaki pasta grafiğe dayalı bir EMF resmi oluşturur.  

|**Çıktı: pasta dilimi grafiği resmi**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|  

1. Microsoft Excel'de bir pasta grafiği oluşturun:  
   1. Microsoft Excel'de yeni bir çalışma kitabı açın.  
   1. Bir çalışsayfaya bazı veriler girin.  
   1. Veriye dayanarak bir pasta grafiği oluşturun.  
   1. Dosyayı kaydedin.  

|**Giriş dosyası.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|  

1. Aspose.Cells'i indirin ve kurun:  
   1. [Aspose.Cells for Node.js via C++'ü İndiriniz](https://downloads.aspose.com/cells/nodejs-cpp).  
   1. Geliştirme bilgisayarınıza kurun.  

Tüm [Aspose](http://www.aspose.com/) bileşenleri, kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun bir süresi yoktur ve yalnızca çıktı belgelerine filigran yerleştirir.  

1. Bir proje oluşturun:  
   1. Tercih edilen IDE'nizi başlatın.  
   1. Yeni bir komut satırı uygulaması oluşturun. Bu örnekte Node.js kullanılmıştır fakat herhangi bir JavaScript çalışma ortamıyla da oluşturabilirsiniz.  
   1. Bir referans ekleyin. Bu proje Aspose.Cells kullanır, bu yüzden Aspose.Cells for Node.js via C++'e referans ekleyin.  
   1. Grafikleri bulan ve dönüştüren kodu yazın. Aşağıdaki kod, görevi gerçekleştirmek için bileşen tarafından kullanılan kod örneğidir. Çok az kod satırı kullanılmıştır.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file which contains the pie chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "PieChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "PieChart.out.emf"), AsposeCells.ImageType.Emf);
```  

### **Bir Sütun Grafiğini Bir Görüntü Dosyasına Dönüştürme**  

İlk olarak, Microsoft Excel'de bir sütun grafiği oluşturun ve yukarıdaki gibi bir görüntü dosyasına dönüştürün. Örnek kodu çalıştırdıktan sonra, şablon Excel dosyasındaki sütun grafiğine göre bir JPEG dosyası oluşturulur.  

|**Çıktı dosyası: bir sütun grafiği görüntüsü.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|  

1. Microsoft Excel'de bir sütun grafiği oluşturun:  
   1. Microsoft Excel'de yeni bir çalışma kitabı açın.  
   1. Bir çalışsayfaya bazı veriler girin.  
   1. Verilere dayalı bir sütun grafiği oluşturun.  
   1. Dosyayı kaydedin.  

|**Giriş dosyası.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|  

1. Yukarıda açıklandığı gibi referanslarla bir projeyi kurun.  
1. Grafik dinamik olarak bir görüntü olarak dönüştürün. Bileşen tarafından görevi gerçekleştirmek için kullanılan kod aşağıda verilmiştir. Kod öncekiyle benzerdir:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing excel file which contains the column chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "ColumnChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "ColumnChart.out.jpeg"), AsposeCells.ImageType.Jpeg);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
