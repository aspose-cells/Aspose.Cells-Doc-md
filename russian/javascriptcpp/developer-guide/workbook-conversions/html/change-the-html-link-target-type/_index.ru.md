---
title: Изменение типа целевой ссылки HTML с помощью JavaScript через C++
linktitle: Изменить тип HTML ссылки
type: docs
weight: 320
url: /ru/javascript-cpp/change-the-html-link-target-type/
description: Узнайте, как изменить тип целевой ссылки HTML с помощью Aspose.Cells for JavaScript через C++. Управляйте атрибутом target в ваших HTML ссылках.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет вам изменять тип целевой ссылки HTML. HTML-ссылка выглядит так

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Как видите, атрибут target в указанной HTML-ссылке — **_self**. Вы можете управлять этим атрибутом, используя свойство [**HtmlSaveOptions.linkTargetType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#linkTargetType--). Это свойство принимает перечисление [**HtmlLinkTargetType**](https://reference.aspose.com/cells/javascript-cpp/htmllinktargettype), которое имеет следующие значения.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

Следующий пример кода демонстрирует использование свойства [**HtmlSaveOptions.linkTargetType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#linkTargetType--). Он меняет тип целевой ссылки на **blank**. По умолчанию он **parent**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlLinkTargetType, Utils } = AsposeCells;

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

            // Create HTML save options and set link target type
            const opts = new HtmlSaveOptions();
            opts.linkTargetType = HtmlLinkTargetType.Self;

            // Save the workbook to HTML using the save options
            const outputData = workbook.save(SaveFormat.Html, opts);

            // Create a downloadable blob for the resulting HTML
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = `<p style="color: green;">File converted and ready for download: ${downloadLink.download}</p>`;
        });
    </script>
</html>
```
