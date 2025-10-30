---
title: JavaScript ile C++ kullanarak Sayfaları kopyalama ve taşıma
linktitle: Çalışsayfa Kopyalama ve Taşıma
type: docs
weight: 10
url: /tr/javascript-cpp/copying-and-moving-worksheets/
description: Bu makale, JavaScript ile C++ API kullanarak hem bir Excel çalışma kitabı içindeki hem de farklı çalışma kitaplarındaki sayfaları programlı olarak nasıl kopyalayıp taşıyacağınızı anlatan örnek kodları içerir.
keywords: sayfa kopyalama JavaScript, sayfa taşıma JavaScript
---

{{% alert color="primary" %}}

Bazen ortak biçimlendirme ve veriye sahip bir dizi çalışma sayfasına ihtiyaç duyarsınız. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalara sahip bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunun bir yolu var: bir sayfa oluşturduktan sonra onu kopyalayarak.

 Aspose.Cells for JavaScript ile C++ destekler, çalışma kitapları içinde veya arasında sayfa kopyalama ve taşıma işlemlerini, veri, biçimlendirme, tablolar, matrisler, grafikler, görüntüler ve diğer nesnelerle yüksek hassasiyetle gerçekleştirir.

{{% /alert %}}

## **Microsoft Excel Kullanarak Sayfaları Taşıma veya Kopyalama**

Microsoft Excel'de çalışma kitapları arasında veya içinde çalışma sayfalarını kopyalama ve taşıma için gereken adımlar aşağıda listelenmiştir.

1. Sayfaları başka bir çalışma kitabına taşımak veya kopyalamak için, sayfaları alacak olan çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1. **Düzenle** menüsünde, **Sayfayı Taşı veya Kopyala**'yı tıklayın.
1. **Kitapçığa** iletişim kutusunda, sayfaların alınacağı çalışma kitabını tıklayın.
1. Seçili sayfaları yeni bir kitapçığa taşımak veya kopyalamak için **Yeni Kitap**'a tıklayın.
1. **Önceki sayfa** kutusunda, taşınan veya kopyalanan sayfaların nereden önce ekleneceğini tıklayın.
1. Sayfaları taşımak yerine kopyalamak için **Kopyasını Oluştur** onay kutusunu seçin.

### **C++ ile Aspose.Cells for JavaScript kullanarak Çalışma Kitabı içinde Sayfaları Kopyala**

Aspose.Cells, mevcut bir çalışma sayfasından veri kopyalamak için kullanılan ve çalışma sayfasının bir kopyasını eklemek için kullanılan [**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#addCopy-number-) adlı aşırı yüklü bir yöntem sağlar. Yöntemin bir sürümü, kaynak çalışma sayfasının endeksini parametre olarak alır. Diğer sürüm, kaynak çalışma sayfasının adını alır.

Aşağıdaki örnek, bir çalışma kitabı içinde mevcut bir çalışma sayfasının nasıl kopyalanacağını gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Sheet Within Workbook</title>
    </head>
    <body>
        <h1>Copy Sheet Within Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Open an existing Excel file.
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheets object with reference to the sheets of the Workbook.
            const sheets = wb.worksheets;

            // Copy data to a new sheet from an existing sheet within the Workbook.
            sheets.addCopy("Sheet1");

            // Save the Excel file.
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWithinWorkbook_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Sheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Çalışma Kitapları Arasında Çalışma Sayfalarını Kopyalama**

Aspose.Cells, kaynak iş sayfasından başka bir iş sayfasına veya çalışma kitabı içinde veya arasında veri ve biçimlendirmeyi kopyumak için kullanılan [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#copy-worksheet-) yöntemi sağlar. Bu yöntem, kaynak iş sayfası nesnesini parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabından diğer bir çalışma kitabına sayfa kopyalamanın nasıl yapılacağını gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Copy Worksheets Between Workbooks</title>
    </head>
    <body>
        <h1>Copy Worksheets Between Workbooks</h1>
        <p>Select the source Excel file (book1.xls) to copy its first worksheet into a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (book1.xls).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create a Workbook from the uploaded file (source workbook)
            const excelWorkbook0 = new Workbook(new Uint8Array(arrayBuffer));

            // Create another Workbook (destination workbook)
            const excelWorkbook1 = new Workbook();

            // Copy the first sheet of the first book into second book.
            excelWorkbook1.worksheets.get(0).copy(excelWorkbook0.worksheets.get(0));

            // Save the file as Excel 97-2003 (.xls)
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetsBetweenWorkbooks_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Copied Workbook';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Aşağıdaki örnek, bir çalışma kitabından başka bir çalışma kitabına bir çalışma sayfasını kopyalamayı göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy Worksheet Between Workbooks Example</h1>
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
            // Create a new Workbook.
            const excelWorkbook0 = new Workbook();

            // Get the first worksheet in the book.
            const ws0 = excelWorkbook0.worksheets.get(0);

            // Put some data into header rows (A1:A4)
            for (let i = 0; i < 5; i++) {
                ws0.cells.get(i, 0).value = `Header Row ${i}`;
            }

            // Put some detail data (A5:A999)
            for (let i = 5; i < 1000; i++) {
                ws0.cells.get(i, 0).value = `Detail Row ${i}`;
            }

            // Define a pagesetup object based on the first worksheet.
            const pagesetup = ws0.pageSetup;

            // The first five rows are repeated in each page...
            // It can be seen in print preview.
            pagesetup.printTitleRows = "$1:$5";

            // Create another Workbook.
            const excelWorkbook1 = new Workbook();

            // Get the first worksheet in the book.
            const ws1 = excelWorkbook1.worksheets.get(0);

            // Name the worksheet.
            ws1.name = "MySheet";

            // Copy data from the first worksheet of the first workbook into the
            // first worksheet of the second workbook.
            ws1.copy(ws0);

            // Saving the modified Excel file
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetFromWorkbookToOther_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and worksheet copied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Çalışma Kitabı İçinde Sayfaları Taşıma**

Aspose.Cells, aynı elektronik tablo içinde bir iş sayfasını başka bir konuma taşımak için [**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#moveto-number-) yöntemini sağlar. Bu yöntem, hedef iş sayfası indeksini parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabı içinde bir çalışma sayfasının başka bir konuma nasıl taşınacağını gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Move Worksheet Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = wb.worksheets;

            // Get the first worksheet
            const worksheet = sheets.get(0);

            // Move the first sheet to the third position (index 2)
            worksheet.moveTo(2);

            // Save the modified workbook in Excel97-2003 format
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MoveWorksheet_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet moved successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
