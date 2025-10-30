---
title: Agregar propiedades personalizadas visibles en el panel de información del documento con JavaScript vía C++
linktitle: Agregar Propiedades Personalizadas visibles dentro del Panel de Información del Documento
type: docs
weight: 300
url: /es/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Aprende cómo agregar propiedades personalizadas a un objeto de libro de trabajo usando Aspose.Cells for JavaScript vía C++. Estas propiedades pueden verse en el panel de información del documento.
---

## **Agregar propiedades personalizadas visibles dentro del Panel de información del documento**

Aspose.Cells for JavaScript vía C++ puede usarse para agregar propiedades personalizadas dentro del objeto del libro de trabajo que son visibles en el panel de información del documento. Puedes abrir el panel de información del documento en Microsoft Excel usando las opciones Archivo > Información > Propiedades > Mostrar panel del documento.

Utilice el método [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/#add-string-string-) para agregar una propiedad personalizada que será visible en el Panel de Información del Documento.

El siguiente ejemplo de código añade dos propiedades personalizadas. La primera propiedad no tiene ningún tipo y la segunda tiene un tipo como DateTime. Cuando abras el archivo de Excel generado por este código, verás estas dos propiedades dentro del Panel de Información del Documento.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook with Custom Properties</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            // Create workbook object
            const workbook = new Workbook();

            // Add simple property without any type
            workbook.contentTypeProperties.add("MK31", "Simple Data");

            // Add date time property with type
            workbook.contentTypeProperties.add("MK32", "04-Mar-2015", "DateTime");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingCustomPropertiesVisible_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Artículo Relacionado**

{{% alert color="primary" %}}

- [Usar Partes de XML Personalizadas en Aspose.Cells](/cells/es/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
