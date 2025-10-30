---
title: JavaScript ve C++ aracılığıyla Satır ve Sütunları Gruplama ve Gruplandırmama
linktitle: Satır ve Sütunları Gruplandırma ve Grubu Çözme
type: docs
weight: 50
url: /tr/javascript-cpp/grouping-and-ungrouping-rows-and-columns/
description: Excel de satır ve sütunları Aspose.Cells for JavaScript kullanarak nasıl gruplayıp gruplandırmayacağınızı keşfedin.
---

## **Giriş**

Bir Microsoft Excel dosyasında, veriler için bir biçim oluşturarak tek bir fare tıklamasıyla ayrıntı seviyelerini gösterip gizleyebilirsiniz.

Yalnızca özetler veya başlıkların bulunduğu satırları veya sütunları hızlı bir şekilde görüntülemek için **Özet Sembolleri**, 1,2,3, + ve - simgelerine tıklayabilirsiniz veya simgeleri kullanarak bir çalışma sayfasındaki bir bölümün altındaki ayrıntıları görebilirsiniz, aşağıdaki şekilde gösterildiği gibi:

|**Satır ve Sütun Gruplama.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Satır ve Sütun Grubu Yönetimi**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her sayfaya erişim sağlayan [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) metodunu içerir. Bir sayfa [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, sayfadaki tüm hücreleri temsil eden [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunu sağlar.

[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonu, bir sayfada satır veya sütunları yönetmek için çeşitli metodlar sağlar, bunlardan bazıları aşağıda daha detaylı anlatılmaktadır.

### **Satır ve Sütun Gruplama**

Satır veya sütunları gruplamak için [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunun [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#groupRows-number-number-boolean-) ve [**groupColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#groupColumns-number-number-) metodları çağrılabilir. Her iki metod da aşağıdaki parametreleri alır:

- İlk satır/sütun indeksi, grup içindeki ilk satır veya sütun.
- Son satır/sütun indeksi, grup içindeki son satır veya sütun.
- Gizli mi, satırları/sütunları gruplandırmadan sonra gizlemek için bir Boolean parametre.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Rows and Columns Example</title>
    </head>
    <body>
        <h1>Group Rows and Columns Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.groupRows(0, 5, true);
            worksheet.cells.groupColumns(0, 2, true);

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows and columns grouped successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Grup Ayarları**

Microsoft Excel, görüntüleme için grup ayarlarını yapılandırmanıza izin verir:

- Detayın altında özet satırlar.
- Ayrıntının sağında özet sütunlar.

Geliştiriciler, bu grup ayarlarını [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfının [**outline**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#outline--) özelliğini kullanarak yapılandırabilirler.

### **Detaydan Aşağı Özet Satırlar**

Özet satırların detayların altında gösterilip gösterilmemesini [**summaryRowBelow**](https://reference.aspose.com/cells/javascript-cpp/outline/#summaryRowBelow--) özelliğini **true** veya **false** yaparak kontrol edebilirler.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Group Rows/Columns and Set Outline</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Grouping first six rows and first three columns
            worksheet.cells.groupRows(0, 5, true);
            worksheet.cells.groupColumns(0, 2, true);

            // Setting SummaryRowBelow property to false
            worksheet.outline.summaryRowBelow = false;

            // Saving the modified Excel file (Excel97To2003 -> .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
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

### **Detayın Sağına Özet Sütunlar**

Geliştiriciler ayrıca, özet sütunların doğru da gösterilip gösterilmeyeceğini [**Outline**](https://reference.aspose.com/cells/javascript-cpp/outline) sınıfının [**summaryColumnRight**](https://reference.aspose.com/cells/javascript-cpp/outline/#summaryColumnRight--) özelliğini **true** veya **false** yaparak kontrol edebilirler.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Group Rows and Columns Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Grouping first six rows and first three columns
            worksheet.cells.groupRows(0, 5, true);
            worksheet.cells.groupColumns(0, 2, true);

            // Set summary column to right
            worksheet.outline.summaryColumnRight = true;

            // Saving the modified Excel file (Excel 97-2003 format)
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

## **Satır ve Sütunların Gruplandırılmasını Kaldırma**

Herhangi bir gruplanmış satır veya sütunu gruplamayı kaldırmak için, [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#ungroupColumns-number-number-) koleksiyonunun [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells), [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#ungroupRows-number-number-boolean-) ve [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#ungroupColumns-number-number-) metodlarını çağırın. Her iki metod da iki parametre alır:

- İlk satır veya sütun dizini, ayrılmak istenen ilk satır/sütun.
- Son satır veya sütun dizini, ayrılmak istenen son satır/sütun.

{1} aşırı yüklemeye sahiptir ve üçüncü Boolean parametre alır. Bunu **true** yaparsanız, tüm gruplanmış bilgiler kaldırılır. Aksi takdirde, yalnızca dış grup bilgisi kaldırılır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Ungroup Rows and Columns Example</h1>
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

            // Instantiating a Workbook object with file content
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Ungrouping first six rows (from 0 to 5)
            worksheet.cells.ungroupRows(0, 5);

            // Ungrouping first three columns (from 0 to 2)
            worksheet.cells.ungroupColumns(0, 2);

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
