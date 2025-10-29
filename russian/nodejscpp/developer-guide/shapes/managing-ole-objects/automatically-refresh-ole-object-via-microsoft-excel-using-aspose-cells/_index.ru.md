---  
title: Автоматическое обновление OLE объектов с помощью Microsoft Excel через Aspose.Cells for Node.js via C++  
linktitle: Автоматическое обновление объекта OLE через Microsoft Excel с помощью Aspose.Cells  
type: docs  
weight: 270  
url: /ru/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/  
description: Узнайте, как автоматически обновлять OLE объекты в Excel с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells предоставляет свойство [**OleObject.getAutoLoad()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getAutoLoad--) для обновления объекта OLE при открытии файла Excel в Microsoft Excel. Благодаря этому свойству объект OLE будет отображать правильное изображение OLE, созданное Microsoft Excel.  
{{% /alert %}}  

Следующий образец кода загружает [образец файла Excel](5115231.xlsx), который содержит ненастоящее изображение OLE. Объект OLE на самом деле является документом Microsoft Word, но образец файла Excel показывает изображение животного вместо изображения Microsoft Word. Но если вы откроете [выходной файл Excel](5115225.xlsx), вы увидите, что Microsoft Excel отображает правильное изображение OLE.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from your sample excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_oleobject.xlsx"));

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Set auto load property of first ole object to true
sheet.getOleObjects().get(0).setAutoLoad(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "RefreshOLEObjects_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
