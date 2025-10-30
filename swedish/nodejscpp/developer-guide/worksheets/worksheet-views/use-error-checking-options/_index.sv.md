---  
title: Använd felkontrollalternativ med Node.js via C++  
linktitle: Använda alternativ för felkontroll  
type: docs  
weight: 140  
url: /sv/nodejs-cpp/use-error-checking-options/  
description: Lär dig hur man programmässigt använder felkontrollalternativ i Excel kalkylblad med Aspose.Cells for Node.js via C++.  
keywords: lagra nummer som text i Excel med Node.js via C++, felkontrollalternativ i Excel Node.js via C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel tillåter användare att definiera felkontrolloptioner och regler. Användare ser ofta felkontroller när de skapar formler, en liten triangel i det övre högra hörnet av en cell markeras när det är ett problem med en cell. Excel tillhandahåller information som hjälper användare att korrigera vanliga problem.  
{{% /alert %}}  

## **Typer av fel**  

Fel som innebär att formeln inte kan returnera ett resultat – till exempel att dela ett tal med noll – kräver omedelbar uppmärksamhet och ett felvärde visas i cellen. Klicka på den gröna triangeln visar ett utropstecken; klicka på detta öppnar en lista med alternativ.  

Felet kan lösas med hjälp av alternativen eller ignoreras. Att ignorera ett fel innebär att detta fel inte kommer att visas vid framtida felkontroller.  

Aspose.Cells tillhandahåller funktioner för felkontrollalternativ. Klassen [**ErrorCheckOption**](https://reference.aspose.com/cells/nodejs-cpp/errorcheckoption) hanterar olika typer av felkontroller, till exempel nummer lagrade som text, formelberäkningsfel och valideringsfel. Använd enumerationen [**ErrorCheckType**](https://reference.aspose.com/cells/nodejs-cpp/errorchecktype) för att ställa in önskad felkontroll.  

## **Nummer som lagras som text**  

Ibland kan nummer formateras och lagras i celler som text. Det kan orsaka problem med beräkningar eller producera förvirrande sorteringsordningar. Nummer som är formaterade som text är vänsterjusterade istället för högerjusterade i cellen. Om en formel som ska utföra en matematisk operation på celler inte returnerar ett värde, kontrollera justeringen i cellerna som formeln hänvisar till - vissa eller alla dessa celler kan vara nummer formaterade som text.  

Du kan använda felkontrolloptionerna för att snabbt konvertera nummer som lagras som text till verkliga nummer.  

1. På **Verktyg**-menyn klickar du på **Alternativ**.  
1. Markera fliken för Felkontroll.  
   **Alternativ för siffror sparade som text** alternativet är markerat som standard.  
1. Inaktivera det.  

Följande exempelkod visar hur man inaktiverar felkontrollen för siffror sparade som text för en arbetsbok i mallen XLS med hjälp av Aspose.Cells API.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a workbook and opening a template spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Instantiate the error checking options
const opts = sheet.getErrorCheckOptions();

const index = opts.add();
const opt = opts.get(index);
// Disable the numbers stored as text option
opt.setErrorCheck(AsposeCells.ErrorCheckType.NumberStoredAsText, false);
// Set the range
opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

const outputFilePath = path.join(dataDir, "out_test.out.xlsx");
// Save the Excel file
workbook.save(outputFilePath);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
