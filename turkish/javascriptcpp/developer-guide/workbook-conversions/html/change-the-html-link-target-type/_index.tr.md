---
title: JavaScript ile HTML Bağlantı Hedef Türünü Değiştirme
linktitle: HTML Bağlantısı Hedef Türünü Değiştirme
type: docs
weight: 320
url: /tr/javascript-cpp/change-the-html-link-target-type/
description: Aspose.Cells for JavaScript i C++ kullanarak HTML bağlantı hedef türünü değiştirmeyi öğrenin. HTML bağlantılarınızda hedef özniteliğini kontrol edin.
---

{{% alert color="primary" %}}

Aspose.Cells, HTML bağlantı hedef türünü değiştirmenize olanak tanır. HTML bağlantısı şuna benzer

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Yukarıdaki HTML bağlantısında hedef özniteliği **_self**. Bu hedef özniteliğini [**HtmlSaveOptions.linkTargetType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#linkTargetType--) özelliği ile kontrol edebilirsiniz. Bu özellik, aşağıdaki değerleri alan [**HtmlLinkTargetType**](https://reference.aspose.com/cells/javascript-cpp/htmllinktargettype) enum'ünü kabul eder.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

Aşağıdaki kod [**HtmlSaveOptions.linkTargetType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#linkTargetType--) özelliğinin kullanımını gösterir. Bağlantı hedef türünü **blank** yapar. Varsayılan ise **parent**.

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
