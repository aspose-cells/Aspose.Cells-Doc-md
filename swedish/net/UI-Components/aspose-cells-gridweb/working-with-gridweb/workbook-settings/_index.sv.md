---
title: Inställningar för arbetsbok
type: docs
weight: 250
url: /sv/net/aspose-cells-gridweb/workbook-settings/
description: Den här artikeln beskriver arbetsboksinställningarna för GridWeb.
keywords: settings
---
Det finns några inställningar vi kan specificera genom att ställa in GridWorkbookSettings:

 
- **[GridWorkbookSettings](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/GridWorkbookSettings)**

|**namn** |**Beskrivning** |
|:- |:- |
| MaxIteration| Hämtar eller ställer in det maximala antalet iterationer för att lösa en cirkulär referens, standardvärdet är 100.|
| Iteration| Hämtar eller ställer in om användning av iteration för att lösa cirkulära referenser.|
| ForceFullCalculate| Hämtar eller ställer in om fullständigt beräknas varje gång en beräkning utlöses.|
| Skapa CalcChain|Hämtar eller ställer in om du skapar beräknade formlerkedja. Standard är falskt.|
| Beräkna på Öppen| Hämtar eller ställer in om alla formler ska beräknas på nytt när filen öppnas.|
| PrecisionAsDisplayed| Sant om beräkningar i den här arbetsboken kommer att göras med enbart precisionen av siffrorna när de visas|
| Datum 1904| Hämtar eller ställer in ett värde som representerar om arbetsboken använder 1904-datumsystemet.|
| CheckCustomNumberFormat| Hämtar eller ställer in om anpassat nummerformat ska kontrolleras när Style.Custom ställs in.|
| Författare| Hämtar och ställer in författaren till filen.|
 


Till exempel ställer följande kod in ReCalculateOnOpen till false för att stoppa uträkningen när filen öppnas:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 följande kod ställer in författaren för filen:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}
 
 