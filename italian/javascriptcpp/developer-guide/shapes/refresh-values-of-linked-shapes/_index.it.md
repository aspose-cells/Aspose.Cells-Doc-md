---
title: Aggiorna i valori delle forme collegate con JavaScript tramite C++
linktitle: Aggiorna i valori delle forme collegate
type: docs
weight: 3200
url: /it/javascript-cpp/refresh-values-of-linked-shapes/
description: Impara come aggiornare i valori delle forme collegate in Excel usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}

A volte hai una forma collegata nel tuo file Excel che è collegata a una cella. In Microsoft Excel, cambiare il valore della cella collegata modifica anche il valore della forma collegata. Funziona anche con Aspose.Cells for JavaScript via C++ se desideri salvare la cartella di lavoro in formato XLS o XLSX. Tuttavia, se desideri salvare la cartella di lavoro in formato PDF o HTML, dovrai chiamare il metodo [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--) per aggiornare il valore della forma collegata.

{{% /alert %}}

## Esempio

Lo screenshot seguente mostra il file Excel di origine utilizzato nel codice di esempio qui sotto. Ha un'immagine collegata collegata alle celle A1 a E4. Modificheremo il valore della cella B4 con Aspose.Cells e poi chiameremo il metodo [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--) per aggiornare il valore dell'immagine e salvarlo in formato PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Puoi scaricare il [file Excel di origine](95584291.xlsx) e il [PDF di output](95584292.pdf) dai link forniti.

### Codice JavaScript per aggiornare i valori delle forme collegate

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh Value Of Linked Shapes Example</title>
    </head>
    <body>
        <h1>Refresh Value Of Linked Shapes Example</h1>
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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Change the value of cell B4
            const cell = worksheet.cells.get("B4");
            cell.value = 100;

            // Update the value of the Linked Picture which is linked to cell B4
            worksheet.shapes.updateSelectedValue();

            // Save the workbook in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRefreshValueOfLinkedShapes.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
