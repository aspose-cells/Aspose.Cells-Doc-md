---
title: Ottieni tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro 
type: docs  
weight: 320  
url: /it/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Impara come ottenere tutti gli indici delle righe nascoste dopo aver aggiornato il filtro automatico usando lo script Aspose.Cells for Java tramite API C++.  
keywords: Ottieni tutti gli indici delle righe nascoste dopo aver aggiornato il filtro automatico JavaScript tramite C++, ottieni tutti gli indici delle righe nascoste dopo aver aggiornato il filtro automatico JavaScript tramite C++, recupera tutti gli indici delle righe nascoste dopo aver aggiornato il filtro automatico JavaScript tramite C++  
---

## **Possibili Scenari di Utilizzo**  

Quando applichi il filtro automatico sulle celle del foglio di lavoro, alcune righe vengono nascoste automaticamente. Ma potrebbe essere che alcune righe siano già nascoste manualmente dall'utente di Excel e non nascoste tramite filtro automatico. Quindi, è difficile sapere quali righe sono nascoste dal filtro automatico e quali manualmente dall'utente di Excel. Lo script Aspose.Cells for Java tramite C++ gestisce questo problema usando l'`Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-). Questo metodo restituisce gli indici di tutte le righe nascoste dal filtro automatico e non manualmente dall'utente di Excel.  

## **Ottenere tutti gli indici delle righe nascoste dopo l'aggiornamento dell'autofiltro**  

Vedi il seguente esempio di codice che carica il [file Excel di esempio](64716909.xlsx) che contiene alcune righe nascoste manualmente dall'utente Excel. Il codice applica il filtro automatico e lo aggiorna usando il metodo `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-) che restituisce gli indici di tutte le righe nascoste dal filtro automatico. Quindi stampa gli indici delle righe nascoste sulla console insieme ai nomi delle celle e ai valori.  

## **Codice di Esempio**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Hidden Rows After Refreshing AutoFilter</title>
    </head>
    <body>
        <h1>Get Hidden Rows After Refreshing AutoFilter</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Apply autofilter
            worksheet.autoFilter.addFilter(0, "Orange");

            // True means it will refresh autofilter and return hidden rows.
            const rowIndices = worksheet.autoFilter.refresh(true);

            console.log("Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.");
            console.log("--------------------------");

            let output = '<p>Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.</p><pre>';
            rowIndices.forEach(r => {
                const cell = worksheet.cells.get(r, 0);
                console.log(`${r}\t${cell.name}\t${cell.stringValue}`);
                output += `${r}\t${cell.name}\t${cell.stringValue}\n`;
            });
            output += '</pre>';

            resultDiv.innerHTML = output;
        });
    </script>
</html>
```


## **Output della console**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}
