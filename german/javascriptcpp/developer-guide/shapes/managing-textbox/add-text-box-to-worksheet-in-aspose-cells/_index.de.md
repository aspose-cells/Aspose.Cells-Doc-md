---
title: Wie man mit JavaScript via C++ ein Textfeld zu einem Arbeitsblatt hinzufügt/einfügt
linktitle: Fügen Sie eine Textbox in ein Arbeitsblatt ein
type: docs
weight: 10
url: /de/javascript-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Wie man mit Aspose.Cells for JavaScript via C++ ein Textfeld zu einem Arbeitsblatt hinzufügt/einfügt.
keywords: Textfeld hinzufügen/einfügen für Arbeitsblatt Excel Aspose JavaScript via C++
---

## Fügen Sie ein Textfeld in das Arbeitsblatt in Excel ein

In den Excel-Programmen (Version 07 und höher) gibt es zwei Stellen, an denen Sie Textfelder einfügen können. Einmal in "Einfügen-Formen", dann auf der rechten Seite des oberen Menüs unter der Option "Einfügen".

### Methode eins:

![1](1.png)

### Methode zwei:

![2](2.png)

## Wie man erstellt

Sie können Textfelder mit horizontal oder vertikal ausgerichtetem Text erstellen.

- Wählen Sie die entsprechende Option (horizontal oder vertikal)
- Klicken Sie links auf die Seite
- Halten Sie die linke Taste gedrückt und ziehen Sie eine Entfernung auf der Seite
- Lassen Sie die linke Taste los

Nun haben Sie ein Textfeld.

## Textfeld in Arbeitsblatt in Aspose.Cells for JavaScript via C++ hinzufügen

Wenn Sie eine große Anzahl von Textfeldern in das Arbeitsblatt einfügen müssen, ist die manuelle Einfügung offensichtlich problematisch. Wenn Sie dies stört, wird dieses Dokument Ihnen sicherlich helfen. [Aspose.Cells](https://products.aspose.com/cells/) bietet eine API, mit der Sie einfache Masseninserts in Ihrem Code durchführen können.

Der folgende Beispielcode erstellt ein Textfeld.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add TextBox</title>
    </head>
    <body>
        <h1>Add TextBox to Workbook</h1>
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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the TextBox to the worksheet
            sheet.textBoxes.add(6, 10, 100, 200);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TextBox added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Sie erhalten eine Datei, die der [Ergebnisdatei](result.xlsx) ähnlich ist. In der Datei werden Sie Folgendes sehen:

![](52449.png)
