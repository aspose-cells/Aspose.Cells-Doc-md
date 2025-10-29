---  
title: Создать общий рабочий файл с помощью Aspose.Cells for Node.js via C++  
linktitle: Создание общей книги с Aspose.Cells  
type: docs  
weight: 40  
url: /ru/nodejs-cpp/create-shared-workbook-with-aspose-cells/  
description: Узнайте, как создать общий рабочий файл, используя Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Microsoft Excel позволяет делиться рабочей книгой, как показано на следующем скриншоте. При совместном использовании несколько пользователей могут редактировать книгу в сети. Aspose.Cells for Node.js via C++ позволяет создавать совместную книгу с помощью свойства [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Создание общей книги с Aspose.Cells**  

Следующий пример кода создает совместную книгу, устанавливая свойство [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--) в значение **true**. Открыв [выходной файл Excel](55541786.xlsx) в Microsoft Excel, вы увидите указание **Shared** рядом с именем файла, как показано на скриншоте.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Образец кода**  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create Workbook object
const wb = new AsposeCells.Workbook();

// Share the Workbook
wb.getSettings().setShared(true);

// Save the Shared Workbook
wb.save("outputSharedWorkbook.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
