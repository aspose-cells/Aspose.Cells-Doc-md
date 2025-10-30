---
title: Utilizza le opzioni di verifica degli errori con JavaScript tramite C++
linktitle: Usa le opzioni di controllo degli errori
type: docs
weight: 140
url: /it/javascript-cpp/use-error-checking-options/
description: Impara come utilizzare programmaticamente le opzioni di verifica degli errori nei fogli di lavoro di Excel usando Aspose.Cells for JavaScript tramite C++.
keywords: memorizza il numero come testo in Excel usando JavaScript tramite C++, verifica gli errori nelle opzioni di Excel JavaScript tramite C++
---

{{% alert color="primary" %}}  
Microsoft Excel consente agli utenti di definire opzioni e regole di controllo degli errori. Gli utenti vedono spesso controlli degli errori quando creano formule, in alto a destra di una cella compare un piccolo triangolo quando c'è un problema con una cella. Excel fornisce informazioni che aiutano gli utenti a correggere problemi comuni.  
{{% /alert %}}  

## **Tipi di errori**  

Errori che indicano che la formula non può restituire un risultato — come dividere un numero per zero — richiedono attenzione immediata e viene visualizzato un valore di errore nella cella. Cliccando sul triangolo verde si mostra un punto esclamativo; cliccandoci sopra si apre una lista di opzioni.  

L'errore può essere risolto usando le opzioni o ignorato. Ignorare un errore significa che quell'errore non comparirà nei controlli successivi.  

Aspose.Cells fornisce funzionalità di opzione di controllo degli errori. La classe [**ErrorCheckOption**](https://reference.aspose.com/cells/javascript-cpp/errorcheckoption) gestisce diversi tipi di controlli degli errori, ad esempio, numeri memorizzati come testo, errori di calcolo delle formule ed errori di validazione. Usa l'enumerazione [**ErrorCheckType**](https://reference.aspose.com/cells/javascript-cpp/errorchecktype) per impostare il controllo degli errori desiderato.  

## **Numeri memorizzati come testo**  

Occasionalmente, i numeri potrebbero essere formattati e memorizzati nelle celle come testo. Questo può causare problemi con i calcoli o produrre ordini di ordinamento confusi. I numeri formattati come testo sono allineati a sinistra invece che a destra nella cella. Se una formula che dovrebbe eseguire un'operazione matematica sulle celle non restituisce un valore, controllare l'allineamento delle celle a cui si riferisce la formula: alcune o tutte quelle celle potrebbero essere numeri formattati come testo.  

È possibile utilizzare le opzioni di controllo degli errori per convertire rapidamente i numeri memorizzati come testo in numeri reali. In Microsoft Excel 2003:  

1. Nel menu **Strumenti**, fare clic su **Opzioni**.  
1. Seleziona la scheda Controllo errori.  
   L'opzione **Numero memorizzato come testo** è selezionata per impostazione predefinita.  
1. Disabilitala.  

Il seguente codice di esempio mostra come disabilitare l'opzione di controllo degli errori del numero memorizzato come testo per un foglio di lavoro nel file XLS di modello utilizzando le API di Aspose.Cells.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Error Check Options</title>
    </head>
    <body>
        <h1>Error Check Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a Workbook by reading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Instantiate the error checking options
            const opts = sheet.errorCheckOptions;

            const index = opts.add();
            const opt = opts.get(index);
            // Disable the numbers stored as text option
            // Converted from opt.setErrorCheck(type, value) to a property-style assignment
            opt.errorCheck = opt.errorCheck || {};
            opt.errorCheck[AsposeCells.ErrorCheckType.NumberStoredAsText] = false;
            // Set the range
            opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

            // Save the Excel file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_test.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
