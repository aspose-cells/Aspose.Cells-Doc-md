---
title: Çerçeve Scriptleri ve Belge Özelliklerini JavaScript ile C++ kullanarak Dışa Aktarmayı Devre Dışı Bırak
linktitle: HTML e Aktarmayı Devre Dışı Bırak Çerçeve Betikleri ve Belge Özellikleri
type: docs
weight: 310
url: /tr/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Bir çalışma kitabını HTML ye dönüştürürken çerçeve scriptleri ve belge özelliklerini nasıl devre dışı bırakacağınızı öğrenin, Aspose.Cells for JavaScript kullanarak C++ ile.
--- 

{{% alert color="primary" %}}

 Aspose.Cells, bir çalışma kitabını HTML'ye dönüştürürken çerçeve scriptleri ve belge özelliklerini dışa aktarır. Aspose.Cells for JavaScript'in C++ sürümünün 8.6.0 versiyonu, bu özellikleri tercihe bağlı olarak devre dışı bırakma seçeneği getirir. Lütfen `HtmlSaveOptions.exportFrameScriptsAndProperties` özelliğini kullanarak dışa aktarımı devre dışı bırakın.

{{% /alert %}}

## **Çerçeve betikleri ve belge özelliklerinin dışa aktarılmasını devre dışı bırak**

Aşağıdaki örnek kod, çerçeve betikleri ve belge özelliklerinin dışa aktarılmasını devre dışı bırakmanıza olanak tanır. Bir çalışma kitabını HTML'e dönüştürdüğünüzde, çıktı dosyası herhangi bir çerçeve betiği ve belge özelliği içermez.

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable exporting frame scripts and document properties
            const options = new HtmlSaveOptions();
            options.exportFrameScriptsAndProperties = false;

            // Save workbook as HTML
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
