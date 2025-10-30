---
title: Misura la larghezza e l altezza del valore della cella in unità di pixel
linktitle: Misura la dimensione
type: docs
weight: 260
url: /it/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Impara come misurare la larghezza e l altezza del valore della cella in unità di pixel attraverso lo Script Aspose.Cells for Java tramite C++.
keywords: Misura la larghezza del valore della cella in unità di pixel JavaScript tramite C++, misura l altezza del valore della cella in unità di pixel JavaScript tramite C++, ottieni la larghezza del valore della cella in unità di pixel JavaScript tramite C++, ottieni l’altezza del valore della cella in unità di pixel JavaScript tramite C++
---

{{% alert color="primary" %}}  

A volte è necessario calcolare la larghezza e l'altezza del valore della cella per adattare il valore della cella all'interno della cella stessa. Aspose.Cells fornisce i seguenti metodi per questo scopo. Utilizzando questi metodi è possibile calcolare la larghezza e l'altezza del valore della cella e quindi impostare la larghezza della colonna e l'altezza della riga di quella cella rispettivamente e questo regolerà o adatterà il valore della cella all'interno della cella.  

In alternativa, puoi anche [adattare automaticamente righe e colonne della tua cella o intervallo di celle](/cells/it/javascript-cpp/autofit-rows-and-columns/) usando le API di Aspose.Cells.  

{{% /alert %}}  

Il codice seguente spiega l'uso dei metodi [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) e [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Size Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell B2 and add some value inside it
            const cell = worksheet.cells.get("B2");
            cell.value = "Welcome to Aspose!";

            // Enlarge its font to size 16
            const style = cell.style;
            style.font.size = 16;
            cell.style = style;

            // Calculate the width and height of the cell value in unit of pixels
            const widthOfValue = cell.widthOfValue;
            const heightOfValue = cell.heightOfValue;

            // Print both values to the page
            document.getElementById('result').innerHTML = `<p>Width of Cell Value: ${widthOfValue}</p><p>Height of Cell Value: ${heightOfValue}</p>`;

            // Set the row height and column width to adjust/fit the cell value inside cell
            worksheet.cells.setColumnWidthPixel(1, widthOfValue);
            worksheet.cells.setRowHeightPixel(1, heightOfValue);

            // Save the output excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```


## **Argomenti avanzati**  
- [Ottieni larghezza testo del valore della cella](/cells/it/javascript-cpp/get-text-width-of-cell-value/)
