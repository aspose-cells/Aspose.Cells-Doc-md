---  
title: Работа с ContentTypeProperties через Node.js с использованием C++  
linktitle: Работа с ContentTypeProperties  
type: docs  
weight: 150  
url: /ru/nodejs-cpp/working-with-contenttypeproperties/  
description: Узнайте, как работать с пользовательскими ContentTypeProperties в файлах Excel с помощью Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells предоставляет метод [**Workbook.getContentTypeProperties()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getContentTypeProperties--) для добавления пользовательских ContentTypeProperties в Excel файл. Также вы можете сделать свойство необязательным, установив свойство [**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/nodejs-cpp/contenttypeproperty/#isNillable--) в значение **true**. Следующий фрагмент кода демонстрирует добавление необязательных пользовательских ContentTypeProperties в Excel файл. На изображении показаны оба свойства, добавленных примером кода.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Выходной файл, сгенерированный образцов кода, прикреплен в качестве справки.

[Выходной файл](95584314.xlsx)

## **Образец кода**  

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

