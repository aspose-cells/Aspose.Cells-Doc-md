---  
title: Eliminar estilos no utilizados dentro del libro con Node.js via C++  
linktitle: Eliminar Estilos No Utilizados dentro del Libro de Trabajo  
type: docs  
weight: 340  
url: /es/nodejs-cpp/remove-unused-styles-inside-the-workbook/  
description: Aprende cómo eliminar estilos no utilizados de un libro usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Los estilos no utilizados en archivos de Excel no solo ocupan espacio, sino que también causan problemas de rendimiento al convertir a diferentes formatos como PDF, HTML, etc. Aspose.Cells proporciona el método [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--) para eliminar todos los estilos no utilizados dentro del libro.  
{{% /alert %}}  

El siguiente código explica el uso de [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--). El código carga el [archivo de plantilla de Excel](5115520.xlsx) que puedes descargar desde el enlace proporcionado. Contiene un estilo no utilizado llamado **AsposeStyle**; este estilo y todos los demás estilos no utilizados serán eliminados después de la ejecución del código.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Template-With-Unused-Custom-Style.xlsx");

// Load template excel file containing unused styles
const workbook = new AsposeCells.Workbook(filePath);

// Remove all unused styles inside the template this will also remove AsposeStyle which is an unused style inside the template
workbook.removeUnusedStyles();

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

