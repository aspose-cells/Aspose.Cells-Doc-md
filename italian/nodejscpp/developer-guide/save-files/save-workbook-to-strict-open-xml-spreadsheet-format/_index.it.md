---  
title: Salvare il Workbook in formato Strict Open XML Spreadsheet con Node.js tramite C++  
linktitle: Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet  
type: docs  
weight: 150  
url: /it/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/  
description: Impara come salvare un workbook in formato Strict Open XML Spreadsheet usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Aspose.Cells for Node.js via C++ consente di salvare il workbook in formato *Strict Open XML Spreadsheet*. A tal fine, fornisce la proprietà [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--). Se imposti il suo valore come [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance), il file Excel di output verrà salvato in formato Strict Open XML Spreadsheet.  

## **Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet**  

Il seguente esempio di codice crea un workbook, imposta il valore della proprietà [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--) su [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance) e lo salva come [file Excel di output](67338272.xlsx). Se apri il file Excel di output in Microsoft Excel e apri la finestra di dialogo Salva con nome..., vedrai il suo formato come *Strict Open XML Spreadsheet* come mostrato in questa schermata.  

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook.
const wb = new AsposeCells.Workbook();

// Specify - Strict Open XML Spreadsheet - Format.
wb.getSettings().setCompliance(AsposeCells.OoxmlCompliance.Iso29500_2008_Strict);

// Add message in cell B4 of first worksheet.
const b4 = wb.getWorksheets().get(0).getCells().get("B4");
b4.putValue("This Excel file has Strict Open XML Spreadsheet format.");

// Save to output Excel file.
wb.save("outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

