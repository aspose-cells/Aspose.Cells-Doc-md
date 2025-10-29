---  
title: 使用 Node.js 通过 C++ 操作内容类型属性  
linktitle: 使用ContentTypeProperties  
type: docs  
weight: 150  
url: /zh/nodejs-cpp/working-with-contenttypeproperties/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 处理 Excel 文件中的自定义内容类型属性。  
---  

Aspose.Cells提供[**Workbook.getContentTypeProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getContentTypeProperties--)方法添加自定义ContentTypeProperties到Excel文件中。你还可以通过设置[**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/nodejs-cpp/contenttypeproperty/#isNillable--)属性为**true**，使其成为可选。以下代码展示了如何添加可选的自定义ContentTypeProperties。图片显示了两个已添加的属性。

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

由示例代码生成的输出文件附在下方以供参考。

[输出文件](95584314.xlsx)

## **示例代码**  

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
