---  
title: Specificera Far East och Latinnamnet på typsnittet i Textalternativ för Form med Node.js via C++  
linktitle: Ange det fjärrösterländska och latinska namnet på teckensnittet i texternas alternativ för Shape  
type: docs  
weight: 1600  
url: /sv/nodejs-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/  
description: Lär dig hur du specificerar Far East och Latin typsnittsnamn i textalternativ för former med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

 Ibland vill du visa text i Far East-språkets typsnitt t.ex. japanska, kinesiska, thailändska, etc. Aspose.Cells for Node.js via C++ tillhandahåller [**TextOptions.getFarEastName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getFarEastName--)-egenskapen som kan användas för att specificera typsnittets namn för Far East-språk. Dessutom kan du också specificera Latin-typsnittets namn med hjälp av [**TextOptions.getLatinName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getLatinName--)-egenskapen.  

## **Ange det fjärrösterländska och latinska namnet på teckensnittet i texternas alternativ för Shape**  

Följande exempel skapar en textruta och lägger till japansk text inuti den. Den specificerar sedan Latin- och Far East-teckensnittsnamnen för texten och sparar arbetsboken som [utdata Excel-fil](67338274.xlsx). Nedan visas en skärmbild av Latin- och Far East-teckensnämnena för den utgående textrutan i Microsoft Excel.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add textbox inside the worksheet.
const idx = ws.getTextBoxes().add(5, 5, 50, 200);
const tb = ws.getTextBoxes().get(idx);

// Set the text of the textbox.
tb.setText("こんにちは世界");

// Specify the Far East and Latin name of the font.
tb.getTextOptions().setLatinName("Comic Sans MS");
tb.getTextOptions().setFarEastName("KaiTi");

// Save the output Excel file.
wb.save("outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
