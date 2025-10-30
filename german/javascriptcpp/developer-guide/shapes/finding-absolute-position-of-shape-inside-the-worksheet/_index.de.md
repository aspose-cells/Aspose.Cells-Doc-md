---
title: Bestimmung der absoluten Position einer Form innerhalb des Arbeitsblatts mit JavaScript via C++
linktitle: Ermittlung der absoluten Position einer Form innerhalb des Arbeitsblatts
type: docs
weight: 8000
url: /de/javascript-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Lernen Sie, wie Sie die absolute Position einer Form innerhalb eines Arbeitsblatts mit Aspose.Cells for JavaScript via C++ ermitteln. 
---

{{% alert color="primary" %}}

Manchmal müssen Sie die absolute Position einer Form in einem Arbeitsblatt kennen. Aspose.Cells for JavaScript via C++ stellt hierfür die Eigenschaften [**Shape.leftToCorner**](https://reference.aspose.com/cells/javascript-cpp/shape/#leftToCorner--) und [**Shape.topToCorner**](https://reference.aspose.com/cells/javascript-cpp/shape/#topToCorner--) bereit. Diese Eigenschaften geben die absolute Position der Form im Arbeitsblatt in Pixeln zurück.

{{% /alert %}}

Der folgende Beispielcode zeigt die absolute Position der ersten Form im Arbeitsblatt in Pixeln an. Der Beispielcode zeigt die folgende Konsolenausgabe:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Shape Position</title>
    </head>
    <body>
        <h1>Get Shape Absolute Position</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file inside the workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first shape inside the worksheet
            const shape = worksheet.shapes.get(0);

            // Displays the absolute position of the shape
            const left = shape.leftToCorner;
            const top = shape.topToCorner;
            const message = `Absolute Position of this Shape is (${left} , ${top})`;
            console.log(message);
            resultDiv.innerHTML = `<p>${message}</p>`;
        });
    </script>
</html>
```
