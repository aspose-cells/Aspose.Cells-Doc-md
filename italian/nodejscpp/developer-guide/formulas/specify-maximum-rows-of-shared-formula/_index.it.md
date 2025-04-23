---  
title: Specificare il numero massimo di righe per le formule condivise con Node.js tramite C++  
linktitle: Specificare il Numero Massimo di Righe della Formula Condivisa  
type: docs  
weight: 40  
url: /it/nodejs-cpp/specify-maximum-rows-of-shared-formula/  
description: Scopri come specificare il numero massimo di righe per le formule condivise usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Il numero massimo di righe predefinito per la formula condivisa è 64. Può essere qualsiasi numero, ad esempio 1000. La performance della formula condivisa varia in base al numero di righe. Perciò, Aspose.Cells fornisce la proprietà [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--) che può essere usata per specificare il numero massimo di righe. La formula condivisa sarà suddivisa in più formule condivise se il numero totale di righe supera questo limite, come mostrato nello screenshot seguente.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Specificare il numero massimo di righe della formula condivisa**  

Il codice di esempio seguente spiega come usare la proprietà [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--). Imposta il numero massimo di righe della formula condivisa a 5, aggiunge la formula condivisa nella cella D1 per 100 righe e salva in [file Excel di output](61767856.xlsx). Se estrai il contenuto del file Excel di output e controlli *sheet1.xml*, vedrai che la formula condivisa si suddivide ogni 5 righe come evidenziato nello screenshot sopra.  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a new workbook
const wb = new AsposeCells.Workbook();

// Set the max rows of shared formula to 5
wb.getSettings().setMaxRowsOfSharedFormula(5);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell D1
const cell = ws.getCells().get("D1");

// Set the shared formula in 100 rows
cell.setSharedFormula("=Sum(A1:A2)", 100, 1);

// Save the output Excel file
wb.save("outputSpecifyMaximumRowsOfSharedFormula.xlsx");
```  

