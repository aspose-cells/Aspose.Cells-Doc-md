---
title: Kopiera sparkline genom att ange dataområde och plats för sparklinegrupp
type: docs
weight: 300
url: /sv/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel tillåter dig att kopiera en sparkline genom att ange dataområde och plats för en sparklinegrupp. Aspose.Cells stöder denna funktion.

{{% /alert %}}

För att kopiera en sparkline till andra celler i Microsoft Excel:

1. Välj cellen som innehåller sparklinen.
2. Välj **Redigera data** från **Sparkline**-avsnittet på fliken **Design**.
3. Välj **Redigera gruppplats och data**.
4. Ange dataområdet och platsen.
1. Klicka på **OK**.

Aspose.Cells tillhandahåller metoden SparklineCollection.Add(dataRange, row, column) för att ange ett sparkline grupps dataområde och plats. Det följande exempelkoden laddar den ursprungliga Excel-filen som visas ovan, sedan får åtkomst till den första sparklinegruppen och lägger till dataområden och platser i sparklinegruppen. Slutligen skriver den utdatafilen till disk som också visas i skärmdumpen ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
