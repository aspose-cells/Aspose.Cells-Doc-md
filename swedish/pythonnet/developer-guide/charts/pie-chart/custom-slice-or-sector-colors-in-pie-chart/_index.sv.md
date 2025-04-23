---
title: Anpassa skiv eller sektorfärger i cirkeldiagram
description: Lär dig hur du använder Aspose.Cells för Python via .NET för att anpassa skiv och sektorfärger i ett pajdiagram. Vår guide visar hur man tilldelar unika färger till varje skiva, sektor eller legion för förbättrad visuellt tilltalande och datarapportering.
keywords: Aspose.Cells för Python via .NET, Pajdiagram, Anpassade skivfärger, Anpassade sektorfärger, Visuell tilltalande, Datarapportering.
type: docs
weight: 60
url: /sv/python-net/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

Den här artikeln förklarar hur man lägger till anpassade färger i cirkeldiagramskivor/sektorer. Som standard använder cirkeldiagram Microsoft Excels standardmall. För att använda andra färger måste du omdefiniera färgerna i diagrammet.

{{% /alert %}}

För att ställa in en anpassad färg för en cirkeldiagrams individuella skivor eller sektorer:

1. Öppna [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series)s [**ChartPoint**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint).
1. Tilldela önskad färg med hjälp av [**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color)s egenskap.

Den här artikeln förklarar också hur man:

- En diagrams kategoridata.
- En diagramtitel länkad till en cell.
- Typsnittsinställningar för diagramtiteln.
- Placeringen av legenden.

{{% alert color="primary" %}}

[**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color) är inte specifikt för cirkeldiagram men kan användas för alla typer av diagram.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CustomSliceSectorColorsPieChart-1.py" >}}
