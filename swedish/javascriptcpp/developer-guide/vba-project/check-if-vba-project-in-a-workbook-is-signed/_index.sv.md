---
title: Kontrollera om VBA projektet i en arbetsbok är signerat med JavaScript via C++
linktitle: Kontrollera om VBA projektet i en arbetsbok är signerat
type: docs
weight: 70
url: /sv/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Lär dig hur du kontrollerar om ett VBA projekt i en arbetsbok är signerat med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Du kan kontrollera om ditt VBA-projekt är signerat eller inte med Microsoft Excel via kommandot **Verktyg > Digitala signaturer...**. På liknande sätt kan du kontrollera det programmatiskt med hjälp av egenskapen [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--) i Aspose.Cells.

{{% /alert %}}

## **Kontrollera om VBA-projektet i en arbetsbok är signerat i JavaScript**

Följande kod laddar arbetsboken och kontrollerar om dess VBA-projekt är signerat med hjälp av [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--)-egenskapen. Egenskapen returnerar **true** om projektet är signerat, annars returnerar den **false**.

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
