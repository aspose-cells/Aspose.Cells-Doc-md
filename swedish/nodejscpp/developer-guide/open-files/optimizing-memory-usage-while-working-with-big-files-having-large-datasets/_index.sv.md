---  
title: Optimering av minnesanvändning vid arbete med stora filer med stora dataset med Node.js via C++  
linktitle: Optimera minnesanvändningen vid arbete med stora filer med stora dataset  
type: docs  
weight: 180  
url: /sv/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/  
---  

{{% alert color="primary" %}}  

När du bygger ett kalkblad med stora datamängder eller läser en stor Microsoft Excel-fil är den totala mängden RAM som processen kommer att använda alltid en oro. Det finns åtgärder som kan anpassas för att hantera utmaningen. Aspose.Cells for Node.js via C++ ger några relevanta alternativ och API-anrop för att sänka, minska och optimera minnesanvändningen. Det kan också hjälpa processen att arbeta mer effektivt och köra snabbare.  

Använd [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) för att optimera minnesanvändningen för celldata och minska den totala minneskostnaden. När man bygger en stor datamängd för celler kan det spara en viss mängd minne jämfört med att använda standardinställningen ([**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)).  

{{% /alert %}}  

## **Optimera minne**  

### **Läsning av stora Excel-filer**  

Det följande exemplet visar hur man läser en stor Microsoft Excel-fil i optimerat läge.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the LoadOptions
const opt = new AsposeCells.LoadOptions();
// Set the memory preferences
opt.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Instantiate the Workbook
// Load the Big Excel file having large Data set in it
const wb = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), opt);
```  

### **Skrivning av stora Excel-filer**  

Det följande exemplet visar hur man skriver en stor datamängd till en arbetsbok i optimerat läge.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Set the memory preferences
wb.getSettings().setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

// To change the memory setting of existing sheets, please change memory setting for them manually:
let cells = wb.getWorksheets().get(0).getCells();
cells.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........

// Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
cells = wb.getWorksheets().add("Sheet2").getCells();
// .........
// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........
```  

## **Försiktighet**  

Det förvalda alternativet, [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/), tillämpas för alla versioner. För vissa situationer, som att bygga ett kalkblad med en stor datamängd för celler, kan [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)-alternativet optimera minnesanvändningen och minska minneskostnaden för applikationen. Dock kan detta alternativ försämra prestandan i vissa speciella fall såsom följande.  

1. **Få åtkomst till celler slumpmässigt och upprepade gånger**: Den mest effektiva sekvensen för att komma åt cellsamlingen är cell för cell i en rad, och därefter rad för rad. Speciellt om du når rader/celler via Enumerator som erhålls från [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection) och [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), maximeras prestandan med [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).  
2. **Infoga & Ta bort celler & rader**: Observera att om det finns många insättnings-/raderingsoperationer för Cell/Rows, kommer prestandaförlusten att bli märkbar för *MemoryPreference*-läget jämfört med *Normal*-läget.  
3. **Att arbeta på olika celltyper**: Om de flesta celler innehåller strängvärden eller formler, kommer minneskostnaden att vara samma som *Normal*-läget, men om det finns många tomma celler eller cellvärden som är numeriska, booleska, etc., ger [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)-alternativet bättre prestanda.  

