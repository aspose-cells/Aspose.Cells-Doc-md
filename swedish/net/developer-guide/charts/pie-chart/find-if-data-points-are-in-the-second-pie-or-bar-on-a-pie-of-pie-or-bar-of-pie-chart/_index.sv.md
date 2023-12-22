---
title: Ta reda på om datapoäng finns i den andra cirkeln eller stapeln på ett cirkel- eller cirkeldiagram
description: Lär dig hur du använder Aspose.Cells for .NET för att ta reda på om datapunkter finns i den andra cirkeln eller stapeln på en cirkel- eller stapeldiagram. Vår guide kommer att visa hur du identifierar och kommer åt den sekundära cirkeln eller stapeln på ett sammansatt diagram, så att du kan analysera och manipulera data effektivt.
keywords: Aspose.Cells for .NET, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.
type: docs
weight: 180
url: /sv/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
##  **Möjliga användningsscenarier**
 Du kan se om datapunkter för serier finns i den andra cirkeln på*Pie of Pie* diagram eller i stapeln av*Bar of Pie* diagram med Aspose.Cells. Vänligen använd[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)egendom för att bestämma det.

 Vänligen ladda ner[exempel på excel-fil](5115193.xlsx)används i följande exempelkod och se dess konsolutgång. Om du öppnar[exempel på excel-fil](5115193.xlsx) , hittar du, alla datapunkter som är mindre än 10 är inuti fältet för*Bar of Pie*diagram som också visas av konsolutgång.
##  **Ta reda på om datapoäng finns i den andra cirkeln eller stapeln på ett cirkel- eller cirkeldiagram**
 Följande exempelkod visar hur du hittar om datapunkter finns i den andra cirkeln eller stapeln på en*Pie of Pie* eller*Bar of Pie*Diagram.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
##  **Konsolutgång**
 Se följande konsolutgång som genereras efter exekveringen av ovanstående exempelkod med[exempel på excel-fil](5115193.xlsx) . Om[IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)är *falsk**, är datapunkten inuti cirkeln eller om den är *sant**, så är datapunkten inuti stapeln.



{{< highlight "java" >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
