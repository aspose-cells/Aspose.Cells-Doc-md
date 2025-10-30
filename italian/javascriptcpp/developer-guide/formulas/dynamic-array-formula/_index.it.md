---
title: Impostare formule di array dinamici con JavaScript via C++
linktitle: Impostazione di Formule Array Dinamiche
description: Come usare la libreria Aspose.Cells per calcolare formule di array dinamici in Excel usando JavaScript via C++. Carica, calcola e salva facilmente i file Excel.
keywords: Formule di array dinamici, Formule di array dinamici in Excel, Imposta formule di array dinamici con JavaScript via C++, Calcolo delle formule di array dinamici con JavaScript via C++, operare formule di array dinamici di Excel.
type: docs
weight: 70
url: /it/javascript-cpp/calculation-of-dynamic-array-formulas/
---

## **Cos'è la Formula Array di Excel**  
In Excel, una formula array è un tipo speciale di formula che ti consente di eseguire calcoli su array di dati anziché su singole celle. Le formule array possono essere utilizzate per eseguire calcoli complessi, manipolare dati e risolvere problemi specifici in modo efficiente. Sono inserite in modo diverso rispetto alle formule regolari e spesso richiedono l'uso di Ctrl + Maiusc + Invio.

Ecco alcuni punti chiave sulle formule array in Excel:  
1. Sintassi:  
<br>  
Le formule array sono scritte come formule regolari ma coinvolgono operazioni su array di valori. Sono racchiuse tra parentesi graffe { } per indicare che sono formule array. Tuttavia, non è necessario digitare queste parentesi graffe manualmente; Excel le aggiunge automaticamente quando si inserisce correttamente la formula.  
2. Inserimento di formule di array:  
<br>  
Per inserire una formula di array, digita la formula nella barra della formula. Invece di premere Invio per completare, premi Ctrl + Shift + Enter. Questo dice a Excel che è una formula di array. Quando inserita correttamente, Excel visualizza la formula tra parentesi graffe nella barra della formula per indicare che è una formula di array.  
3. Casi d'uso:  
<br>  
Le formule array sono utili per eseguire calcoli su più celle o intervalli contemporaneamente. Possono essere utilizzati per calcoli matematici avanzati, operazioni condizionali, filtraggio dati e altro ancora.  
4. Benefici:  
<br>  
Le formule array ti permettono di eseguire calcoli complessi in una singola formula, il che può migliorare l'efficienza e semplificare i fogli di lavoro. Possono gestire grandi set di dati ed eseguire calcoli che altrimenti richiederebbero più passaggi intermedi.  
5. Limitazioni:  
<br>  
Le formule array possono essere più difficili da capire e risolvere rispetto alle formule regolari. Possono rallentare le prestazioni del foglio di lavoro, specialmente se utilizzate ampiamente o con grandi set di dati.  
6. Esempi:  
<br>  
Sommare i valori in un intervallo: **{=SUMMA(A1:A5*B1:B5)}**  
<br>  
Trova il valore massimo in un intervallo: **{=MAX(A1:A5+B1:B5)}**  
<br>  
<image src="1.png" width="70%" />  
<br>  

Ricorda che le formule di matrice dovrebbero essere usate con prudenza ed è importante capire come funzionano prima di implementarle nei fogli di calcolo. Possono essere strumenti potenti per l'analisi e la manipolazione dei dati in Excel.

## **Cos'è la Formula di Matrice Dinamica in Excel**  
Le formule di matrice dinamica sono una nuova funzionalità introdotta in Excel 365 ed Excel 2021. Ti consentono di lavorare con matrici di dati in modo più semplice ed efficiente rispetto alle formule di matrice tradizionali. Le formule di matrice dinamica spargono automaticamente i risultati nelle celle adiacenti, eliminando la necessità di Ctrl + Maiusc + Invio e consentendo una manipolazione più semplice dei dati.

