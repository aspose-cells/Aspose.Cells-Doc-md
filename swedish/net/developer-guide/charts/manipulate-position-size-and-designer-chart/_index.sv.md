---
title: Hantera position, storlek och formgivning av diagram
description: Lär dig hur du använder Aspose.Cells for .NET för att effektivt hantera position, storlek och formgivning av diagram i Microsoft Excel. Vår guide kommer att visa hur du justerar dessa egenskaper för förbättrad layout och visualisering.
keywords: Aspose.Cells for .NET, Position, Storlek, Formgivning av diagram, Microsoft Excel, Layout, Visualisering.
type: docs
weight: 45
url: /sv/net/manipulate-position-size-and-designer-chart/
---

## **Diagramposition och storlek**
Ibland vill du ändra positionen eller storleken på det nya eller befintliga diagrammet inuti kalkylarket. Aspose.Cells tillhandahåller [Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) egenskapen för att uppnå detta. Du kan använda dess underliggande egenskaper för att ändra diagrammet med ny **höjd** och **bredd** eller ompositionera det med nya **X** och **Y** koordinater.
### **Kontrollera diagrammets position och storlek**
För att ändra diagrammets position (X, Y-koordinater) eller storlek (höjd, bredd), använd dessa egenskaper:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

Följande exempel förklarar användningen av ovanstående API:er, den laddar den befintliga arbetsboken som innehåller ett diagram i dess första kalkylblad. Sedan ändrar det storlek och position för diagrammet med Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **Manipulering av Designerdiagram**
Det finns tillfällen då du behöver manipulera eller modifiera diagram i designmallfiler. Aspose.Cells stöder fullständigt manipulation av designmallinnehåll och element. Data, diagraminnehåll, bakgrundsbild och formatering kan bevaras med noggrannhet.
### **Manipulera designmallar i mallfiler för diagram**
För att manipulera designmallar i mallfiler, använd de diagramrelaterade API:erna. Till exempel kan du använda Worksheet.Charts egenskapen för att hämta de befintliga diagrammen i mallfilen.
#### **Skapa ett diagram**
Följande exempel visar hur man skapar ett pyramiddiagram. Senare kommer vi att manipulera detta diagram.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **Manipulera diagrammet**
Följande exempel visar hur man manipulerar det befintliga diagrammet. I det här exemplet ändrar vi det skapade diagrammet ovan. I den genererade utmatningen, notera att datumetiketten för en datapunkt har ställts in till 'Storbritannien, 30K'.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Manipulera ett linjediagram i designmallen**
I det här exemplet kommer vi att manipulera ett linjediagram. Vi kommer att lägga till några data-serier i det befintliga diagrammet och ändra deras linjefärger.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
