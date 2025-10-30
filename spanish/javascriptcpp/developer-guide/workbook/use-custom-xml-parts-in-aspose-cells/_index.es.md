---
title: Usar Partes XML Personalizadas en Aspose.Cells con JavaScript a través de C++
linktitle: Usar Partes XML Personalizadas en Aspose.Cells
type: docs
weight: 390
url: /es/javascript-cpp/use-custom-xml-parts-in-aspose-cells/
description: Aprende cómo usar partes XML personalizadas en Aspose.Cells for JavaScript a través de C++. Integra datos XML externos en archivos de Excel sin problemas.
---

## Usando Partes XML Personalizadas en Aspose.Cells

Las Partes XML Personalizadas son los datos XML que almacenan diferentes aplicaciones como SharePoint, etc., dentro del archivo de Excel. Estos datos son consumidos por diferentes aplicaciones que los necesitan. Microsoft Excel no hace uso de estos datos, por lo que no existe una interfaz gráfica para agregarlo. Puedes ver estos datos cambiando la extensión de **.xlsx** a **.zip** y abriéndolo con **WinZip**. También puedes abrir el archivo ZIP usando cualquier utilidad de compresión de Windows de terceros como WinRAR o WinZip, etc. Los datos están presentes dentro de la carpeta **customXml**.

 Puedes agregar partes XML personalizadas usando Aspose.Cells for JavaScript a través de C++ mediante el método [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/).

El siguiente código de muestra hace uso del método [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/) y agrega el **XML del Catálogo de Libros** cuyo nombre es **BookStore**. La siguiente imagen muestra el resultado de este código. Como puedes ver, el XML del Catálogo de Libros se agrega dentro del nodo BookStore, que es el nombre de esta propiedad.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Código JavaScript para usar partes XML personalizadas

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Custom XML to Workbook Example</h1>
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

        const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create an instance of Workbook class
            const workbook = new Workbook();

            // Add Custom XML Part to ContentTypePropertyCollection
            workbook.contentTypeProperties.add("BookStore", booksXML);

            // Save the resultant spreadsheet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom XML added and file prepared. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## Artículo Relacionado

- [Agregar propiedades personalizadas visibles dentro del Panel de información del documento](/cells/es/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
