---
title: Kontrollera om VBA koden är signerad med JavaScript via C++
linktitle: Kontrollera om VBA koden är signerad
type: docs
weight: 100
url: /sv/javascript-cpp/check-if-vba-code-is-signed/
description: Lär dig hur du kontrollerar om VBA kodprojektet är signerat med Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells låter användaren kontrollera om VBA-kodprojektet är signerat eller inte. Använd [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--) -egenskapen för att kontrollera om VBA-kodprojektet är signerat eller inte.

{{% /alert %}}

Följande kod förklarar hur man kontrollerar om VBA-koden är signerad eller inte med hjälp av [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--)-egenskapen. Du kan använda vilken som helst av dina Excel-filer för att testa denna kod. För teständamål kan du använda [denna Excel-fil som används i koden](5115032.xlsm).

## **Kontrollera om VBA-koden är signerad i JavaScript**

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

## Konsoloutput

Nedan är konsoloutputen av ovanstående kod med [exempel excelfil](5115032.xlsm) tillhandahållen via länken.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
