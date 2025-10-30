---
title: Excel i Pdf, Görüntü ve diğer biçimlere dönüştürün
linktitle: Çalışma Kitabı Dönüşümleri
type: docs
weight: 65
url: /tr/javascript-cpp/convert-workbook-to-different-formats/
description: Excel dosyalarını Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML ve daha fazlasına dönüştürmek için C++ ile JavaScript kullanın.
---

{{% alert color="primary" %}}
Aspose.Cells, birçok biçim arasında dönüşümü destekler. Teknik olarak, dönüştürme, bir elektronik tabloyu bir dosya biçiminde yüklemek ve başka bir biçimde kaydetmek anlamına gelir.
{{% /alert %}}

## **Excel Çalışma Kitabını PDF'e Dönüştür**
PDF dosyaları, kuruluşlar, devlet kurumları ve bireyler arasında belge değişiminde geniş ölçüde kullanılır. Standart bir belge biçimidir ve yazılım geliştiriciler genellikle Microsoft Excel dosyalarını PDF belgelerine dönüştürmek için bir yol bulmaları istenir.

Aspose.Cells, Excel dosyalarını PDF'ye dönüştürmeyi destekler ve dönüşümde yüksek görsel sadakati korur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save As PDF Example</title>
    </head>
    <body>
        <h1>Save Excel as PDF Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the document in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

## **Excel Çalışma Kitabını JPG'e Dönüştür**
Aspose.Cells, Excel dosyalarını JPG'ye dönüştürmeyi destekler. Aşağıdaki kod örneği, çalışma kitabını JPG olarak nasıl kaydedeceğinizi gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Convert Workbook to JPG Example</title>
    </head>
    <body>
        <h1>Convert Workbook to JPG Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JPG</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Convert workbook to JPG image
            const outputData = workbook.save(SaveFormat.Jpeg);
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Image1.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JPG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed. Click the download link to get the JPG image.</p>';
        });
    </script>
</html>
```

## **Excel Çalışma Kitabını Görüntüye Dönüştür**
Aspose.Cells, Excel dosyalarını görüntüye dönüştürmeyi destekler. Aşağıdaki kod örneği, çalışma kitabını görüntü olarak nasıl kaydedeceğinizi gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Convert Workbook to Images</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to Images</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <div id="downloads"></div>
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

            document.getElementById('result').innerHTML = '<p>Converting workbook to images...</p>';
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Define desired image formats
            const formats = [
                { fmt: SaveFormat.Bmp, name: 'Image1.bmp', mime: 'image/bmp' },
                { fmt: SaveFormat.Jpeg, name: 'Image1.jpg', mime: 'image/jpeg' },
                { fmt: SaveFormat.Png, name: 'Image1.png', mime: 'image/png' },
                { fmt: SaveFormat.Emf, name: 'Image1.emf', mime: 'image/emf' },
                { fmt: SaveFormat.Gif, name: 'Image1.gif', mime: 'image/gif' }
            ];

            const downloadsDiv = document.getElementById('downloads');
            downloadsDiv.innerHTML = '';

            // Convert and create download links for each image format
            for (const f of formats) {
                const outputData = workbook.save(f.fmt);
                const blob = new Blob([outputData], { type: f.mime });
                const url = URL.createObjectURL(blob);

                const a = document.createElement('a');
                a.href = url;
                a.download = f.name;
                a.textContent = 'Download ' + f.name;
                a.style.display = 'block';
                downloadsDiv.appendChild(a);
            }

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed. Click the links below to download the images.</p>';
        });
    </script>
</html>
```

## **Excel Çalışma Kitabını XPS'ye Dönüştürme**
XPS belge formatı, her bir sayfanın düzenini ve her bir sayfanın görsel görünümünü tanımlayan yapılandırılmış XML işaretleme ve belgelerin dağıtımı, arşivleme, işleme ve yazdırma kurallarıyla birlikte renderleme kurallarından oluşur.

XPS için işaretleme dili, XAML'nin bir alt kümesi olup Windows Presentation Foundation (WPF) temel yapı taşlarını kullanarak belgelere vektör grafik öğelerini dahil etmesine izin verir. Kullanılan öğeler, yol ve diğer geometrik temel yapı taşları terimleriyle tanımlanır.

