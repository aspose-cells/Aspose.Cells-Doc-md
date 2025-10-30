---
title: Überprüfen, ob das VBA Projekt geschützt und gesperrt zum Ansehen ist mit JavaScript über C++
linktitle: Überprüfen, ob das VBA Projekt geschützt und für die Anzeige gesperrt ist
type: docs
weight: 30
url: /de/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Erfahren Sie, wie Sie überprüfen, ob ein VBA Projekt in einer Excel Datei mit Aspose.Cells for JavaScript über C++ geschützt und zum Ansehen gesperrt ist.
---

## Überprüfen, ob das VBA-Projekt in JavaScript über C++ geschützt und gesperrt zum Ansehen ist

Aspose.Cells ermöglicht es, zu überprüfen, ob das VBA (Visual Basic for Applications)-Projekt einer Excel-Datei geschützt und zum Betrachten gesperrt ist. Für diese API bietet die [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--)-Eigenschaft. Wenn es gesperrt ist, dann gibt die [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--)-Eigenschaft **true** zurück.

## **Beispielcode**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](43352065.xlsm) und überprüft, ob das VBA (Visual Basic for Applications)-Projekt der Excel-Datei geschützt und zum Betrachten gesperrt ist. Bitte beachten Sie auch die Konsolenausgabe zur Referenz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check VBA Project Protection Example</title>
    </head>
    <body>
        <h1>Check if VBA Project is Protected</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.xlsb,.csv" />
        <button id="runExample">Check VBA Protection</button>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm) to check.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the VBA project of the workbook.
            const vbaProject = workbook.vbaProject;

            // Whether "Lock project for viewing" is true or not.
            const isLocked = vbaProject ? vbaProject.islockedForViewing : null;

            if (isLocked === null) {
                resultDiv.innerHTML = '<p style="color: orange;">The workbook does not contain a VBA project.</p>';
            } else {
                resultDiv.innerHTML = `<p>Is VBA Project Locked for Viewing: <strong>${isLocked}</strong></p>`;
                console.log("Is VBA Project Locked for Viewing: " + isLocked);
            }
        });
    </script>
</html>
```

## **Konsolenausgabe**

Dies ist die Konsolenausgabe des obigen Beispielcodes, dass mit der bereitgestellten [Beispiel-Excel-Datei](43352065.xlsm) ausgeführt wird.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
