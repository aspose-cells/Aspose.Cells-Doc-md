---  
title: Node.js ve C++ kullanarak ContentTypeProperties ile çalışma  
linktitle: ContentTypeProperties ile Çalışma  
type: docs  
weight: 150  
url: /tr/nodejs-cpp/working-with-contenttypeproperties/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarında özel ContentTypeProperties ile nasıl çalışılacağını öğrenin.  
---  

Aspose.Cells, Excel dosyasına özel ContentTypeProperties eklemek için [**Workbook.getContentTypeProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getContentTypeProperties--) yöntemini sağlar. Ayrıca, [**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/nodejs-cpp/contenttypeproperty/#isNillable--) özelliğini **true** olarak ayarlayarak özelliği isteğe bağlı hale getirebilirsiniz. Aşağıdaki kod örneği, isteğe bağlı özel ContentTypeProperties'lerin bir Excel dosyasına nasıl ekleneceğini gösterir. Aşağıdaki resim, örnek kod tarafından eklenen her iki özelliği de göstermektedir.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Örnek kod tarafından oluşturulan çıktı dosyası referans için ekte bulunmaktadır.

[Çıkış Dosyası](95584314.xlsx)

## **Örnek Kod**  

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

