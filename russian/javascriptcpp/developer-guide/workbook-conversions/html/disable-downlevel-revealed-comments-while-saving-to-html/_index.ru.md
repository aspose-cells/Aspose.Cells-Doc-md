---
title: Отключить раскрываемые комментарии Downlevel при сохранении в HTML с помощью JavaScript через C++
linktitle: Отключить отображение комментариев уровня Downlevel при сохранении в HTML
type: docs
weight: 20
url: /ru/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Узнайте, как отключить раскрываемые комментарии downlevel при сохранении Excel файла в HTML с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML, Aspose.Cells отображает Downlevel Conditional Comments. Эти условные комментарии актуальны для более старых версий Internet Explorer и не важны для современных браузеров. Подробнее об этом можно прочитать по ссылке.

- [Условный комментарий - условный комментарий с раскрытием](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for JavaScript через C++ позволяет избавиться от этих раскрываемых комментариев Downlevel, установив свойство [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--) в **true**.

## **Отключить отображение устаревших комментариев при сохранении в HTML**

Следующий пример показывает использование свойства [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--). Скриншот демонстрирует эффект этого свойства, когда оно не установлено в true. Загрузите [пример файла Excel](50528257.xlsx), использованный в этом коде, и [сгенерированный HTML](50528258.zip) для ознакомления.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Disable Downlevel Revealed Comments Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load sample workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable DisableDownlevelRevealedComments
            const opts = new HtmlSaveOptions();
            opts.disableDownlevelRevealedComments = true;

            // Save the workbook in html
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisableDownlevelRevealedComments_true.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML with DisableDownlevelRevealedComments = true. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
