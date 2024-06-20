---
title: Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj eller stapeldiagram
description: Lär dig hur du använder Aspose.Cells for .NET för att ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj eller stapeldiagram. Vår guide kommer att demonstrera hur du identifierar och får åtkomst till den sekundära pajen eller stapeln på ett sammansatt diagram, vilket gör det möjligt för dig att analysera och manipulera datan effektivt.
keywords: Aspose.Cells for .NET, Paj av paj diagram, Stapel av paj diagram, Sekundär paj, Sekundär stapel, Dataanalys, Datamanipulering.
type: docs
weight: 180
url: /sv/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Möjliga användningsscenario**
Du kan ta reda på om datapunkterna i serien finns i den andra pajen på *Paj av paj*-diagram eller i stapeln på *Stapel av paj*-diagram med hjälp av Aspose.Cells. Använd egenskapen [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) för att bestämma det.

Ladda ner den [exempelfil i Excel](5115193.xlsx) som används i följande exempelkod och se dess konsoloutput. Om du öppnar [exempelfilen i Excel](5115193.xlsx) hittar du att alla datapunkter som är mindre än 10 finns inuti stapeln på *Stapel av paj*-diagram som också visas i konsoloutputen.
## **Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj- eller stapeldiagram**
Följande exempelkod visar hur du tar reda på om datapunkterna finns i den andra pajen eller stapeln på ett *Paj av paj*- eller *Stapel av paj*-diagram.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **Konsoloutput**
Se den följande konsoloutputen som genererats efter att ovanstående exempelkod har körts med [exempelfilen i Excel](5115193.xlsx). Om [IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) är **false**, finns datapunkten inuti pajskalet och om den är **true** är datapunkten inuti stapeln.



{{< highlight java >}}

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
