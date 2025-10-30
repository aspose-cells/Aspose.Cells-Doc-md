---
title: Hantera position, storlek och formgivning av diagram
description: Lär dig hur du använder Aspose.Cells för Python via .NET för att effektivt manipulera position, storlek och design av diagram i Microsoft Excel. Vår guide visar hur du justerar dessa egenskaper för förbättrad layout och visualisering.
keywords: Aspose.Cells för Python via .NET, Position, Storlek, Designer Diagram, Microsoft Excel, Layout, Visualisering.
type: docs
weight: 45
url: /sv/python-net/manipulate-position-size-and-designer-chart/
---

## **Diagramposition och storlek**
Ibland vill du ändra position eller storlek på det nya eller befintliga diagrammet inuti arbetsbladet. Aspose.Cells för Python via .NET tillhandahåller [Chart.chart_object](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/chart_object) egenskapen för att uppnå detta. Du kan använda dess underegenskaper för att ändra storlek på diagrammet med ny **höjd** och **bredd** eller omplacera det med nya **X** och **Y** koordinater.
### **Kontrollera diagrammets position och storlek**
För att ändra diagrammets position (X, Y-koordinater) eller storlek (höjd, bredd), använd dessa egenskaper:

1. [Chart.chart_object.x](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/x)
1. [Chart.chart_object.y](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/y)
1. [Chart.chart_object.height](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/height)
1. [Chart.chart_object.width](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/width)

Följande exempel förklarar användningen av ovan nämnda API:er, det laddar det befintliga arbetsboken som innehåller ett diagram i dess första arbetsblad. Sedan ändrar det storlek på och omplacerar diagrammet med Aspose.Cells för Python via .NET.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartPosition-1.py" >}}
## **Manipulering av Designerdiagram**
Det finns tillfällen då du behöver manipulera eller ändra diagram i designer mallfiler. Aspose.Cells för Python via .NET stöder fullt ut manipulation av designerdiagraminnehåll och element. Data, diagraminnehåll, bakgrundsbild och formateringar kan bevaras med exakthet.
### **Manipulera designmallar i mallfiler för diagram**
För att manipulera designmallar i mallfiler, använd de diagramrelaterade API:erna. Till exempel kan du använda Worksheet.Charts egenskapen för att hämta de befintliga diagrammen i mallfilen.
#### **Skapa ett diagram**
Följande exempel visar hur man skapar ett pyramiddiagram. Senare kommer vi att manipulera detta diagram.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-HowToCreateChart-1.py" >}}
#### **Manipulera diagrammet**
Följande exempel visar hur man manipulerar det befintliga diagrammet. I det här exemplet ändrar vi det skapade diagrammet ovan. I den genererade utmatningen, notera att datumetiketten för en datapunkt har ställts in till 'Storbritannien, 30K'.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyPieChart-1.py" >}}
#### **Manipulera ett linjediagram i designmallen**
I det här exemplet kommer vi att manipulera ett linjediagram. Vi kommer att lägga till några data-serier i det befintliga diagrammet och ändra deras linjefärger.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyLineChart-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
