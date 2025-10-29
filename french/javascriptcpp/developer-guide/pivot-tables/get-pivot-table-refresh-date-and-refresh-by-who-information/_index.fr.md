---
title: Obtenir la date de rafraîchissement du tableau croisé dynamique et les informations sur le rafraîchissement par qui
type: docs
weight: 100
url: /fr/javascript-cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Comment obtenir la date d’actualisation du tableau croisé dynamique et l’utilisateur qui l’a actualisé avec Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript Excel, bibliothèque JavaScript Excel, Obtenir la date d’actualisation du tableau croisé dynamique et l’utilisateur ayant effectué la mise à jour avec Aspose.Cells for JavaScript bibliothèque Excel.
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ prend désormais en charge la récupération de la date d’actualisation et de l’utilisateur qui a actualisé le tableau dans un classeur.

{{% /alert %}}

## **Comment obtenir la date de rafraîchissement du tableau croisé dynamique et les informations sur le rafraîchissement par qui**
[**PivotTable.refreshDate**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshDate--) renvoie la date à laquelle le rapport de tableau croisé dynamique a été rafraîchi pour la dernière fois. De même, la propriété [**PivotTable.refreshedByWho**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshedByWho--) renvoie le nom de l'utilisateur qui a rafraîchi le rapport la dernière fois. L'exemple suivant illustre cette fonctionnalité et le fichier d'exemple peut être téléchargé à partir du lien suivant.

[SourcePivotTable.xlsx](77496335.xlsx)

**Code d'exemple**

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
