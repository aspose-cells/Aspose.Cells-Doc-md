---
title: JavaScript kullanarak Excel Çalışma Sayfasını bölmeden ekranını bölme C++ ile
linktitle: Bölünmüş Ekran
type: docs
weight: 190
url: /tr/javascript-cpp/how-to-split-screen-of-excel-worksheet
description: Bu yazıda, çalışma sayfasını iki veya dört bölüme ayırarak belirli satır ve/veya sütunları ayrı panellerde göstermek için programatik olarak JavaScript ve C++ Eklentisi kullanmayı öğreneceksiniz.
keywords: Üst satırları dondurun, Üst satırı dondurun.
---

## **Giriş**

Bu makalede, çalışma sayfasını iki veya dört parçaya bölerek belirli satır ve/veya sütunları ayrı bölmelerde görüntülemenin C++ kullanılarak programatik olarak nasıl yapılacağı anlatılacaktır. Büyük veri setleriyle çalışırken, aynı çalışma sayfasındaki birkaç alanı aynı anda görmemiz gerekebilir, böylece farklı alt kümeleri karşılaştırabiliriz. Bölme ekran fonksiyonu ihtiyacınızı karşılayabilir.

## **Excel'de ekranı nasıl bölebilirsiniz**
Bir elektronik tabloyu ikiye veya dörde bölmek için aşağıdakileri yapın:

1. Bölme yapmak istediğiniz satır/sütun/hücreyi seçin.
2. Görünüm sekmesinde, Pencereler grubunda, Böl düğmesini tıklayın.

**![Bölünmüş Ekran](Bölünmüş-Ekran.png)**

## **Excel'de sütunlara dik olarak elektronik tabloyu bölmek**

Elektronik tablonun farklı alanlarını dikey olarak ayırmak için, bölmenin görünmesini istediğiniz sütunun sağındaki sütunu seçin ve Excel'de Böl düğmesini tıklayın.

C++ ile Aspose.Cells for JavaScript kullanarak sütunlar üzerinde dikey bölme yapmak kolaydır; yalnızca üst satırda aktif hücre olarak bir hücre seçmek ve sonra [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--) yöntemiyle bölmek yeterlidir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Split Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Sets C1 cell in the top row as the active cell.
            sheet.activeCell = "C1";

            // Split worksheet vertically on columns
            sheet.split();

            // Save the modified workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Satırlara yatay olarak elektronik tabloyu bölmek**
Excel'de pencerenizi yatay olarak ayırmak için, bölmeyi istediğiniz satırın altındaki satırı seçin.

C++ ile Aspose.Cells for JavaScript kullanarak satırları yatay olarak bölmek de kolaydır; yalnızca sol sütunda aktif hücre olarak bir hücre seçmek ve sonra [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--) yöntemiyle bölmek yeterlidir.

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Sets A6 cell in the left column as the active cell.
            sheet.activeCell = "A6";

            // Split worksheet horizontally on rows
            sheet.split();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Elektronik tabloyu dört bölüme ayırmak**
Aynı elektronik tablonun dört farklı bölümünü aynı anda görüntülemek için, Excel'de ekranınızı hem dikey hem yatay olarak bölebilirsiniz.

C++ ile Aspose.Cells for JavaScript kullanarak sütunlar üzerinde dikey bölme yapmak da kolaydır; yalnızca ilk satır ve sütun dışında bir hücreyi aktif hücre olarak seçmek ve sonra [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--) yöntemiyle bölmek yeterlidir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Active Cell and Split Worksheet Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Split Worksheet Example</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Sets E6 cell as the active cell.
            sheet.activeCell = "E6";

            // Split worksheet into four parts
            sheet.split();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet updated successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Bölünmüş bölgeyi kaldırmak için**
Elektronik tabloyu bölme ayarını kaldırmak için, sadece Böl düğmesini tekrar tıklayın.

C++ ile Aspose.Cells for JavaScript [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--) yöntemi sunar, bölme ayarını kaldırmak için.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Split Worksheet Example</title>
    </head>
    <body>
        <h1>Split Worksheet Example</h1>
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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Remove split and then split worksheet into four parts
            sheet.removeSplit();
            sheet.split();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet split operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
