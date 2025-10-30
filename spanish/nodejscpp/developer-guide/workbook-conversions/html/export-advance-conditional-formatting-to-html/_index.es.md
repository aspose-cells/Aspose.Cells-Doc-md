---  
title: Exportar formato condicional DataBar, ColorScale y IconSet al convertir Excel a HTML con Node.js a través de C++  
linktitle: Exportar Formato Condicional DataBar, ColorScale e IconSet al convertir Excel a HTML  
type: docs  
weight: 30  
url: /es/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/  
---  

{{% alert color="primary" %}} 

Puedes exportar formato condicional DataBar, ColorScale y IconSet al convertir tu archivo de Excel en HTML. Esta función tiene soporte parcial en Microsoft Excel, pero Aspose.Cells for Node.js via C++ la soporta completamente.

{{% /alert %}}  

## **Exportar Formato Condicional DataBar, ColorScale e IconSet al convertir Excel a HTML**  
La siguiente captura de pantalla muestra el [archivo de Excel de muestra](5115558.xlsx) con Formato Condicional DataBar, ColorScale e IconSet. Puede descargar el [archivo de Excel de muestra](5115558.xlsx) desde el enlace proporcionado.  

![todo:image_alt_text](conversion_1.png)  

La siguiente captura de pantalla muestra el archivo HTML de salida de Aspose.Cells que muestra Formato Condicional DataBar, ColorScale e IconSet. Como puede ver, se ve exactamente como el [archivo de Excel de muestra](5115558.xlsx).  

![todo:image_alt_text](conversion_2.png)  

### **Código de muestra**  
El siguiente código de ejemplo convierte un archivo Excel de muestra en HTML, realizando una conversión normal de [Excel a HTML](/cells/es/nodejs-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
