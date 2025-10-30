---  
title: Erstellen Sie eine gemeinsame Arbeitsmappe mit Aspose.Cells for Node.js via C++  
linktitle: Freigegebene Arbeitsmappe mit Aspose.Cells erstellen  
type: docs  
weight: 40  
url: /de/nodejs-cpp/create-shared-workbook-with-aspose-cells/  
description: Lernen Sie, wie man mit Aspose.Cells for Node.js via C++ eine gemeinsame Arbeitsmappe erstellt.  
---  

## **Mögliche Verwendungsszenarien**  

Microsoft Excel ermöglicht das Teilen der Arbeitsmappe wie im folgenden Screenshot gezeigt. Beim Teilen der Arbeitsmappe können mehr als ein Benutzer die Arbeitsmappe im Netzwerk bearbeiten. Aspose.Cells for Node.js via C++ ermöglicht es, eine gemeinsame Arbeitsmappe mit der [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--) Eigenschaft zu erstellen.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Gemeinsame Arbeitsmappe mit Aspose.Cells erstellen**  

Der folgende Beispielcode erstellt ein geteiltes Arbeitsbuch, indem er die [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--)-Eigenschaft auf **true** setzt. Wenn Sie die [Ausgabedatei](55541786.xlsx) in Microsoft Excel öffnen, sehen Sie **Shared** mit dem Namen der Arbeitsmappe, wie in diesem Screenshot gezeigt.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Beispielcode**  

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
