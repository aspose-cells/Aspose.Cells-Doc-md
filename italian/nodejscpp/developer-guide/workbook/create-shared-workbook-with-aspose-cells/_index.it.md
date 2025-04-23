---  
title: Crea un file condiviso con Aspose.Cells for Node.js via C++  
linktitle: Creare un libro di lavoro condiviso con Aspose.Cells  
type: docs  
weight: 40  
url: /it/nodejs-cpp/create-shared-workbook-with-aspose-cells/  
description: Impara a creare un workbook condiviso usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Microsoft Excel permette di condividere il workbook come mostrato nello screenshot seguente. Quando condividi il workbook, più utenti possono modificarlo sulla rete. Aspose.Cells for Node.js via C++ ti consente di creare un workbook condiviso con la proprietà [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Creare un libro di lavoro condiviso con Aspose.Cells**  

Il seguente esempio di codice crea un workbook condiviso impostando la proprietà [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--) come **true**. Quando apri il [file Excel di output](55541786.xlsx) in Microsoft Excel, vedrai la dicitura **Shared** insieme al nome del workbook come mostrato in questa schermata.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Codice di Esempio**  

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

