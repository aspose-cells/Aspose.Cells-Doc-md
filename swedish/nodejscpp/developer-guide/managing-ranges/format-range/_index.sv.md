---  
title: Formatera områden med Node.js via C++  
linktitle: Formatera områden  
type: docs  
weight: 105  
url: /sv/nodejs-cpp/how-to-format-a-range/  
description: Lär dig att formatera ett cellområde i Excel med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  
När du behöver tillämpa en stil på ett område kan du använda områdesformatering.  

## **Hur man formaterar ett område i Excel**  

För att formatera ett område med celler i Excel kan du använda de inbyggda formateringsalternativen som tillhandahålls av Excel. Så här kan du formatera en område med celler direkt i Excel:  

1. Öppna Excel och öppna arbetsboken som innehåller det område du vill formatera.  

2. Välj det område med celler som du vill formatera. Du kan klicka och dra för att markera området, eller så kan du använda tangentbordsgenvägar som Skift + Piltangenter för att utöka markeringen.  

3. När området är markerat högerklickar du på det markerade området och väljer "Formatera celler" från snabbmenyn. Alternativt kan du gå till fliken Start i Excel-ribbonen, klicka på rullgardinsmenyn "Format" i gruppen "Celler" och välja "Formatera celler".  

4. Dialogrutan "Formatera celler" visas. Här kan du välja olika formateringsalternativ att tillämpa på det markerade området. Till exempel kan du ändra teckensnittsstil, teckenstorlek, teckenfärg, nummerformat, linjer, bakgrundsfärg, etc. Utforska de olika flikarna i dialogrutan för att komma åt olika formateringsalternativ.  

5. Efter att ha gjort de önskade formateringsändringarna klickar du på "OK"-knappen för att tillämpa formateringen på det markerade området.  

## **Hur man formaterar ett område med Node.js**  

För att formatera ett område med Aspose.Cells for Node.js via C++ kan du använda följande metoder:  
1. [Range.applyStyle(style, flag)](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  
3. [Range.setStyle(style)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  

## **Exempelkod**  
I det här exemplet skapar vi en Excel-arbetsbok, lägger till en del provdata, får åtkomst till den första arbetsbladet och definierar två intervall("A1:C3" och "A4:C5"). Sedan skapar vi nya stilar, ställer in olika formateringsalternativ (t.ex., teckenfärg, fetstil) och tillämpar stilen på intervallet. Slutligen sparar vi arbetsboken i en ny fil.  
<br>  
![todo:image_alt_text](format-range.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = workbook.getWorksheets().get(0);

const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Access the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Define the range
const range = worksheet.getCells().createRange("A1:C3");

// Apply formatting to the range
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Red);
style.getFont().setIsBold(true);

const flag = new AsposeCells.StyleFlag();
flag.setFont(true);
range.applyStyle(style, flag);

// Define the range
const range2 = worksheet.getCells().createRange("A4:C5");

// Apply formatting to the range
const style2 = workbook.createStyle();
style2.getFont().setColor(AsposeCells.Color.Blue);
style2.getFont().setIsItalic(true);
range2.setStyle(style2);

// Save the modified workbook
workbook.save("output.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
