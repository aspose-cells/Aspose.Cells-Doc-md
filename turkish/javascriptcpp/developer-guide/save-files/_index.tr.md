---
title: JavaScript ile C++ kullanarak Dosya Kaydetmenin Farklı Yolları
linktitle: Dosyaları Kaydet
type: docs
weight: 40
url: /tr/javascript-cpp/different-ways-to-save-files/
description: Aspose.Cells for JavaScript C++ ile çeşitli formatlarda dosya kaydedebilir, bunlar arasında PDF, HTML, DOCX, PPTX, JSON ve MHTML bulunur.
keywords: Aspose.Cells, JavaScript kullanarak Excel i PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML ve daha fazlasına kaydeder.
---

{{% alert color="primary" %}}

Aspose.Cells, dosyalar oluşturmayı ve kaydetmeyi mümkün kılar. Bu makalede dosyaların kaydedilebileceği çeşitli yollar açıklanmaktadır.

{{% /alert %}}

## **Dosyaları Kaydetmenin Farklı Yolları**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir sınıf sağlar ve Excel dosyalarıyla çalışmak için gerekli özellikleri ve yöntemleri içerir. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyalarını kaydetmek için kullanılan [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) adlı yöntemi sağlar. [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) yöntemi, farklı yollarla dosya kaydetmek için çeşitli aşırı yükleme seçeneklerine sahiptir.

Dosyanın kaydedildiği dosya biçimi, [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) enumerasyonu tarafından belirlenir

|**Dosya Biçimi Türleri**|**Açıklama**|
| :- | :- |
|CSV|CSV dosyasını temsil eder|
|Excel97To2003|Excel 97 - 2003 dosyasını temsil eder|
|Xlsx|Excel 2007 XLSX dosyasını temsil eder|
|Xlsm|Excel 2007 XLSM dosyasını temsil eder|
|Xltx|Excel 2007 şablonu XLTX dosyasını temsil eder|
|Xltm|Excel 2007 makro etkin XLTM dosyasını temsil eder|
|Xlsb|Excel 2007 ikili XLSB dosyasını temsil eder|
|SpreadsheetML|Yaygın Çalışma Kitabı XML dosyasını temsil eder|
|TSV|Tab boşluklu değerler dosyasını temsil eder|
|TabDelimited|Tab Delimited metin dosyasını temsil eder|
|ODS|ODS dosyasını temsil eder|
|Html|HTML dosya(lar)ını temsil eder|
|MHtml|MHTML dosya(lar)ını temsil eder|
|Pdf|PDF dosyasını temsil eder|
|XPS|XPS belgesini temsil eder|
|TIFF|Etiketli Görüntü Dosya Biçimi (TIFF)ni temsil eder|

## **Farklı Biçimlere Dosya Kaydetme Yöntemleri**

Dosya kaydetmek için bir depolama konumuna, dosya adını (depolama yolu dahil) ve istenen dosya biçimini ([**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) sıralamasından) çağırdığınızda [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) nesnesinin [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) metodunu kullanarak belirtin.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Save Formats Example</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLinks a { display: block; margin: 6px 0; }
        </style>
    </head>
    <body>
        <h1>Aspose.Cells Save Formats Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.ods" />
        <button id="runExample">Save in Multiple Formats</button>
        <div id="result"></div>
        <div id="downloadLinks"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XlsSaveOptions } = AsposeCells;

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
            const downloadLinks = document.getElementById('downloadLinks');
            downloadLinks.innerHTML = '';
            result.innerHTML = '';

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare format list to save
            const formats = [
                { format: SaveFormat.Excel97To2003, name: 'output.xls', options: new XlsSaveOptions() },
                { format: SaveFormat.Xlsx, name: 'output.xlsx' },
                { format: SaveFormat.Xlsb, name: 'output.xlsb' },
                { format: SaveFormat.Ods, name: 'output.ods' },
                { format: SaveFormat.Pdf, name: 'output.pdf' },
                { format: SaveFormat.Html, name: 'output.html' },
                { format: SaveFormat.SpreadsheetML, name: 'output.xml' }
            ];

            // Save in each format and create download link
            for (let i = 0; i < formats.length; i++) {
                const f = formats[i];
                let outputData;
                if (f.options) {
                    outputData = workbook.save(f.format, f.options);
                } else {
                    outputData = workbook.save(f.format);
                }
                const blob = new Blob([outputData]);
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = f.name;
                link.textContent = 'Download ' + f.name;
                downloadLinks.appendChild(link);
            }

            result.innerHTML = '<p style="color: green;">Files saved in memory. Click the download links below to download each format.</p>';
        });
    </script>
