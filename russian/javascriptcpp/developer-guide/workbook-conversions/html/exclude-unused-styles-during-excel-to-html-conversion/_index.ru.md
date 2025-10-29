---
title: Исключение неиспользуемых стилей при преобразовании Excel в HTML с помощью JavaScript через C++
linktitle: Исключить неиспользуемые стили во время конвертации Excel в HTML
type: docs
weight: 30
url: /ru/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Узнайте, как исключить неиспользуемые стили при преобразовании Excel в HTML с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**  

Файлы Microsoft Excel могут содержать много неиспользуемых стилей. При экспорте файла Excel в HTML эти неиспользуемые стили также экспортируются, что может увеличить размер HTML. Можно исключить неиспользуемые стили при преобразовании Excel в HTML с помощью свойства [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--). При установке его в **true**, все неиспользуемые стили исключаются из выходного HTML. Следующий скриншот показывает пример неиспользуемого стиля внутри сформированного HTML.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Исключить неиспользуемые стили во время преобразования Excel в HTML**  

Следующий пример кода создает рабочую книгу и также создает неиспользуемый именованный стиль. Так как [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--) установлено в **true**, этот неиспользуемый стиль не будет экспортирован в [выходной HTML](61767778.zip). Но если установить его в **false**, этот неиспользуемый стиль будет присутствовать внутри HTML, что видно в разметке, как показано в предыдущем скриншоте.  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Exclude Unused Styles</title>
    </head>
    <body>
        <h1>Exclude Unused Styles from Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

            if (fileInput.files.length > 0 && fileInput.files[0].size === 0) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a valid Excel file.</p>';
                return;
            }

            // Instantiate workbook from selected file or create a new one
            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Create an unused named style
            const style = wb.createStyle();
            style.name = "UnusedStyle_XXXXXXXXXXXXXX";

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some value in cell C7
            const cell = ws.cells.get("C7");
            cell.value = "This is sample text.";

            // Specify html save options, we want to exclude unused styles
            const opts = new HtmlSaveOptions();
            // Comment this line to include unused styles
            opts.excludeUnusedStyles = true;

            // Save the workbook in html format
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExcludeUnusedStylesInExcelToHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML generated successfully. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
