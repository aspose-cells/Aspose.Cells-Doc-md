---
title: Überprüfung, ob VBA Code mit JavaScript via C++ signiert ist
linktitle: Überprüfen, ob VBA Code signiert ist
type: docs
weight: 100
url: /de/javascript-cpp/check-if-vba-code-is-signed/
description: Erfahren Sie, wie Sie überprüfen, ob das VBA Code Projekt mit Aspose.Cells for JavaScript über C++ signiert ist. 
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es dem Benutzer zu prüfen, ob das VBA-Codeprojekt signiert ist oder nicht. Bitte verwenden Sie die [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--)-Eigenschaft, um zu überprüfen, ob das VBA-Codeprojekt signiert ist oder nicht.

{{% /alert %}}

Der folgende Code erklärt, wie überprüft wird, ob der VBA-Code mit der [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--)-Eigenschaft signiert ist. Sie können jede Ihrer Excel-Dateien zum Testen dieses Codes verwenden. Für Testzwecke können Sie [diese Excel-Datei im Code verwenden](5115032.xlsm).

## **Überprüfen, ob VBA-Code signiert ist in JavaScript**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const vbaProject = workbook.vbaProject;
            const isSigned = vbaProject.isSigned();

            resultDiv.innerHTML = `<p>Is VBA Code Project Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```

## Konsolenausgabe

Unten ist die Konsolenausgabe des obigen Codes mithilfe der [Beispieldatei](5115032.xlsm), die über den Link bereitgestellt wird.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
