---  
title: Обновление дней с сохранением истории журналов изменений в общем рабочем спряжении с помощью Node.js через C++  
linktitle: Обновление дней, сохраняющих историю журналов версий в общей книге  
type: docs  
weight: 80  
url: /ru/nodejs-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/  
description: Узнайте, как обновлять количество дней для сохранения истории журналов изменений в общих рабочих книгах с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**

Когда вы делитесь рабочей книгой, появляется опция, называемая ***Хранить историю изменений в течение N дней***, как показано на следующем снимке экрана. Вы можете обновить количество дней для сохранения истории, используя Aspose.Cells for Node.js via C++ с помощью свойства [**WorksheetCollection.getDaysPreservingHistory()**](https://reference.aspose.com/cells/nodejs-cpp/revisionlogcollection/#getDaysPreservingHistory--).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Обновление дней, сохраняющих историю журналов версий в общей книге**

В следующем образце кода создается пустая книга, затем ее делят и обновляются журналы ревизии для сохранения истории на 7 дней, что обычно составляет 30 дней. Пожалуйста, обратитесь к [выходному файлу Excel](60489773.xlsx), созданному кодом в качестве справки.

## **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Share the workbook
workbook.getSettings().setShared(true);

// Update DaysPreservingHistory of RevisionLogs
workbook.getWorksheets().getRevisionLogs().setDaysPreservingHistory(7);

// Save the workbook
workbook.save("outputShared_DaysPreservingHistory.xlsx");
```  

