---
title: C++ ile JavaScript Kullanarak Yazdırma Seçeneklerini Ayarlama
linktitle: Baskı Seçeneklerini Ayarlama
type: docs
weight: 40
url: /tr/javascript-cpp/setting-print-options/
description: Bu makale, JavaScript API ve C++ Kütüphanesi kullanarak Excel Çalışma Sayfası Sayfa Kurulumu özelliğinin Yazdırma Seçeneklerini programatik olarak nasıl ayarlayacağınızı gösterir. Yazdırma Alanı, Yazdırma Başlıkları ve Sayfa Sırası ayarlanabilir.
keywords: excel yazdırma alanı JavaScript ile C++ kullanarak ayarla, excel yazdırma başlıklarını JavaScript ile C++ kullanarak ayarla, excel sayfa sırasını JavaScript ile C++ kullanarak ayarla
---

{{% alert color="primary" %}}

Microsoft Excel'in sayfa düzeni ayarları, kullanıcıların çalışma sayfalarının nasıl basılacağını kontrol etmelerini sağlayan birkaç baskı seçeneği (ayrıca sayfa seçenekleri olarak da adlandırılır) sunar.

{{% /alert %}}

## **Baskı Seçeneklerini Ayarlama**

Bu baskı seçenekleri, kullanıcıların şunları yapmalarını sağlar:

- Çalışma sayfasında belirli bir baskı alanı seçin.
- Başlıkları yazdırın.
- Izgaraları yazdırın.
- Satır/sütun başlıklarını yazdırın.
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Hücre hatalarını yazdırın.
- Sayfa sıralamasını tanımlayın.

Aspose.Cells for JavaScript C++ ile Microsoft Excel tarafından sunulan tüm yazdırma seçeneklerini destekler ve geliştiriciler bu seçenekleri [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) sınıfı tarafından sunulan özellikleri kullanarak çalışma sayfaları için kolayca yapılandırabilir. Bu özelliklerin nasıl kullanılacağı aşağıda daha detaylı olarak anlatılmıştır.

### **Baskı Alanı Belirle**

Varsayılan olarak, baskı alanı veri içeren çalışma sayfasının tüm alanlarını içerir. Geliştiriciler, çalışma sayfasının belirli bir baskı alanını belirleyebilirler.

Belirli bir baskı alanı seçmek için, [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) sınıfının [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) özelliğini kullanın. Bu özelliğe baskı alanını tanımlayan bir hücre aralığı atayın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Print Area Example</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Specifying the cells range (from A1 cell to T35 cell) of the print area
            pageSetup.printArea = "A1:T35";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintArea_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Başlıkları Yazdırma**

Aspose.Cells, basılı bir çalışma sayfasının tüm sayfalarında tekrarlanacak satır ve sütun başlıklarını belirlemenize izin verir. Bunu yapmak için [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) sınıfının [**PageSetup.printTitleColumns**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleColumns--) ve [**PageSetup.printTitleRows**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleRows--) özelliklerini kullanın.

Tekrar edilecek satırlar veya sütunlar, satır veya sütun numaralarını geçirerek tanımlanır. Örneğin satırlar $1:$2 ve sütunlar $A:$B olarak tanımlanır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Title</title>
    </head>
    <body>
        <h1>Set Print Title Columns and Rows Example</h1>
        <p>You may optionally select an existing Excel file to modify. If no file is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Defining column numbers A & B as title columns
            pageSetup.printTitleColumns = "$A:$B";

            // Defining row numbers 1 & 2 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintTitle_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print title columns and rows set successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **Diğer Yazdırma Seçeneklerini Belirleme**

[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) sınıfı ayrıca aşağıdaki genel yazdırma seçeneklerini ayarlamak için birkaç başka özellik sunar:

- [**PageSetup.printGridlines**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printGridlines--): yazdırıp yazdırmamayı belirleyen bir Boolean özelliği.
- [**PageSetup.printHeadings**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printHeadings--): satır ve sütun başlıklarının yazdırılıp yazdırılmayacağını belirleyen bir Boolean özelliği.
- [**PageSetup.blackAndWhite**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#blackAndWhite--): çalışma sayfasını siyah beyaz modda yazdırıp yazdırmayacağını belirleyen bir Boolean özellik.
- [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--): çalışma sayfasında yazdırma yorumlarını göstermenip göstermeyeceğini veya sayfanın sonunda gösterip göstermeyeceğini tanımlar.
- [**PageSetup.printDraft**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printDraft--): grafikleri olmadan sayfayı yazdırıp yazdırmayacağını tanımlayan bir boolean özelliği.
- [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--): Hücre hatalarını, görüntülendiği gibi, boş, çizgi veya N/A olarak yazdırmayı tanımlar.

[**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) ve [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--) özelliklerini ayarlamak için Aspose.Cells for JavaScript C++ ile iki adet sıralama dizisi sağlar, [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) ve [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype), bunlar sırasıyla [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) ve [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--) özelliklerine atanacak önceden tanımlanmış değerleri içerir.

[**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) enumundaki önceden tanımlanmış değerler aşağıda listelenmiş ve açıklamalarıyla birlikte verilmiştir.

|**Yazdırma Yorumları Türleri**|**Açıklama**|
| :- | :- |
|PrintInPlace| Çalışma sayfasında görüntülenen yorumları yazdırmayı belirtir.
|PrintNoComments| Yorumları yazdırmamayı belirtir.
|PrintSheetEnd| Yorumları çalışma sayfasının sonunda yazdırmayı belirtir.

[**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype) enumundaki önceden tanımlanmış değerler aşağıda listelenmiş ve açıklamalarıyla birlikte verilmiştir.

|**Yazdırma Hataları Türleri**|**Açıklama**|
| :- | :- |
|PrintErrorsBlank| Hataları yazdırmamayı belirtir.
|PrintErrorsDash| Hataları "--" olarak yazdırmayı belirtir.
|PrintErrorsDisplayed| Hataları görüntülendiği gibi yazdırmayı belirtir.
|PrintErrorsNA| Hataları "#N/A" olarak yazdırmayı belirtir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Other Print Options</title>
    </head>
    <body>
        <h1>Other Print Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintCommentsType, PrintErrorsType } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = PrintErrorsType.PrintErrorsNA;

            // Saving the modified workbook to Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OtherPrintOptions_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Sayfa Sırasını Belirleme**

[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) sınıfı, yazdırılacak birden fazla sayfayı sıralamak için kullanılan [**PageSetup.order**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#order--) özelliği sağlar. Sayfaları sıralamanın iki olasılığı vardır.

-  sağa doğru herhangi bir sayfa yazdırmadan önce tüm sayfaları alt alta yazdırır.
-  aşağıdaki sayfaları yazdırmadan önce soldan sağa sayfaları yazdırır.

Aspose.Cells, tüm önceden tanımlanmış sıralama türlerini içeren [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype) enumunu sağlar.

[**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype) enumunun önceden tanımlanmış değerleri aşağıda listelenmiştir.

|**Yazdırma Sıralama Türleri**|**Açıklama**|
| :- | :- |
|DownThenOver|Aşağıdan önce ardından sıralama temsil eder.
|OverThenDown|Ardından aşağıdan önce sıralama temsil eder.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Set Page Order Example</title>
    </head>
    <body>
        <h1>Set Page Order Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintOrderType } = AsposeCells;

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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;
            pageSetup.order = PrintOrderType.OverThenDown;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPageOrder_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page order set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
