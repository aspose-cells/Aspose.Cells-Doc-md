---  
title: Revisionstags in einer freigegebenen Arbeitsmappe mit Node.js über C++ aktualisieren  
linktitle: Aktualisieren von Tagen unter Beibehaltung des Verlaufprotokolls in einer freigegebenen Arbeitsmappe  
type: docs  
weight: 80  
url: /de/nodejs-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/  
description: Erfahren Sie, wie Sie die Tage zur Beibehaltung der Änderungsprotokollhistorie in freigegebenen Arbeitsmappen mit Aspose.Cells for Node.js via C++ aktualisieren.  
---  

## **Mögliche Verwendungsszenarien**

Wenn Sie eine Arbeitsmappe freigeben, erscheint die Option ***Änderungshistorie für N Tage aufbewahren***, wie im folgenden Screenshot gezeigt. Sie können die Anzahl der Tage zur Historie mit Aspose.Cells for Node.js via C++ und der Eigenschaft [**WorksheetCollection.getDaysPreservingHistory()**](https://reference.aspose.com/cells/nodejs-cpp/revisionlogcollection/#getDaysPreservingHistory--) aktualisieren.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Aktualisieren von Tagen unter Beibehaltung des Verlaufprotokolls in einer freigegebenen Arbeitsmappe**

Der folgende Beispielcode erstellt eine leere Arbeitsmappe, teilt sie dann und aktualisiert die Revisionsprotokolle, um den Verlauf 7 Tage lang zu speichern, was normalerweise 30 Tage beträgt. Bitte sehen Sie die [Ausgabedatei Excel](60489773.xlsx), die vom Code erstellt wurde, als Referenz an.

## **Beispielcode**

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
