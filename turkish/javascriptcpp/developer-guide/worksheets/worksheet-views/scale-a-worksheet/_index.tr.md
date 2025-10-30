---
title: JavaScript ile C++ kullanarak Bir Çalışma Sayfasını Ölçeklendirme
linktitle: Sayfa Çalışma Sayfasını Nasıl Ölçeklendirilir
type: docs
weight: 130
url: /tr/javascript-cpp/how-to-scale-a-worksheet/
description: Bu makale, Aspose.Cells for JavaScript kullanılarak bir çalışma sayfasını nasıl ölçeklendireceğinizi anlatan kodu gösterir.
keywords: JavaScript ile çalışma sayfasını ölçekleme, JavaScript kullanarak çalışma sayfasını nasıl ölçeklersiniz, C++ ile çalışma sayfasını ölçeklendirme.
---

## **Olası Kullanım Senaryoları**
Çalışma sayfasını ölçeklendirmek, çalıştığınız bağlama bağlı olarak çeşitli yarar sağlayabilir. İşte birkaç yaygın neden:
1. Sayfaya Sığdır: Yazdırırken tüm içeriğin tek bir sayfaya veya belirli sayıda sayfaya sığmasını sağlamak, böylece okumayı ve yönetimi kolaylaştırmak, çok sayfalı sayfaları çevirmeye gerek kalmadan.

1. Sunum: Çalışma sayfasını daha düzenli ve profesyonel görünmesini sağlamak, özellikle toplantılarda veya raporlarda başkalarıyla paylaşıldığında.

1. Okunabilirlik: Metin ve diğer öğelerin boyutunu daha iyi okunabilirlik için ayarlamak, özellikle küçük fontları okumakta zorluk çeken kişiler için.

1. Alan Yönetimi: Çalışma sayfasında alan kullanımını optimize etmek, gereksiz boş alanın olmamasını ve tüm önemli bilgilerin görünür olmasını sağlamak, aşırı kaydırmadan.

1. Veri Görselleştirme: Çizelge ve grafiklerde, uygun alanı doldurmak için boyut ayarlaması yaparak onları daha anlaşılır hale getirmeye yardımcı olabilir.

1. Tutarlılık: Birden fazla çalışma sayfası veya belge arasında tutarlı görünüm ve his sağlamak, özellikle profesyonel ve eğitimsel ortamlar için önemlidir.

## **Excel'de Çalışma Sayfasını Nasıl Ölçeklendirilir**
Excel’de çalışma sayfasını ölçeklendirmek, içeriğinizi yazdırırken tek bir sayfaya veya belirli sayfa sayısına sığdırmaya yardımcı olabilir. İşte çalışma sayfasını ölçeklendirme adımları:

1. Çalışma Sayfanızı Açın: Ölçeklendirmek istediğiniz Excel çalışma sayfasını açın.

1. Sayfa Düzeni Sekmesine Gidin: Ribbon'da Sayfa Düzeni sekmesine tıklayın.

1. Ölçekleme Gruplarına Göz Atma: Sayfa Düzeni sekmesinde, Ölçekleyecek Gruplarını bulun. Burada ölçeklendirme ayarlarını yapabilirsiniz. Genişlik: Yazdırılan çalışma sayfasının kaç sayfa genişliğinde olacağını belirlemenizi sağlar. Yükseklik: Yazdırılan çalışma sayfasının kaç sayfa yüksekliğinde olacağını belirlemenizi sağlar. Ölçek: Burada özel bir ölçek yüzdesi de ayarlayabilirsiniz.
<br>
<img src="1.png" width=60% />

1. Genişlik ve Yükseklik Ayarları: Genişlik ve yüksekliği istediğiniz sayfa sayısına ayarlayın. Örneğin, çalışma sayfasını tek sayfaya sığdırmak istiyorsanız her ikisini de 1 sayfa yapın.

1. Ölçekleme Yüzdesini (gerekirse) Ayarlayın: Belirli bir ölçek yüzdesi ayarlamak istiyorsanız, Ölçek kutusunu ayarlayın. Örneğin, %50 olarak ayarlarsanız, her şey yarı boyutuna gelir.


## **JavaScript ile C++ kullanarak Çalışma Sayfasını Nasıl Ölçeklendirilir**
Aspose.Cells for JavaScript C++ aracılığıyla Excel dosyalarıyla programatik olarak çalışmak için güçlü bir kütüphanedir. Aspose.Cells kullanarak çalışma sayfasını ölçeklendirmek için şu adımları izleyin: [örnek dosyayı](sample.xlsx) yükleyin ve içeriğin istenilen sayfa sayısına veya orijinal boyutun belirli bir yüzdesine sığması için yazdırma ayarlarını ayarlayın.

### **Örnek: Sayfaya Sığdır**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Fit To Page Example</title>
    </head>
    <body>
        <h1>Fit Worksheet to One Page</h1>
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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the worksheet to fit to 1 page wide and 1 page tall
            pageSetup.fitToPagesWide = 1;
            pageSetup.fitToPagesTall = 1;

            // Saving the modified workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_fit_to_page.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet fitted to one page. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="3.png" width=60% />

### **Örnek: Yüzdeye Ölçekle**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Scale Worksheet</title>
    </head>
    <body>
        <h1>Scale Worksheet Example</h1>
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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the scaling to a specific percentage (e.g., 75%)
            pageSetup.zoom = 75;

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_scaled_percentage.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Scaled Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scaling applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="2.png" width=60% />
