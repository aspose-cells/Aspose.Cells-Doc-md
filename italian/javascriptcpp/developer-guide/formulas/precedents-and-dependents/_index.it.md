---
title: Precedenti e dipendenti con JavaScript via C++
linktitle: Precedenti e Dipendenti
type: docs
weight: 230
url: /it/javascript-cpp/precedents-and-dependents/
description: Impara a tracciare le celle precedenti e dipendenti nei fogli di calcolo usando Aspose.Cells for JavaScript via C++. Comprendi come identificare le celle collegate nei fogli finanziari complessi.
---

{{% alert color="primary" %}} 

I fogli di lavoro finanziari complessi, specialmente quelli sviluppati in collaborazione, possono nascondere errori imbarazzanti. Verificare la precisione delle formule e trovare la fonte di un errore può essere difficile quando la formula utilizza celle precedenti e dipendenti.

{{% /alert %}} 
## **Introduzione**
- Le **celle precedenti** sono celle a cui si fa riferimento in una formula in un'altra cella. Ad esempio, se la cella D10 contiene la formula =B5, la cella B5 è una cella precedente rispetto alla cella D10.
- **Celle dipendenti** contengono formule che si riferiscono ad altre celle. Ad esempio, se la cella D10 contiene la formula =B5, la cella D10 dipende dalla cella B5.

Per rendere il foglio di calcolo facile da leggere, potresti voler mostrare chiaramente quali celle del foglio di calcolo sono utilizzate in una formula. Allo stesso modo, potresti voler estrarre le celle dipendenti da altre celle.

Aspose.Cells ti consente di tracciare le celle e scoprire quali sono collegate.
## **Il Tracciamento delle Celle Precedenti e Dipendenti: Microsoft Excel**
Le formule possono cambiare in base alle modifiche apportate da un cliente. Ad esempio, se la cella C1 dipende da C3 e C4 contenenti una formula, e la cella C1 viene modificata (in modo che la formula venga sovrascritta), C3 e C4, o altre celle, devono cambiare per bilanciare il foglio di calcolo in base alle regole aziendali.

Allo stesso modo, supponiamo che la cella C1 contenga la formula "=(B1*22)/(M2*N32)". Voglio trovare le celle di cui C1 dipende, cioè le celle precedenti B1, M2 e N32.

Potresti aver bisogno di tracciare la dipendenza di una particolare cella verso altre celle. Se le regole aziendali sono incorporate nelle formule, vorremmo scoprire la dipendenza ed eseguire alcune regole in base ad essa. Allo stesso modo, se il valore di una particolare cella viene modificato, quali celle nel foglio di calcolo sono influenzate da tale modificare?

Microsoft Excel consente agli utenti di tracciare le celle precedenti e dipendenti.

1. Nella **Barra degli strumenti Vista**, seleziona **Verifica formule**. Verrà visualizzata la finestra di verifica delle formule.
1. Tracciare Precedenti:
   1. Seleziona la cella che contiene la formula per la quale desideri trovare le celle precedenti.
   1. Per visualizzare una freccia tracciante su ciascuna cella che fornisce direttamente dati alla cella attiva, fare clic su **Traccia Precedenti** sulla barra degli strumenti **Auditing delle Formule**.
1. Traccia delle formule che fanno riferimento a una particolare cella (dipendenti)
   1. Selezionare la cella per la quale si desidera identificare le celle dipendenti.
   1. Per visualizzare una freccia traccia a ciascuna cella che dipende dalla cella attiva, clicca su **Traccia Dipendenti** sulla barra degli strumenti di auditing delle formule.
## **Tracciamento delle Celle Precedenti e Dipendenti: Aspose.Cells**
### **Tracciamento dei Precedenti**
Aspose.Cells rende facile ottenere le celle precedenti. Non solo può recuperare le celle che forniscono dati alle precedenti formule semplici, ma può anche trovare le celle che forniscono dati alle precedenti formule complesse con intervalli denominati.

Nell'esempio sottostante viene utilizzato un file excel modello, Book1.xls. Il foglio di calcolo contiene dati e formule nel primo Foglio di lavoro.

Aspose.Cells fornisce il metodo [Cell.precedents()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedents--) della classe [Cell](https://reference.aspose.com/cells/javascript-cpp/cell) usato per tracciare i precedenti di una cella. Restituisce una collezione di aree riferite. Come puoi vedere sopra, in Book1.xls, la cella B7 contiene una formula "=SUM(A1:A3)". Quindi le celle A1:A3 sono i precedenti della cella B7. Il seguente esempio dimostra la funzione di tracciamento dei precedenti usando il file modello Book1.xls.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Precedents Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet's cells
            const cells = workbook.worksheets.get(0).cells;

            // Get cell B4
            const cell = cells.get("B4");

            if (cell) {
                // Get precedents (converted from getPrecedents)
                const ret = cell.precedents;

                if (!ret.isNull() && ret.count > 0) {
                    const area = ret.get(0);

                    const sheetName = area.sheetName;
                    const startAddress = AsposeCells.CellsHelper.cellIndexToName(area.startRow, area.startColumn);
                    const endAddress = AsposeCells.CellsHelper.cellIndexToName(area.endRow, area.endColumn);

                    console.log(sheetName);
                    console.log(startAddress);
                    console.log(endAddress);

                    document.getElementById('result').innerHTML = `<pre>Sheet: ${sheetName}\nStart: ${startAddress}\nEnd: ${endAddress}</pre>`;
                } else {
                    document.getElementById('result').innerHTML = '<p style="color: red;">No precedents found for the cell.</p>';
                }
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">Cell B4 is null.</p>';
            }
        });
    </script>
