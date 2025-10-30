---
title: PDF ye kaydederken yorumları yazdırma  C++ kullanımıyla JavaScript
linktitle: PDF ye kaydederken Yorumları Yazdır
type: docs
weight: 10
url: /tr/javascript-cpp/print-comments-while-saving-to-pdf/
description: Excel dosyalarını PDF ye kaydederken yorumları yazdırmayı öğrenin  C++ ve Script ile.
---

{{% alert color="primary" %}}  

Microsoft Excel, aşağıdaki seçeneklerle PDF biçimine yazdırırken veya kaydederken yorumları yazdırmanıza izin verir  

- Hiçbiri  
- Sayfa sonunda  
- Sayfada gösterildiği gibi  

Aspose.Cells, aynı özelliği desteklemek için [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) enumunu sağlar. [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) enumunun aşağıdaki üyeleri vardır  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **PDF'ye kaydederken yorumları yazdır**  

Aşağıdaki örnek kod, yorumları PDF'ye kaydederken nasıl kullanılacağını gösterir [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) kullanımı.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Print Comments to PDF</title>
    </head>
    <body>
        <h1>Print Comments While Saving to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            const worksheet = workbook.worksheets.get(0);

            worksheet.pageSetup.printComments = AsposeCells.PrintCommentsType.PrintSheetEnd;

            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PrintCommentWhileSavingToPdf_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved to PDF with comments printed at sheet end. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
