---
title: Anpassade segment- eller sektorfärger i cirkeldiagram
type: docs
weight: 60
url: /sv/net/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

Den här artikeln förklarar hur du lägger till anpassade färger till cirkeldiagramsegment/sektorer. Som standard använder cirkeldiagram standardmallen Microsoft Excel. Om du vill använda andra färger, definiera om färgerna i diagrammet.

{{% /alert %}}

Så här ställer du in en anpassad färg för ett cirkeldiagrams enskilda segment eller sektorer:

1.  Få tillgång till[**Serier**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) föremål[**ChartPoint**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint).
1.  Tilldela den färg du väljer med hjälp av[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)fast egendom.

Den här artikeln förklarar också hur du:

- Ett diagrams kategoridata.
- En diagramtitel kopplad till en cell.
- Teckensnittsinställningarna för diagramtiteln.
- Legendens position.

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor) är inte specifikt för cirkeldiagram men det kan användas för alla typer av diagram.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
