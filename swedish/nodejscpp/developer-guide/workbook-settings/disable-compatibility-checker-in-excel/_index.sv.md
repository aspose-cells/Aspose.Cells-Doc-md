---  
title: Inaktivera kompatibilitetskontroll i Excel med Node.js via C++  
linktitle: Inaktivera kompatibilitetskontroll i Excel  
type: docs  
weight: 170  
url: /sv/nodejs-cpp/disable-compatibility-checker-in-excel/  
description: Lär dig hur du inaktiverar kompatibilitetskontroll genom Aspose.Cells for Node.js via C++ API.  
keywords: Node.js Inaktivera kompatibilitetskontroll, Excel Inaktivera kompatibilitetskontroll i Node.js via C++, Inaktivera kompatibilitetskontroll i arbetsbok.  
---  

## Inaktivera kompatibilitetskontroll i Excel-Arbetsblad i Node.js  

{{% alert color="primary" %}}  
Microsoft Excels kompatibilitetskontroll flaggar för när en fil sparas i ett tidigare filformat kan orsaka funktionalitetsproblem eller förlust av fidelitet. Kompatibilitetskontrollen är en funktion i Microsoft Office Excel 2007 och Microsoft Excel 2010.  

När du sparar en arbetsbok i en tidigare version, Excel 97 genom Excel 2003, från Excel 2007 eller Excel 2010 skannar kompatibilitetskontrollen arbetsboken för att se om den innehåller funktioner som inte stöds av den tidigare versionen. För att hjälpa dig fatta beslut om hur du hanterar kompatibilitetsproblem visar kompatibilitetskontrollen dialogrutor med alternativ. Den kan också användas för att skapa en rapport om eventuella problem i arbetsboken eller inaktivera funktionen.  

Ibland måste du inaktivera kompatibilitetskontrollen för ett särskilt kalkylblad. Med Aspose.Cells API:erna kan du göra detta programmatiskt så att användare inte blir frustrerade eller förvirrade av dialogrutan för kompatibilitetskontroll som dyker upp när de sparar om filen manuellt i Microsoft Excel.  
{{% /alert %}}  

## **Hur man inaktiverar kompatibilitetskontrollen med hjälp av Microsoft Excel**  

För att inaktivera kompatibilitetskontrollen i Microsoft Excel (t.ex. Microsoft Excel 2007/2010):  

- (Excel 2007) Klicka på Office-knappen, klicka på **Förbered**, klicka på **Kör kompatibilitetskontroll**, och avmarkera sedan alternativet **Kontrollera kompatibilitet när du sparar arbetsboken**.  
- (Excel 2010) På fliken Fil klickar du på **Info**, sedan **Sök efter problem**, klickar på **Kontrollera kompatibilitet** och avmarkerar till sist alternativet **Kontrollera kompatibilitet när du sparar den här arbetsboken**.  

## **Hur man inaktiverar kompatibilitetskontrollen med hjälp av Aspose.Cells API:er**  

Ställ in egenskapen [**Workbook.getCheckCompatibility()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCheckCompatibility--) till **false** för att inaktivera Microsoft Excels kompatibilitetskontroll.  

### **Kodexempel**  

Följande kodexempel visar hur man inaktiverar kompatibilitetskontrollen med Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Disable the compatibility checker
workbook.getSettings().setCheckCompatibility(false);

const outputFilePath = path.join(dataDir, "Output_BK_CompCheck.out.xlsx");
// Saving the Excel file
workbook.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
