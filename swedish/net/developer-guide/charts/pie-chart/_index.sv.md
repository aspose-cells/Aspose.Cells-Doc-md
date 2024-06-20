---
title: Skapa cirkeldiagram med ledarlinjer
description: Lär dig hur du använder Aspose.Cells for .NET för att skapa ett cirkeldiagram med ledarlänkar i Microsoft Excel. Vår guide kommer att visa hur du lägger till ledarlänkar som ansluter data punkter till legenden och förbättrar överblickligheten för ditt diagram.
keywords: Aspose.Cells for .NET, Cirkeldiagram, Ledarlänkar, Microsoft Excel, Visualisering av data, Anpassning av diagram.
linktitle: Cirkeldiagram
type: docs
weight: 45
url: /sv/net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Den här artikeln förklarar hur du skapar ett cirkeldiagram med ledarlänkar från grunden med hjälp av Aspose.Cells for .NET API. I Excel är 'Visa ledarlänkar' alternativet inställt som standard så när du skapar ett cirkeldiagram i Excel visas ledarlänkarna. Men när du skapar ett liknande diagram med Aspose.Cells API:er måste du explicit ange [**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) egenskapen.

{{% /alert %}}

För att demonstrera användningen av Aspose.Cells for .NET API för att skapa ett cirkeldiagram med ledarlänkar kommer vi först att skapa en ny [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) och mata in viss data som kommer att fungera som datakälla för serier. När data är på plats kommer vi att lägga till en [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) av typ [**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) till samlingen av diagram och ställa in dess olika aspekter för att få önskad diagramvy.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Hittills har vi skapat ett cirkeldiagram och ställt in dess olika aspekter. Nu kommer vi att slå på ledarlänkarna för diagrammet. Observera, för att visa ledarlänkar måste vi flytta dataetiketterna lite.

Följande kodsnutt slår på ledarlänkarna, uppdaterar diagrammet och beräknar sedan dataetiketternas positioner för att flytta dem på lämpligt sätt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Slutligen sparar följande kod diagrammet i bildformat och arbetsboken i XLSX-format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Resulterande Cirkeldiagram**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Fortsatta ämnen**
- [Anpassade färgval för skiv- eller sektorfärger i cirkeldiagram](/cells/sv/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj- eller stapeldiagram](/cells/sv/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Relaterade artiklar

- [Skapa diagram](/cells/sv/net/creating-charts/)
- [Anpassning av diagram](/cells/sv/net/customizing-charts/)
- [Dataformatering i diagram](/cells/sv/net/data-formatting-in-charts/)
- [Ställa in diagramens utseende](/cells/sv/net/setting-chart-appearance/)

