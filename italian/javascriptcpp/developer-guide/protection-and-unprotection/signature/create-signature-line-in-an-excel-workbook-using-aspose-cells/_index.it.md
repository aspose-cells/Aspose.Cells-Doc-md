---
title: Crea Linea di Firma in un Workbook Excel utilizzando Aspose.Cells for JavaScript via C++
linktitle: Crea LINEA FIRMA in un workbook Excel utilizzando Aspose.Cells
type: docs
weight: 150
url: /it/javascript-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Questo articolo descrive come creare una Linea di Firma in un Workbook Excel utilizzando codice JavaScript con Aspose.Cells for JavaScript tramite C++.
keywords: Crea Linea di Firma in un Workbook Excel JavaScript tramite C++, come creare una Linea di Firma in un Workbook Excel, come aggiungere una Linea di Firma, come aggiungere una Linea di Firma al file Excel.
---

## **Introduzione**  

Microsoft Excel fornisce la funzionalità di aggiungere **Linea firma** in workbook Excel. È possibile aggiungere una linea di firma facendo clic sulla scheda **Inserisci** e quindi selezionando **Linea firma** dal gruppo **Testo**.  

## **Come Creare una Linea di Firma per Excel**  

 Aspose.Cells for JavaScript tramite C++ fornisce anche questa funzionalità ed espone la proprietà [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) a questo scopo. Questo articolo spiegherà come usare questa proprietà per aggiungere una Linea di Firma usando Aspose.Cells.  

Il codice di esempio seguente aggiunge una linea di firma usando la proprietà [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) e salva il workbook.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Signature Line Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SignatureLine, Utils } = AsposeCells;

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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create signature line object
            const signatureLine = new SignatureLine();
            signatureLine.signer = "John Doe";
            signatureLine.title = "Development Lead";
            signatureLine.email = "john.doe@aspose.com";

            // Adds a Signature Line to the first worksheet.
            workbook.worksheets.get(0).shapes.addSignatureLine(1, 1, signatureLine);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Signature line added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