Punti chiave sulle formule di matrice dinamica in Excel:  
1. Spillaggio Automatico:  
<br>  
Le formule di matrice dinamica spargono automaticamente i risultati nelle celle adiacenti in base alla dimensione dei dati in uscita. Ciò significa che non è necessario selezionare un intervallo di celle prima di inserire la formula o utilizzare Ctrl + Maiusc + Invio per confermare la formula.  
2. Inserimento singola cella:  
<br>  
Le formule di matrice dinamica vengono inserite in una singola cella, ed Excel popola automaticamente le celle adiacenti con i risultati. Ciò rende più facile gestire e comprendere le formule, in quanto è necessario inserire la formula una sola volta.  
3. Nuove funzioni:  
<br>  
Le formule di array dinamico introducono nuove funzioni che possono gestire array in modo nativo, come **FILTRO**, **ORDINA**, **UNICO**, **SEQUENZA**, **ORDINAPER**, e **ARRAYALEATORIO**. Queste funzioni possono restituire valori multipli o manipolare array direttamente, semplificando calcoli complessi.  
4. Gestione flessibile dell'intervallo:  
<br>  
Le formule di array dinamico regolano dinamicamente le dimensioni del range ricaduto in base alle dimensioni dei dati di input o ai calcoli eseguiti. Questa flessibilità consente un uso più efficiente dello spazio del foglio di lavoro e semplifica la creazione di formule.  
5. Prestazioni migliorate:  
<br>  
Le formule di array dinamico possono migliorare le prestazioni rispetto alle formule di array tradizionali, specialmente quando si lavora con grandi set di dati o calcoli complessi.  
6. Compatibilità:  
<br>  
Le formule di array dinamico sono disponibili in Excel 365 ed Excel 2021. Potrebbe non essere supportato nelle versioni precedenti di Excel.  
7. Esempi di formule di array dinamiche:  
<br>  
**FILTRO**: Restituisce un array di valori che soddisfano i criteri specificati.  
<br>  
**ORDINA**: Ordina i valori in un intervallo o array.  
<br>  
**UNICO**: Restituisce valori unici da un elenco o intervallo.  
<br>  
**SEQUENZA**: Genera una sequenza di numeri o date.  
<br>  
**ARRAYALEATORIO**: Genera un array di numeri casuali.  
<br>  
<image src="2.png" width="70%" />  
<br>  

Le formule di array dinamico offrono capacità potenti per la manipolazione e l'analisi dei dati in Excel, rendendo più semplice lavorare con array di dati e svolgere calcoli complessi in modo efficiente.

## **Qual è la differenza tra formule di array e formule di array dinamico in Excel**  
In Excel, sia le formule di array che le formule di array dinamico vengono utilizzate per eseguire calcoli su valori multipli contemporaneamente, ma presentano alcune differenze in termini di funzionalità e modalità di implementazione.

### **Caratteristiche delle formule di array**  
1. Le formule di array sono formule tradizionali in Excel che possono eseguire calcoli su array di dati.  
2. Vengono inseriti premendo Ctrl + Shift + Invio dopo aver digitato la formula, il che indica a Excel che si tratta di una formula di matrice.  
3. Le formule di matrice hanno limitazioni in termini di capacità di riversare i risultati nelle celle adiacenti. Generalmente restituiscono un singolo risultato, anche se quel risultato potrebbe essere un array di celle.  
4. Sono presenti da molto tempo e sono supportati in tutte le versioni di Excel.

### **Caratteristiche delle formule ad array dinamico**  
1. Le formule ad array dinamico sono una nuova funzionalità introdotta in Excel 365 (abbonamento a Office 365) e Excel 2021.  
2. Spilling automatico dei risultati nelle celle adiacenti in base alla dimensione dei dati di input o al calcolo della formula.  
3. Le formule di array dinamiche non richiedono di premere Ctrl + Shift + Invio; basta digitare la formula in una cella e Excel popolerà automaticamente le celle adiacenti con i risultati.  
4. Queste formule hanno la capacità di restituire più risultati (un intervallo di celle) direttamente senza bisogno di una formula di matrice o di Ctrl + Shift + Invio.  
5. Hanno nuove funzioni come **FILTER**, **SORT**, **UNIQUE**, ecc., che possono gestire gli array nativamente e restituire risultati in formato array dinamico.  
In sintesi, le formule ad array dinamico sono un modo più moderno e conveniente per lavorare con le matrici in Excel, fornendo uno spill automatico dei risultati e semplificando il processo di lavoro con le matrici rispetto alle formule di matrice tradizionali. Tuttavia, sono disponibili solo nelle versioni più recenti di Excel che supportano gli array dinamici.

## **Come impostare e calcolare le formule ad array dinamico in Excel**  
Impostare le formule ad array dinamico in Excel comporta l'uso di funzioni specifiche progettate per lavorare con matrici di dati e consentire ai risultati di spillare automaticamente nelle celle circostanti. 

