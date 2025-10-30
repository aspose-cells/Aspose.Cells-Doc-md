---
title: Trova il nome dell elemento radice della mappa XML con JavaScript tramite C++
linktitle: Trova il nome dell elemento radice della mappa XML
type: docs
weight: 30
url: /it/javascript-cpp/find-the-root-element-name-of-xml-map/
description: Impara come trovare il nome dell elemento radice di una mappa XML in Excel usando Aspose.Cells for JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**

Puoi trovare il *Nome dell'Elemento Radice della Mappa Xml* usando Aspose.Cells for JavaScript tramite C++ con la proprietà [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--). Lo screenshot seguente mostra il nome dell'elemento radice della mappa XML in Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Codice di Esempio**

Il seguente esempio di codice carica il [file Excel di esempio](55541789.xlsx) e accede alla prima mappa XML, stampando la sua proprietà [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--). Si prega di consultare l’output della console del codice di esempio qui sotto.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Root Element Name Of Xml Map</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Get Root Element Name</button>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first Xml Map inside the Workbook
            const xmap = workbook.worksheets.xmlMaps.get(0);

            // Get Root Element Name of Xml Map
            const rootName = xmap.rootElementName;

            // Display result
            resultDiv.innerHTML = `<p>Root Element Name Of Xml Map: ${rootName}</p>`;
            console.log("Root Element Name Of Xml Map: " + rootName);
        });
    </script>
</html>
```

## **Output della console**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
