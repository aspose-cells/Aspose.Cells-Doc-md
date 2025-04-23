---
title: Encontrar el nombre del elemento raíz del mapa XML con Node.js a través de C++
linktitle: Encuentre el nombre del elemento raíz de XML Map
type: docs
weight: 30
url: /es/nodejs-cpp/find-the-root-element-name-of-xml-map/
description: Aprende cómo encontrar el nombre del elemento raíz de un mapa XML en Excel usando Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**

Puedes encontrar el *Nombre del Elemento Raíz del Mapa XML* usando Aspose.Cells for Node.js via C++ con la propiedad [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--). La siguiente captura de pantalla muestra el nombre del elemento raíz del mapa XML en Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Código de muestra**

El siguiente ejemplo carga el [archivo de ejemplo de Excel](55541789.xlsx) y accede al primer mapa XML, imprimiendo su propiedad [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--). Consulta la salida en la consola del código de ejemplo que se muestra a continuación.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRootElementNameOfXmlMap.xlsx");

// Load sample Excel file having Xml Map
const wb = new AsposeCells.Workbook(filePath);

// Access first Xml Map inside the Workbook
const xmap = wb.getWorksheets().getXmlMaps().get(0);

// Print Root Element Name of Xml Map on Console
console.log("Root Element Name Of Xml Map: " + xmap.getRootElementName());
```

## **Salida de la consola**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
