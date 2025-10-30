---
title: Importar XML en libro de Excel con Node.js via C++
linktitle: Mapas XML
type: docs
weight: 210
url: /es/nodejs-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Importar datos desde archivos XML en Excel usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells permite importar el mapa XML dentro del libro usando el método [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-). Puedes importar Mapas XML usando Microsoft Excel con los siguientes pasos:

- Selecciona la pestaña **Desarrollador**
- Haz clic en **Importar** en la sección de XML y sigue los pasos requeridos.

Deberás proporcionar tus datos XML para completar la importación. Aquí tienes un [ejemplo de datos XML](5115037.txt) que puedes usar para pruebas.

{{% /alert %}}

## **Importar Mapa XML usando Microsoft Excel**

La siguiente captura de pantalla muestra cómo importar un Mapa XML usando Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Importar Mapa XML usando Aspose.Cells for Node.js via C++**

El siguiente código de ejemplo muestra cómo utilizar el [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-). Genera el [archivo de Excel de salida](5115036.xlsx) como se muestra en esta captura de pantalla.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Local XML file path
const XML = path.join(dataDir, "sampleXML.txt");

// Import your XML Map data starting from cell A1
workbook.importXml(XML, "Sheet1", 0, 0);

// Save workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## **Temas avanzados**
- [Agregar Mapa XML dentro del libro usando el método XmlMapCollection.add()](/cells/es/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Exportar datos XML vinculados al mapa XML dentro del libro](/cells/es/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Encontrar el nombre del elemento raíz del mapa XML](/cells/es/nodejs-cpp/find-the-root-element-name-of-xml-map/)
- [Vincular celdas a elementos del mapa XML](/cells/es/nodejs-cpp/link-cells-to-xml-map-elements/)

{{< app/cells/assistant language="nodejs-cpp" >}}
