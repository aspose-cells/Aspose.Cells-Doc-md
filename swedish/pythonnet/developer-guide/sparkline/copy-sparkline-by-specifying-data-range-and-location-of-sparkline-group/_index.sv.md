---
title: Kopiera sparkline genom att ange dataområde och plats för sparklinegrupp
type: docs
weight: 300
url: /sv/python-net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel tillåter att du kopierar en sparkline genom att specificera dataintervall och plats för en sparkline-grupp. Aspose.Cells för Python via .NET stödjer denna funktion.

{{% /alert %}}

För att kopiera en sparkline till andra celler i Microsoft Excel:

1. Välj cellen som innehåller sparklinen.
2. Välj **Redigera data** från **Sparkline**-avsnittet på fliken **Design**.
3. Välj **Redigera gruppplats och data**.
4. Ange dataområdet och platsen.
1. Klicka på **OK**.

Aspose.Cells för Python via .NET tillhandahåller metoden SparklineCollection.Add(dataRange, rad, kolumn) för att ange dataintervall och plats för en sparkline-grupp. Följande kod exempelt laddar ursprungs-Excel-filen som visas i skärmbilden ovan, hämtar den första sparkline-gruppen och lägger till dataintervall och platser i denna grupp. Slutligen skriver det ut den genererade Excel-filen till disken, vilket också visas i skärmbilden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-CopySparkline-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
