---  
title: Expandir texto de derecha a izquierda al exportar archivo de Excel a HTML con Node.js a través de C++  
linktitle: Expandir texto de derecha a izquierda al exportar archivo Excel a HTML  
type: docs  
weight: 60  
url: /es/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/  
---  

{{% alert color="primary" %}}  

Aspose.Cells ahora admite expandir texto de derecha a izquierda al exportar archivos Excel a HTML. Esta función se ha implementado desde la v8.9.0.0. Ahora, si su archivo Excel de origen contiene algún texto que se expande de derecha a izquierda, entonces Aspose.Cells lo exportará a HTML correctamente.  

{{% /alert %}}  
## **Expandir texto de derecha a izquierda al exportar archivo Excel a HTML**  
El siguiente código de muestra convierte el [archivo de Excel de muestra](5115502.xlsx) en HTML. Esta captura de pantalla muestra cómo se ve el archivo de Excel de muestra en Microsoft Excel 2013.  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)  

Esta captura de pantalla muestra el [HTML de salida generado con una versión anterior](5115509).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)  

Esta captura de pantalla muestra el [HTML de salida generado con una versión más reciente](5115508).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)  

Como puede ver en las capturas de pantalla, la nueva versión expande correctamente el texto alineado a la derecha hacia la izquierda, al igual que Microsoft Excel.  


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load source excel file inside the workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save workbook in html format
wb.save(path.join(dataDir, `ExpandTextFromRightToLeft_out_${AsposeCells.CellsHelper.getVersion()}.html`), AsposeCells.SaveFormat.Html);
```  

