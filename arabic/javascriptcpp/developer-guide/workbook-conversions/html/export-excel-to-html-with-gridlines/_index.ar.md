---
title: تصدير إكسل إلى HTML بخطوط الشبكة باستخدام via JavaScript
linktitle: تصدير Excel إلى HTML مع خطوط الشبكة
type: docs
weight: 40
url: /ar/javascript-cpp/export-excel-to-html-with-gridlines/
description: تعرّف على كيفية تصدير ملف إكسل إلى صيغة HTML مع خطوط الشبكة باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}

إذا كنت ترغب في تصدير ملف إكسل الخاص بك إلى HTML بخطوط الشبكة، يرجى استخدام خاصية [HtmlSaveOptions.exportGridLines()](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportGridLines--) وتعيينها على **true**.

{{% /alert %}}
## **تصدير Excel إلى HTML مع خطوط الشبكة**
يعرض الكود النموذجي التالي إنشاء مجلد عمل، وملئه بقيم، ثم حفظه بصيغة HTML بعد ضبط [HtmlSaveOptions.exportGridLines()](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportGridLines--) إلى **true**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Export To HTML With GridLines Example</title>
    </head>
    <body>
        <h1>Export To HTML With GridLines Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions, SaveFormat } = AsposeCells;

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
            // Create your workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Fill worksheet with some integer values
            for (let r = 0; r < 10; r++) {
                for (let c = 0; c < 10; c++) {
                    const cell = ws.cells.get(r, c);
                    cell.value = r * 1;
                }
            }

            // Save your workbook in HTML format and export gridlines
            const opts = new HtmlSaveOptions();
            opts.exportGridLines = true;

            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ExportToHTMLWithGridLines_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
