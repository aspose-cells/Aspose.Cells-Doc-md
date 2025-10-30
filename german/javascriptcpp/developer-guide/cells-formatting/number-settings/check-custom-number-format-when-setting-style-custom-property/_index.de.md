---
title: Benutzerdefiniertes Zahlenformat überprüfen beim Festlegen von Style.Custom Eigenschaft
linktitle: Benutzerdefiniertes Zahlenformat überprüfen beim Festlegen von Style.Custom Eigenschaft
description: Aspose.Cells ist eine JavaScript Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die die Überprüfung benutzerdefinierter Nummernformate beim Stylen unterstützt. Dieser Artikel zeigt, wie Sie die Aspose.Cells Bibliothek verwenden, um benutzerdefinierte Nummernformate zu überprüfen, um die Korrektheit des Stylings sicherzustellen.
keywords: Aspose.Cells, JavaScript Bibliotheken, Tabellenkalkulationen, Styling, benutzerdefinierte Nummernformatierung, Überprüfung, Validierung
type: docs
weight: 170
url: /de/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einem [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-)-Eigenschaft einen ungültigen benutzerdefinierten Nummernformat-Code zuweisen, wird Aspose.Cells for JavaScript via C++ keine Ausnahme auslösen. Möchten Sie jedoch, dass Aspose.Cells prüft, ob das zugewiesene benutzerdefinierte Nummernformat gültig ist, setzen Sie bitte die [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-)-Eigenschaft auf **true**.

## **Prüfen des benutzerdefinierten Nummernformats beim Setzen der Style.custom-Eigenschaft**

Der folgende Beispielcode weist der [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-)-Eigenschaft ein ungültiges benutzerdefiniertes Nummernformat zu. Da wir die [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-)-Eigenschaft bereits auf **true** gesetzt haben, löst es eine Ausnahme aus, z.B. ungültiges Nummernformat. Lesen Sie die Kommentare im Code für weitere Hilfe.

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Check Custom Number Format</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new empty workbook if no file is provided
                workbook = new Workbook();
            }

            // Setting this property to true will make Aspose.Cells throw an exception
            // when invalid custom number format is assigned to Style.custom property
            workbook.settings.checkCustomNumberFormat = true;

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access cell A1 and put some number to it
            const cell = sheet.cells.get("A1");
            cell.value = 2347;

            // Access cell's style and set its Style.custom property
            const style = cell.style;

            // This line will throw exception if workbook.settings.checkCustomNumberFormat is set to true
            style.custom = "ggg @ fff"; // Invalid custom number format

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