</html>
```

## **Çalışma Kitabını Pdf'ye Nasıl Kaydedilir**
Taşınabilir Belge Formatı (PDF), Adobe tarafından 1990'larda oluşturulan bir belge türüdür. Bu dosya biçiminin amacı, belgelerin ve diğer referans materyallerinin, uygulama yazılımına, donanımına ve İşletim Sistemine bağımsız bir formatta temsili için bir standart getirmektir. PDF dosya biçimi, metin, resimler, bağlantılar, form alanları, zengin medya, dijital imzalar, ekler, meta veriler, Coğrafi konum özellikleri ve 3D nesneler gibi bilgileri içerebilir ve bunlar kaynak belgeye ait olabilir.

Aşağıdaki kod, çalışma kitabını Aspose.Cells kullanarak PDF dosyası olarak kaydetmenin nasıl yapılacağını gösterir:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Save to PDF and PDF/A-1a</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none; margin-right: 10px;"></a>
            <a id="downloadLink2" style="display: none;"></a>
        </div>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet and set value to A1
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");
            cell.value = "Hello World!";

            // Save as PDF (first file)
            const outputData1 = workbook.save(SaveFormat.Pdf);
            const blob1 = new Blob([outputData1], { type: 'application/pdf' });
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'pdf1.pdf';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download pdf1.pdf';

            // Save as PDF with PDF/A-1a compliance
            const saveOptions = new PdfSaveOptions();
            saveOptions.compliance = PdfCompliance.PdfA1a;

            const outputData2 = workbook.save(SaveFormat.Pdf, saveOptions);
            const blob2 = new Blob([outputData2], { type: 'application/pdf' });
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'pdfa1a.pdf';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download pdfa1a.pdf';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF files generated successfully. Use the download links above.</p>';
        });
    </script>
</html>
```

## **Çalışma Kitabını Metin veya CSV Formatına Nasıl Kaydedilir**

Bazen, birden fazla çalışma sayfası olan bir çalışma kitabını metin formatına dönüştürmek veya kaydetmek isteyebilirsiniz. Metin formatları (örneğin TXT, TabDelim, CSV, vb.) için, varsayılan olarak hem Microsoft Excel hem de Aspose.Cells sadece etkin çalışma sayfasının içeriğini kaydeder.

Aşağıdaki kod örneği, tüm çalışma kitabını metin biçimine kaydetmenin nasıl yapılacağını açıklar. Kaynak çalışma kitabını yükleyin; bu, herhangi bir Microsoft Excel veya OpenOffice elektronik tablosu dosyası (XLS, XLSX, XLSM, XLSB, ODS ve diğerleri) olabilir ve herhangi sayıda çalışma sayfası içerebilir.

Kod çalıştırıldığında, çalışma kitabındaki tüm sayfaların verilerini TXT formatına dönüştürür.

Aynı örneği değiştirerek dosyanızı CSV'ye kaydedebilirsiniz. Varsayılan olarak, [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#separator--) virgüldür, bu yüzden CSV formatında kaydederken ayırıcı belirtmeyin. Lütfen dikkat: Eğer değerlendirme sürümünü kullanıyorsanız ve [**TxtSaveOptions.exportAllSheets**](https://reference.aspose.com/cells/javascript-cpp/txtsaveoptions/#exportAllSheets--) özelliği doğru olsa bile, program yalnızca bir çalışma sayfası dışa aktarır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Workbook to Txt</title>
    </head>
    <body>
        <h1>Export Workbook to Txt Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Export to TXT</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtSaveOptions } = AsposeCells;

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

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Text save options. You can use any type of separator
            const opts = new TxtSaveOptions();
            opts.separator = '\t';
            opts.exportAllSheets = true;

            // Save entire workbook data into file (Tab delimited)
            const outputData = workbook.save(SaveFormat.TabDelimited, opts);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.txt';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Text File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook exported to TXT successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Özel Ayraçlı Metin Dosyalarına Nasıl Kaydedilir**

Metin dosyaları, biçimlendirme olmadan elektronik tablo verisi içerir. Dosya, verileri arasında özelleştirilmiş sınıflandırıcılara sahip bir düz metin dosyası türündedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to CSV (with custom separator)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, TxtSaveOptions } = AsposeCells;

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

            // Create a Workbook object and open the file from the uploaded data
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate Text File's Save Options
            const options = new TxtSaveOptions();

            // Specify the separator
            options.separator = ";";

            // Save the file with the options (returns file data)
            const outputData = wb.save(options);

            const blob = new Blob([outputData], { type: 'text/csv' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the CSV file.</p>';
        });
    </script>
