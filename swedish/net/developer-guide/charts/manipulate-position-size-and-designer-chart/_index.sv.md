---
title: Manipulera positionsstorlek och designerdiagram
type: docs
weight: 45
url: /sv/net/manipulate-position-size-and-designer-chart/
---
## **Kartans position och storlek**
 Ibland vill du ändra positionen eller storleken på det nya eller befintliga diagrammet i kalkylbladet. Aspose.Cells tillhandahåller[Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) egendom för att uppnå detta. Du kan använda dess underegenskaper för att ändra storlek på diagrammet med nytt**höjd** och**bredd** eller placera om den med ny** X** och**Y** koordinater.
### **Kontrollera diagramposition och storlek**
För att ändra diagrammets position (X, Y-koordinater) eller storlek (höjd, bredd), använd dessa egenskaper:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

Följande exempel förklarar användningen av ovanstående API:er, det laddar den befintliga arbetsboken som innehåller ett diagram i sitt första kalkylblad. Sedan ändrar den storlek och placerar om diagrammet med Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **Manipulera designerdiagram**
Det finns tillfällen då du behöver manipulera eller ändra diagram i designermallfiler. Aspose.Cells stöder fullt ut manipulering av designerdiagraminnehåll och element. Data, diagraminnehåll, bakgrundsbild och formatering kan bevaras med noggrannhet.
### **Manipulera designerdiagram i mallfiler**
För att manipulera designerdiagram i mallfiler, använd diagramrelaterade API. Till exempel kan du använda egenskapen Worksheet.Charts för att hämta den befintliga diagramsamlingen i mallfilen.
#### **Skapa ett diagram**
Följande exempel visar hur man skapar ett pyramiddiagram. Vi kommer att manipulera detta diagram senare.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **Manipulera diagrammet**
Följande exempel visar hur man manipulerar det befintliga diagrammet. I det här exemplet ändrar vi diagrammet som skapats ovan. I den genererade utdatan, notera att datumetiketten för en datapunkt har ställts in på 'Storbritannien, 30K'.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Manipulera ett linjediagram i designermallen**
I det här exemplet kommer vi att manipulera ett linjediagram. Vi kommer att lägga till några dataserier till det befintliga diagrammet och ändra deras linjefärger.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

