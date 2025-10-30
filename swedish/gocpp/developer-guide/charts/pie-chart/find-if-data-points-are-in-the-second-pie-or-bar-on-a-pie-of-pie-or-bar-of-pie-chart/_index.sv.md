---
title: Hitta om datapunkter är i den andra tårtan eller stapeln i ett Pie of Pie eller Bar of Pie diagram med Golang via C++
linktitle: Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj eller stapeldiagram
description: Lär dig hur du använder Aspose.Cells for C++ för att avgöra om datapunkter finns i den andra tårten eller stolpen på ett Pie of Pie eller Bar of Pie diagram. Vår guide visar hur man identifierar och får tillgång till sekundärtårten eller stolpen på ett sammansatt diagram, vilket möjliggör effektiv dataanalys och manipulerering.
keywords: Aspose.Cells for C++, Pie of Pie diagram, Bar of Pie diagram, Sekundär tår, Sekundär stolpe, Dataanalys, Datahantering.
type: docs
weight: 180
url: /sv/go-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Möjliga användningsscenario**
Du kan avgöra om seriedatapunkter finns i den andra tårtan på *Pie of Pie*-diagrammet eller i stapeln på *Bar of Pie*-diagrammet med Aspose.Cells. Använd egenskapen [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/go-cpp/chartpoint/isinsecondaryplot/) för att avgöra det.

Ladda ner den [exempelfil i Excel](5115193.xlsx) som används i följande exempelkod och se dess konsoloutput. Om du öppnar [exempelfilen i Excel](5115193.xlsx) hittar du att alla datapunkter som är mindre än 10 finns inuti stapeln på *Stapel av paj*-diagram som också visas i konsoloutputen.

## **Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj- eller stapeldiagram**
Följande exempelkod visar hur du tar reda på om datapunkterna finns i den andra pajen eller stapeln på ett *Paj av paj*- eller *Stapel av paj*-diagram.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfDataPointsAreInTheSecondPieOrBarOnAPieOfPieOrBarOfPieChart.go" >}}
## **Konsoloutput**
Se följande konsolutskrift som genererats efter körning av ovanstående exempel med [sample excel-fil](5115193.xlsx). Om [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) är **falskt**, är datapunkten inom tårtan, men om den är **sant**, är datapunkten inom stolpen.

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