</html>
```
### **Tracciamento dei Dipendenti**
Aspose.Cells permette di ottenere le celle dipendenti nei fogli di calcolo. Aspose.Cells non solo può recuperare le celle che forniscono dati riguardo a una formula semplice ma anche trovare le celle che forniscono dati ai dipendenti di formule complesse con intervalli nominati.

Aspose.Cells fornisce il metodo [Cell.dependents(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependents-boolean-) della classe [Cell](https://reference.aspose.com/cells/javascript-cpp/cell) usato per tracciare i dipendenti di una cella. Ad esempio, in Book1.xlsx ci sono formule: "=A1+20" e "=A1+30" nelle celle B2 e C2 rispettivamente. Il seguente esempio dimostra come tracciare i dipendenti per la cella A1 usando il file modello Book1.xlsx.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Get Cell Dependents Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("B2");
            // Ensure dependents is accessed as a property (converted from getDependents)
            const dependents = cell.dependents;

            if (Array.isArray(dependents)) {
                let out = '<p>Dependents found:</p><ul>';
                for (const c of dependents) {
                    console.log(c.name);
                    out += `<li>${c.name}</li>`;
                }
                out += '</ul>';
                resultDiv.innerHTML = out;
            } else {
                console.error("Dependents is not an array");
                resultDiv.innerHTML = '<p style="color: red;">Dependents is not an array</p>';
            }
        });
    </script>
</html>
```
### **Tracciamento delle celle precedenti e dipendenti secondo la catena di calcolo**
Le API di tracciamento dei precedenti e dei dipendenti sopra sono basate sull'espressione della formula stessa. Offrono semplicemente un modo conveniente per gli utenti di tracciare le interdipendenze di alcune formule. Se ci sono molte formule nel workbook e l'utente ha bisogno di tracciare tutti i precedenti e i dipendenti di ogni cella, le prestazioni saranno scarse. Per tale situazione, l'utente dovrebbe considerare di usare i metodi [Cell.precedentsInCalculation()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedentsInCalculation--) e [Cell.dependentsInCalculation(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependentsInCalculation-boolean-). Questi due metodi tracciano le dipendenze secondo la catena di calcolo. Per usarli, prima abilitare la catena di calcolo con [FormulaSettings.enableCalculationChain()](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--). Quindi eseguire il calcolo completo del Workbook con [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--). Dopodiché, puoi tracciare i precedenti o i dipendenti di tutte le celle necessarie.

Per alcuni formule, i precedenti risultanti potrebbero essere diversi per precedenti e precedentiInCalculation, e i dipendenti risultanti potrebbero essere diversi per dipendenti e dipendentiInCalculation. Per esempio, se la formula della cella A1 è "=IF(TRUE,B2,C3)", i precedenti forniranno B2 e C3 come precedenti di A1. Di conseguenza, B2 e C3 entrambi hanno come dipendente A1 durante il controllo con dipendenti. Tuttavia, per il calcolo di questa formula, è ovvio che solo B2 può influenzare il risultato calcolato. Quindi, precedentiInCalculation non fornirà C3 per A1, e dipendentsInCalculation non fornirà A1 per C3. A volte gli utenti potrebbero avere l'esigenza di tracciare solo le interdipendenze che effettivamente influenzano il risultato calcolato delle formule basate sui dati attuali del Workbook, quindi devono usare anche dipendentsInCalculation/precedentsInCalculation invece di dipendenti/precedenti.

Il seguente esempio dimostra come tracciare i precedenti e i dipendenti secondo la catena di calcolo per le celle:


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;

            // Setting formulas
            cells.get("A1").formula = "=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2";
            cells.get("A2").formula = "=IF(TRUE,B2,B1)";

            // Enable calculation chain
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate formulas
            workbook.calculateFormula();

            // Collect output
            let output = '';

            let en = cells.get("B1").dependentsInCalculation;
            output += "B1's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                // If it's an iterable but doesn't have length
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("B2").dependentsInCalculation;
            output += "B2's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("A1").precedentsInCalculation;
            output += "A1's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }
            output += "\n";

            en = cells.get("A2").precedentsInCalculation;
            output += "A2's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }

            resultDiv.innerHTML = '<pre>' + output.replace(/</g, '&lt;') + '</pre>';

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```
