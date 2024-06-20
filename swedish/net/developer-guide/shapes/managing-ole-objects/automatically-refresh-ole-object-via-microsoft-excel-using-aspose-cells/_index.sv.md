---
title: Automatisk uppdatering av OLE objekt via Microsoft Excel med Aspose.Cells
type: docs
weight: 270
url: /sv/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload)-egenskapen för att uppdatera OLE-objektet när Excel-filen öppnas i Microsoft Excel. På grund av denna egenskap kommer OLE-objektet att visa korrekt OLE-bild som genererats av Microsoft Excel.

{{% /alert %}}

Följande provkod laddar [provexempel Excel-filen](5115231.xlsx) som har en icke verklig OLE-bild. OLE-objektet är faktiskt ett Microsoft Word-dokument men provexempelfilen visar djurbilden istället för Microsoft Word-bilden. Men om du öppnar [utmatningsexelfilen](5115225.xlsx) kommer du att se att Microsoft Excel visar den korrekta OLE-bilden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
