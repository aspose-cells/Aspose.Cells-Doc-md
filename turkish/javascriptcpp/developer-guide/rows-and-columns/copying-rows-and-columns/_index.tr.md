---
title: JavaScript ile Satır ve Sütun Kopyalama C++ ile
linktitle: Satır ve Sütunları Kopyalama
type: docs
weight: 40
url: /tr/javascript-cpp/copying-rows-and-columns/
description: Bu makale, C++ API aracılığıyla Aspose.Cells for JavaScript kullanarak satır ve sütunların nasıl kopyalanacağını gösterir.
keywords: JavaScript ve C++ aracılığıyla Satır ve Sütun Kopyalama, JavaScript te Satırları Kopyala, JavaScript kullanarak Sütunları Kopyala, C++ ile Aspose.Cells for JavaScript kullanarak Satır ve Sütunları Nasıl Yapıştırılır, Çoklu satır ve sütunları yapıştır, Tek Satır veya Sütunu Kopyala ve Yapıştır.
---

## **Giriş**  

Bazen, bir çalışma sayfasında tüm çalışma sayfasını kopyalamadan satır ve sütunları kopyalamanız gerekir. Aspose.Cells ile, çalışma kitapları arasında veya içinde satır ve sütunları kopyalamak mümkündür.  
Bir satır (veya sütun) kopyalandığında, içindeki veriler, güncellenmiş referanslarla formülleri - ve değerleri, yorumları, biçimlendirmeyi, gizli hücreleri, görüntüleri ve diğer çizim nesnelerini içeren veriler de kopyalanır.  

## **Microsoft Excel ile Satırları ve Sütunları Nasıl Kopyalanır**  

1. Kopyalamak istediğiniz satırı veya sütunu seçin.  
1. Satır veya sütunları kopyalamak için **Standart** araç çubuğunda **Kopyala**'yı tıklayın veya **CTRL**+**C**'ye basın.  
1. Kopyalamak istediğiniz seçimin altında veya sağındaki bir satır veya sütunu seçin.  
1. Satır veya sütunları kopyalarken, **Ekle** menüsünde **Kopyalanan Hücreler**'i tıklayın.  

{{% alert color="primary" %}}  
Hedef hücrelerin içeriği herhangi bir içeriği Çıkar veya tıklamak yerine **Standart** araç çubuğunda **Yapıştır**'ı tıklarsanız değiştirilir.  
{{% /alert %}}  

## **Microsoft Excel ile Yapıştırma Seçenekleri Kullanarak Satır ve Sütunları Nasıl Yapıştırılır**  

1. Kopyalamak istediğiniz veri veya diğer özelliklere sahip hücreleri seçin.  
1. Ana sekmede **Kopyala**'yı tıklayın.  
1. Kopyaladığınız şeyi yapıştırmak istediğiniz alanın ilk hücresine tıklayın.  
1. Ana sekmede **Yapıştır**'ın yanındaki oku tıklayın ve ardından **Yapıştırma**'yı seçin.  
1. İstediğiniz **seçenekleri** seçin.  

## **C++ aracılığıyla Aspose.Cells for JavaScript kullanarak Satır ve Sütunların nasıl Kopyalanacağı**  

## **Tek Satırları Nasıl Kopyalanır**  

Aspose.Cells, [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) metodunu sağlar; bu metod, kaynak satırdan hedef satıra formüller, değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kopyalar.  

[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) yöntemi aşağıdaki parametreleri alır:  

- kaynaktaki [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) nesnesi,  
- kaynak satır dizini, ve  
- hedef satır dizini.  

Bu yöntemi kullanarak bir sayfa içinde veya başka bir sayfaya satır kopyalayabilirsiniz. [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) yöntemi, Microsoft Excel'e benzer şekilde çalışır. Örneğin, hedef satırın yüksekliğini açıkça ayarlamanıza gerek yoktur, bu değer de kopyalanır.  

Aşağıdaki örnek, bir sayfada satır kopyalamayı göstermektedir. Bir şablon Microsoft Excel dosyası kullanır ve ikinci satırı (veri, biçimlendirme, yorumlar, resimler vb. ile birlikte) kopyalar ve aynı sayfadaki 12. satıra yapıştırır.  

