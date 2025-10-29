---
title: Избегайте экспоненциальной нотации больших чисел при импорте из HTML
linktitle: Избегайте экспоненциальной нотации больших чисел при импорте из HTML
type: docs
weight: 10
url: /ru/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Узнайте, как предотвращать преобразование больших чисел в экспоненциальный формат при импорте из HTML с помощью Aspose.Cells for JavaScript через C++.
--- 

{{% alert color="primary" %}}  

Иногда ваш HTML содержит числа вроде 1234567890123456, которые длиннее 15 цифр, и при импорте в Excel эти числа преобразуются в экспоненциальную нотацию, например 1.23457E+15. Если вы хотите импортировать число как есть без преобразования в экспоненциальную нотацию, используйте свойство [**HtmlLoadOptions.keepPrecision**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#keepPrecision--) и установите его в **true** при загрузке HTML.  

{{% /alert %}}  

Следующий пример кода объясняет использование свойства [**HtmlLoadOptions.keepPrecision**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#keepPrecision--). API импортирует число как есть, без преобразования в экспоненциальное нотацию.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat } = AsposeCells;

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
            // Sample Html containing large number with digits greater than 15
            const html = "<html><body><p>1234567890123456</p></body></html>";

            // Convert Html to byte array
            const byteArray = new TextEncoder().encode(html);

            // Set Html load options and keep precision true
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);
            loadOptions.keepPrecision = true;

            // Convert byte array into stream
            const stream = byteArray;

            // Create workbook from stream with Html load options
            const workbook = new Workbook(stream, loadOptions);

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Auto fit the sheet columns
            sheet.autoFitColumns();

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAvoidExponentialNotationWhileImportingFromHtml.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```
