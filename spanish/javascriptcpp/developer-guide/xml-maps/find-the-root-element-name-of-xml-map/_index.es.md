---
title: Encontrar el nombre del elemento raíz del mapa XML con JavaScript vía C++
linktitle: Encuentre el nombre del elemento raíz de XML Map
type: docs
weight: 30
url: /es/javascript-cpp/find-the-root-element-name-of-xml-map/
description: Aprenda cómo encontrar el nombre del elemento raíz de un mapa XML en Excel usando Aspose.Cells for JavaScript vía C++.
---

## **Escenarios de uso posibles**

Puedes encontrar el *Nombre del elemento raíz del mapa XML* usando Aspose.Cells for JavaScript vía C++ con la propiedad [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--). La siguiente captura de pantalla muestra el nombre del elemento raíz del mapa XML en Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Código de muestra**

El siguiente ejemplo carga el [archivo de ejemplo de Excel](55541789.xlsx) y accede al primer mapa XML, imprimiendo su propiedad [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--). Consulta la salida en la consola del código de ejemplo que se muestra a continuación.

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

## **Salida de la consola**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
