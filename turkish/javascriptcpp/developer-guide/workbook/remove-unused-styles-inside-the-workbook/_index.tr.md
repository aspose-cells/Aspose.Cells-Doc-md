---
title: Kullanilmayan Stilleri JavaScript ile C++ kullanarak Çalışma Kitabından Kaldırın
linktitle: Çalışma Kitabı İçinde Kullanılmayan Stilleri Kaldırma
type: docs
weight: 340
url: /tr/javascript-cpp/remove-unused-styles-inside-the-workbook/
description: C++ kullanarak Aspose.Cells for JavaScript ile bir çalışma kitabından kullanılmayan stilleri kaldırmayı öğrenin.
---

{{% alert color="primary" %}}  
Excel dosyalarındaki kullanılmayan stiller sadece yer kaplamaz, aynı zamanda PDF, HTML vb. farklı formatlara dönüştürürken performans sorunlarına da neden olur. Aspose.Cells, çalışma kitabındaki tüm kullanılmayan stilleri kaldırmanızı sağlayan [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#removeUnusedStyles--) sağlar.  
{{% /alert %}}  

Aşağıdaki kod, [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#removeUnusedStyles--) kullanımını açıklar. Kod, sağlanan bağlantıdan indirilebilecek şablon Excel dosyasını yükler. Bu dosyada **AsposeStyle** adlı kullanılmayan bir stil bulunmaktadır; bu stil ve diğer tüm kullanılmayan stiller, kod yürütüldükten sonra kaldırılacaktır.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Unused Styles</title>
    </head>
    <body>
        <h1>Remove Unused Styles Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Remove all unused styles inside the workbook
            workbook.removeUnusedStyles();

            // Save the modified workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Unused styles removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
