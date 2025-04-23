---
title: Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj eller stapeldiagram
type: docs
weight: 910
url: /sv/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Möjliga användningsscenario**
Du kan kontrollera om datamarker för serier finns i den andra tårtan på *Tårta av tårta*-diagram eller i stapeln på *Stapel av tårta*-diagram med hjälp av Aspose.Cells. Använd egenskapen [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) för att avgöra det.

Vänligen ladda ner den [exempelfil i Excel](5473373.xlsx) som används i följande exempelkod och se dess konsoloutput. Om du öppnar den [exempelfil i Excel](5473373.xlsx) kommer du att finna att alla datamarkörer som är mindre än 10 finns inne i stapeln på *Stapel av tårta*-diagrammet, vilket också visas i konsoloutput.
## **Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj- eller stapeldiagram**
Följande exempelkod visar hur du tar reda på om datapunkterna finns i den andra pajen eller stapeln på ett *Paj av paj*- eller *Stapel av paj*-diagram.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **Konsoloutput**
Se följande konsoloutput genererad efter att ovanstående exempelkod har körts med den [exempelfil i Excel](5473373.xlsx). Om [IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) är **false**, är datamarkören inne i tårtan, och om det är **true**, är datamarkören inne i stapeln.

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: false

Value: 9

IsInSecondaryPlot: true

Value: 2

IsInSecondaryPlot: true

Value: 40

IsInSecondaryPlot: false

Value: 5

IsInSecondaryPlot: true

Value: 4

IsInSecondaryPlot: true

Value: 25

IsInSecondaryPlot: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
