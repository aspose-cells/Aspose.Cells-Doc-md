---
title: PDF ile JavaScript aracılığıyla C++
linktitle: Pdf
type: docs
weight: 220
url: /tr/javascript-cpp/convert-excel-to-pdf/
description: Aspose.Cells for JavaScript ile C++ kullanarak Excel Çalışma Kitabını PDF e nasıl dönüştüreceğinizi öğrenin. 
---

{{% alert color="primary" %}}
Aspose.Cells, Excel Çalışma Kitabını PDF'ye dönüştürmeyi destekler. Bu örnekte, bir Excel Çalışma Kitabının tam dönüşümünü göreceğiz.
{{% /alert %}}

## **Excel Çalışma Kitabını PDF'e Dönüştürme**

PDF dosyaları, kuruluşlar, devlet kurumları ve bireyler arasında belge değişiminde geniş ölçüde kullanılır. Standart bir belge biçimidir ve yazılım geliştiriciler genellikle Microsoft Excel dosyalarını PDF belgelerine dönüştürmek için bir yol bulmaları istenir.

Aspose.Cells, Excel dosyalarını PDF'ye dönüştürmeyi destekler ve dönüşümde yüksek görsel sadakati korur.

{{% alert color="primary" %}}
Aspose.Cells for JavaScript, C++ aracılığıyla, çıktı belgelerinde API ve Sürüm Numarası hakkında bilgileri doğrudan yazar. Örneğin, Belgeyi PDF'ye dönüştürürken, Aspose.Cells for JavaScript, **PDF Üretici** alanını 'Aspose.Cells v23.2' gibi bir değerle doldurur.

Lütfen bu bilgileri çıktı Belgelerinde [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#producer--) özelliği ile değiştirebileceğinizi unutmayın.
{{% /alert %}}

### **Doğrudan Dönüşüm**

Aspose.Cells for JavaScript, C++ aracılığıyla, elektronik tabloları PDF'ye dönüştürmeyi diğer yazılım bağımsız olarak destekler. Basitçe bir Excel dosyasını [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) yöntemiyle PDF olarak kaydedin. [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) yöntemi, yerel Excel dosyalarını PDF formatına dönüştüren [**SaveFormat.Pdf**](https://reference.aspose.com/cells/javascript-cpp/saveformat) enum üyesini sağlar.

Doğrudan Excel elektronik tablolarını PDF biçimine dönüştürmek için aşağıdaki adımları izleyin:

1. Boş kurucuyu çağırarak [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının nesnesini örnekleyin.
1. Varolan bir şablon dosyasını açabilir/yükleyebilir veya çalışma kitabını sıfırdan oluşturuyorsanız bu adımı atlayabilirsiniz.
3. Aspose.Cells'in API'lerini kullanarak elektronik tabloda herhangi bir işlem yapın (giriş verileri, biçimlendirme uygulama, formüller belirleme, resimler veya diğer çizim nesneleri ekleme vb.).
1. Elektronik tablo kodu tamamlandığında, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) yöntemini çağırarak elektronik tabloyu kaydedin.

Dosya biçimi PDF olmalı, bu nedenle nihai PDF belgesini oluşturmak için *Pdf* (önceden tanımlanmış bir değer) olarak [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) sınıfının numaralandırmasından seçim yapın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the document in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to PDF completed! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **Gelişmiş Dönüşüm**

Dönüşüm için farklı özellikleri ayarlamak için [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) sınıfını kullanabilirsiniz. [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) sınıfının farklı özelliklerini ayarlamak, çıktı PDF'nin yazdırma, font, güvenlik ve sıkıştırma ayarları üzerinde kontrol sahibi olmanızı sağlar. 

En önemli özellik [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--), PDF standartları uyumluluk seviyesini ayarlamanıza olanak tanır. Şu anda PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab ve PDF/A-3u formatlarına kaydedebilirsiniz. PDF/A formatı ile, çıktı dosyasının boyutu düzenli PDF dosyasının boyutundan daha büyüktür.

#### **Çalışma Kitabını PDF/A Uyumlu Dosyalara Kaydetme**

Aşağıdaki kod parçacığı, Excel dosyalarını PDF/A uyumlu PDF biçimine kaydetmek için [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) sınıfının nasıl kullanılacağını göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create PDF/A from Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCompliance } = AsposeCells;

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
            // Instantiate new workbook
            const workbook = new Workbook();

            // Insert a value into the A1 cell in the first worksheet
            workbook.worksheets.get(0).cells.get(0, 0).value = "Testing PDF/A";

            // Define PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set the compliance type
            pdfSaveOptions.compliance = PdfCompliance.PdfA1b;

            // Save the file to PDF with options
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF/A File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF/A created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Lütfen dikkat edin, [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) özelliği, Aspose.Cells for JavaScript, C++ sürümü 5.3.0 ile birlikte eklmiştir.
{{% /alert %}}

