---
title: Agregar mapa XML dentro del libro de trabajo usando XmlMapCollection.Add con JavaScript vía C++  
linktitle: Agregar mapa XML dentro del libro usando el método XmlMapCollection.Add  
type: docs  
weight: 10  
url: /es/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: Aprenda cómo agregar un mapa XML dentro del libro de trabajo usando XmlMapCollection.Add con Aspose.Cells for JavaScript vía C++.  
---  

## **Escenarios de uso posibles**  

Aspose.Cells proporciona el método [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/javascript-cpp/xmlmapcollection/#add-string-) que puede usar para importar su mapa XML dentro del libro.  

## **Agregar mapa XML dentro del libro utilizando el método XmlMapCollection.Add**  

El siguiente código de ejemplo agrega un mapa XML dentro del libro utilizando el método [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/javascript-cpp/xmlmapcollection/#add-string-) y lo guarda como [archivo de Excel de salida](5115434.xlsx). La captura de pantalla muestra el mapa XML que se ha importado de [sample.xml](5115433.xml) dentro del archivo de Excel de salida.  

![add-xml-map](add-xml-map.png)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add XML Map to Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xml" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an XML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const xmlString = new TextDecoder().decode(arrayBuffer);

            // Create workbook object
            const wb = new Workbook();

            // Add xml map found inside the uploaded sample.xml into the workbook
            // Note: converted getter/setter usage to property access per universal conversion rules
            wb.worksheets.xmlMaps.add(xmlString);

            // Save the workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">XML map added and workbook saved. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
