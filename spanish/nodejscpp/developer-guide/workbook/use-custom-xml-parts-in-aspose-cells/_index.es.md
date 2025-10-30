---
title: Usar Partes XML Personalizadas en Aspose.Cells con Node.js a través de C++
linktitle: Usar Partes XML Personalizadas en Aspose.Cells
type: docs
weight: 390
url: /es/nodejs-cpp/use-custom-xml-parts-in-aspose-cells/
description: Aprende cómo usar partes XML personalizadas en Aspose.Cells for Node.js via C++. Integra datos XML externos dentro de archivos de Excel de forma sencilla.
--- 

## Usando Partes XML Personalizadas en Aspose.Cells

Las Partes XML Personalizadas son los datos XML que almacenan diferentes aplicaciones como SharePoint, etc., dentro del archivo de Excel. Estos datos son consumidos por diferentes aplicaciones que los necesitan. Microsoft Excel no hace uso de estos datos, por lo que no existe una interfaz gráfica para agregarlo. Puedes ver estos datos cambiando la extensión de **.xlsx** a **.zip** y abriéndolo con **WinZip**. También puedes abrir el archivo ZIP usando cualquier utilidad de compresión de Windows de terceros como WinRAR o WinZip, etc. Los datos están presentes dentro de la carpeta **customXml**.

Puedes agregar partes XML personalizadas usando Aspose.Cells a través del método [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/).

El siguiente código de muestra hace uso del método [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) y agrega el **XML del Catálogo de Libros** cuyo nombre es **BookStore**. La siguiente imagen muestra el resultado de este código. Como puedes ver, el XML del Catálogo de Libros se agrega dentro del nodo BookStore, que es el nombre de esta propiedad.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Código Node.js para usar partes XML personalizadas

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "output.xlsx");

// The sample XML that will be injected to Workbook
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

// Create an instance of Workbook class
const workbook = new AsposeCells.Workbook();

// Add Custom XML Part to ContentTypePropertyCollection
workbook.getContentTypeProperties().add("BookStore", booksXML);

// Save the resultant spreadsheet
workbook.save(filePath);
```

## Artículo Relacionado

- [Agregar propiedades personalizadas visibles dentro del Panel de información del documento](/cells/es/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="nodejs-cpp" >}}
