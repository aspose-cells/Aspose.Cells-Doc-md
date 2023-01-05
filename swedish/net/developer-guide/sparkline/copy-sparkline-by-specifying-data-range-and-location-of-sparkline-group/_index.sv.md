---
title: Kopiera Sparkline genom att ange dataintervall och plats för Sparkline Group
type: docs
weight: 300
url: /sv/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
{{% alert color="primary" %}}

Microsoft Excel låter dig kopiera en sparkline genom att ange dataintervallet och platsen för en sparkline-grupp. Aspose.Cells stöder den här funktionen.

{{% /alert %}}

Så här kopierar du en sparkline till andra celler i Microsoft Excel:

1. Välj cellen som innehåller gnistan.
1.  Välj**Redigera data** från**Sparkline** avsnitt av**Design** flik.
1.  Välj**Redigera gruppplats och data**.
1. Ange dataintervall och plats.
1.  Klick**OK**.

Aspose.Cells tillhandahåller metoden SparklineCollection.Add(dataRange, row, column) för att ange en sparkline-grupps dataområde och plats. Följande exempelkod laddar källfilen för Excel som visas i skärmdumpen ovan, kommer sedan åt den första sparklinegruppen och lägger till dataområden och platser i sparklinegruppen. Slutligen skriver den utdata Excel-filen på disken som också visas i skärmdumpen ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
