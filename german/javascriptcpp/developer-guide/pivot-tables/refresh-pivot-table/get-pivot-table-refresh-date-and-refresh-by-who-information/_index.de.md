---
title: Abrufen des Aktualisierungsdatums und der Aktualisierungsinformationen durch wen der Pivot Tabelle
type: docs
weight: 100
url: /de/javascript-cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Wie man das Aktualisierungsdatum einer Pivot Tabelle und den Aktualisierenden Nutzer mit Aspose.Cells for JavaScript via C++ erhält.
keywords: Aspose.Cells for JavaScript Excel, Excel JavaScript Bibliothek, Abrufen des Aktualisierungsdatums und des Aktualisierenden Nutzers der Pivot Tabelle mit Aspose.Cells for JavaScript Excel Library.
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ unterstützt jetzt das Abrufen des Aktualisierungsdatums und des Aktualisierenden Nutzers aus einer Arbeitsmappe.

{{% /alert %}}

## **Wie man das Aktualisierungsdatum und die Aktualisierung durch Informationen erhält**
[**PivotTable.refreshDate**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshDate--) gibt das Datum zurück, an dem der PivotTable-Bericht zuletzt aktualisiert wurde. Ebenso gibt die Eigenschaft [**PivotTable.refreshedByWho**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshedByWho--) den Namen des Benutzers zurück, der den Bericht zuletzt aktualisiert hat. Das folgende Beispiel zeigt diese Funktion, und die Beispieldatei kann über den folgenden Link heruntergeladen werden.

[SourcePivotTable.xlsx](77496335.xlsx)

**Beispielcode**

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