</html>
```

## **Bir Akışa Dosya Nasıl Kaydedilir**

Dosyaları akışa kaydetmek için bir *MemoryStream* veya *FileStream* nesnesi oluşturun ve dosyayı bu akış nesnesine [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) nesnesinin [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) yöntemi ile kaydedin. [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) topluluğu kullanarak istediğiniz dosya biçimini belirtin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Load the workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook to a binary (xlsx) and provide it as a download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Excel Dosyasını Html ve Mht Dosyalarına Nasıl Kaydedilir**
Aspose.Cells, bir Excel dosyasını, JSON, CSV veya Aspose.Cells tarafından .html ve .mht dosyaları olarak yüklenebilecek diğer dosyaları kolaylıkla kaydedebilir.
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells MHTML Save Example</title>
    </head>
    <body>
        <h1>Save Workbook to MHTML Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to MHTML format
            const outputData = workbook.save(SaveFormat.MHtml);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.mht';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook saved to MHTML format successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **Excel Dosyasını OpenOffice (ODS, SXC, FODS, OTS) Dosyalarına Nasıl Kaydedilir**
Dosyaları Açık Ofis formatında kaydedebiliriz: ODS, SXC, FODS, OTS vb.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Convert to ODS/SXC/FODS</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert and Save</button>
        <div>
            <a id="downloadOds" style="display: none; margin-right: 10px;">Download ODS File</a>
            <a id="downloadSxc" style="display: none; margin-right: 10px;">Download SXC File</a>
            <a id="downloadFods" style="display: none;">Download FODS File</a>
        </div>
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

            // Save as ODS
            const odsData = workbook.save(SaveFormat.Ods);
            const odsBlob = new Blob([odsData]);
            const downloadOds = document.getElementById('downloadOds');
            downloadOds.href = URL.createObjectURL(odsBlob);
            downloadOds.download = 'Out.ods';
            downloadOds.style.display = 'inline-block';
            downloadOds.textContent = 'Download ODS File';

            // Save as SXC
            const sxcData = workbook.save(SaveFormat.Sxc);
            const sxcBlob = new Blob([sxcData]);
            const downloadSxc = document.getElementById('downloadSxc');
            downloadSxc.href = URL.createObjectURL(sxcBlob);
            downloadSxc.download = 'Out.sxc';
            downloadSxc.style.display = 'inline-block';
            downloadSxc.textContent = 'Download SXC File';

            // Save as FODS
            const fodsData = workbook.save(SaveFormat.Fods);
            const fodsBlob = new Blob([fodsData]);
            const downloadFods = document.getElementById('downloadFods');
            downloadFods.href = URL.createObjectURL(fodsBlob);
            downloadFods.download = 'Out.fods';
            downloadFods.style.display = 'inline-block';
            downloadFods.textContent = 'Download FODS File';

            resultDiv.innerHTML = '<p style="color: green;">Files ready. Click the download links to save the converted files.</p>';
        });
    </script>
</html>
```

## **Excel Dosyasını JSON veya XML'e Nasıl Kaydedilir**

JSON (JavaScript Object Notation), veri paylaşımı için insan tarafından okunabilir metin kullanan açık standart bir dosya formatıdır. JSON dosyaları .json uzantısıyla saklanır. JSON, daha az biçimlendirme gerektirir ve XML için iyi bir alternatiftir. JSON, JavaScript'ten türetilmiş, ancak dilsiz bir veri formatıdır. JSON'un oluşturulması ve ayrıştırılması modern birçok programlama dilince desteklenmektedir. application/json, JSON için kullanılan medya türüdür.

Aspose.Cells, dosyaların JSON veya XML olarak kaydedilmesini destekler.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells JSON Export Example</title>
    </head>
    <body>
        <h1>Convert Excel to JSON</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
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

            // Save workbook as JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```


## **Gelişmiş Konular**
- [Çalışma kitabının sıkıştırma seviyesi ayarlanabilir.](/cells/tr/javascript-cpp/adjust-workbook-compression-level/)
- [Sıkı Açık XML Elektronik Tablo Biçimine Çalışma Kitabını Kaydet](/cells/tr/javascript-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Yanıt Nesnesine Dosya Kaydetme](/cells/tr/javascript-cpp/saving-file-to-response-object/)
