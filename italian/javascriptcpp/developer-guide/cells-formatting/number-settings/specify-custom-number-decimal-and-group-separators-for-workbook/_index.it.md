---
title: Specificare i Separatori Decimali e di Gruppo Personalizzati per il Workbook
linktitle: Specificare i Separatori Decimali e di Gruppo Personalizzati per il Workbook
type: docs
weight: 110
url: /it/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Modifica i separatori decimali e di gruppo dei numeri in Excel usando Aspose.Cells for JavaScript via C++.
keywords: specifica separatore decimale personalizzato Excel JavaScript via C++, specifica separatore di gruppo personalizzato Excel JavaScript via C++, modifica separatore decimale e di gruppo Excel JavaScript via C++
---

{{% alert color="primary" %}}

In Microsoft Excel, è possibile specificare i separatori decimali e migliaia personalizzati invece di utilizzare i separatori di sistema dalle **Opzioni Avanzate di Excel** come mostrato nella schermata sottostante.

Aspose.Cells fornisce i metodi [**WorkbookSettings.numberDecimalSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberDecimalSeparator-string-) e [**WorkbookSettings.numberGroupSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberGroupSeparator-string-) per impostare i separatori personalizzati per formattare/parsing i numeri.

{{% /alert %}}

## **Specificare i Separatori Personalizzati utilizzando Microsoft Excel**

La seguente schermata mostra le **Opzioni Avanzate di Excel** e evidenzia la sezione per specificare i **Separatori Personalizzati**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Specificare separatori personalizzati utilizzando Aspose.Cells for JavaScript via C++**

Il seguente codice di esempio illustra come specificare i separatori personalizzati utilizzando l'API Aspose.Cells. Specifica i separatori personalizzati per il numero decimale e per il raggruppamento come rispettivamente punto e spazio.

### Codice JavaScript per specificare separatori decimali e di gruppo personalizzati per i numeri

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
