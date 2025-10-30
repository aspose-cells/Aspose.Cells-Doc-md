---
title: Elimina la tabella pivot da un foglio di lavoro
type: docs
weight: 60
url: /it/javascript-cpp/delete-pivot-table-from-a-worksheet/
description: Script Aspose.Cells for Java tramite C++ per rimuovere Tabelle Pivot dai Fogli di Lavoro Excel
keywords: Script Aspose.Cells for Java tramite C++ Excel, libreria Excel JavaScript, rimuovi tabella pivot dal foglio di lavoro, rimuovi tabella pivot da excel, come eliminare tabella pivot con Script Aspose.Cells for Java tramite C++, elimina tabella pivot, elimina tabella pivot da excel, elimina tabella pivot, Script Aspose.Cells for Java tramite C++ rimuove tabella pivot, rimuovi tabella pivot, elimina tabella pivot, come eliminare tabella pivot
---

{{% alert color="primary" %}}

Script Aspose.Cells for Java tramite C++ fornisce una funzionalità per eliminare o rimuovere la Tabella Pivot da un Foglio di Lavoro. Puoi eliminare la tabella pivot usando l'oggetto tabella pivot o la posizione della tabella pivot. Si prega di usare il metodo [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-) per eliminare la tabella pivot usando l'oggetto tabella pivot e il metodo [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-) per eliminare l'oggetto tabella pivot usando la sua posizione all'interno della collezione di tabelle pivot.

{{% /alert %}}

## **Come eliminare una tabella pivot dal foglio di lavoro usando Aspose.Cells for JavaScript via C++**

Il codice di esempio seguente elimina due tabelle pivot dal foglio di lavoro. Prima rimuove la tabella pivot utilizzando il metodo [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-) e poi rimuove la tabella pivot utilizzando il metodo [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Table</title>
    </head>
    <body>
        <h1>Remove Pivot Table Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table object
            const pivotTable = worksheet.pivotTables.get(0);

            // Remove pivot table using pivot table object
            worksheet.pivotTables.remove(pivotTable);
            // OR remove by index:
            // worksheet.pivotTables.removeAt(0);

            // Saving the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
