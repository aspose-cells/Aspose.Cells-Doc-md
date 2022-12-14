---
title: Ta reda på om datapoäng finns i den andra cirkeln eller stapeln på ett cirkel- eller cirkeldiagram
type: docs
weight: 910
url: /sv/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
## **Möjliga användningsscenarier**
 Du kan se om datapunkter för serier finns i den andra cirkeln på*Pie of Pie* diagram eller i stapeln av*Bar of Pie* diagram med Aspose.Cells. Vänligen använd[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot)egendom för att bestämma det.

 Vänligen ladda ner[exempel på excel-fil](5473373.xlsx) används i följande exempelkod och se dess konsolutgång. Om du öppnar[exempel på excel-fil](5473373.xlsx), hittar du, alla datapunkter som är mindre än 10 är inuti fältet för*Bar of Pie*diagram som också visas av konsolutgång.
## **Ta reda på om datapoäng finns i den andra cirkeln eller stapeln på ett cirkel- eller cirkeldiagram**
 Följande exempelkod visar hur du hittar om datapunkter finns i den andra cirkeln eller stapeln på en*Pie of Pie* eller*Bar of Pie*Diagram.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **Konsolutgång**
 Se följande konsolutgång som genereras efter exekveringen av ovanstående exempelkod med[exempel på excel-fil](5473373.xlsx) . Om[IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) är**falsk** , är datapunkten inne i cirkeln eller om den är det**Sann**då finns datapunkten inuti fältet.

{{< highlight "java" >}}

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
