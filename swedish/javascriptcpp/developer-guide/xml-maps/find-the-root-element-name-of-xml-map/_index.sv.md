---
title: Hitta namnet på rot elementet för XML kartan med JavaScript via C++
linktitle: Hitta det rotelementnamn för XML karta
type: docs
weight: 30
url: /sv/javascript-cpp/find-the-root-element-name-of-xml-map/
description: Lär dig hur du hittar rot elementets namn för en XML karta i Excel med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**

Du kan hitta *Rot-elementnamnet för XML-karta* med Aspose.Cells for JavaScript via C++ med [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--)-egenskapen. Följande skärmbild visar rot-elementets namn för XML-kartan i Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Exempelkod**

Följande kodexempel laddar [exempel-Excelfil](55541789.xlsx) och går till den första XML-kartan och skriver ut dess egenskap [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--). Se konsolutskriften för kodexemplet nedan.

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

## **Konsoloutput**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
