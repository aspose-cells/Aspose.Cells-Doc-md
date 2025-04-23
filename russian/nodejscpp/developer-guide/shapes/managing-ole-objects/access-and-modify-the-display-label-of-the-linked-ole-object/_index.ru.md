---
title: Доступ и изменение отображаемой метки связанного Ole объекта с помощью Node.js через C++
linktitle: Доступ и изменение отображаемой метки связанного объекта OLE
type: docs
weight: 100
url: /ru/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Узнайте, как получить доступ и изменить отображаемую метку связанного Ole объекта с помощью Aspose.Cells for Node.js via C++. 
---

## **Возможные сценарии использования**

Microsoft Excel позволяет изменять отображаемую метку Ole объекта, как показано на следующем скриншоте. Также можно получать или изменять отображаемую метку Ole объекта с помощью API Aspose.Cells, используя свойство [**OleObject.getLabel()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getLabel--).

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Доступ и изменение отображаемой метки связанного объекта OLE**

Пожалуйста, посмотрите следующий пример кода, он загружает [пример файла Excel](64716810.xlsx), содержащий Ole объект. Код получает Ole объект и изменяет его метку с Sample APIs на Aspose APIs. Ниже приведён вывод в консоль, показывающий эффект работы примера на примерном файле Excel.

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleAccessAndModifyLabelOfOleObject.xlsx");

// Load the sample Excel file 
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first Ole Object
let oleObject = ws.getOleObjects().get(0);

// Display the Label of the Ole Object
console.log("Ole Object Label - Before: " + oleObject.getLabel());

// Modify the Label of the Ole Object
oleObject.setLabel("Aspose APIs");

// Save workbook to memory stream
const ms = wb.save(AsposeCells.SaveFormat.Xlsx);

// Set the workbook reference to null
wb.dispose();

// Load workbook from memory stream
const wbFromStream = new AsposeCells.Workbook(ms);

// Access first worksheet
const wsFromStream = wbFromStream.getWorksheets().get(0);

// Access first Ole Object
oleObject = wsFromStream.getOleObjects().get(0);

// Display the Label of the Ole Object that has been modified earlier
console.log("Ole Object Label - After: " + oleObject.getLabel());
```

## **Вывод в консоль**

{{< highlight javascript >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
