---  
title: Node.js経由でC++を使用し、ContentTypePropertiesの操作方法  
linktitle: ContentTypePropertiesの操作  
type: docs  
weight: 150  
url: /ja/nodejs-cpp/working-with-contenttypeproperties/  
description: Aspose.Cells for Node.js via C++を使用してExcelファイルのカスタムContentTypePropertiesの操作方法を学習。  
---  

Aspose.Cellsは、ExcelファイルにカスタムContentTypePropertiesを追加するための [**Workbook.getContentTypeProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getContentTypeProperties--) メソッドを提供します。 [**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/nodejs-cpp/contenttypeproperty/#isNillable--) プロパティを **true** に設定することで、プロパティをオプションにすることも可能です。以下のコードスニペットは、オプションのカスタムContentTypePropertiesをExcelファイルに追加する例です。以下の画像は、サンプルコードで追加された両方のプロパティを示しています。

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

サンプルコードによって生成された出力ファイルが添付されています。

[出力ファイル](95584314.xlsx)

## **サンプルコード**  

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
