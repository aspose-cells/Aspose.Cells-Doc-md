---
title: Trouver le nom de l élément racine de la carte XML avec JavaScript via C++
linktitle: Trouver le nom de l élément racine de la carte XML
type: docs
weight: 30
url: /fr/javascript-cpp/find-the-root-element-name-of-xml-map/
description: Apprenez comment trouver le nom de l élément racine d une carte XML dans Excel en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez trouver le *nom de l'élément racine de la carte XML* en utilisant Aspose.Cells for JavaScript via C++ avec la propriété [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--). La capture d'écran suivante montre le nom de l'élément racine de la carte XML dans Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Code d'exemple**

Le code d'exemple suivant charge le [fichier Excel d'exemple](55541789.xlsx) et accède à la première carte XML pour afficher sa propriété [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--). Veuillez voir la sortie de la console du code d'exemple ci-dessous.

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

## **Sortie console**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
