---
title: Applicare una sfumatura alle righe e alle colonne alternate con la formattazione condizionale
linktitle: Applicare una sfumatura alle righe e alle colonne alternate con la formattazione condizionale
description: Come usare la libreria Aspose.Cells in JavaScript tramite C++ per applicare ombre di formattazione condizionale per righe e colonne alternate. Regolando questi criteri, avrai un controllo maggiore sull aspetto delle celle.
keywords: Aspose.Cells, Formattazione condizionale, JavaScript tramite C++, Righe alternate, Colonne alternate, Ombre
type: docs
weight: 30
url: /it/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Le API di Aspose.Cells forniscono i mezzi per aggiungere e manipolare regole di formattazione condizionale per l'oggetto [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Queste regole possono essere adattate in vari modi per ottenere la formattazione desiderata in base a condizioni o regole. Questo articolo dimostrerà l'uso delle API Aspose.Cells for JavaScript tramite C++ per applicare ombreggiature a righe e colonne alternate con l'aiuto di regole di formattazione condizionale e delle funzioni incorporate di Excel.

{{% /alert %}}

Questo articolo fa uso di funzioni integrate di Excel come ROW, COLUMN e MOD. Ecco alcuni dettagli di queste funzioni per una migliore comprensione dello snippet di codice fornito in seguito.

- La funzione **ROW()** restituisce il numero di riga di un riferimento di cella. Se si omette il parametro reference, si assume che il riferimento sia l'indirizzo della cella in cui è stato inserito il funzione ROW.
- La funzione **COLUMN()** restituisce il numero di colonna di un riferimento di cella. Se si omette il parametro reference, si assume che il riferimento sia l'indirizzo della cella in cui è stato inserito il funzione COLUMN.
- La funzione **MOD()** restituisce il resto dopo che un numero è diviso per un divisore, dove il primo parametro della funzione è il valore numerico di cui si desidera trovare il resto e il secondo parametro è il numero utilizzato per dividere il parametro del numero. Se il divisore è 0, restituirà l'errore #DIV/0!.

Iniziamo a scrivere del codice per raggiungere questo obiettivo con l'aiuto delle API Aspose.Cells for JavaScript tramite C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Conditional Formatting</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, Utils } = AsposeCells;

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
            // Create an instance of Workbook
            const book = new Workbook();

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Add FormatConditions to the instance of Worksheet
            let idx = sheet.conditionalFormattings.add();

            // Access the newly added FormatConditions via its index
            const conditionCollection = sheet.conditionalFormattings.get(idx);

            // Define a CellsArea on which conditional formatting will be applicable (A1 to I20)
            const area = CellArea.createCellArea("A1", "I20");

            // Add area to the instance of FormatConditions
            conditionCollection.addArea(area);

            // Add a condition to the instance of FormatConditions (Expression type)
            idx = conditionCollection.addCondition(AsposeCells.FormatConditionType.Expression);

            // Access the newly added FormatCondition via its index
            const formatCondition = conditionCollection.get(idx);

            // Set the formula for the FormatCondition
            formatCondition.formula1 = "=MOD(ROW(),2)=0";

            // Set the background color and pattern for the FormatCondition's Style
            formatCondition.style.backgroundColor = AsposeCells.Color.Blue;
            formatCondition.style.pattern = AsposeCells.BackgroundType.Solid;

            // Save the result and provide a download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


Il seguente screenshot mostra il foglio elettronico caricato nell'applicazione Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Per applicare l'ombreggiatura alle colonne alternative, tutto ciò che devi fare è modificare la formula **=MOD(FILA(),2)=0** in **=MOD(COLONNA(),2)=0**, cioè; invece di ottenere l'indice di riga, modifica la formula per recuperare l'indice di colonna.  
Il foglio elettronico risultante, in questo caso, avrà questo aspetto.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
