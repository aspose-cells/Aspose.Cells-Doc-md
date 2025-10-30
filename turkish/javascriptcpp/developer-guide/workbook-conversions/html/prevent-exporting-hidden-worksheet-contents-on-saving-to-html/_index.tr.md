---
title: JavaScript kullanarak C++ ile HTML ye Kaydederken Gizli Çalışma Sayfası İçeriğinin Dışa Aktarılmasını Engelleyin
linktitle: HTML ye Kaydederken Gizli Çalışma Sayfası İçeriğinin Dışa Aktarılmasını Engelleyin
type: docs
weight: 210
url: /tr/javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Excel dosyalarını HTML ye kaydederken gizli çalışma sayfası içeriğinin dışa aktarımını nasıl engelleyeceğinizi öğrenin, Aspose.Cells for JavaScript kullanarak C++ üzerinden.
---

{{% alert color="primary" %}}

Excel çalışma kitaplarını HTML olarak kaydedebilirsiniz. Ancak, çalışma kitabı gizli çalışma sayfalarını içeriyorsa, Aspose.Cells varsayılan olarak gizli çalışma sayfası içeriğini (_files) dizinine dışa aktarır. Bu dizin, çalışma sayfaları, resimler, tabstrip.htm, stylesheet.css gibi dosyalar içerir. Bazı durumlarda, gizli çalışma sayfalarının bu şekilde içeriğinin dışa aktarılması uygun olmayabilir. Örneğin, gizli çalışma sayfası dışa aktarılmaması gereken resimler içeriyorsa.

{{% /alert %}}

Aspose.Cells for JavaScript, [**HtmlSaveOptions.exportHiddenWorksheet**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportHiddenWorksheet--) özelliğini sağlar. Varsayılan olarak, **true** olarak ayarlanmıştır ve gizli çalışma sayfaları HTML'ye alınır. Bunu **false** yaparsanız, Aspose.Cells gizli çalışma sayfası içeriğini dışa aktarmayacaktır.

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
