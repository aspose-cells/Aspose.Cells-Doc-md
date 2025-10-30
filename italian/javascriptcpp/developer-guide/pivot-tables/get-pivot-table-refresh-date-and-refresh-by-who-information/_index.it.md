---
title: Ottenere la data di aggiornamento della tabella pivot e informazioni sull aggiornamento da parte di chi
type: docs
weight: 100
url: /it/javascript-cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Come ottenere la data di aggiornamento della tabella pivot e le informazioni su chi ha aggiornato con Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript Excel, libreria JavaScript di Excel, ottenere la data di aggiornamento della tabella pivot e le informazioni su chi ha aggiornato usando Aspose.Cells for JavaScript Excel Library.
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ ora supporta l'estrazione della data di aggiornamento e delle informazioni su chi ha aggiornato da un libro di lavoro.

{{% /alert %}}

## **Come ottenere la data di aggiornamento della tabella pivot e informazioni sull'aggiornamento da parte di chi**
[**PivotTable.refreshDate**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshDate--) restituisce la data in cui il rapporto della tabella pivot è stato aggiornato l'ultima volta. Allo stesso modo, [**PivotTable.refreshedByWho**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshedByWho--) restituisce il nome dell'utente che ha aggiornato il rapporto l'ultima volta. L'esempio seguente illustra questa funzionalità e il file di esempio può essere scaricato dal seguente link.

[SourcePivotTable.xlsx](77496335.xlsx)

**Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Info</title>
    </head>
    <body>
        <h1>Pivot Table Information</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            const pivotTable = worksheet.pivotTables.get(0);

            const refreshedByWho = pivotTable.refreshedByWho;
            const refreshDate = pivotTable.refreshDate;

            console.log("Pivot table refresh by who = " + refreshedByWho);
            console.log("Pivot table refresh date = " + refreshDate);

            document.getElementById('result').innerHTML = `
                <p>Pivot table refresh by who = ${refreshedByWho}</p>
                <p>Pivot table refresh date = ${refreshDate}</p>
            `;
        });
    </script>
</html>
```
