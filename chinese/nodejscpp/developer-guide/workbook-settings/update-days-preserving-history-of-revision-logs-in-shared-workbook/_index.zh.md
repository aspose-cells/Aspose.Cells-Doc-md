---  
title: 在共享工作簿时，更新保持修订日志历史天数，使用Node.js通过C++  
linktitle: 在共享工作簿中保留修订日志的更新日志  
type: docs  
weight: 80  
url: /zh/nodejs-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/  
description: 学习如何用Aspose.Cells for Node.js via C++更新共享工作簿中保持修订日志的天数。  
---  

## **可能的使用场景**

共享工作簿时，你会看到一个选项“***保持更改历史N天***”，如下图所示。你可以使用Aspose.Cells for Node.js via C++的[**WorksheetCollection.getDaysPreservingHistory()**](https://reference.aspose.com/cells/nodejs-cpp/revisionlogcollection/#getDaysPreservingHistory--)属性来更新保存历史的天数。

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **在共享工作簿中保留修订日志的更新日志**

以下示例代码创建一个空白工作簿，然后共享它并将修订日志天数修改为7天，通常是30天。请参考代码生成的[输出Excel文件](60489773.xlsx)。

## **示例代码**

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

