---
title: Personalización del XML de la cinta con Node.js a través de C++
linktitle: Personalizar el menú de Excel
type: docs
weight: 1500
url: /es/nodejs-cpp/customizing-the-ribbon-xml/
description: Aprenda cómo personalizar el XML de la Cinta en Excel usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Microsoft Office reemplazó los menús y barras de herramientas con una cinta en la parte superior de la ventana de la aplicación desde la oficina 2007. La cinta es personalizable. 
 Aspose.Cells for Node.js via C++ le permite

- Mantener el XML de la cinta sin analizarlo,
- Leer y escribir el XML de la cinta sin analizarlo,
- Obtener y establecer datos XML de la cinta.

Si desea cambiar el XML de la cinta, debe analizarlo con un analizador XML u otra herramienta XML de la cinta.

{{% /alert %}} 

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");
// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

const ribbonXml = `<customUI xmlns="http://schemas.microsoft.com/office/2006/01/customui"></customUI>`;
workbook.setRibbonXml(ribbonXml);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
