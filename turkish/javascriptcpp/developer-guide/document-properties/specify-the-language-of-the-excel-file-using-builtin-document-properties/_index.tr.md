---
title: BuiltIn Document Properties kullanarak Excel Dosyasının Dilini JavaScript ile C++ kullanarak belirtin
linktitle: Dahili Belge Özelliklerini Kullanarak Excel Dosyasının Dilini Belirtme
type: docs
weight: 30
url: /tr/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Olası Kullanım Senaryoları**

Bir Excel dosyasının dilini sağ tıklayarak Dosya özelliklerinden > Ayrıntılar seçerek ve Dil alanını düzenleyerek değiştirebilirsiniz. Lütfen bunu programlı olarak değiştirmek için [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--) özelliğini kullanın ve C++ API'leriyle Aspose.Cells for JavaScript kullanın.

## **Dahili Belge Özelliklerini Kullanarak Excel Dosyasının Dilini Belirtme**

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve bu kitabın dil adlı dahili belge özelliğini değiştirir. Bu kod tarafından oluşturulan [çıktı Excel dosyasını](64716891.xlsx) ve modifiye edilen Dil alanını gösteren ekran görüntüsünü inceleyin.

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Language Using BuiltInDocumentProperties</h1>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Create workbook object.
            const wb = new Workbook();

            // Access built-in document property collection.
            const bdpc = wb.builtInDocumentProperties;

            // Set the language of the Excel file.
            bdpc.language = "German, French";

            // Save the workbook in xlsx format.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Language set successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
