---
title: JavaScript ile C++ kullanarak Excel Grafiklerini Görüntüye Dönüştür
linktitle: Bir Excel Grafikini Görüntüye Dönüştür
type: docs
weight: 20
url: /tr/javascript-cpp/convert-an-excel-chart-to-image/
description: Excel grafiklerini Aspose.Cells for JavaScript kullanarak C++ ile görsele dönüştürmenin nasıl yapıldığını öğrenin.
---

{{% alert color="primary" %}}  

Grafikler görsel olarak çekicidir ve kullanıcıların verilerdeki karşılaştırmaları, desenleri ve trendleri görmesini kolaylaştırır. Örneğin, çalışsayfa numaralarını analiz etmek yerine, bir grafik, satışların düşüp düşmediğini veya yükseldiğini veya gerçek satışların projeksiyonlanmış satışlarla nasıl karşılaştırıldığını hemen gösterir. İnsanlar genellikle istatistiksel ve grafiksel bilgileri anlaşılması ve bakımı kolay bir şekilde sunmaları istenir. Bir resim yardımcı olur.  

Bazen, uygulama veya web sayfalarında grafiklere ihtiyaç duyulur. Veya bir Word belgesi, PDF dosyası, PowerPoint sunumu veya başka bir uygulama için gerekebilir. Her durumda, grafiği başka yerlerde kullanabilmek için bir görsel olarak render etmek istersiniz.  

{{% /alert %}}  

## **Grafikleri Görüntüye Dönüştürme**  

Buradaki örneklerde, bir pasta grafiği ve bir sütun grafiği resimlere dönüştürülmüştür.  

### **Bir Dilim Grafiğini Bir Görüntü Dosyasına Dönüştürme**  

İlk olarak, Microsoft Excel'de bir pasta grafik oluşturun ve ardından bunu C++ kullanarak Aspose.Cells for JavaScript ile bir görüntü dosyasına dönüştürün. Bu örnekteki kod, şablon Microsoft Excel dosyasındaki pasta grafik temel alınarak bir EMF görüntüsü oluşturur.  

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
   1. [C++ ile Aspose.Cells for JavaScript indir](https://downloads.aspose.com/cells/javascript-cpp).  
   1. Geliştirme bilgisayarınıza kurun.  

Tüm [Aspose](http://www.aspose.com/) bileşenleri, kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun bir süresi yoktur ve yalnızca çıktı belgelerine filigran yerleştirir.  

1. Bir proje oluşturun:  
   1. Tercih edilen IDE'nizi başlatın.  
   1. Yeni bir konsol uygulaması oluşturun. Bu örnek JavaScript uygulaması kullanmaktadır, ancak herhangi bir JavaScript çalışma zamanı ortamı kullanılarak da oluşturulabilir.  
   1. Bir referans ekleyin. Bu proje Aspose.Cells kullanmaktadır, bu yüzden Aspose.Cells for JavaScript ile C++ referansı ekleyin.  
   1. Grafikleri bulan ve dönüştüren kodu yazın. Aşağıdaki kod, görevi gerçekleştirmek için bileşen tarafından kullanılan kod örneğidir. Çok az kod satırı kullanılmıştır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Chart to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (EMF) and prepare download link
            const imageData = chart.toImage(AsposeCells.ImageType.Emf);
            const blob = new Blob([imageData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PieChart.out.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to EMF successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
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

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Chart to Image</title>
    </head>
    <body>
        <h1>Convert Chart to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageType, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (JPEG)
            const imageData = await chart.toImage(ImageType.Jpeg);

            // Create a Blob and provide a download link
            const blob = new Blob([imageData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ColumnChart.out.jpeg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to image successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
