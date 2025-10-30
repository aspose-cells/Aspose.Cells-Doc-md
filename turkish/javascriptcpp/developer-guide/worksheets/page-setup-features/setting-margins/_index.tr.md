---
title: Kenarlık Ayarları JavaScript ile C++ kullanarak
linktitle: Kenar Boşlukları Ayarlama
type: docs
weight: 20
url: /tr/javascript-cpp/setting-margins/
description: Bu makalede, örnek kod kullanarak bir Excel çalışma sayfasının kenarlıklarını nasıl ayarlayacağınızı öğreneceksiniz. Ayrıca, JavaScript API kullanarak sayfa ortası, başlık ve altbilgi kenarlıklarını programlı olarak nasıl ayarlayacağınızı da öğrenin.
keywords: excel çalışma sayfası kenarlıklarını JavaScript ve C++ ile ortalamak, çalışma sayfası başlık ve altbilgi kenarlıklarını JavaScript ve C++ ile ayarlamak
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel'in sayfa düzeni seçeneklerini tamamen destekler. Geliştiriciler, baskı işlemini kontrol etmek için çalışma sayfaları için sayfa düzeni ayarlarını yapılandırabilirler. Bu konu, Aspose.Cells'ı kullanarak sayfa kenar boşluklarını yapılandırmanın nasıl yapıldığını tartışmaktadır.

{{% /alert %}}

## **Kenar Boşlukları Ayarlama**

Aspose.Cells for JavaScript, C++ ile [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfını sağlar ve bu sınıf bir Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir.

[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) özelliği, çalışma sayfası için sayfa düzenleme seçeneklerini ayarlamak amacıyla kullanılır. [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) özniteliği, baskılanacak çalışma sayfası için farklı sayfa düzeni seçenekleri ayarlamaya imkan sağlayan [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) sınıfının bir nesnesidir. [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) sınıfı, sayfa düzeni ayarlarını yapmak için çeşitli özellikler ve yöntemler sağlar.

### **Sayfa Kenar Boşlukları**

Sayfa kenarlıklarını (sol, sağ, üst, alt) [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) sınıf üyeleri kullanarak ayarlayın. Aşağıda belirtilen üyeler, sayfa kenarlıklarını belirtmek için kullanılır:

- [**PageSetup.leftMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#leftMargin--)
- [**PageSetup.rightMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#rightMargin--)
- [**PageSetup.topMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#topMargin--)
- [**PageSetup.bottomMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#bottomMargin--)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Page Margins Example</title>
    </head>
    <body>
        <h1>Set Page Margins Example</h1>
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
                // Proceed with a new empty workbook if no file selected
            }

            const file = fileInput.files.length ? fileInput.files[0] : null;
            let workbook;
            if (file) {
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheets = workbook.worksheets;
            const worksheet = worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            pageSetup.bottomMargin = 2;
            pageSetup.leftMargin = 1;
            pageSetup.rightMargin = 1;
            pageSetup.topMargin = 3;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetMargins_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page margins set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Sayfa Üzerinde Ortala**

Bir şeyi yatay ve dikey olarak sayfada ortalayabilirsiniz. Bunun için [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) sınıfının, [**PageSetup.centerHorizontally**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#centerHorizontally--) ve [**PageSetup.centerVertically**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#centerVertically--) üyeleri bazı kullanışlıdır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Center On Page</title>
    </head>
    <body>
        <h1>Center On Page Example</h1>
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
            // Create a workbook object (blank workbook)
            const workbook = new Workbook();

            // Get the worksheets in the workbook
            const worksheets = workbook.worksheets;

            // Get the first (default) worksheet
            const worksheet = worksheets.get(0);

            // Get the pagesetup object
            const pageSetup = worksheet.pageSetup;

            // Specify Center on page Horizontally and Vertically
            pageSetup.centerHorizontally = true;
            pageSetup.centerVertically = true;

            // Save the Workbook in Excel 97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CenterOnPage_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Üst Bilgi ve Alt Bilgi Kenar Boşlukları**

Başlık ve altbilgi kenar boşluklarını [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) sınıf üyeleri olan [**PageSetup.headerMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerMargin--) ve [**PageSetup.footerMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerMargin--) kullanarak ayarla.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Header/Footer Margins</title>
    </head>
    <body>
        <h1>Set Header/Footer Margins Example</h1>
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
            // Create a new workbook (equivalent to new AsposeCells.Workbook() in JavaScript)
            const workbook = new Workbook();

            // Get the worksheets collection
            const worksheets = workbook.worksheets;

            // Get the first (default) worksheet
            const worksheet = worksheets.get(0);

            // Get the pageSetup object
            const pageSetup = worksheet.pageSetup;

            // Specify Header / Footer margins (converted from setHeaderMargin/setFooterMargin)
            pageSetup.headerMargin = 2;
            pageSetup.footerMargin = 2;

            // Save the Workbook as Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CenterOnPage_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
