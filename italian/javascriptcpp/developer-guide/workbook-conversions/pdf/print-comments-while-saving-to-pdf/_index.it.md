---
title: Stampa commenti durante il salvataggio in PDF con JavaScript via C++
linktitle: Stampa commenti durante il salvataggio in PDF
type: docs
weight: 10
url: /it/javascript-cpp/print-comments-while-saving-to-pdf/
description: Impara come stampare commenti durante il salvataggio di documenti Excel in PDF usando Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  

Microsoft Excel consente di stampare i commenti durante la stampa o il salvataggio nel formato PDF con le seguenti opzioni  

- Nessuna  
- Alla fine del foglio  
- Come visualizzato nel foglio  

Aspose.Cells fornisce l'enumerazione [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) per supportare la stessa funzionalità. L'enumerazione [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) ha i seguenti membri  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **Stampa commenti durante il salvataggio in PDF**  

Il seguente esempio di codice illustra come usare [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) per stampare commenti durante il salvataggio in PDF.  

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
