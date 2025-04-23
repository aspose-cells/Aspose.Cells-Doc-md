---  
title: Сохранить рабочую книгу в строгий формат Open XML Spreadsheet с помощью Node.js через C++  
linktitle: Сохранить книгу в формате строгой открытой электронной таблицы XML  
type: docs  
weight: 150  
url: /ru/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/  
description: Узнайте, как сохранить рабочую книгу в формате Strict Open XML Spreadsheet, используя Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Aspose.Cells for Node.js via C++ позволяет сохранять рабочую книгу в формате *Strict Open XML Spreadsheet*. Для этого он предоставляет свойство [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--). Если установить его значение как [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance), то итоговый файл Excel будет сохранен в формате Strict Open XML Spreadsheet.  

## **Сохранить книгу в формате Strict Open XML Spreadsheet**  

Следующий пример кода создает рабочую книгу и устанавливает значение свойства [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--) как [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance), затем сохраняет ее как [выходной файл Excel](67338272.xlsx). Если открыть выходной файл Excel в Microsoft Excel и выбрать «Сохранить как…», вы увидите его формат как *Strict Open XML Spreadsheet*, что показано на этом скриншоте.  

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)  

## **Образец кода**  

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

