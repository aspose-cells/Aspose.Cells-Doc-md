---
title: JavaScript ve C++ ile Satır ve Sütunları Gizleme ve Gösterme
linktitle: Satır ve Sütunları Gizleme ve Gösterme
type: docs
weight: 60
url: /tr/javascript-cpp/hiding-and-showing-rows-and-columns/
description: Bir çalışma sayfasında satırları ve sütunları gizleme ve gösterme nasıl yapılır, Aspose.Cells for JavaScript kullanarak.
---

{{% alert color="primary" %}}

Bazen bir çalışma sayfasında belirli satırları veya sütunları gizlemek ve daha sonra göstermek anlamlı olabilir. Microsoft Excel bu özelliği sağlar ve Aspose.Cells de aynısını sağlar.

{{% /alert %}}

## **Satır ve Sütunların Görünürlüğünü Kontrol Etme**

C++ aracılığıyla Aspose.Cells for JavaScript, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine olanak tanıyan [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfıyla temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonu, çalışma sayfasındaki satır veya sütunları yönetmek için çeşitli yöntemler sunar. Bazıları aşağıda tartışılmıştır.

### **Satır ve Sütunları Gizleme**

Geliştiriciler, belirli bir satır veya sütunu gizlemek için sırasıyla [**hideRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRow-number-) ve [**hideColumn(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumn-number-) metodlarını çağırabilirler. Her iki yöntem de gizlenmek istenen satır ve sütun indekslerini parametre olarak alır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Row and Column Example</h1>
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

            // Instantiating a Workbook object with Uint8Array
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the 3rd row of the worksheet
            worksheet.cells.hideRow(2);

            // Hiding the 2nd column of the worksheet
            worksheet.cells.hideColumn(1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row and column hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Bir satır veya sütunu sıfır genişliğine ayarlayarak bir satır veya sütunu gizlemek de mümkündür.

{{% /alert %}}

### **Satır ve Sütunları Gösterme**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunun [**unhideRow(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRow-number-number-) ve [**unhideColumn(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumn-number-number-) metodlarını sırasıyla çağırarak herhangi bir gizli satır veya sütunu gösterebilirler. Her iki yöntem de iki parametre alır:

- **Satır veya sütun dizini** - belirli bir satır veya sütunun gösterilmesi için kullanılan dizin.
- **Satır yüksekliği veya sütun genişliği** - gizlendikten sonra atanan satır yüksekliği veya sütun genişliği.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Unhide Rows and Columns Example</title>
    </head>
    <body>
        <h1>Unhide Rows and Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unhiding the 3rd row and setting its height to 13.5
            worksheet.cells.unhideRow(2, 13.5);

            // Unhiding the 2nd column and setting its width to 8.5
            worksheet.cells.unhideColumn(1, 8.5);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Gizli bir sütunu görünür hale getirirken, önceden atanmış genişliğe veya orijinal genişliğe geri yüklemeniz gerekiyorsa, negatif genişlikle sütunu gizleme kaldırın. Örneğin: worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **Birden Fazla Satır ve Sütunu Gizleme**

Geliştiriciler, aynı anda birden fazla satır veya sütunu gizlemek için sırasıyla [**hideRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRows-number-number-) ve [**hideColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumns-number-number-) metodlarını çağırabilirler. Her iki yöntem de gizlenecek başlangıç satırı veya sütunu indeksi ve satır veya sütun sayısı parametreleri olarak alır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Rows and Columns</title>
    </head>
    <body>
        <h1>Hide Rows and Columns Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding 3, 4, and 5 rows in the worksheet (rows are zero-based index)
            worksheet.cells.hideRows(2, 3);

            // Hiding 2 and 3 columns in the worksheet (columns are zero-based index)
            worksheet.cells.hideColumns(1, 2);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Rows and columns hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Birden fazla satır ve sütunu görünür yapmak için [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) sınıfının [**unhideRows(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRows-number-number-number-) ve [**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumns-number-number-number-) metodlarını kullanmak da mümkündür.

{{% /alert %}}
