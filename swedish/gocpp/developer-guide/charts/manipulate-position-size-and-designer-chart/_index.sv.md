---
title: Manipulera Position, Storlek och Designer Diagram med Golang via C++
linktitle: Hantera position, storlek och formgivning av diagram
description: Lär dig hur du använder Aspose.Cells for C++ för att effektivt manipulera position, storlek och designers diagram i Microsoft Excel. Vår guide visar hur du justerar dessa egenskaper för förbättrad layout och visualisering.
keywords: Aspose.Cells for C++, Position, Storlek, Designer Diagram, Microsoft Excel, Layout, Visualisering.
type: docs
weight: 45
url: /sv/go-cpp/manipulate-position-size-and-designer-chart/
---

## **Diagramposition och storlek**
Ibland vill du ändra positionen eller storleken på det nya eller befintliga diagrammet i kalkbladet. Aspose.Cells erbjuder egenskapen [Chart.GetChartObject()](https://reference.aspose.com/cells/go-cpp/chart/getchartobject/) för att göra detta. Du kan använda dess underegenskaper för att omstorla diagrammet med ny **höjd** och **bredd** eller omlokera det med nya **X** och **Y**-koordinater.

### **Kontrollera diagrammets position och storlek**
För att ändra diagrammets position (X, Y-koordinater) eller storlek (höjd, bredd), använd dessa egenskaper:

1. [Chart.GetX()](https://reference.aspose.com/cells/go-cpp/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/go-cpp/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/go-cpp/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/go-cpp/shape/getwidth/)

Följande exempel förklarar användningen av ovanstående API:er, den laddar den befintliga arbetsboken som innehåller ett diagram i dess första kalkylblad. Sedan ändrar det storlek och position för diagrammet med Aspose.Cells.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart.go" >}}
## **Manipulering av Designerdiagram**
Det finns tillfällen då du behöver manipulera eller modifiera diagram i designmallfiler. Aspose.Cells stöder fullständigt manipulation av designmallinnehåll och element. Data, diagraminnehåll, bakgrundsbild och formatering kan bevaras med noggrannhet.

### **Manipulera designmallar i mallfiler för diagram**
För att manipulera designmallar i mallfiler, använd de diagramrelaterade API:erna. Till exempel kan du använda Worksheet.Charts egenskapen för att hämta de befintliga diagrammen i mallfilen.

#### **Skapa ett diagram**
Följande exempel visar hur man skapar ett pyramiddiagram. Senare kommer vi att manipulera detta diagram.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-1.go" >}}
#### **Manipulera diagrammet**
Följande exempel visar hur man manipulerar det befintliga diagrammet. I det här exemplet ändrar vi det skapade diagrammet ovan. I den genererade utmatningen, notera att datumetiketten för en datapunkt har ställts in till 'Storbritannien, 30K'.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-2.go" >}}
#### **Manipulera ett linjediagram i designmallen**
I det här exemplet kommer vi att manipulera ett linjediagram. Vi kommer att lägga till några data-serier i det befintliga diagrammet och ändra deras linjefärger.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-3.go" >}}
