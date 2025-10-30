---
title: Inserisci tabella pivot
linktitle: Tabelle Pivot
type: docs
weight: 160
url: /it/javascript-cpp/create-pivot-table/
description: Creare e formattare tabelle pivot di file di fogli di calcolo di Excel.
---

## **Creare tabella pivot**

È possibile usare Aspose.Cells for JavaScript tramite C++ per aggiungere tabelle pivot ai fogli di calcolo in modo programmatico.

### **Modello di oggetto di tabella pivot**

Aspose.Cells for JavaScript tramite C++ fornisce un set speciale di classi utilizzate per creare e controllare le tabelle pivot. Queste classi vengono usate per creare e impostare gli oggetti [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable), i mattoni fondamentali di una tabella pivot. Gli oggetti sono:

- [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) rappresenta un campo in un [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection) rappresenta una raccolta di tutti gli oggetti [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) in [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) rappresenta una tabella pivot su un foglio di lavoro.
- [**PivotTableCollection**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) rappresenta una raccolta di tutti gli oggetti [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) su un foglio di lavoro.

### **Creare una semplice tabella pivot utilizzando Aspose.Cells**

1. Aggiungi dati a un foglio di lavoro utilizzando il metodo [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) dell'oggetto [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).
   Questi dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo [**add**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#add-string-string-string-) della raccolta [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection), incapsulata nell'oggetto Foglio di lavoro.
1. Accedi al nuovo oggetto [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) dalla raccolta [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) passando l'indice di PivotTable.
1. Utilizza uno qualsiasi degli oggetti [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) (spiegati sopra) per gestire la tabella pivot.

Dopo aver eseguito il codice di esempio, viene aggiunta una tabella pivot al foglio di lavoro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Pivot Table Example</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                // Instantiate a new Workbook object
                const workbook = new Workbook();

                // Obtaining the reference of the newly added worksheet
                const sheetIndex = workbook.worksheets.add();
                const sheet = workbook.worksheets.get(sheetIndex);
                const cells = sheet.cells;

                // Setting the value to the cells
                let cell = cells.get("A1");
                cell.value = "Sport";
                cell = cells.get("B1");
                cell.value = "Quarter";
                cell = cells.get("C1");
                cell.value = "Sales";

                cell = cells.get("A2");
                cell.value = "Golf";
                cell = cells.get("A3");
                cell.value = "Golf";
                cell = cells.get("A4");
                cell.value = "Tennis";
                cell = cells.get("A5");
                cell.value = "Tennis";
                cell = cells.get("A6");
                cell.value = "Tennis";
                cell = cells.get("A7");
                cell.value = "Tennis";
                cell = cells.get("A8");
                cell.value = "Golf";

                cell = cells.get("B2");
                cell.value = "Qtr3";
                cell = cells.get("B3");
                cell.value = "Qtr4";
                cell = cells.get("B4");
                cell.value = "Qtr3";
                cell = cells.get("B5");
                cell.value = "Qtr4";
                cell = cells.get("B6");
                cell.value = "Qtr3";
                cell = cells.get("B7");
                cell.value = "Qtr4";
                cell = cells.get("B8");
                cell.value = "Qtr3";

                cell = cells.get("C2");
                cell.value = 1500;
                cell = cells.get("C3");
                cell.value = 2000;
                cell = cells.get("C4");
                cell.value = 600;
                cell = cells.get("C5");
                cell.value = 1500;
                cell = cells.get("C6");
                cell.value = 4070;
                cell = cells.get("C7");
                cell.value = 5000;
                cell = cells.get("C8");
                cell.value = 6430;

                const pivotTables = sheet.pivotTables;

                // Adding a PivotTable to the worksheet
                const index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

                // Accessing the instance of the newly added PivotTable
                const pivotTable = pivotTables.get(index);

                // Unshowing grand totals for rows.
                pivotTable.rowGrand = false;

                // Dragging the first field to the row area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);

                // Dragging the second field to the column area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 1);

                // Dragging the third field to the data area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);

                // Saving the Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'CreatePivotTable_out.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created successfully! Click the download link to get the file.</p>';
            });
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Quando si assegna un intervallo di celle come origine dati, l'intervallo deve andare dall'angolo in alto a sinistra a quello in basso a destra. Ad esempio, "A1:C3" è valido ma "C3:A1" non lo è.

{{% /alert %}}
