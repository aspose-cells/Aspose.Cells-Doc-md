---
title: Kopiera Sparkline genom att specificera dataintervall och plats för Sparkline gruppen med Golang via C++
linktitle: Kopiera Sparkline genom att specificera dataområde och plats
type: docs
weight: 300
url: /sv/go-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Lär dig hur du kopierar sparklines genom att specificera dataområde och plats med Aspose.Cells for C++.
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

Aspose.Cells tillhandahåller metoden `SparklineCollection.Add(dataRange, row, column)` för att specificera ett sparklines dataområde och plats. Följande exempel kod laddar källfilen i Excel som visas i skärmbilden ovan, nås den första sparklinesgruppen och lägger till dataområden och platser i sparklinesgruppen. Slutligen skriver den utdatafilen till disk som också visas i skärmbilden ovan.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopySparklineBySpecifyingDataRangeAndLocationOfSparklineGroup.go" >}}
