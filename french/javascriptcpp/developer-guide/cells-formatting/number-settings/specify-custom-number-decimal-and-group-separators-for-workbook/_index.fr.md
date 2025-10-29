---
title: Spécifier les séparateurs de décimales et de groupes de nombres personnalisés pour le classeur
linktitle: Spécifier les séparateurs de décimales et de groupes de nombres personnalisés pour le classeur
type: docs
weight: 110
url: /fr/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Modifier les séparateurs décimaux et de regroupement des nombres dans Excel en utilisant Aspose.Cells for JavaScript via C++.
keywords: spécifier le séparateur décimal personnalisé excel JavaScript via C++, spécifier le séparateur de regroupement personnalisé excel JavaScript via C++, changer le séparateur décimal et de regroupement excel JavaScript via C++
---

{{% alert color="primary" %}}

Dans Microsoft Excel, vous pouvez spécifier les séparateurs décimaux et de milliers personnalisés au lieu d'utiliser les Séparateurs Système à partir des **Options Excel Avancées** comme indiqué dans la capture d'écran ci-dessous.

Aspose.Cells fournit les méthodes [**WorkbookSettings.numberDecimalSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberDecimalSeparator-string-) et [**WorkbookSettings.numberGroupSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberGroupSeparator-string-) pour définir les séparateurs personnalisés pour le formatage/analyse des nombres.

{{% /alert %}}

## **Spécification des séparateurs personnalisés à l'aide de Microsoft Excel**

La capture d'écran suivante montre les **Options Excel Avancées** et met en évidence la section pour spécifier les **Séparateurs Personnalisés**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Spécification des séparateurs personnalisés à l'aide de Aspose.Cells for JavaScript via C++**

Le code d'exemple suivant illustre comment spécifier les séparateurs personnalisés à l'aide de l'API Aspose.Cells. Il spécifie les séparateurs de décimales et de groupes numériques personnalisés comme point et espace respectivement.

### Code JavaScript pour spécifier les séparateurs de nombres décimaux et de regroupement personnalisés

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom Number Separator Example</h1>
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

            // Load workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify custom separators
            workbook.settings.numberDecimalSeparator = '.';
            workbook.settings.numberGroupSeparator = ' ';

            const worksheet = workbook.worksheets.get(0);

            // Set cell value
            const cell = worksheet.cells.get("A1");
            cell.value = 123456.789;

            // Set custom cell style
            const style = cell.style;
            style.custom = "#,##0.000;[Red]#,##0.000";
            cell.style = style;

            worksheet.autoFitColumns();

            // Save workbook as pdf
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomSeparator_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
