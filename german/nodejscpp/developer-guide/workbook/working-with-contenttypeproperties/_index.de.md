---  
title: Arbeiten mit ContentTypeProperties mit Node.js über C++  
linktitle: Arbeiten mit ContentTypeProperties  
type: docs  
weight: 150  
url: /de/nodejs-cpp/working-with-contenttypeproperties/  
description: Lernen Sie, wie Sie mit benutzerdefinierten ContentTypeProperties in Excel Dateien mithilfe von Aspose.Cells for Node.js via C++ arbeiten.  
---  

Aspose.Cells bietet die [**Workbook.getContentTypeProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getContentTypeProperties--)-Methode zum Hinzufügen benutzerdefinierter ContentTypeProperties zu einer Excel-Datei. Sie können die Eigenschaft auch optional machen, indem Sie die [**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/nodejs-cpp/contenttypeproperty/#isNillable--)-Eigenschaft auf **true** setzen. Das folgende Codebeispiel demonstriert das Hinzufügen optionaler benutzerdefinierter ContentTypeProperties zu einer Excel-Datei. Das folgende Bild zeigt beide Eigenschaften, die durch den Beispielcode hinzugefügt wurden.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Die durch den Beispielcode generierte Ausgabedatei ist als Referenz angehängt.

[Ausgabedatei](95584314.xlsx)

## **Beispielcode**  

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
