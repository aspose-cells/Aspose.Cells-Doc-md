---
title: Imprimir comentarios al guardar en PDF con JavaScript vía C++
linktitle: Imprimir comentarios al guardar en PDF
type: docs
weight: 10
url: /es/javascript-cpp/print-comments-while-saving-to-pdf/
description: Aprende cómo imprimir comentarios al guardar documentos de Excel en PDF usando Aspose.Cells for JavaScript vía C++.
---

{{% alert color="primary" %}}  

Microsoft Excel te permite imprimir comentarios al imprimir o guardar en formato PDF con las siguientes opciones  

- Ninguno  
- Al final de la hoja  
- Según se muestra en la hoja  

Aspose.Cells proporciona el enumerado [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) para soportar la misma función. El enumerado [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) tiene los siguientes miembros  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **Imprimir comentarios al guardar en PDF**  

El siguiente código de ejemplo ilustra cómo usar [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) para imprimir comentarios al guardar en PDF.  

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
