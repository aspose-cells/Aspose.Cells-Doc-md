---  
title: Inställning av formelberäkningsläge för arbetsbok med Node.js via C++  
linktitle: Ställa in formelberäkningsläget för arbetsboken  
description: Denna artikel presenterar hur man ställer in formelberäkningsläget för en arbetsbok i Microsoft Excel med Aspose.Cells for Node.js via C++. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda metoden som tillhandahålls av Aspose.Cells för att ställa in formelberäkningsläget och få resultatet. Slutligen sparar vi den modifierade Excel filen till disken.  
keywords: Aspose.Cells, Excel, arbetsbok, formelberäkningsläge, inställningar, Node.js via C++  
type: docs  
weight: 110  
url: /sv/nodejs-cpp/setting-formula-calculation-mode-of-workbook/  
---  

{{% alert color="primary" %}}  
Microsoft Excel tillåter dig att ställa in formelberäkningsläget, det vill säga hur formler beräknas. Det finns tre möjliga värden:  

- Automatisk - beräknas om varje gång något ändras och varje gång en arbetsbok öppnas.  
- Automatisk, utom för datatabeller - beräknas om varje gång något ändras, men exkluderar datatabeller.  
- Manuell - beräknas endast när användaren uttryckligen begär det genom att trycka på F9 eller CTRL+ALT+F9 eller när arbetsboken sparas.  
{{% /alert %}}  

För att ställa in formelberäkningsläge i Microsoft Excel:  

1. Välj **Formler** och sedan **Beräkningsalternativ**.  
1. Välj ett av alternativen.  

Aspose.Cells for Node.js via C++ tillåter dig också att ställa in **Formelberäkningsläge** med hjälp av [**FormulaSettings.getCalculationMode()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getCalculationMode--) lägets egenskap. Du kan tilldela den [**CalcModeType**](https://reference.aspose.com/cells/nodejs-cpp/calcmodetype) enumeration som har några av följande värden:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Set the Formula Calculation Mode to Manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
