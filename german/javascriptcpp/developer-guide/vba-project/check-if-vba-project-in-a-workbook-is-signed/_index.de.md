---
title: Überprüfen, ob das VBA Projekt in einer Arbeitsmappe mit JavaScript über C++ signiert ist
linktitle: Überprüfen, ob das VBA Projekt in einer Arbeitsmappe signiert ist
type: docs
weight: 70
url: /de/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Erfahren Sie, wie Sie überprüfen, ob ein VBA Projekt in einer Arbeitsmappe mit Aspose.Cells for JavaScript über C++ signiert ist.
---

{{% alert color="primary" %}}

Sie können über Microsoft Excel mithilfe des Menübefehls **Extras > Digitale Signaturen...** prüfen, ob Ihr VBA-Projekt signiert ist oder nicht. Ebenso können Sie dies programmgesteuert mithilfe der Aspose.Cells-[**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--)-Eigenschaft überprüfen.

{{% /alert %}}

## **Überprüfen, ob das VBA-Projekt in einer Arbeitsmappe in JavaScript signiert ist**

Der folgende Code lädt die Arbeitsmappe und überprüft, ob ihr VBA-Projekt mit der [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--)-Eigenschaft signiert ist. Die Eigenschaft gibt **true** zurück, wenn das Projekt signiert ist, andernfalls **false**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const isSigned = workbook.vbaProject.isSigned;

            console.log("VBA Project is Signed: " + isSigned);
            document.getElementById('result').innerHTML = `<p>VBA Project is Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```
