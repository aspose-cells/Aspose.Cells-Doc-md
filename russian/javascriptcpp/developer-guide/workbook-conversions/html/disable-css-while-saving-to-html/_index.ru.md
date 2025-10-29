---
title: Отключить CSS при сохранении в HTML с помощью JavaScript через C++
linktitle: Отключить CSS при сохранении в HTML
type: docs
weight: 320
url: /ru/javascript-cpp/disable-css-while-saving-to-html/
description: Узнайте, как отключить CSS при сохранении Excel файлов в HTML с помощью Aspose.Cells for JavaScript через C++. 
---

## **Возможные сценарии использования**

При сохранении файла Excel в одностраничный HTML, CSS-элементы обычно внедряются в HTML и размещаются в разделе HEAD. Если вы вставите такой файл как содержание/тело письма, большинство почтовых клиентов удалит CSS и произойдет неправильное отображение. В версии Aspose.Cells 24.12 появилась возможность по желанию отключить CSS, чтобы стили применялись непосредственно к HTML-элементам. Для установки HTML в качестве содержимого тела письма используйте свойство [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--) и установите его в **true**.

## **Отключить CSS при сохранении в HTML**

Следующий пример показывает использование свойства [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--). 

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Disable CSS Example</title>
    </head>
    <body>
        <h1>Disable CSS Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const opts = new HtmlSaveOptions();
            opts.disableCss = true;

            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisable.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file generated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
