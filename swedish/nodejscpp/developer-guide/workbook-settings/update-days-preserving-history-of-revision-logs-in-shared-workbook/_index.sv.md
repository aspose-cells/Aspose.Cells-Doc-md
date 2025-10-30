---  
title: Uppdatera dagar och behåll revisionslogg i delad arbetsbok med Node.js via C++  
linktitle: Uppdatera antal sparade historikrevisioner på delad arbetsbok  
type: docs  
weight: 80  
url: /sv/nodejs-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/  
description: Lär dig hur du uppdaterar dagarna för att behålla revisionsloggen i delade arbetsböcker med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**

När du delar en arbetsbok får du ett alternativ som heter ***Behåll ändringshistorik i N dagar*** som visas i följande skärmbild. Du kan uppdatera antalet dagar för att behålla historiken med Aspose.Cells for Node.js via C++ med egenskapen [**WorksheetCollection.getDaysPreservingHistory()**](https://reference.aspose.com/cells/nodejs-cpp/revisionlogcollection/#getDaysPreservingHistory--).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Uppdatera antal sparade historikrevisioner på delad arbetsbok**

Följande exempelkod skapar en tom arbetsbok, delar den sedan och uppdaterar revisionsloggar dagar med bibehållen historia till 7 dagar, vilket normalt är 30 dagar. Se [output Excel-filet](60489773.xlsx) som genereras av koden för en referens.

## **Exempelkod**

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

{{< app/cells/assistant language="nodejs-cpp" >}}
