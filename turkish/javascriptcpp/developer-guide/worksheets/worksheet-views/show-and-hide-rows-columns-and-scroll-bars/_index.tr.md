---
title: JavaScript ile C++ kullanarak Satır, Sütun ve Kaydırma Çubuklarını gösterme ve gizleme
linktitle: Satırları Sütunları ve Kaydırma Çubuklarını Göster ve Gizle
type: docs
weight: 20
url: /tr/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/
description: Bu makale, JavaScript ile C++ kullanarak Excel çalışma sayfasındaki satır ve sütunları programatik olarak gösterip gizlemeyi ve kaydırma çubuklarının görünürlüğünü kontrol etmeyi gösterir. Aynı zamanda çoklu satır ve sütunları verimli şekilde gizleme yöntemlerini açıklar.
---

{{% alert color="primary" %}}  
Aspose.Cells, bir çalışma sayfasının Satırların, Sütunların ve Kaydırma Çubuklarının görünürlüğünü kontrol etmenin yollarını sağlar.  
{{% /alert %}}  

## **Satır ve Sütunları Göster ve Gizle**  

Aspose.Cells for JavaScript ile C++ Bir Microsoft Excel Dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine olanak tanıyan [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonunu sağlar. [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonu, bir çalışma sayfasındaki satır veya sütunları yönetmek için birkaç yöntem sunar. Bunlardan bazıları aşağıda tartışılmıştır.  

### **Satır ve Sütunları Göster**  

Geliştiriciler, [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonunun [**unhideRow(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRow-number-number-) ve [**unhideColumn(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumn-number-number-) metodlarını sırasıyla çağırarak herhangi bir gizli satır veya sütunu gösterebilirler. Her iki yöntem de iki parametre alır:  

- **Satır veya sütun dizini** - belirli bir satır veya sütunun gösterilmesi için kullanılan dizin.  
- **Satır yüksekliği veya sütun genişliği** - gizlendikten sonra atanan satır yüksekliği veya sütun genişliği.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unhide Row and Column Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.unhideRow(2, 13.5);
            worksheet.cells.unhideColumn(1, 8.5);

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
Gizli bir sütunu görünür yapmak için, önce daha önce atanan genişliğine veya orijinal genişliğine geri yüklemeniz gerekirse, lütfen negatif genişlik değeri ile sütunu gizlemeyi açın. Örneğin: worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **Satır ve Sütunları Gizle**  

Geliştiriciler, belirli bir satır veya sütunu gizlemek için sırasıyla [**hideRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRow-number-) ve [**hideColumn(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumn-number-) metodlarını çağırabilirler. Her iki yöntem de gizlenmek istenen satır ve sütun indekslerini parametre olarak alır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Hide Row/Column Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Hide the 3rd row (index 2) and 2nd column (index 1)
            worksheet.cells.hideRow(2);
            worksheet.cells.hideColumn(1);

            // Save the modified workbook and provide a download link
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding 3, 4 and 5 rows in the worksheet (rows are zero-based index)
            worksheet.cells.hideRows(2, 3);

            // Hiding 2 and 3 columns in the worksheet (columns are zero-based index)
            worksheet.cells.hideColumns(1, 2);

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

## **Kaydırma Çubuklarını Göster ve Gizle**  

Kaydırma çubukları, herhangi bir dosyanın içeriğini gezinmek için kullanılır. Genellikle iki tür kaydırma çubuğu bulunur:  

- Dikey kaydırma çubukları  
- Yatay kaydırma çubukları  

Microsoft Excel ayrıca yatay ve dikey kaydırma çubukları sağlar böylece kullanıcılar çalışma sayfası içeriğinde kaydırma yapabilirler. Aspose.Cells kullanarak geliştiriciler Excel dosyalarında her iki türde de kaydırma çubuklarının görünürlüğünü kontrol edebilirler.  

### **Kaydırma Çubuklarının Görünürlüğünü Kontrol Etmek**  

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasını yönetmek için geniş özellikler ve yöntemler içerir. Kaydırma çubuklarının görünürlüğünü kontrol etmek için [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) ve [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) özelliklerini kullanın. [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) ve [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) Boolean özellikleridir, bu da bu özelliklerin yalnızca **doğru** veya **yanlış** değerleri depolayabileceği anlamına gelir.  

#### **Kaydırma Çubuklarını Görünür Yapma**  

Kaydırma çubuklarını görünür hale getirmek için [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) veya [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) özelliğini **true** olarak ayarlayın.  

#### **Kaydırma çubuklarını gizleme**  

Kaydırma çubuklarını gizlemek için [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) veya [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) özelliğini **false** olarak ayarlayın.  

**Örnek Kod**  

Aşağıda, bir Excel dosyasını, book1.xls'yi açan, her iki kaydırma çubuğunu gizleyen ve ardından değiştirilmiş dosyayı output.xls olarak kaydeden tam bir kod bulunmaktadır.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Hide Scrollbars Example</h1>
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

            // Hiding the vertical scroll bar of the Excel file
            workbook.settings.isVScrollBarVisible = false;

            // Hiding the horizontal scroll bar of the Excel file
            workbook.settings.isHScrollBarVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scrollbars hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