Bir XPS dosyası aslında belgeyi oluşturan dosyaları içeren Open Packaging Conventions kullanan bir Unicode ZIP arşividir. Bunlar, her sayfa için bir XML işaretleme dosyasını, metni, gömülü yazı tiplerini, rastgele görüntüleri ve 2D vektör grafikleri yanı sıra dijital hak yönetimi bilgilerini içerir. Bir XPS dosyasının içeriği, ZIP dosyalarını destekleyen bir uygulamada açılarak kolayca incelenebilir.

Aspose.Cells 6.0.0'dan itibaren Microsoft Excel'den XPS dönüşümü desteklenmektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render to XPS</title>
    </head>
    <body>
        <h1>Render Worksheet / Workbook to XPS</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkSheet" style="display: none; margin-right: 10px;">Download Sheet XPS</a>
            <a id="downloadLinkWorkbook" style="display: none;">Download Workbook XPS</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XpsSaveOptions, SheetSet } = AsposeCells;

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
            const downloadLinkSheet = document.getElementById('downloadLinkSheet');
            const downloadLinkWorkbook = document.getElementById('downloadLinkWorkbook');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read file from input
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Render the sheet to XPS
            const options = new XpsSaveOptions();
            const sheetSet = new SheetSet([sheet.index]);
            options.sheetSet = sheetSet;
            const outputDataSheet = workbook.save(SaveFormat.Xps, options);
            const blobSheet = new Blob([outputDataSheet], { type: 'application/vnd.ms-xps' });
            downloadLinkSheet.href = URL.createObjectURL(blobSheet);
            downloadLinkSheet.download = 'out_printingxps.out.xps';
            downloadLinkSheet.style.display = 'inline-block';
            downloadLinkSheet.textContent = 'Download Sheet XPS';

            // Export the whole workbook to XPS
            const outputDataWorkbook = workbook.save(SaveFormat.Xps, new XpsSaveOptions());
            const blobWorkbook = new Blob([outputDataWorkbook], { type: 'application/vnd.ms-xps' });
            downloadLinkWorkbook.href = URL.createObjectURL(blobWorkbook);
            downloadLinkWorkbook.download = 'out_whole_printingxps.out.xps';
            downloadLinkWorkbook.style.display = 'inline-block';
            downloadLinkWorkbook.textContent = 'Download Workbook XPS';

            resultDiv.innerHTML = '<p style="color: green;">XPS files generated. Use the links above to download the sheet and workbook XPS files.</p>';
        });
    </script>
</html>
```

## **Excel'i Ods, Sxc ve Fods (OpenOffice / LibreOffice Calc) formatlarına dönüştür**
Aspose.Cells, Excel dosyalarını Ods, Sxc ve Fods dosyalarına dönüştürmeyi destekler. Aşağıdaki kod örneği, [şablon](book1.xlsx) dosyasını Ods, Sxc ve Fods dosyasına nasıl dönüştüreceğinizi gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save As Multiple Formats Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Save As ODS / SXC / FODS Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert and Download</button>
        <div style="margin-top: 10px;">
            <a id="downloadLinkOds" style="display: none; margin-right: 10px;">Download ODS</a>
            <a id="downloadLinkSxc" style="display: none; margin-right: 10px;">Download SXC</a>
            <a id="downloadLinkFods" style="display: none; margin-right: 10px;">Download FODS</a>
        </div>
        <div id="result" style="margin-top: 10px;"></div>

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
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as ods file
            const outputOds = workbook.save(SaveFormat.Ods);
            const blobOds = new Blob([outputOds]);
            const downloadLinkOds = document.getElementById('downloadLinkOds');
            downloadLinkOds.href = URL.createObjectURL(blobOds);
            downloadLinkOds.download = 'Out.ods';
            downloadLinkOds.style.display = 'inline-block';
            downloadLinkOds.textContent = 'Download ODS File';

            // Save as sxc file
            const outputSxc = workbook.save(SaveFormat.Sxc);
            const blobSxc = new Blob([outputSxc]);
            const downloadLinkSxc = document.getElementById('downloadLinkSxc');
            downloadLinkSxc.href = URL.createObjectURL(blobSxc);
            downloadLinkSxc.download = 'Out.sxc';
            downloadLinkSxc.style.display = 'inline-block';
            downloadLinkSxc.textContent = 'Download SXC File';

            // Save as fods file
            const outputFods = workbook.save(SaveFormat.Fods);
            const blobFods = new Blob([outputFods]);
            const downloadLinkFods = document.getElementById('downloadLinkFods');
            downloadLinkFods.href = URL.createObjectURL(blobFods);
            downloadLinkFods.download = 'Out.fods';
            downloadLinkFods.style.display = 'inline-block';
            downloadLinkFods.textContent = 'Download FODS File';

            result.innerHTML = '<p style="color: green;">Files converted successfully! Click the download links to get the converted files.</p>';
        });
    </script>
</html>
```

