---
title: Skapa cirkeldiagram med ledarlinjer
description: Lär dig hur du använder Aspose.Cells for .NET för att skapa ett cirkeldiagram med ledarlinjer i Microsoft Excel. Vår guide kommer att visa hur man lägger till ledarlinjer som kopplar datapunkter till förklaringen och förbättrar den övergripande tydligheten i ditt diagram.
keywords: Aspose.Cells for .NET, Pie Chart, Leader Lines, Microsoft Excel, Data Visualization, Chart Customization.
linktitle: Tårtdiagram
type: docs
weight: 45
url: /sv/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

Den här artikeln förklarar hur du skapar ett cirkeldiagram med ledarlinjer från början medan du använder Aspose.Cells for .NET API. I Excel är alternativet "Visa ledarlinjer" inställt som standard så när du skapar ett cirkeldiagram i Excel visas ledarlinjerna. Men när du skapar ett liknande diagram med Aspose.Cells API:er måste du uttryckligen ställa in[**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) fast egendom.

{{% /alert %}}

 För att demonstrera användningen av Aspose.Cells for .NET API för att skapa ett cirkeldiagram med ledarlinjer, kommer vi först att skapa ett nytt[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) och mata in några data som kommer att fungera som seriedatakällan. När uppgifterna är på plats kommer vi att lägga till en[**Diagram**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) av typ[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)till samlingen av sjökort och ställ in dess olika aspekter för att få önskad sjökortsvy.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Hittills har vi skapat ett cirkeldiagram och angett dess olika aspekter. Nu ska vi slå på ledarlinjerna för diagrammet. Observera att för att visa ledarlinjerna måste vi flytta dataetiketterna lite.

Följande kodbit aktiverar ledarlinjerna, uppdaterar diagrammet och beräknar sedan dataetiketternas positioner för att flytta dem därefter.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Slutligen sparar följande kod diagrammet i bildformat och arbetsboken i XLSX-format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Resulterande cirkeldiagram**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

##  **Förhandsämnen**
- [Anpassade segment- eller sektorfärger i cirkeldiagram](/cells/sv/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Ta reda på om datapoäng finns i den andra cirkeln eller stapeln på ett cirkel- eller cirkeldiagram](/cells/sv/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

##  relaterade artiklar

- [Skapa diagram](/cells/sv/net/creating-charts/)
- [Anpassa diagram](/cells/sv/net/customizing-charts/)
- [Dataformatering i diagram](/cells/sv/net/data-formatting-in-charts/)
- [Ställa in diagrammets utseende](/cells/sv/net/setting-chart-appearance/)