Kaynak satır yüksekliğini almak için [**Cells.rowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-boolean-cellsunittype-) metodunu kullanmadan adımı atlayabilirsiniz, daha sonra hedef satır yüksekliği [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) yöntemi ile otomatik olarak ayarlanır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Row</title>
    </head>
    <body>
        <h1>Copy Row Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook.
            const wsTemplate = workbook.worksheets.get(0);

            // Copy the second row (index 1) with data, formatting, images and drawing objects
            // To the 16th row (index 15) in the worksheet.
            wsTemplate.cells.copyRow(wsTemplate.cells, 1, 15);

            // Save the excel file in Excel97To2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Satırları kopyalarken, ilgili resimler, grafikler veya diğer çizim nesnelerinin Microsoft Excel ile aynı olduğu gibi dikkate alınması önemlidir:  

1. Kaynak satır dizini 5 ise, resim, grafik vb., başlangıç satır dizini 4 ve bitiş satır dizini 6 içinde bulunduruluyorsa kopyalanır.  
1. Var olan resimler, grafikler vb. hedef satırdan silinmez.  
{{% /alert %}}  

## **Birden Fazla Satırın Nasıl Kopyalanacağı**  

Ayrıca, [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) metodunu kullanırken, ek olarak bir tamsayı parametresi alan ve kopyalanacak kaynak satır sayısını belirten toplu satır kopyalama işlemi yapabilirsiniz.  

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

            // Instantiate workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection of first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Copy the first 3 rows to 7th row (indexes are zero-based)
            cells.copyRows(cells, 0, 6, 3);

            // Save the result and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Sütunları Kopyalamak**  

Aspose.Cells, [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) sınıfının [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) metodunu sağlar, bu yöntem, formüller ve güncellenmiş referanslar dahil olmak üzere tüm veri türlerini, değerleri, yorumları, hücre biçimlerini, gizli hücreleri, resimleri ve diğer çizim nesnelerini kaynak sütundan hedef sütuna kopyalar.  

[**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) yöntemi aşağıdaki parametreleri alır:  

- kaynaktaki [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) nesnesi,  
- kaynak sütun indeksi ve  
- hedef sütun indeksi.  

Bir sayfa içinde veya başka bir sayfaya sütun kopyalamak için [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) yöntemini kullanabilirsiniz.  

Bu örnek, bir çalışma sayfasından bir sütunu kopyalar ve başka bir iş kitabındaki bir çalışma sayfasına yapıştırır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Copy Column Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const excelWorkbook1 = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book.
            const ws1 = excelWorkbook1.worksheets.get(0);

            // Copy the first column from the first worksheet into the third column of the same worksheet.
            const cells = ws1.cells;
            cells.copyColumn(cells, cells.columns.get(0).index, cells.columns.get(2).index);

            // Autofit the column.
            ws1.autoFitColumn(2);

            // Save the excel file (Excel97To2003 format for .xls)
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Birden Çok Sütun Nasıl Kopyalanır**  

[**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) yöntemine benzer şekilde, Aspose.Cells API'leri de çok sayıda kaynak sütunu yeni konuma kopyalamak için [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) metodunu sağlar.  

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create an instance of Workbook class by loading the existing spreadsheet
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet's cells collection
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Copy the first 3 columns to the 7th column
            cells.copyColumns(cells, 0, 6, 3);

            // Save the result and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Yapıştırma Seçenekleri ile Satır ve Sütunların Nasıl Yapıştırılacağı**  

Aspose.Cells şimdi, [**PasteOptions**](https://reference.aspose.com/cells/javascript-cpp/pasteoptions/) işlevler [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) ve [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) kullanırken uygun yapıştırma seçeneğini Excel ile benzer şekilde ayarlamayı sağlar.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Change Chart Data Source</title>
    </head>
    <body>
        <h1>Change Chart Data Source Example</h1>
        <p>Select an Excel file (sampleChangeChartDataSource.xlsx) from your local machine.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PasteType, CopyOptions, PasteOptions } = AsposeCells;

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

            // Access the first sheet which contains chart
            const source = workbook.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = workbook.worksheets.add("DestSheet");

            // Set CopyOptions.ReferToDestinationSheet to true
            const options = new CopyOptions();
            options.referToDestinationSheet = true;

            // Set PasteOptions
            const pasteOptions = new PasteOptions();
            pasteOptions.pasteType = PasteType.Values;
            pasteOptions.onlyVisibleCells = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options, pasteOptions);

            // Save workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataSource.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
