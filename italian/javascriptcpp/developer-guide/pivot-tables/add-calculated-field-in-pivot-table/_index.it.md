---
title: Aggiungi campo calcolato nella tabella pivot
type: docs
weight: 130
url: /it/javascript-cpp/add-calculated-field-in-pivot-table/
description: Come aggiungere un campo calcolato in una tabella pivot con Aspose.Cells for JavaScript tramite C++.
keywords: L Aspose.Cells for JavaScript tramite C++ Excel, libreria JavaScript Excel, aggiunta di un campo calcolato in una tabella pivot utilizzando la libreria JavaScript Excel.
---

## **Possibili Scenari di Utilizzo**
Quando crei una tabella pivot basata su dati noti, scopri che i dati al suo interno non sono quelli che desideri. I dati che desideri sono la combinazione di questi dati originali. Ad esempio, è necessario aggiungere, sottrarre, moltiplicare e dividere i dati originali prima di volerli. A questo punto, è necessario creare un campo calcolato e impostare la formula corrispondente per il calcolo. Quindi eseguire alcune statistiche e altre operazioni sul campo calcolato. 

## **Come aggiungere un campo calcolato nella tabella pivot in Excel**
Inserisci un campo calcolato in una tabella pivot in Excel, segui questi passaggi:

1. Seleziona la tabella pivot a cui desideri aggiungere un campo calcolato. 
2. Vai alla scheda Analizza tabella pivot nel menu a nastro.
3. Fai clic su "Campi, elementi e set" e quindi seleziona "Campo calcolato" dal menu a discesa.
4. Nel campo "Nome", inserire un nome per il campo calcolato.
5. Nel campo "Formula", inserire la formula per il calcolo che si desidera eseguire utilizzando i nomi dei campi del PivotTable appropriati e gli operatori matematici. 
<br>
<img src="1.png" width=80% />
6. Fare clic su "ok" per creare il campo calcolato.
7. Il nuovo campo calcolato apparirà nell'elenco dei campi del PivotTable nella sezione dei Valori.
8. Trascinare il campo calcolato nella sezione dei Valori del PivotTable per visualizzare i valori calcolati.
<br>
<img src="2.png" width=80% />

## **Come aggiungere un campo calcolato in una tabella pivot usando la libreria Aspose.Cells for JavaScript tramite C++**
Aggiungi campo calcolato al file Excel utilizzando Aspose.Cells for JavaScript via C++. Si prega di vedere il seguente esempio di codice. Dopo aver eseguito il codice di esempio, viene aggiunta una tabella pivot con campo calcolato al foglio di lavoro.
1. Impostare i dati originali e creare una tabella pivot. 
2. Creare il campo calcolato in base al PivotField esistente nella tabella pivot.
3. Aggiungere il campo calcolato all'area dati. 
4. Infine, salvare il libro di lavoro nel formato [output XLSX](out.xlsx). 

## **Codice di Esempio**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldType, Utils } = AsposeCells;

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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";
            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";
            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;
            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Adding a PivotTable to the worksheet (converted getPivotTables -> pivotTables)
            const i = ws.pivotTables.add("=A1:C5", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(PivotFieldType.Row, 0);
            // Adding a calculated field to PivotTable and drag it to data area.
            pivotTable.addCalculatedField("total", "=Count*Price", true);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