#### **PDF Oluşturma Saatini Ayarlayın**

[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) sınıfı ile PDF oluşturma saatinizi alabilir veya ayarlayabilirsiniz. Aşağıdaki kod, PDF dosyasının oluşturma zamanını belirlemek için [**PdfSaveOptions.createdTime**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#createdTime--) özelliğin kullanımını göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const options = new PdfSaveOptions();
            options.createdTime = new Date();

            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **İçerik Erişilebilirlik Kopyalama seçeneğini Ayarlayın**

[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) sınıfı ile dönüştürülen PDF'de içerik erişimini kontrol etmek için PDF [**PdfSecurityOptions.accessibilityExtractContent**](https://reference.aspose.com/cells/javascript-cpp/pdfsecurityoptions/#accessibilityExtractContent--) seçeneğini alabilir veya ayarlayabilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Convert to PDF with Security Options</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Security Options</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfSecurityOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOpt = new PdfSaveOptions();

            // Create an instance of PdfSecurityOptions
            const securityOptions = new PdfSecurityOptions();

            // Set AccessibilityExtractContent to false (converted from setAccessibilityExtractContent(false))
            securityOptions.accessibilityExtractContent = false;

            // Set the security option in the PdfSaveOptions (converted from setSecurityOptions)
            pdfSaveOpt.securityOptions = securityOptions;

            // Save the workbook to PDF format while passing the PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOpt);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outFile.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

#### **Özel özellikleri PDF'ye aktar**

[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) sınıfı ile kaynak elektronik tablodaki özel özellikleri PDF'ye aktarabilirsiniz. Özellikleri nasıl aktarılacağını belirtmek için [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/javascript-cpp/pdfcustompropertiesexport/) numaralama sağlanmaktadır. Bu özellikler, aşağıdaki resimde gösterildiği gibi Adobe Acrobat Reader'da Dosya'ya tıklayarak ardından özellikler seçeneğini tıklayarak görüntülenebilir. Şablon dosyası "sourceWithCustProps.xlsx" test etmek için [buradan](sourceWithCustProps.xlsx) indirilebilir ve çıktı PDF dosyası "outSourceWithCustProps" analiz için [buradan](outSourceWithCustProps.pdf) temin edilebilir.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Custom Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCustomPropertiesExport } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
            pdfSaveOptions.customPropertiesExport = PdfCustomPropertiesExport.Standard;

            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourceWithCustProps.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **Dönüşüm Özellikleri**

Her yeni sürümle dönüşüm özelliklerini geliştirmeye çalışıyoruz. Aspose.Cell'in Excel'den PDF'ye dönüştürme hala birkaç kısıtlamaya sahiptir. HaritaÇizelgesi, PDF biçimine dönüştürülürken desteklenmez. Ayrıca, bazı çizim nesneleri iyi desteklenmez.

Aşağıdaki tablo, Aspose.Cells kullanarak PDF'ye dışa aktarırken tamamen veya kısmen desteklenen tüm özellikleri listeleyen bir tablodur. Bu tablo son değildir ve tüm elektronik tablo özniteliklerini kapsamaz, ancak dışa aktarmak için tamamen veya kısmen desteklenmeyen özellikleri tanımlar.

|**Belge Öğesi**|**Özellik**|**Desteklenen**|**Notlar**|
| :- | :- | :- | :- |
|Hizalama| |Evet| |
|Arka plan Ayarları| |Evet| |
|Kenarlık|Renk|Evet| |
|Kenarlık|Çizgi stili|Evet| |
|Kenarlık|Çizgi genişliği|Evet| |
|Hücre Verisi| |Evet| |
|Yorumlar| |Evet| |
|Koşullu Biçimlendirme| |Evet| |
|Döküman Özellikleri| |Evet| |
|Çizim Nesneleri| |Kısmen|Çizim nesneleri için gölge ve 3-B efektleri iyi desteklenmez; WordArt ve SmartArt kısmen desteklenir.|
|Yazı Tipi|Boyut|Evet| |
|Yazı Tipi|Rengi|Evet| |
|Yazı Tipi|Stili|Evet| |
|Yazı Tipi|Altı çizili|Evet| |
|Yazı Tipi|Efektleri|Evet||
|Resimler| |Evet| |
|Hyperlink| |Evet| |
|Grafikler| |Kısmen|Harita Grafikleri desteklenmiyor.|
|Birleştirilmiş Hücreler| |Evet| |
|Sayfa Sonu| |Evet| |
|Sayfa Ayarı|Üstbilgi/Altbilgi|Evet| |
|Sayfa Ayarı|Kenar Boşlukları|Evet| |
|Sayfa Ayarı|Sayfa Yönü|Evet| |
|Sayfa Ayarı|Sayfa Boyutu|Evet| |
|Sayfa Ayarı|Yazdırma Alanı|Evet| |
|Sayfa Ayarı|Yazdırma Başlıkları|Evet| |
|Sayfa Ayarı|Ölçekleme|Evet| |
|Satır Yüksekliği/Sütun Genişliği| |Evet| |
|RTL (Sağdan Sola) Dil| |Evet| |

{{% alert color="primary" %}}
Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.
{{% /alert %}}

## **Gelişmiş Konular**
- [Adlandırılmış Yer İmleriyle PDF Yer İmi Ekleyin](/cells/tr/javascript-cpp/add-pdf-bookmarks-with-named-destinations/)
- [Çıktı PDF'inde Boş Sayfa Oluşmasını Engelle](/cells/tr/javascript-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [PDF'ye Kaydederken Yalnızca Belirli Unicode Karakterlerin Yazı Tipini Değiştirme](/cells/tr/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [XLSX Dosyasını PDF Biçimine Dönüştür](/cells/tr/javascript-cpp/convert-xlsx-file-to-pdf-format/)
- [PDFA-1a uyumlu PDF biçimine Excel dosyasını dönüştür](/cells/tr/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Resim veya Grafiklerle XLS Dosyasını PDF Biçimine Dönüştür](/cells/tr/javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Grafik Tablosu için PdfBookmarkEntry Oluştur](/cells/tr/javascript-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır](/cells/tr/javascript-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [DrawObjectEventHandler sınıfını kullanarak PDF'ye dönüştürürken DrawObject ve Sınırlı Alın](/cells/tr/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Excel Dosyasını PDF'e Dönüştürürken Yazı Tipi Yedeği İçin Uyarıları Al](/cells/tr/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Excel'den PDF'e Dönüştürme Sırasında Hataları Yoksay](/cells/tr/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Oluşturulan Sayfa Sayısını Sınırla - Excel'den PDF'e Dönüştürme](/cells/tr/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDF'ye kaydederken yorumları yazdır](/cells/tr/javascript-cpp/print-comments-while-saving-to-pdf/)
- [Excel'i PDF'e dönüştürürken Office Eklentilerini renderla](/cells/tr/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Excel'den PDF'ye Dönüşümde Her Excel Çalışsayarı İçin Bir PDF Sayfası Oluştur](/cells/tr/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Aspose.Cells ile çıktı PDF'inde Unicode Ek Karakterlerini renderla](/cells/tr/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Eklenti Görüntülerini Yeniden Örnekle](/cells/tr/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Her Çalışsayarı Farklı Bir PDF Dosyasına Kaydet](/cells/tr/javascript-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Excel'i Standart veya Minimum Boyutta PDF olarak kaydet](/cells/tr/javascript-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Belirtilen Çalışsayfalarını PDF olarak kaydet](/cells/tr/javascript-cpp/save-specified-worksheets-to-pdf/)
- [Güvenli PDF Belgeleri](/cells/tr/javascript-cpp/secure-pdf-documents/)
- [Çıktı PDF ve görüntülerde metin geçişini belirle](/cells/tr/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
