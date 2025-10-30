---
title: Skapa cirkeldiagram med ledarlinjer
description: Lär dig hur du använder Aspose.Cells för Python via .NET för att skapa ett tårtdiagram med ledande linjer i Microsoft Excel. Vår guide visar hur man lägger till ledande linjer som kopplar datapunkter till legenden och förbättrar diagrammets tydlighet.
keywords: Aspose.Cells för Python via .NET, Tårtdiagram, Ledande linjer, Microsoft Excel, Data Visualisering, Diagramanpassning.
linktitle: Cirkeldiagram
type: docs
weight: 45
url: /sv/python-net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Denna artikel förklarar hur man skapar ett tårtdiagram med ledande linjer från början med Aspose.Cells för Python via .NET API. I Excel är alternativet 'Visa ledande linjer' inställt som standard, så när du skapar ett tårtdiagram i Excel visas ledande linjer. Men när du skapar liknande diagram med Aspose.Cells för Python via .NET API:er måste du uttryckligen ställa in [**Series.has_leader_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/has_leader_lines) egenskapen.

{{% /alert %}}

För att demonstrera användningen av Aspose.Cells för Python via .NET API för att skapa ett tårtdiagram med ledande linjer, kommer vi först att skapa en ny [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) och mata in data som kommer att fungera som serie datakälla. När datan är på plats, lägger vi till en [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) av typ [**ChartType.PIE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/) i diagramkollektionen och ställer in dess olika aspekter för att få önskat diagramutsik.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateWorkbook.py" >}}

Hittills har vi skapat ett cirkeldiagram och ställt in dess olika aspekter. Nu kommer vi att slå på ledarlänkarna för diagrammet. Observera, för att visa ledarlänkar måste vi flytta dataetiketterna lite.

Följande kodsnutt slår på ledarlänkarna, uppdaterar diagrammet och beräknar sedan dataetiketternas positioner för att flytta dem på lämpligt sätt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TurnOnLeaderLines.py" >}}

Slutligen sparar följande kod diagrammet i bildformat och arbetsboken i XLSX-format.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SaveChartInImageAndWorkbookInXLSX.py" >}}

|**Resulterande Cirkeldiagram**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Fortsatta ämnen**
- [Anpassade färgval för skiv- eller sektorfärger i cirkeldiagram](/cells/sv/python-net/custom-slice-or-sector-colors-in-pie-chart/)
- [Ta reda på om datapunkterna finns i den andra pajen eller stapeln på ett paj- eller stapeldiagram](/cells/sv/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Relaterade artiklar

- [Skapa diagram](/cells/sv/python-net/creating-charts/)
- [Anpassning av diagram](/cells/sv/python-net/customizing-charts/)
- [Dataformatering i diagram](/cells/sv/python-net/data-formatting-in-charts/)
- [Ställa in diagramens utseende](/cells/sv/python-net/setting-chart-appearance/)

{{< app/cells/assistant language="python-net" >}}
