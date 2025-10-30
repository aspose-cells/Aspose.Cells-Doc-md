---
title: Excel den HTML ye Döküman, Çalışma Kitabı ve Çalışma Sayfası Özelliklerini Dışa Aktarma JavaScript ve C++ aracılığıyla
linktitle: Excel den HTML e belge çalışma kitabı ve çalışma sayfası özelliklerini dışa aktar
type: docs
weight: 50
url: /tr/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Excel den HTML ye Döküman, Çalışma Kitabı ve Çalışma Sayfası özelliklerini Aspose.Cells for JavaScript C++ kullanarak dışa aktarmayı öğrenin.
---

## **Olası Kullanım Senaryoları**  

Microsoft Excel dosyası Microsoft Excel veya Aspose.Cells for JavaScript C++ kullanılarak HTML'ye dışa aktarıldığında, aşağıdaki ekran görüntüsünde gösterildiği gibi çeşitli Döküman, Çalışma Kitabı ve Çalışma Sayfası özellikleri de dışa aktarılır. Bu özellikleri dışa aktarmamak için [**HtmlSaveOptions.exportDocumentProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportDocumentProperties--), [**HtmlSaveOptions.exportWorkbookProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorkbookProperties--) ve [**HtmlSaveOptions.exportWorksheetProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetProperties--) değerlerini **false** yapabilirsiniz. Bu özelliklerin varsayılan değeri **true**'dur. Aşağıdaki ekran görüntüsü, bu özelliklerin dışa aktarılan HTML'de nasıl göründüğünü gösterir.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Belge, Çalışma Kitabı ve Çalışma Sayfası Özelliklerini Excel'den HTML'e Dışa Aktar**  

Aşağıdaki örnek kod, [örnek Excel dosyasını](61767776.xlsx) yükler ve Belge, Çalışma Kitabı ve Çalışma Sayfası özelliklerini dışa aktarmadan HTML'ye dönüştürür [çıktı HTML'si](61767779.zip).  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export HTML without Properties</title>
    </head>
    <body>
        <h1>Export Excel to HTML (without document/workbook/worksheet properties)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

            // Load the sample Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // We do not want to export document, workbook and worksheet properties
            options.exportDocumentProperties = false;
            options.exportWorkbookProperties = false;
            options.exportWorksheetProperties = false;

            // Export the Excel file to Html with Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
