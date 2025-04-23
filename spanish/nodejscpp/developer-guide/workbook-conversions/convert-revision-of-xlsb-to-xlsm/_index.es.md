---  
title: Convertir la Revisión de XLSB a XLSM con Node.js a través de C++  
linktitle: Convertir revisión de XLSB a XLSM  
type: docs  
weight: 290  
url: /es/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/  
description: Aprende cómo convertir completamente las revisiones de archivos XLSB en formato XLSM usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells ahora admite la conversión completa de revisiones de archivos XLSB a archivos XLSM. Las revisiones se encuentran dentro de la ruta \xl\revisions. Puedes verlas cambiando la extensión de tu archivo XLSB a ZIP. La ruta \xl\revisions contiene archivos que terminan con extensión .bin.  

Cuando conviertes tu archivo XLSB a un archivo XLSM usando Aspose.Cells, estos archivos .bin se convierten exitosamente en archivos .xml como se muestra en estas dos capturas de pantalla.  

{{% /alert %}}  

El siguiente ejemplo de código muestra cómo convertir un archivo XLSB a formato XLSM usando Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsb");

// Open workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save Workbook to XLSM format
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```  

