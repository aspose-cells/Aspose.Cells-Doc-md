---  
title: Arbeitsmappe im Strict Open XML Spreadsheet Format mit Node.js via C++ speichern  
linktitle: Arbeitsmappe im strengen Open XML Tabellenformat speichern  
type: docs  
weight: 150  
url: /de/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/  
description: Erfahren Sie, wie man eine Arbeitsmappe im Strict Open XML Spreadsheet Format mit Aspose.Cells for Node.js via C++ speichert.  
---  

## **Mögliche Verwendungsszenarien**  

Aspose.Cells for Node.js via C++ ermöglicht es, die Arbeitsmappe im *Strict Open XML Spreadsheet*-Format zu speichern. Dafür bietet es die Eigenschaft [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--). Wenn Sie den Wert auf [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance) setzen, wird die Excel-Datei im Strict Open XML Spreadsheet-Format gespeichert.  

## **Arbeitsmappe im Strict Open XML-Tabellenkalkulationsformat speichern**  

Das folgende Beispiel erstellt eine Arbeitsmappe, setzt die [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--)-Eigenschaft auf [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance) und speichert sie als [Ausgabedatei](67338272.xlsx). Wenn Sie die Ausgabedatei in Microsoft Excel öffnen und den „Speichern unter“-Dialog öffnen, sehen Sie das Format als *Strict Open XML Spreadsheet*, wie in diesem Screenshot gezeigt.  

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)  

## **Beispielcode**  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
