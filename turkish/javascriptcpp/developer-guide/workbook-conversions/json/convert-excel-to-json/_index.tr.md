---
title: Excel’i JSON’a Dönüştürmek, JavaScript ve C++ kullanarak
linktitle: Excel i JSON a Dönüştür
type: docs
weight: 300
url: /tr/javascript-cpp/convert-excel-to-json/
description: Bir Excel dosyasını JSON’a dönüştürmenin nasıl yapıldığını Aspose.Cells for JavaScript kullanarak C++ ile öğrenin.
keywords: Çalışma Kitabını JSON JavaScript e C++ ile İçe Aktarma, Excel i JSON JavaScript e C++ ile Dönüştürme
---

{{% alert color="primary" %}}  
Aspose.Cells, bir Workbook'un JSON (JavaScript Nesne Gösterimi) dosyasına dönüştürülmesini destekler.  
{{% /alert %}}  

## **Excel Çalışma Kitabını JSON'a Dönüştür**  

Excel Çalışma Kitabını JSON'a dönüştürmenin nasıl yapılacağını merak etmeye gerek yok, çünkü Aspose.Cells for JavaScript C++ kütüphanesi en iyi çözümü sağlar. Aspose.Cells API, tabloları JSON formatına dönüştürmeye destek sağlar. Çalışma kitabını JSON'a dışa aktarmak için, [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) metodunun ikinci parametresi olarak [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/) iletiniz. Ayrıca, sayfayı JSON'a dışa aktarma için ek ayarlar belirtmek üzere [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions/) sınıfını da kullanabilirsiniz.  

Aşağıdaki kod örneği, Excel Workbook'u JSON'a dışa aktarmayı gösterir. Kaynak dosyayı ([sample.xlsx](sample.xlsx)) JSON dosyasına dönüştürmek için kodu kullanın ve referans için sunulmuştur.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to JSON Example</h1>
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

            // Convert the workbook to JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to JSON completed. Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```  

Aşağıdaki kod örneği, JsonSaveOptions sınıfını kullanarak ek ayarları belirler ve Excel Workbook'u JSON'a dışa aktarmayı gösterir. Kaynak dosya ([sample.xlsx](sample.xlsx))'yi JSON dosyasına dönüştürmek için kodu inceleyebilirsiniz.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, JsonSaveOptions, Utils } = AsposeCells;

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

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an options of saving the file.
            const options = new JsonSaveOptions();

            // Set the exporting range.
            options.exportArea = CellArea.createCellArea("B1", "C4");

            // Convert the workbook to json file.
            const outputData = workbook.save(SaveFormat.Json, options);

            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```
