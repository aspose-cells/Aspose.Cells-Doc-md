---
title: Farbe des Glüheffekts einer Form mit JavaScript via C++ auslesen
linktitle: Lesen Sie die Farbe des Leuchteffekts der Form.
type: docs
weight: 330
url: /de/javascript-cpp/read-color-of-shape-s-glow-effect/
description: Erfahren Sie, wie Sie die Farbe eines Glüheffekts einer Form mit Aspose.Cells for JavaScript via C++ auslesen. 
---

## Mögliche Anwendungsszenarien

Wenn Sie die Farbe des Glüheffekts eines Shapes lesen möchten, verwenden Sie bitte die Eigenschaft [**Shape.color**](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#color--). Sie hilft Ihnen, die verschiedenen Eigenschaften im Zusammenhang mit der Farbe des Glüheffekts des Shapes zu finden.

## Farbe des Glow-Effekts der Form lesen

Bitte sehen Sie sich den folgenden Beispielcode und seine [Quelldatei](22774108.xlsx) sowie die Konsolenausgabe zu Ihrer Referenz an. Der folgende Screenshot zeigt den Leuchteffekt der Form in der Quelldatei, wenn sie in Microsoft Excel angezeigt wird.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## JavaScript-Code zum Lesen der Farbe des Leuchteffekts der Form

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Glow Effect Color Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the shape
            const shape = sheet.shapes.get(0);

            // Read the glow effect color and its various properties
            const effect = shape.glow;
            const color = effect.color;

            const colorValue = color.color;
            const colorIndex = color.colorIndex;
            const isShapeColor = color.isShapeColor;
            const transparency = color.transparency;
            const type = color.type;

            console.log("Color: " + colorValue);
            console.log("ColorIndex: " + colorIndex);
            console.log("IsShapeColor: " + isShapeColor);
            console.log("Transparency: " + transparency);
            console.log("Type: " + type);

            resultDiv.innerHTML = `
                <h2>Glow Effect Color Properties</h2>
                <ul>
                    <li><strong>Color:</strong> ${colorValue}</li>
                    <li><strong>ColorIndex:</strong> ${colorIndex}</li>
                    <li><strong>IsShapeColor:</strong> ${isShapeColor}</li>
                    <li><strong>Transparency:</strong> ${transparency}</li>
                    <li><strong>Type:</strong> ${type}</li>
                </ul>
            `;
        });
    </script>
</html>
```

## Konsolenausgabe



{{< highlight javascript >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
