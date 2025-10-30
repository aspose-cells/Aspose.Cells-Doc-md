---
title: Text aus der Gear Type SmartArt Form mit JavaScript via C++ extrahieren
linktitle: Extrahieren Sie Text aus der SmartArt Form des Zahnradtyps
type: docs
weight: 500
url: /de/javascript-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Lernen Sie, wie Sie Text aus der Gear Type SmartArt Form mit Aspose.Cells for JavaScript via C++ extrahieren.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells kann Text aus der Gear Type Smart Art-Form extrahieren. Dafür sollten Sie zuerst die Smart Art-Form in Gruppenform umwandeln, indem Sie die [**Shape.resultOfSmartArt**](https://reference.aspose.com/cells/javascript-cpp/shape/#resultOfSmartArt--)-Eigenschaft verwenden. Dann erhalten Sie das Array aller einzelnen Formen, die die Gruppe bilden, mit der [**GroupShape.groupedShapes**](https://reference.aspose.com/cells/javascript-cpp/groupshape/#groupedShapes--)-Eigenschaft. Schließlich können Sie alle einzelnen Formen in einer Schleife durchgehen und deren Text mit der [**Shape.text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--)-Eigenschaft extrahieren.

## **Text aus dem SmartArt-Form 'Zahnräder' extrahieren**

Der folgende Beispielcode lädt die [Beispieldatei Excel](67338483.xlsx) mit der SmartArt-Form des Zahnradtyps. Anschließend werden die Texte aus den einzelnen Formen extrahiert, wie oben diskutiert. Bitte beachten Sie die Konsolenausgabe des folgenden Codes zur Referenz.

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Gear SmartArt Text Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Get the result of gear type smart art shape in the form of group shape.
            const groupShape = shape.resultOfSmartArt;

            // Get the list of individual shapes consisting of group shape.
            const shapes = groupShape.groupedShapes;

            // Extract the text of gear type shapes and display them.
            const results = [];
            for (let i = 0; i < shapes.count; i++) {
                const s = shapes.get(i);

                if (s.type === AsposeCells.AutoShapeType.Gear9 || s.type === AsposeCells.AutoShapeType.Gear6) {
                    const text = s.text;
                    results.push(text);
                    console.log("Gear Type Shape Text: " + text);
                }
            }

            if (results.length) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Found gear shape texts:</p><ul>' + results.map(t => '<li>' + t + '</li>').join('') + '</ul>';
            } else {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No gear type SmartArt shapes found in the first shape.</p>';
            }
        });
    </script>
</html>
```

## **Konsolenausgabe**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
