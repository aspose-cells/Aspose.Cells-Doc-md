---  
title: Spara arbetsbok till Strict Open XML Kalkylbladsformat med Node.js via C++  
linktitle: Spara arbetsbok till strikt öppet XML kalkylbladsformat  
type: docs  
weight: 150  
url: /sv/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/  
description: Lär dig hur du sparar en arbetsbok i Strict Open XML Kalkylbladsformat med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Aspose.Cells for Node.js via C++ tillåter dig att spara arbetsboken i *Strict Open XML Kalkylblad* format. För detta syfte, tillhandahåller det egenskapen [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--). Om du sätter dess värde till [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance), kommer den resulterande Excel-filen att sparas i Strict Open XML Kalkylbladsformat.  

## **Spara arbetsbok i strikt öppet XML-kalkylbladsformat**  

Följande exempel skapar en arbetsbok och ställer in värdet av egenskapen [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--) till [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance) och sparar den som [utdata Excel-fil](67338272.xlsx). Om du öppnar den genererade Excel-filen i Microsoft Excel och öppnar Spara Som... dialogrutan, kommer du att se dess format som *Strict Open XML Kalkylblad* som visas i denna skärmbild.  

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)  

## **Exempelkod**  

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
