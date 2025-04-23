---  
title: Behåll separatorer för tomma rader vid export av kalkylblad till CSV format med Node.js via C++  
linktitle: Behåll avskiljare för tomma rader vid export av kalkylblad till CSV format  
type: docs  
weight: 160  
url: /sv/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/  
---  

## **Behåll separatorer för tomma rader vid export av kalkylblad till CSV-format**  

Aspose.Cells ger möjlighet att behålla radseparatorer när man konverterar kalkylblad till CSV-format. För detta kan du använda [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--)-egenskapen av [**TxtSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/). [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) är en boolean-egenskap. För att behålla separatorerna för tomma rader vid konvertering av Excel-fil till CSV, ställ in [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--)-egenskapen till **true**.  

Följande kod laddar [käll-Excel-filen](84378743.xlsx). Den ställer in [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--)-egenskapen till **true** och sparar den som [utdata.csv](84378744.csv). Skärmbilden visar jämförelsen mellan käll-Excel-filen, standardutdata som genereras vid konvertering av kalkblad till CSV och den utdata som genereras när [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) ställs in på **true**.  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Set KeepSeparatorsForBlankRow to true to show separators in blank rows
options.setKeepSeparatorsForBlankRow(true);

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```  

