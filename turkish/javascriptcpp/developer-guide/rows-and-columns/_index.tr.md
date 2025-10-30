---
title: JavaScript ile C++ kullanarak Satır ve Sütunları Biçimlendirme
linktitle: Satır ve Sütunlar
type: docs
weight: 100
url: /tr/javascript-cpp/adjusting-row-height-and-column-width/
description: Aspose.Cells for JavaScript via C++ satır yüksekliği veya sütun genişliğini değiştirmeyi destekleyebilir, ayrıca satır veya sütunlara biçimlendirme uygulayabilir.
keywords: Satır yüksekliği ve sütun genişliği ayarlı, satır yüksekliği ve sütun genişliği ayarlı, satır yüksekliğini veya sütun genişliğini değiştirme, satır ve sütunları biçimlendirme, satır yüksekliği ve sütun genişliği ayarlama hakkında bilgi.
---

{{% alert color="primary" %}}
Tablolar ve sütunlar ile çalışırken, satırların yüksekliğini veya sütunların genişliğini değiştirmek gerekebilir. Bazen, satır veya sütun üzerinde biçimlendirme uygulamak, verileri göstermek için mevcut yüksekliği veya genişliği değiştirmeyi gerektirir. Normalde kullanıcılar, Microsoft Excel kullanarak satır yüksekliği ve sütun genişliklerini WYSIWYG ortamında ayarlar. Ancak, Aspose.Cells ile geliştiriciler bu işlemleri çalışma zamanında gerçekleştirebilir.
{{% /alert %}}

## **Satırlarla Çalışmak**

### **Satır Yüksekliğini Ayarlamak**

Aspose.Cells for JavaScript C++ ile bir sınıf sağlar, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), bu sınıf Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonu sağlar.

[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonu, bir çalışma sayfasında satır veya sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda daha ayrıntılı olarak tartışılmıştır.

### **Bir Satırın Yüksekliğini Ayarlama**

Yalnızca bir satırın yüksekliğini [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunun [**rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-) yöntemi çağrılarak ayarlamak mümkündür. [**rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-) yöntemi aşağıdaki parametreleri alır:

- **Satır dizini**, yüksekliği değiştirdiğiniz satırın dizini.
- **Satır yüksekliği**, satıra uygulanan satır yüksekliği.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Row Height Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.rows.get(1).height = 13;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row height set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Bir Çalışma Sayfasındaki Tüm Satırların Yüksekliğini Ayarlama**

Eğer geliştiriciler, çalışma sayfasındaki tüm satırlar için aynı satır yüksekliğini ayarlamak isterse, bunu [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunun [**standardHeight()**](https://reference.aspose.com/cells/javascript-cpp/cells/#standardHeight--) özelliğini kullanarak yapabilirler.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Standard Row Height</title>
    </head>
    <body>
        <h1>Set Standard Row Height Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the height of all rows in the worksheet to 15
            worksheet.cells.standardHeight = 15;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Standard row height set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sütunlarla Çalışmak**

### **Bir Sütunun Genişliğini Ayarlama**

Bir sütunun genişliğini [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunun [**columnWidth(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidth-number-number-) yöntemi çağrılarak ayarlayın. [**columnWidth(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidth-number-number-) yöntemi aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliği değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, istenen sütun genişliği.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Column Width Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Set Column Width</button>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the width of the second column to 17.5
            worksheet.cells.columns.get(1).width = 17.5;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Piksel cinsinden Sütun Genişliğini Ayarlama**

Bir sütunun genişliğini [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunun [**columnWidthPixel(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidthPixel-number-number-) yöntemi çağrılarak ayarlayın. [**columnWidthPixel(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidthPixel-number-number-) yöntemi aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliği değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, pikseller cinsinden istenen sütun genişliği.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Column Width In Pixels</title>
    </head>
    <body>
        <h1>Set Column Width In Pixels</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Set the width of the column in pixels
            // Converted from: worksheet.getCells().setColumnWidthPixel(7, 200);
            // UNIVERSAL GETTER/SETTER CONVERSION applied:
            worksheet.cells.columnWidthPixel = [7, 200];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetColumnWidthInPixels_Out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Bir Çalışma Sayfasındaki Tüm Sütunların Genişliğini Ayarlama**

Tüm sütunlar için aynı sütun genişliğini ayarlamak için, [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunun [**standardWidth()**](https://reference.aspose.com/cells/javascript-cpp/cells/#standardWidth--) özelliğini kullanın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Standard Width Example</title>
    </head>
    <body>
        <h1>Set Standard Width Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the width of all columns in the worksheet to 20.5
            worksheet.cells.standardWidth = 20.5;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Standard width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Satır ve Sütunları Otomatik Sığdır](/cells/tr/javascript-cpp/autofit-rows-and-columns/)
- [Aspose.Cells Kullanarak Metni Sütunlara Dönüştürme](/cells/tr/javascript-cpp/convert-text-to-columns-using-aspose-cells/)
- [Satırları ve Sütunları Kopyalama](/cells/tr/javascript-cpp/copying-rows-and-columns/)
- [Çalışma Sayfasındaki Boş Satırları ve Sütunları Silme](/cells/tr/javascript-cpp/delete-blank-rows-and-columns-in-a-worksheet/)
- [Satır ve Sütunları Gruplama ve Grubu Kaldırma](/cells/tr/javascript-cpp/grouping-and-ungrouping-rows-and-columns/)
- [Satır ve Sütunları Gizleme ve Gösterme](/cells/tr/javascript-cpp/hiding-and-showing-rows-and-columns/)
- [Excel Çalışma Sayfasına Satır Eklemek veya Silmek](/cells/tr/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/)
- [Excel dosyasının Satır ve Sütunlarını Eklemek ve Silmek](/cells/tr/javascript-cpp/inserting-and-deleting-rows-and-columns/)
- [Çalışma Sayfasındaki Yinelemeli Satırları Kaldırma](/cells/tr/javascript-cpp/remove-duplicate-rows-in-a-worksheet/)
- [Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle](/cells/tr/javascript-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
