---
title: JavaScript ile C++ kullanarak Satır ve Sütunları Otomatik Sığdırma
linktitle: Satırların ve Sütunların Otomatik Sığdırması
type: docs
weight: 20
url: /tr/javascript-cpp/autofit-rows-and-columns/
description: Bu makale, JavaScript ile C++ kullanarak hücre aralığındaki satırları, sütunları, birleştirilmiş hücrelerin satırlarını ve aralıktaki satırları nasıl otomatik sığdıracağınızı gösterir.
keywords: JavaScript ile Satırları Otomatik Sığdırma, C++ ile Sütunları Otomatik Sığdırma, C++ ile Bir Aralıkta Satırı Otomatik Sığdırma JavaScript, C++ ile Birleştirilmiş Hücrelerin Satırlarını Otomatik Sığdırma
---

{{% alert color="primary" %}}  
Microsoft Excel, hücrelerin içeriklerine göre genişlik ve yüksekliği otomatik olarak ayarlamalarına izin verir. Bu özellik, C++ ile Aspose.Cells for JavaScript üzerinden de kullanılabilir, böylece geliştiriciler çalışma zamanında bir hücrenin boyutunu otomatik olarak ayarlayabilirler.  
{{% /alert %}}  

## **Otomatik Uydurma**  

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve yöntem yelpazesi sunar. Bu makale, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfını kullanarak satır veya sütunları otomatik sığdırmaya bakıyor.  

### **Satırı Otomatik Uydurma - Basit**  

Bir satırın genişliği ve yüksekliğini otomatik boyutlandırmanın en basit yolu, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-) metodunu çağırmaktır. [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-) yöntemi, yeniden boyutlandırılacak satırın satır indeksini parametre olarak alır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>AutoFit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1 is the 2nd row; original code used 1)
            worksheet.autoFitRow(1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Hücre Aralığında Satır Otomatik Sığdırma**  

Bir satır, birçok sütundan oluşur. Aspose.Cells, satırdaki hücre aralığındaki içeriğe göre satırı otomatik sığdırmak için [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-) metodunun aşırı yüklenmiş bir versiyonunu çağırmaya izin verir. Aşağıdaki parametreleri alır:  

- **Satır dizini**, otomatik olarak uyarlama yapılacak satırın dizini.  
- **İlk sütun dizini**, satırın ilk sütununun dizini.  
- **Son sütun dizini**, satırın son sütununun dizini.  

[**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-) metodu, satırdaki tüm sütunların içeriğini kontrol eder ve ardından satırı otomatik sığdırır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>Auto-Fit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1, startColumn 0, endColumn 5)
            worksheet.autoFitRow(1, 0, 5);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Hücre Aralığında Sütun Otomatik Sığdırma**  

Bir sütun, birçok satırdan oluşur. Bir sütunu, sütun içindeki hücre aralığındaki içeriğe göre otomatik sığdırmak mümkündür; bunun için [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-) metodunun aşırı yüklenmiş bir versiyonu çağrılır ve aşağıdaki parametreleri alır:  

- **Sütun dizini**, otomatik olarak sığdırılacak sütunun dizini.  
- **İlk satır indeksi**, sütunun ilk satırının indeksi.  
- **Son satır indeksi**, sütunun son satırının indeksi.  

[**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-) metodu, sütundaki tüm satırların içeriğini kontrol eder ve sonra sütunu otomatik sığdırır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells AutoFit Column Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the Column of the worksheet (column index 4)
            worksheet.autoFitColumn(4);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Birleştirilmiş Hücreler İçin Satırları Otomatik Uydurma**  

Aspose.Cells kullanılarak, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) API'si kullanılarak birleştirilmiş hücreler için bile satırları otomatik sığdırmak mümkündür. [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) sınıfı, birleştirilmiş hücreler için satırları otomatik sığdırmak amacıyla kullanılabilecek [**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--) özelliği sağlar. [**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--), aşağıdaki üyeleri içeren [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/javascript-cpp/autofitmergedcellstype) yinelemeli nesnesini kabul eder.  

- Hiçbiri: Birleştirilmiş hücreleri yoksay.  
- FirstLine: Sadece ilk satırın yüksekliğini artırır.  
- LastLine: Sadece son satırın yüksekliğini artırır.  
- EachLine: Her satırın yüksekliğini artırır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows for Merged Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoFitterOptions, AutoFitMergedCellsType } = AsposeCells;

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

            // Create or load workbook
            let wb;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Get the first (default) worksheet
            const worksheet = wb.worksheets.get(0);

            // Create a range A1:B1
            const range = worksheet.cells.createRange(0, 0, 1, 2);

            // Merge the cells
            range.merge();

            // Insert value to the merged cell A1
            const cell = worksheet.cells.get(0, 0);
            cell.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style = cell.style;

            // Set wrapping text on
            style.isTextWrapped = true;

            // Apply the style to the cell
            cell.style = style;

            // Create an object for AutoFitterOptions
            const options = new AutoFitterOptions();

            // Set auto-fit for merged cells
            options.autoFitMergedCellsType = AutoFitMergedCellsType.EachLine;

            // Autofit rows in the sheet (including the merged cells)
            worksheet.autoFitRows(options);

            // Save the Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AutofitRowsforMergedCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Ayrıca, seçimli satır/sütun aralığını ve [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) örneğini kabul eden [**autoFitRows**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) ve [**autoFitColumns**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-) metodlarının aşırı yüklenmiş versiyonlarını kullanarak istenilen [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) ile seçili satır/sütunları otomatik sığdırmak için deneyebilirsiniz.  

Yukarıdaki metodların imzaları aşağıdaki gibidir:  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) options)  
1. autoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) options)  
{{% /alert %}}  

## **Bilinmesi Gerekenler**  

{{% alert color="primary" %}}  
Bir hücre birleştirilmişse, otomatik sığdırma yöntemleri uygulanmaz ki bu da Microsoft Excel'dekiyle aynıdır. Bunu aşmak için autofilter API kullanabilirsiniz. Ayrıca, hücredeki metin sarılmışsa, [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-) yöntemi de uygulanmaz. Bir diğer önemli nokta, *autoFit* yöntemlerinin zaman alıcı olduğu ve bu nedenle, uygulamanızın verimliliğini sağlamak için bu yöntemleri olabildiğince az kullanmanızdır.  
{{% /alert %}}  

## **Gelişmiş Konular**  
- [Birleştirilmiş Hücreler için Satırları Otomatik Uydurma](/cells/tr/javascript-cpp/autofit-rows-for-merged-cells/)
