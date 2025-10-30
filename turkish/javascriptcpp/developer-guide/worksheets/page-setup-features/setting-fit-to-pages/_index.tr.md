---
title: Excel i sığdırılmış sayfa genişliği ve yüksekliğiyle nasıl yazdırılır JavaScript ve C++ ile
linktitle: Excel i Geniş ve Yüksek olarak Yazdırma
type: docs
weight: 200
url: /tr/javascript-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Bu makale, Aspose.Cells for JavaScript ve C++ kullanarak FitToPagesWide ve FitToPagesTall ayarlama kodunu açıklar.
keywords: JavaScript ve C++ ile FitToPagesWide ve FitToPagesTall ayarlama, JavaScript te FitToPagesWide ve FitToPagesTall ekleme, Excel de FitToPagesWide ve FitToPagesTall ayarlama, Excel de FitToPagesWide ve FitToPagesTall temizleme, Excel i sığdırılmış sayfa genişliği ve yüksekliğiyle yazdırma, Bir sayfaya çalışma sayfası yazdırma, Tüm sütunları tek sayfada yazdırma.
---

## **Giriş**

FitToPagesWide ve FitToPagesTall ayarları, e-print uygulamalarında (Microsoft Excel gibi) baskı sırasında bir e-tablonun nasıl ölçekleneceğini kontrol etmek için kullanılır. Bu ayarlar, baskı alınan çıktının yatay ve dikey olarak belirli bir sayfa sayısı içinde kalmasını sağlar. İşte her ayarın detayları:

1. FitToPagesWide: Bu ayar, baskı sonucunun kaç sayfa genişliğinde olacağını belirtir. Örneğin, FitToPagesWide 1 olarak ayarlandığında, içeriğin tek bir sayfa genişliğine sığacak şekilde ölçeklendiği anlamına gelir, sayfanın genişliği ne olursa olsun.
2. FitToPagesTall: Bu ayar, yazdırılan çıktının kaç sayfa yüksekliğinde olacağını belirler. Örneğin, FitToPagesTall'i 1 olarak ayarlamak, içeriğin tek bir sayfa yüksekliğine sığacak şekilde ölçekleneceği anlamına gelir, satır sayısı ne olursa olsun.

## **Neden FitToPagesWide ve FitToPagesTall Kullanılır**
İşte FitToPagesWide ve FitToPagesTall ayarlarını kullanmanın bazı nedenleri:
1. Yazdırılan Düzen Üzerinde Kontrol: Genişlik ve yükseklik olarak sayfa sayısını belirleyerek, yazdırılan belgenin okunabilir ve iyi organize edilmiş olmasını sağlayabilirsiniz, hiçbir sütun veya satır sayfalar arasında garip şekilde bölünmez.
2. Tutarlılık: Birden fazla sayfa veya rapor yazdırıyorsanız, bu ayarları kullanmak, tutarlı bir biçim korumanıza yardımcı olur, böylece yazdırılmış belgeleri karşılaştırmak ve analiz etmek daha kolay olur.
3. Profesyonel Sunum: İçeriği uygun şekilde ölçeklendirmek ve belirli sayfa sayısına sığdırmak, verilerinizin daha profesyonel ve düzenli görünmesini sağlar.

## **Excel'de Dosyayı Geniş ve Yüksek olarak Yazdırmak için nasıl yapılır**

Microsoft Excel'de FitToPagesWide ve FitToPagesTall ayarlarını yapmak için aşağıdaki adımları izleyin:

1. Excel çalışma kitabınızı açın ve yazdırmak istediğiniz sayfaya gidin.
2. Şerit üzerindeki Sayfa Düzeni sekmesine gidin.
3. Sayfa Kurulumu grubunda, sağ alt köşedeki küçük oka tıklayarak Sayfa Yapılandırma iletişim kutusunu açın.
4. Sayfa Yapılandırma iletişim kutusunda, Sayfa sekmesine gidin.
5. Ölçeklendirme altında "Uygun Ölçek" seçeneğini seçin ve ardından şu şekilde sayfa sayısını belirtin: Genişlik için ilk kutuya (Fit to x pages wide) kaç sayfaya sığdırmak istediğinizi girin. Yükseklik için ikinci kutuya (Fit to y pages tall) kaç sayfaya sığdırmak istediğinizi girin.
<br>
<img src="2.png" width=60% />

6. Ayarları uygulamak için Tamam'a tıklayın.

## **Aspose.Cells for JavaScript ve C++ kullanarak Excel'i sığdırılmış sayfa genişliği ve yüksekliğiyle nasıl yazdırılır**

Belirtilen çalışma sayfasında FitToPagesWide ve FitToPagesTall ayarlarını yapmak için: İlk olarak, [örnek dosya](input.xlsx) yüklenir, ardından istenen çalışma sayfası için [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) nesnesinin [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) ve [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--) özelliklerini değiştirmelisiniz. İşte JavaScript'te bir örnek:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Worksheet Fit To Pages and Save as PDF</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the number of pages to which the length of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesWide = 1;

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_net.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

Çıktı sonucu:
<br>
<img src="1.png" width=60% />

## **Aspose.Cells for JavaScript ve C++ kullanarak Çalışma sayfasını Tek Sayfa olarak nasıl yazdırılır**

Çalışma sayfasını tek sayfa olarak yazdırmak için: İlk olarak, [örnek dosya](sample.xlsx) yüklenir, ardından [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/) nesnesinin [**PdfSaveOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) özelliği ayarlanır. İşte JavaScript'te bir örnek:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>One Page Per Sheet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            // Save the workbook to PDF format and provide download link
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Çıktı sonucu:
<br>
<img src="3.png" width=60% />

## **Aspose.Cells for JavaScript kullanarak Çalışma Sayfasındaki Tüm Sütunları Bir Sayfada Nasıl Yazdırılır**

Çalışma sayfasındaki tüm sütunları bir sayfada yazdırmak için: Öncelikle, [örnek dosyayı](sample.xlsx) yükleyin ve ardından [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/) nesnesinin [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) özelliğini ayarlamanız gerekir. İşte JavaScript'te bir örnek:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>All Columns In One Page Per Sheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PdfSaveOptions and set allColumnsInOnePagePerSheet property
            const options = new AsposeCells.PdfSaveOptions();
            options.allColumnsInOnePagePerSheet = true;

            // Save the workbook to PDF format with the options
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AllColumnsInOnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Çıktı sonucu:
<br>
<img src="4.png" width=60% />
