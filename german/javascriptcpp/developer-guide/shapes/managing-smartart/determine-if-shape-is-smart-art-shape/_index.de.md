---
title: Bestimmen, ob eine Form eine Smart Art Form ist mit JavaScript via C++
linktitle: Bestimmen, ob es sich um eine SmartArt Form handelt
type: docs
weight: 400
url: /de/javascript-cpp/determine-if-shape-is-smart-art-shape/
description: Lernen Sie, wie Sie feststellen, ob eine Form in Excel eine Smart Art Form ist, mit Aspose.Cells for JavaScript via C++.
---

## **Mögliche Verwendungsszenarien**  

Smart Art Shapes sind spezielle Formen in Microsoft Excel, die es Ihnen ermöglichen, komplexe Diagramme automatisch zu erstellen. Sie können feststellen, ob die Form eine Smart Art-Form oder eine normale Form ist, indem Sie die [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--)-Eigenschaft verwenden.  

## **Feststellen, ob eine Form ein SmartArt-Form ist**  

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](55541792.xlsx), die eine Smart Art Shape enthält, wie in diesem Screenshot gezeigt. Danach gibt er den Wert der [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--)-Eigenschaft der ersten Form aus. Bitte beachten Sie die Konsolenausgabe des Beispielcodes unten.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is smart art (converted to property access)
            const isSmartArt = shape.isSmartArt;

            document.getElementById('result').innerHTML = `<p>Is Smart Art Shape: ${isSmartArt}</p>`;
        });
    </script>
</html>
```  

## **Konsolenausgabe**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}
