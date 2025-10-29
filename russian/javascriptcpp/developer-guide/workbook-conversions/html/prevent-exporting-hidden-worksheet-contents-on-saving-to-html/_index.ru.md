---
title: Предотвращение экспорта скрытого содержимого листа при сохранении в HTML с помощью JavaScript через C++
linktitle: Предотвращение экспорта скрытого содержимого листа при сохранении в HTML
type: docs
weight: 210
url: /ru/javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Узнайте, как предотвратить экспорт скрытого содержимого листов при сохранении Excel файлов в HTML с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}

Вы можете сохранять книги Excel в HTML. Однако, если в книге есть скрытые листы, Aspose.Cells по умолчанию экспортирует скрытое содержимое листа в выходной каталог HTML (_files), который содержит файлы, такие как листы, изображения, tabstrip.htm, stylesheet.css и т. д. Иногда экспорт содержимого скрытых листов таким образом нецелесообразен. Например, если скрытый лист содержит изображения, которые не должны быть экспортированы в каталог _files.

{{% /alert %}}

Aspose.Cells for JavaScript через C++ предоставляет свойство [**HtmlSaveOptions.exportHiddenWorksheet**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportHiddenWorksheet--). По умолчанию оно установлено в **true**, и скрытые листы экспортируются в HTML. Если установить его в **false**, Aspose.Cells не будет экспортировать содержимое скрытых листов.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - HTML Without Hidden Content</title>
    </head>
    <body>
        <h1>Save Workbook as HTML Without Hidden Worksheet Content</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and do not export hidden worksheet contents
            const options = new HtmlSaveOptions();
            options.exportHiddenWorksheet = false;

            // Save workbook to HTML format using the options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HtmlWithoutHiddenContent_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved to HTML without hidden content. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
