---
title: Скрывать наложенное содержание с помощью CrossHideRight при сохранении в HTML с помощью JavaScript через C++
linktitle: Скрытие перекрывающегося контента с помощью CrossHideRight при сохранении в HTML
type: docs
weight: 100
url: /ru/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML вы можете указать разные типы пересечения для строк ячеек. По умолчанию Aspose.Cells генерирует HTML по Microsoft Excel, но если изменить тип пересечения на [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype), то все строки справа от ячейки, наложенные или перекрывающиеся с содержимым ячейки, скрываются.

## **Скрытие перекрывающегося содержимого с CrossHideRight при сохранении в Html**

Следующий пример загрузит [образец файла Excel](64716894.xlsx), сохранит его в [выходной HTML](64716893.zip), установив [**HtmlSaveOptions.htmlCrossStringType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#htmlCrossStringType--) в [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). Скриншот показывает, как [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) влияет на вывод HTML по умолчанию.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hiding Overlaid Content With CrossHideRight While Saving To Html</title>
    </head>
    <body>
        <h1>Hiding Overlaid Content With CrossHideRight While Saving To Html</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.htmlCrossStringType = AsposeCells.HtmlCrossType.CrossHideRight;

            // Save to HTML with HtmlSaveOptions
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
