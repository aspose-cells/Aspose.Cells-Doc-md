---
title: Excel, OpenOffice, Json, Csv ve Html dosyalarını yükleme ve yönetme
linktitle: Dosyaları Açma
type: docs
weight: 20
url: /tr/javascript-cpp/loading-saving-and-managing/
description: Aspose.Cells ile JavaScript ve C++ kullanarak Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Resim, Mht ve XPS dosyalarını oluşturmak, açmak ve yönetmek çok basittir.
---

{{% alert color="primary" %}}

Aspose.Cells ile, örneğin verileri almak veya geliştirme sürecini hızlandırmak için tasarımcı şablonu kullanmak gibi, Excel dosyalarını oluşturmak, açmak ve yönetmek çok basittir.

{{% /alert %}}

## **Yeni Bir Çalışma Kitabı Oluşturma**
Aşağıdaki örnek sıfırdan yeni bir çalışma kitabı oluşturur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/Aspose.Cells.lic",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a Workbook object (new blank workbook)
            const wb = new Workbook();

            // Access the first worksheet in the workbook
            const sheet = wb.worksheets.get(0);

            // Access the "A1" cell in the sheet
            const cell = sheet.cells.get("A1");

            // Input the "Hello World!" text into the "A1" cell
            cell.value = "Hello World!";

            // Save the Excel file and prepare download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MyBook_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell updated. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Bir Dosyayı Açma ve Kaydetme**
Aspose.Cells ile, Excel dosyalarını açmak, kaydetmek ve yönetmek çok basittir.

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

            // Creating a Workbook object and opening an Excel file using its file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding new sheet
            const sheetIndex = workbook.worksheets.add("MySheet");
            const sheet = workbook.worksheets.get(sheetIndex);

            // Setting active sheet
            workbook.worksheets.activeSheetIndex = 1;

            // Setting values.
            const cells = sheet.cells;

            // Setting text
            cells.get("A1").putValue("Hello!");

            // Setting number
            cells.get("A2").putValue(1000);

            // Setting Date Time
            const cell = cells.get("A3");
            cell.putValue(new Date());
            const style = cell.style;
            style.number = 14;
            cell.style = style;

            // Setting formula
            cells.get("A4").formula = "=SUM(A1:A3)";

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Dosyaları Açmanın Farklı Yolları](/cells/tr/javascript-cpp/different-ways-to-open-files/)
- [Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele](/cells/tr/javascript-cpp/filter-defined-names-while-loading-workbook/)
- [Çalışma Kitabını veya Çalışma Sayfasını Yüklerken Nesneleri Filtrele](/cells/tr/javascript-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Şablon dosyasından çalışma kitabını yüklerken veri türünü filtreleme](/cells/tr/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Excel Dosyası Yüklenirken Uyarıları Al](/cells/tr/javascript-cpp/get-warnings-while-loading-excel-file/)
- [Grafikleri Olmadan Kaynak Excel Dosyasını Yükleme](/cells/tr/javascript-cpp/load-source-excel-file-without-charts/)
- [Bir Çalışma Kitabındaki Belirli Çalışma Sayfalarını Yükleme](/cells/tr/javascript-cpp/load-specific-worksheets-in-a-workbook/)
- [Belirtilen Yazıcı Kağıdı Boyutuyla Çalışma Kitabı Yükle](/cells/tr/javascript-cpp/load-workbook-with-specified-printer-paper-size/)
- [Farklı Microsoft Excel Sürümlerini Açma](/cells/tr/javascript-cpp/opening-different-microsoft-excel-versions-files/)
- [Farklı Biçimlerde Dosyaları Açma](/cells/tr/javascript-cpp/opening-files-with-different-formats/)
- [Büyük Veri Kümesine Sahip Büyük Dosyalarla Çalışırken Hafıza Kullanımını Optimize Etme](/cells/tr/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Numbers Elektronik Tablosu, Apple Inc. tarafından geliştirildi.](/cells/tr/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Çok uzun sürüyorsa, Duraklatma İzleyiciyi kullanarak dönüşümü veya yüklemeyi durdurun](/cells/tr/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [LightCells API'sını Kullanma](/cells/tr/javascript-cpp/using-lightcells-api/)
- [CSV'yi JSON'a dönüştür](/cells/tr/javascript-cpp/convert-csv-to-json/)
- [Excel’i JSON’a dönüştürmek](/cells/tr/javascript-cpp/convert-excel-to-json/)
- [JSON'ı CSV'ye dönüştür](/cells/tr/javascript-cpp/convert-json-to-csv/)
- [JSON’u Excel’e dönüştürmek](/cells/tr/javascript-cpp/convert-json-to-excel/)
- [Excel’i Html’e dönüştürmek](/cells/tr/javascript-cpp/convert-excel-to-html/)
