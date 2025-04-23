---  
title: Lavorare con ContentTypeProperties con Node.js via C++  
linktitle: Lavorare con ContentTypeProperties  
type: docs  
weight: 150  
url: /it/nodejs-cpp/working-with-contenttypeproperties/  
description: Impara come lavorare con ContentTypeProperties personalizzati in file Excel utilizzando Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells fornisce il metodo [**Workbook.getContentTypeProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getContentTypeProperties--) per aggiungere proprietà ContentTypePersonalizzate a un file Excel. Puoi anche rendere la proprietà opzionale impostando la proprietà [**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/nodejs-cpp/contenttypeproperty/#isNillable--) su **true**. Il seguente frammento di codice dimostra come aggiungere proprietà ContentTypePersonalizzate opzionali a un file Excel. L'immagine seguente mostra entrambe le proprietà aggiunte dal codice di esempio.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Il file di output generato dal codice di esempio è allegato per riferimento.

[File di Output](95584314.xlsx)

## **Codice di Esempio**  

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

