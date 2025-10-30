---
title: Kontrollera om VBA projektet är skyddat och låst för visning med JavaScript via C++
linktitle: Kontrollera om VBA projektet är skyddat och låst för visning
type: docs
weight: 30
url: /sv/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Lär dig hur du kontrollerar om ett VBA projekt i en Excel fil är skyddat och låst för visning med Aspose.Cells for JavaScript via C++.
---

## Kontrollera om VBA-projekt är skyddat och låst för visning i JavaScript via C++

Aspose.Cells låter dig kontrollera om VBA (Visual Basic for Applications) projektet för en Excel-fil är skyddat och låst för visning. För detta tillhandahåller API:n egenskapen [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--). Om det är låst för visning, returnerar egenskapen [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--) **true**.

## **Exempelkod**

Följande kodexempel laddar det [exempel-Excel-filen](43352065.xlsm) och kontrollerar om VBA (Visual Basic for Applications) projektet för Excel-filen är skyddat och låst för visning. Se även dess Konsolutdata för referens.

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

## **Konsoloutput**

Detta är konsolresultatet av ovanstående exempelkod när den exekveras med den medföljande [exempelvisningsfilen för Excel](43352065.xlsm).

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
