---
title: Automatisk uppdatering av OLE objekt
type: docs
weight: 270
url: /sv/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET tillhandahåller egenskapen [**OleObject.auto_load**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/auto_load) för att uppdatera OLE-objektet när Excel-filen öppnas i Microsoft Excel. På grund av denna egenskap visas rätt OLE-bild som genereras av Microsoft Excel.

{{% /alert %}}

Följande provkod laddar [provexempel Excel-filen](5115231.xlsx) som har en icke verklig OLE-bild. OLE-objektet är faktiskt ett Microsoft Word-dokument men provexempelfilen visar djurbilden istället för Microsoft Word-bilden. Men om du öppnar [utmatningsexelfilen](5115225.xlsx) kommer du att se att Microsoft Excel visar den korrekta OLE-bilden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-RefreshOLEObjects-1.py" >}}
