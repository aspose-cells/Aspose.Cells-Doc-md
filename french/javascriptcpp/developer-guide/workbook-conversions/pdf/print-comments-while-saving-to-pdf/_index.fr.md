---
title: Imprimer les commentaires lors de l enregistrement en PDF avec JavaScript via C++
linktitle: Imprimer les commentaires lors de l enregistrement au format PDF
type: docs
weight: 10
url: /fr/javascript-cpp/print-comments-while-saving-to-pdf/
description: Apprendre comment imprimer les commentaires lors de l enregistrement des documents Excel en PDF en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  

Microsoft Excel permet d'imprimer les commentaires lors de l'impression ou de l'enregistrement au format PDF avec les options suivantes  

- Aucun  
- À la fin de la feuille  
- Tel qu'affiché sur la feuille  

Aspose.Cells fournit l'énumération [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) pour supporter la même fonctionnalité. L'énumération [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) a les membres suivants  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **Imprimer les commentaires lors de l'enregistrement au format PDF**  

Le code d'exemple suivant illustre comment utiliser [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) pour imprimer les commentaires lors de l'enregistrement en PDF.  

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