## **Excel Çalışma Kitabını MHTML Dosyalarına Dönüştürme**
MHTML, normal HTML'yi dış kaynaklarla (genellikle bağlantılı olarak bulunan, resimler, animasyonlar, sesler vb.) tek bir dosyaya birleştirir. Bunlar, .mht dosya uzantılı e-postalar için kullanılır.

Aspose.Cells, MHTML dosyalarını okuma ve yazma desteği sağlamaktadır.

Aşağıdaki kod örneği, bir çalışma kitabını MHTML dosyası olarak kaydetmenin nasıl yapıldığını göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to MHT Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            window.asposeCellsReady = true;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            if (!window.asposeCellsReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a workbook and open the uploaded XLSX file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify the HTML Saving Options
            const sv = new HtmlSaveOptions(SaveFormat.MHtml);

            // Save the MHT file (returns binary data)
            const outputData = workbook.save(SaveFormat.MHtml, sv);

            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `${file.name}.out.mht`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHT File';

            resultDiv.innerHTML = '<p style="color: green;">MHT file generated successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Excel Çalışma Kitabını HTML'ye Dönüştürme**
Aspose.Cells API, elektronik tabloyu HTML formatına aktarmayı destekler. Bu amaçla, Aspose.Cells [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions) sınıfını kullanarak çıktı HTML'sinin çeşitli yönlerini kontrol etme esnekliği sağlar.

Aşağıdaki kod örneği, bir çalışma kitabını HTML dosyası olarak kaydetme yöntemini gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Converting Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
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

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in HTML format
            const outputData = workbook.save(SaveFormat.Html);

            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToHTMLFiles_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

## **HTML için Görüntü Tercihlerini Ayarlama**
8.0.2 sürümünden itibaren, Aspose.Cells [**imageOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#imageOptions--) sınıfı için [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions) sınıfını açtı ve geliştiricilerin, elektronik tabloları HTML formatına kaydederken resim tercihini belirtmelerine olanak tanıdı.

Uygulanabilecek bazı görüntü ayarlarının detayları aşağıda verilmiştir.

- [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/): Görüntü türünü belirtir. Lütfen not edin, tüm şekiller, grafikler de dahil olmak üzere çıktı HTML'de resim olarak oluşturulur.
- [**quality**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#quality--): JPG olarak belirtildiğinde, [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/) parametresi kullanıldığında görüntü kalitesini 0 ile 100 arasında belirler.
- [**verticalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#verticalResolution--): Görselin dikey düzeyde inç başına nokta cinsinden çözünürlüğünü alır veya ayarlar.
- [**horizontalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#horizontalResolution--): Görselin yatay düzeyde inç başına nokta cinsinden çözünürlüğünü alır veya ayarlar.
- [**TiffCompression**](https://reference.aspose.com/cells/javascript-cpp/tiffcompression/): [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/) parametresi TIFF olarak belirtildiğinde, görüntülerin sıkıştırma türünü alır veya ayarlar.
- [**transparent**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#transparent--): Görüntü biçimi Png olarak belirtildiğinde bir görüntünün arka planının saydam olup olmayacağını belirtir.

## **Excel Çalışma Kitabını Markdown'a Dönüştür**
Aspose.Cells API, elektronik tabloları Markdown formatına da dışa aktarma desteği sağlar. Aktif sayfayı Markdown'a aktarmak için [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-) metodunun ikinci parametresi olarak [**SaveFormat.Markdown**](https://reference.aspose.com/cells/javascript-cpp/saveformat) kullanın. Ayrıca, sayfayı Markdown'a dışa aktarma için ek ayarlar belirlemek amacıyla [**MarkdownSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/markdownsaveoptions) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, [**SaveFormat.Markdown**](https://reference.aspose.com/cells/javascript-cpp/saveformat) enum üyesi kullanılarak aktif sayfayı Markdown'e dışa aktarmayı göstermektedir. Lütfen kod tarafından oluşturulan [çıktı Markdown dosyasını](md_sample.txt) inceleyin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as Markdown</title>
    </head>
    <body>
        <h1>Save Excel as Markdown Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to Markdown</button>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving as Markdown
            const outputData = workbook.save(SaveFormat.Markdown);
            const blob = new Blob([outputData], { type: 'text/markdown' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.md';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Markdown File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the Markdown file.</p>';
        });
    </script>
</html>
```

## **Excel Çalışma Kitabını JSON'a Dönüştür**
Aspose.Cells, bir çalışma kitabını Json (JavaScript Nesne Notasyonu) dosyasına dönüştürmeyi destekler.

Aşağıdaki kod örneği, [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat) enum üyesi kullanılarak aktif sayfayı Json'a dışa aktarmayı göstermektedir. Lütfen kodu, [kaynak dosyasını](Book1.xlsx) Json çıktısına dönüştürmek için kullanın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Convert the workbook to JSON format
            const outputData = workbook.save(SaveFormat.Json);

            // Create a downloadable blob for the JSON result
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **Excel'i XML'e Dönüştür**
Aspose.Cells, bir çalışma kitabını Excel 2003 Elektronik Tablo XML ve düz XML veriye dönüştürmeyi destekler.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to XML Examples</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <br/><br/>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Spreadsheet XML</a>
        <a id="downloadLink2" style="display: none;">Download Data XML</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XmlSaveOptions } = AsposeCells;

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

            // Save as Excel 2003 Spreadsheet XML
            const spreadsheetData = workbook.save(SaveFormat.Excel2003Xml);
            const blob1 = new Blob([spreadsheetData]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Spreadsheet.xml';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Spreadsheet XML';

            // Save as plain XML data with XmlSaveOptions
            const xmlSaveOptions = new XmlSaveOptions();
            const dataXml = workbook.save(SaveFormat.SpreadsheetML, xmlSaveOptions);
            const blob2 = new Blob([dataXml]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'data.xml';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Data XML';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Use the links above to download the generated XML files.</p>';
        });
    </script>
</html>
```

## **Excel Çalışma Kitabını TIFF'e Dönüştür**
Aspose.Cells, bir çalışma kitabını TIFF dosyasına dönüştürmeyi destekler.

Aşağıdaki kod parçası, Excel'i TIFF'e dönüştürmeyi göstermektedir:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to TIFF</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to TIFF format
            const outputData = workbook.save(SaveFormat.Tiff);
            const blob = new Blob([outputData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF File';

            resultDiv.innerHTML = '<p style="color: green;">File converted to TIFF successfully! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```

## **Excel Çalışma Kitabını DOCX'e Dönüştür**
Aspose.Cells API, elektronik tabloları DOCX formatına dönüştürme desteği sağlar. Çalışma kitabını DOCX'e aktarmak için [**SaveFormat.Docx**](https://reference.aspose.com/cells/javascript-cpp/saveformat) parametresi ile [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-) metodunu kullanın. Ayrıca, sayfayı DOCX'e aktarmak için ek ayarları belirlemek amacıyla [**DocxSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/docxsaveoptions) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, [**SaveFormat.Docx**](https://reference.aspose.com/cells/javascript-cpp/saveformat) enum üyesi kullanılarak aktif sayfayı DOCX'e aktarmayı göstermektedir. Lütfen kod tarafından oluşturulan [çıktı DOCX dosyasını](Book1.docx) inceleyin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as DOCX (Markdown/Docx conversion per original code)
            const outputData = workbook.save(SaveFormat.Docx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.docx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Docx File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the DOCX file.</p>';
        });
    </script>
</html>
```

## **Excel Çalışma Kitabını PPTX'e Dönüştür**
Aspose.Cells API, elektronik tabloları PPTX formatına dönüştürme desteği sağlar. Çalışma kitabını PPTX'e aktarmak için [**SaveFormat.Pptx**](https://reference.aspose.com/cells/javascript-cpp/saveformat) parametresi ile [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-) metodunu kullanın. Ayrıca, sayfayı PPTX'e aktarmak için [**PptxSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pptxsaveoptions) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, [**SaveFormat.Pptx**](https://reference.aspose.com/cells/javascript-cpp/saveformat) enum üyesi kullanılarak aktif sayfayı PPTX'e aktarmayı göstermektedir. Lütfen kod tarafından oluşturulan [çıktı PPTX dosyasını](Book1.pptx) inceleyin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save as PPTX Example</title>
    </head>
    <body>
        <h1>Save Excel as PPTX Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PPTX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Save as PPTX
            const outputData = workbook.save(SaveFormat.Pptx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const baseName = file.name.replace(/\.[^/.]+$/, "");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.pptx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted PPTX File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the PPTX file.</p>';
        });
    </script>
</html>
```

## **Excel Çalışma Kitabını EPUB'a dönüştür**
Aspose.Cells API, elektronik tabloları EPUB formatına dönüştürme desteği sağlar. Çalışma kitabını EPUB'a aktarmak için [**SaveFormat.Epub**](https://reference.aspose.com/cells/javascript-cpp/saveformat) parametresi ile [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-) metodunu kullanın. Ayrıca, sayfayı EPUB'a aktarmak için [**EBookSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/ebooksaveoptions) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, aktif sayfayı EPUB'a aktarmayı [**SaveFormat.Epub**](https://reference.aspose.com/cells/javascript-cpp/saveformat) enum üyesi kullanarak göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Converting To EPUB Files</title>
    </head>
    <body>
        <h1>Converting To EPUB Files</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to EPUB</button>
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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in EPUB format
            const outputData = workbook.save(SaveFormat.Epub);

            const blob = new Blob([outputData], { type: 'application/epub+zip' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToEPUBFiles_out.epub';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download EPUB File';

            result.innerHTML = '<p style="color: green;">File converted to EPUB successfully! Click the download link to get the EPUB file.</p>';
        });
    </script>
</html>
```

## **Excel Çalışma Dosyasını AZW3'e dönüştür**
Aspose.Cells API, elektronik tabloları AZW3 formatına dönüştürmeyi destekler. Çalışma kitabını AZW3'e aktarmak için [**SaveFormat.Azw3**](https://reference.aspose.com/cells/javascript-cpp/saveformat) parametresi ile [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-) metodunu kullanın. Ayrıca, sayfayı AZW3'e aktarmak için [**EBookSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/ebooksaveoptions) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, aktif sayfayı AZW3'e [**SaveFormat.Azw3**](https://reference.aspose.com/cells/javascript-cpp/saveformat) enum üyesi kullanarak aktarmayı göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Convert to AZW3 Example</title>
    </head>
    <body>
        <h1>Convert Excel to AZW3 (EPUB) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to AZW3</button>
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

            // Load your sample excel file in a workbook object
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in AZW3 format
            const outputData = wb.save(SaveFormat.Azw3);
            const blob = new Blob([outputData]);

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToEPUBFiles_out.azw3';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download AZW3 File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the AZW3 file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [XLSB Revizyonunu XLSM'ye Dönüştür](/cells/tr/javascript-cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/tr/javascript-cpp/convert-excel-to-html/)
- [Görüntü](/cells/tr/javascript-cpp/convert-excel-to-image/)
- [Json](/cells/tr/javascript-cpp/convert-workbook-to-json/)
- [Excel çalışma kitabını Ods, Sxc ve Fods (OpenOffice / LibreOffice calc) formatlarına dönüştür.](/cells/tr/javascript-cpp/convert-excel-to-ods/)
- [Pdf](/cells/tr/javascript-cpp/convert-excel-workbook-to-pdf/)
- [Excel'i CSV, TSV ve Txt'e dönüştür](/cells/tr/javascript-cpp/convert-excel-to-csv-tsv-and-txt/)
- [Belge Dönüşüm İlerlemesini İzle](/cells/tr/javascript-cpp/track-document-conversion-progress/)
- [CSV, TSV ve TXT'yi Excel'e Dönüştür](/cells/tr/javascript-cpp/convert-csv-tsv-and-txt-to-excel/)
