---
title: Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj eller stapeldiagram
description: Lär dig hur du använder Aspose.Cells för Python via .NET för att ta reda på om datapunkter finns i den andra pajen eller stolpen på ett Paj av Paj eller Bar av Paj diagram. Vår guide visar hur man identifierar och får tillgång till den sekundära pajen eller stolpen på ett sammansatt diagram, vilket gör att du kan analysera och manipulera datan effektivt.
keywords: Aspose.Cells för Python via .NET, Paj av Paj diagram, Bar av Paj diagram, Sekundär Paj, Sekundär Stolpe, Dataanalys, Datahantering.
type: docs
weight: 180
url: /sv/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Möjliga användningsscenario**
Du kan ta reda på om datapunkter i serien finns i den andra pajen på *Paj av Paj*-diagrammet eller i stolpen på *Bar av Paj*-diagrammet med Aspose.Cells för Python via .NET. Vänligen använd egenskapen [ChartPoint.is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot) för att avgöra detta.

Ladda ner den [exempelfil i Excel](5115193.xlsx) som används i följande exempelkod och se dess konsoloutput. Om du öppnar [exempelfilen i Excel](5115193.xlsx) hittar du att alla datapunkter som är mindre än 10 finns inuti stapeln på *Stapel av paj*-diagram som också visas i konsoloutputen.

## **Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj- eller stapeldiagram**
Följande exempelkod visar hur du tar reda på om datapunkterna finns i den andra pajen eller stapeln på ett *Paj av paj*- eller *Stapel av paj*-diagram.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindDataPointsInPieBar.py" >}}
## **Konsoloutput**
Se följande konsolutdata som genererats efter körning av ovanstående kod med [exempel Excel-fil](5115193.xlsx). Om [is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot/) är **falskt**, är datapunkten inuti Paj, och om den är **sann**, är datapunkten inuti Stolpen.



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
