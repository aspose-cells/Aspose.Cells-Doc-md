---  
title: Преобразование ревизии XLSB в XLSM с помощью Node.js через C++  
linktitle: Преобразование ревизии из XLSB в XLSM  
type: docs  
weight: 290  
url: /ru/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/  
description: Узнайте, как полностью преобразовать ревизии файлов XLSB в формат XLSM с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells теперь полностью поддерживает преобразование ревизий файлов XLSB в файлы XLSM. Ревизии находятся по пути \xl\revisions. Их можно просмотреть, изменив расширение файла XLSB на ZIP. Путь \xl\revisions содержит файлы с расширениями .bin.  

Когда вы преобразуете файл XLSB в XLSM с помощью Aspose.Cells, эти .bin файлы успешно преобразуются в .xml файлы, как показано на двух скриншотах.  

{{% /alert %}}  

Следующий пример показывает, как преобразовать файл XLSB в формат XLSM с помощью Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsb");

// Open workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save Workbook to XLSM format
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
