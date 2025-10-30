---
title: Konvertieren Sie die Smart Art mit JavaScript via C++ in Gruppenform
linktitle: Konvertieren Sie die SmartArt in eine Gruppenform
type: docs
weight: 200
url: /de/javascript-cpp/convert-the-smart-art-to-group-shape/
---

## **Mögliche Verwendungsszenarien**

Sie können Smart Art Shape mit der [**Shape.resultOfSmartArt**](https://reference.aspose.com/cells/javascript-cpp/shape/#resultOfSmartArt--)-Methode in Gruppengefüge umwandeln. Dadurch können Sie Smart Art Shapes wie ein Gruppengefüge behandeln. Folglich haben Sie Zugriff auf die einzelnen Teile oder Formen des Gruppengefüges.

## **Konvertieren des SmartArt in Gruppenform**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](55541793.xlsx), die eine Smart Art Shape enthält, wie in diesem Screenshot gezeigt. Danach wandelt er die Smart Art Shape in Gruppengefüge um und gibt die Shape.isGroup-Eigenschaft aus. Bitte beachten Sie die Konsolenausgabe des Beispielcodes unten.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Result Of SmartArt</title>
    </head>
    <body>
        <h1>Get Result Of SmartArt Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is smart art (property access, not method)
            const isSmartArt = shape.isSmartArt;

            // Determine if shape is group shape (property access)
            const isGroup = shape.isGroup;

            // Convert smart art shape into group shape result and check if group (getResultOfSmartArt -> resultOfSmartArt property)
            const resultOfSmartArtIsGroup = shape.resultOfSmartArt.isGroup;

            const html = [
                `<p>Is Smart Art Shape: ${isSmartArt}</p>`,
                `<p>Is Group Shape: ${isGroup}</p>`,
                `<p>Result of SmartArt is Group: ${resultOfSmartArtIsGroup}</p>`
            ].join('');

            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **Konsolenausgabe**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
