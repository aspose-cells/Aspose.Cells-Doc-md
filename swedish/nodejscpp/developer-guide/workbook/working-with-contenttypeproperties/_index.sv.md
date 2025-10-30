---  
title: Arbeta med ContentTypeProperties med Node.js via C++  
linktitle: Arbeta med ContentTypeProperties  
type: docs  
weight: 150  
url: /sv/nodejs-cpp/working-with-contenttypeproperties/  
description: Lär dig hur man arbetar med anpassade ContentTypeProperties i Excel filer med Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells tillhandahåller [**Workbook.getContentTypeProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getContentTypeProperties--) metod för att lägga till anpassade ContentTypeProperties i en Excel-fil. Du kan också göra egenskapen valfri genom att sätta [**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/nodejs-cpp/contenttypeproperty/#isNillable--) egenskapen till **true**. Följande kodavsnitt demonstrerar att lägga till valfria anpassade ContentTypeProperties i en Excel-fil. Bilden nedan visar båda egenskaperna som tillfogades av kodexemplet.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Utdatafilen som genererats av exempelkoden bifogas för referens.

[Utdatafil](95584314.xlsx)

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

//source directory
const outputDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);
let index = workbook.getContentTypeProperties().add("MK31", "Simple Data");
workbook.getContentTypeProperties().get(index).setIsNillable(false);
index = workbook.getContentTypeProperties().add("MK32", new Date().toISOString(), "DateTime");
workbook.getContentTypeProperties().get(index).setIsNillable(true);
workbook.save(path.join(outputDir, "WorkingWithContentTypeProperties_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
