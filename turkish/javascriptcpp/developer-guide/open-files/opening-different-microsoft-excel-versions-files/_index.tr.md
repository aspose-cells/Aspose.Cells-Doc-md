---
title: JavaScript ile C++ kullanarak Farklı Microsoft Excel Sürümleri Dosyalarını Açma
linktitle: Farklı Microsoft Excel Sürümleri Dosyalarını Açın
type: docs
weight: 20
url: /tr/javascript-cpp/opening-different-microsoft-excel-versions-files/
description: Bu makale, C++ kullanarak Aspose.Cells for JavaScript ile farklı Excel sürüm dosyalarını nasıl açacağınızı açıklar.
keywords: JavaScript ile C++ kullanarak Farklı Microsoft Excel dosyalarını Açma, Şifreli Excel Dosyalarını JavaScript ile C++ kullanarak nasıl açarım
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel 95/97 - 2003, SpreadsheetML, Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX veya Şifreli Excel Dosyaları gibi çeşitli farklı Microsoft Excel Sürümlerini açabilir.

{{% /alert %}}

## **Farklı Microsoft Excel Sürümleri Dosyalarını Açma**

Bir uygulama genellikle, farklı sürümlerde oluşturulan Microsoft Excel dosyalarını açabilmelidir. Örneğin, Microsoft Excel 95, 97 veya Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365. Bir dosyayı, XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited veya TSV, CSV, ODS ve diğer formatlarda yüklemeniz gerekebilir. Yükleyiciyi kullanın veya [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının [**fileFormat**](https://reference.aspose.com/cells/javascript-cpp/workbook/#fileFormat--) tip özniteliğini belirterek formatı [**FileFormatType**](https://reference.aspose.com/cells/javascript-cpp/fileformattype) enumuyla belirtin.

[**FileFormatType**](https://reference.aspose.com/cells/javascript-cpp/fileformattype) enumu, aşağıda verilen bazı önceden tanımlanmış dosya formatlarını içerir.

|**Dosya Biçimi Türleri**|**Açıklama**|
| :- | :- |
|Csv|CSV dosyasını temsil eder|
|Excel97To2003|Excel 97 - 2003 dosyasını temsil eder|
|Xlsx|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX dosyasını temsil eder|
|Xlsm|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSM dosyasını temsil eder|
|Xltx|Excel 2007/2010/2013/2016/2019 ve Office 365 şablonu XLTX dosyasını temsil eder|
|Xltm|Excel 2007/2010/2013/2016/2019 ve Office 365 makro etkin XLTM dosyasını temsil eder|
|Xlsb|Excel 2007/2010/2013/2016/2019 ve Office 365 binary XLSB dosyasını temsil eder|
|SpreadsheetML|SpreadsheetML dosyasını temsil eder|
|Tsv|TSV dosyasını temsil eder|
|TabDelimited|Tab Delimited metin dosyasını temsil eder|
|Ods|ODS dosyasını temsil eder|
|Html|HTML dosyasını temsil eder|
|Mhtml|MHTML dosyasını temsil eder|

### **Microsoft Excel 95/5.0 Dosyalarını Aç**

Bir Microsoft Excel 95/5.0 dosyasını açmak için [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) kullanın ve yüklenmek üzere şablon dosyası için [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) sınıfının ilgili özniteliğini ayarlayın. Bu özelliği test etmek için örnek bir dosya aşağıdaki bağlantıdan indirilebilir:

[Excel95 Dosyası](Excel95.xls)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Excel95_5.0.xls Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Open Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions1 = new LoadOptions(LoadFormat.Auto);

            // Create a Workbook object and opening the file from the stream
            const wbExcel95 = new Workbook(new Uint8Array(arrayBuffer), loadOptions1);
            console.log("Microsoft Excel 95/5.0 workbook opened successfully!");

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 95/5.0 workbook opened successfully!</p>';
        });
    </script>
</html>
```

### **Microsoft Excel 97 - 2003 Dosyalarını Aç**

Bir Microsoft Excel 97 - 2003 dosyasını açmak için [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) kullanın ve yüklenmek üzere şablon dosyası için [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) sınıfının ilgili özniteliğini ayarlayın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Excel 97-2003 Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel 97-2003 (.xls) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const loadOptions1 = new LoadOptions(LoadFormat.Excel97To2003);
            const wbExcel97 = new Workbook(new Uint8Array(arrayBuffer), loadOptions1);

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 97 - 2003 workbook opened successfully!</p>';

            const outputData = wbExcel97.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

### **Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX Dosyalarını Aç**

XLSX veya XLSB formatında, yani Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 formatında bir dosya açmak için dosya yolunu belirtin. Ayrıca [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) kullanabilir ve yüklenmek üzere şablon dosyası için [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) sınıfının ilgili özniteliğini/ayrıcalıklarını ayarlayabilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Open Excel 2007 Xlsx Example</title>
    </head>
    <body>
        <h1>Open Excel 2007 Xlsx Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel .xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);

            // Create a Workbook object and open the file from the uploaded data
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 2007 - Office365 workbook opened successfully!</p>';

            // Save the workbook back to a downloadable file (unchanged content)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book_Excel2007_output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Opened Workbook';
        });
    </script>
</html>
```

### **Şifreli Excel Dosyalarını Aç**

Microsoft Excel kullanarak şifrelenmiş Excel dosyaları oluşturmak mümkündür. Şifrelenmiş bir dosyayı açmak için [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) kullanın ve şablon dosyası için özniteliklerini ve seçeneklerini (örneğin, bir şifre verin) ayarlayın.
Bu özelliği test etmek için bir örnek dosya aşağıdaki bağlantıdan indirilebilir:

[Encrypted Excel](EncryptedExcel.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Encrypted Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Open Encrypted Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an encrypted Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions
            const loadOptions = new LoadOptions();

            // Specify the password (converted from setPassword to property assignment)
            loadOptions.password = "1234";

            // Create a Workbook object opening the file from the uploaded bytes with loadOptions
            const wbEncrypted = new Workbook(new Uint8Array(arrayBuffer), loadOptions);
            console.log("Encrypted excel file opened successfully!");

            // Save the workbook so user can download it (using Excel97To2003 format for .xls)
            const outputData = wbEncrypted.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            // Use original name with a prefix to indicate it's been opened
            const originalName = file.name || 'output.xls';
            downloadLink.download = 'opened_' + originalName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Opened Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Encrypted Excel file opened successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Aspose.Cells ayrıca şifre korumalı Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 dosyalarını açmayı destekler.
