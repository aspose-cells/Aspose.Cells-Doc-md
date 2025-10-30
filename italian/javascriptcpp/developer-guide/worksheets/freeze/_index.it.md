---
title: Bloccare le finestre dell intervallo di Excel con JavaScript tramite C++
linktitle: Blocca riquadri
type: docs
weight: 190
url: /it/javascript-cpp/how-to-freeze-panes-of-excel-worksheet
description: In questo articolo imparerai come bloccare le finestre dei fogli Excel programmaticamente usando Aspose.Cells for JavaScript tramite C++.
keywords: Blocca pannelli, Blocca finestra.
---

## **Introduzione**  

In questo articolo, impareremo Come Bloccare i Pannelli. Quando hai una grande quantità di dati sotto un'intestazione comune, non riesci a vedere l'intestazione quando scorri verso il basso il foglio. E ogni record contiene molti dati. Puoi bloccare i pannelli in modo da poter vedere quella parte bloccata anche quando il resto dei dati viene scrollato. Puoi facilmente vedere gli intestazioni nelle righe superiori o nelle prime colonne. Bloccare e sbloccare i pannelli cambia solo la visualizzazione dei dati senza modificare i dati stessi.  

## **In Excel**  

**![Blocca riquadri in Excel](Freeze-panes.png)**  

1. Se vuoi bloccare i pannelli, blocca righe e colonne, allora prima seleziona una cella (come B2).  
2. Fare clic su Visualizza > Blocca riquadri.  
3. Nel menu a discesa, fare clic su Blocca riquadri.  
4. Se scorri verso il basso o a destra, la prima riga e colonna sono bloccate.  

**![Pannelli bloccati](Frozen-Panes.png)**  

Come puoi vedere, la prima riga e la colonna A sono bloccate, la seconda riga è la 32 e la seconda colonna visibile è D.  

Bloccare i riquadri consente di visualizzare grandi quantità di dati senza dover tenere traccia di etichette di Righe o Colonne.  

## **Blocca finestre con Aspose.Cells for JavaScript tramite C++**  
È semplice bloccare le finestre con Aspose.Cells for JavaScript tramite C++. Usa il metodo [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) per bloccare le finestre alla cella selezionata.  
1. Costruire un libro di lavoro per aprire il file o creare un file vuoto.  
2. Blocca i riquadri con il metodo Worksheet.freezePanes()  
3. Salvare il file.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <p>Select an Excel file (Freeze.xlsx) and click "Run Example" to freeze panes at B2.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Freezing panes at the cell B2
            worksheet.freezePanes("B2", 1, 1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Panes frozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```  

File Excel di esempio allegato (Freeze.xlsx).