Ecco una guida passo dopo passo per impostare le formule ad array dinamico:  
1. Seleziona la cella:  
<br>  
Scegli la cella in cui desideri visualizzare i risultati della formula ad array dinamico. Le formule ad array dinamico fanno spillare i risultati nelle celle adiacenti, quindi assicurati che ci sia abbastanza spazio per l'output spillato.  
2. Inserire la Formula:  
<br>  
Digita la formula ad array dinamico nella barra delle formule della cella selezionata. Utilizza una delle funzioni ad array dinamico disponibili in Excel 365 e Excel 2021, come **FILTRO**, **ORDINA**, **UNICO**, **SEQUENZA**, **ORDINAPER**, o **MATR.CASUALE**.  
<br>  
Ad esempio, potresti utilizzare la funzione FILTRO per filtrare un elenco di dati in base a criteri specifici: **=FILTRO(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.  
<br>  
<image src="3.png" width="70%" />  
<br>  
3. Premere Invio:  
<br>  
Dopo aver digitato la formula, premi semplicemente Invio sulla tastiera. A differenza delle formule di matrice tradizionali, non è necessario premere Ctrl + Maiusc + Invio.  
4. Osservare l'intervallo di spillaggio:  
<br>  
Excel spillare automaticamente i risultati della formula nelle celle circostanti. La gamma spillata si regola dinamicamente in base alle dimensioni dei dati di output o al calcolo eseguito dalla formula. Excel evidenzia la gamma spillata con un bordo e un'icona a freccia diagonale per indicare che contiene dati spillati.  
5. Interagire con l'intervallo spillato:  
<br>  
Puoi interagire con l'intervallo spillato come con qualsiasi altro intervallo di celle in Excel. Utilizza l'intervallo spillato in altre formule, esegui calcoli su di esso, formattalo o fai riferimento ad esso in grafici o tabelle.  
6. Aggiornare la Formula:  
<br>  
Se è necessario modificare la formula di array dinamico, basta modificare la formula nella cella originale in cui è stata inserita. Dopo aver apportato le modifiche, premi di nuovo Invio per confermare i cambiamenti. Excel aggiornerà automaticamente l'intervallo spillato se necessario.  
7. Cancellare l'intervallo spillato:  
<br>  
Se desideri cancellare i dati spillati, puoi eliminare la formula dalla cella originale. Excel cancellerà anche l'intervallo spillato. In alternativa, puoi eliminare direttamente l'intervallo spillato selezionandolo e premendo il tasto Canc.  
<br>  

Seguendo questi passaggi, puoi configurare formule di array dinamico in Excel per analizzare e manipolare in modo efficiente array di dati, consentendo un'analisi e una segnalazione più facili dei dati.

## **Come impostare e aggiornare formule di array dinamico utilizzando Aspose.Cells**  
Vedi il seguente esempio di codice che carica il [file Excel di esempio](dynamicArrayFormula.xlsx) che contiene alcuni dati fittizi. Dopo aver caricato il file, chiama la funzione [Cell.dynamicArrayFormula(string, FormulaParseOptions, boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dynamicArrayFormula-string-formulaparseoptions-boolean-) per impostare la formula di array dinamico e la funzione [Workbook.refreshDynamicArrayFormulas(boolean)](https://reference.aspose.com/cells/javascript-cpp/workbook/#refreshDynamicArrayFormulas-boolean-) per aggiornare le formule di array dinamici prima di chiamare il calcolo della formula, e infine salva il workbook come [file Excel di output](out.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Dynamic Array Formula Example</title>
    </head>
    <body>
        <h1>Dynamic Array Formula Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FormulaParseOptions } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const ws = wb.worksheets.get(0);

            // Getting the F16 cell
            const f16 = ws.cells.get("F16");

            // Set dynamic array formula (converted from setDynamicArrayFormula to property assignment)
            // Assigning an array containing the formula string, parse options object, and the boolean flag
            f16.dynamicArrayFormula = ["=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=25),\"\")", new FormulaParseOptions(), false];

            // Refresh the dynamic array formulas
            wb.refreshDynamicArrayFormulas(true);

            // Calculate formulas
            wb.calculateFormula();

            // Saving the modified Excel file and preparing download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

La snapshot di output:  
<br>  
<image src="4.png" width="70%" />  
<br>
