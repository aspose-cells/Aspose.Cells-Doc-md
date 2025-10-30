---
title: Çalışma Sayfalarını Kopyala ve Taşı, İşlevselliği İçinde ve İş kitapları Arasında, C++ ile JavaScript kullanarak
linktitle: Çalışma Kitapları Arasında ve İçinde Çalışma Sayfalarını Kopyalayın ve Taşıyın
type: docs
weight: 80
url: /tr/javascript-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Aspose.Cells for JavaScript kullanarak iş kitapları içinde ve arasında çalışma sayfalarının nasıl kopyalanıp taşınacağını öğrenin. Çalışma kitabı yapılarını verimli bir şekilde yönetin.
---

{{% alert color="primary" %}}

Bazen, ortak biçimlendirme ve veri girişi gerektiren sayısız çalışma sayfasına ihtiyacınız olabilir. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfaları olan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu vardır: bir sayfa oluşturarak ve ardından bunu üç kez kopyalayarak.

Aspose.Cells for JavaScript kullanarak C++ ile çalışma kitapları içinde veya arasında çalışma sayfalarının kopyalanmasını veya taşınmasını destekler. Veri, biçimlendirme, tablolar, matrisler, grafikler, resimler ve diğer nesneler dahil olmak üzere çalışma sayfaları en yüksek doğrulukla kopyalanır.

{{% /alert %}}

## **Çalışma Sayfalarını Kopyalama ve Taşıma**

### **Bir Çalışma Sayfasını Bir Çalışma Kitabı İçinde Kopyalama**

Tüm örnekler için ilk adımlar aynıdır.

1. Microsoft Excel'de bazı veriler içeren iki çalış kitabı oluşturun. Bu örneğin amaçları için, Microsoft Excel'de iki yeni çalışma kitabı oluşturduk ve çalışma sayfalarına bazı veriler girdik.

- İlkÇalışmaKitabı.xlsx (3 çalışsayfası).
- İkinciÇalışmaKitabı.xlsx (1 çalışsayfası).

1. Aspose.Cells'i indirin ve kurun:
   1. [Aspose.Cells for JavaScript indir](https://downloads.aspose.com/cells/javascript-cpp).
   1. Geliştirme bilgisayarınıza kurun.
      Tüm [Aspose](http://www.aspose.com/) bileşenleri yüklendiğinde değerlendirme modunda çalışır. Değerlendirme modunun bir zaman limiti yoktur ve yalnızca üretilen belgelere filigran enjekte eder.
1. Bir proje oluşturun:
   1. Geliştirme ortamınızı başlatın.
   1. Yeni bir konsol uygulaması oluşturun.
1. Referanslar ekleyin:
   1. Projeye Aspose.Cells'e bir başvuru ekleyin.
      Örneğin, ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll referansı ekleyin.
1. Bir çalışma kitabı içindeki çalışsayfayı kopyalama
   İlk örnek, İlkÇalışmaKitabı.xlsx içindeki ilk çalışsayfayı (Kopya) kopyalar.

Kod çalıştırıldığında, Kopya adlı çalışsayfa, İlkÇalışmaKitabı.xlsx içinde Last Sheet adıyla kopyalanır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Copy Worksheet Example</title>
    </head>
    <body>
        <h1>Copy Worksheet Example</h1>
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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Copy the first sheet of the first book within the workbook
            workbook.worksheets.get(2).copy(workbook.worksheets.get("Copy"));

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FirstWorkbookCopied_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Bir Çalışma Kitabı içinde bir Çalışsayfayı Taşıma**

Aşağıdaki kod, bir çalışma kitabı içindeki bir çalışsayfayı bir konumdan başka bir konuma taşımanın nasıl yapıldığını gösterir. Kod çalıştırıldığında, İlkÇalışmaKitabı.xlsx içindeki İndex 1'de Move olarak adlandırılan çalışsayfa, İndex 2'ye taşınır.

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Move the first sheet to index 1
            const worksheets = workbook.worksheets;
            const worksheet = worksheets.get(0);
            worksheet.moveTo(1);

            // Saving the modified Excel file and offering it for download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FirstWorkbookMoved_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet moved successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Kopylama**

Kodu yürütmek, Copy adlı sayfayı SecondWorkbook.xlsx içine Sheet2 adıyla kopyalar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Copy Worksheets Between Workbooks</h1>
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
            // Create two workbooks
            const excelWorkbook3 = new Workbook();
            const excelWorkbook4 = new Workbook();

            // Create source worksheet
            excelWorkbook3.worksheets.add("Copy");

            // Add new worksheet into second Workbook
            excelWorkbook4.worksheets.add();

            // Copy the first sheet of the first book into second book.
            excelWorkbook4.worksheets.get(1).copy(excelWorkbook3.worksheets.get("Copy"));

            // Save the file.
            const outputData = excelWorkbook4.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetsBetweenWorkbooks_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheets copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Taşıma**

Kod çalıştırıldığında, İlkÇalışmaKitabı.xlsx içindeki Move adlı çalışsayfa, İkinciÇalışmaKitabı.xlsx içine Sheet3 adıyla taşınır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Move Worksheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download First Workbook</a>
        <a id="downloadLink2" style="display: none;">Download Second Workbook</a>
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
            // Create new workbooks instead of opening existing files
            const excelWorkbook5 = new Workbook();
            const excelWorkbook6 = new Workbook();

            // Add New Worksheet
            excelWorkbook6.worksheets.add();

            // Copy the sheet from first book into second book.
            excelWorkbook6.worksheets.get(0).copy(excelWorkbook5.worksheets.get(0));

            // Remove the copied worksheet from first workbook
            excelWorkbook5.worksheets.removeAt(0);

            // Save the first workbook
            const outputData1 = excelWorkbook5.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'FirstWorkbookWithMove_out.xlsx';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download FirstWorkbookWithMove_out.xlsx';

            // Save the second workbook
            const outputData2 = excelWorkbook6.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'SecondWorkbookWithMove_out.xlsx';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download SecondWorkbookWithMove_out.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks processed successfully. Click the download links to retrieve the files.</p>';
        });
    </script>
</html>
```
