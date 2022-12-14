---
title: Uppdatera OLE-objekt automatiskt via Microsoft Excel med Aspose.Cells
type: docs
weight: 270
url: /sv/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---
{{% alert color="primary" %}}

 Aspose.Cells tillhandahåller[**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) egenskap för att uppdatera OLE-objektet när excel-filen öppnas i Microsoft Excel. På grund av den här egenskapen kommer OLE-objektet att visa den korrekta OLE-bilden genererad av Microsoft Excel.

{{% /alert %}}

 Följande exempelkod laddar[exempel på excel-fil](5115231.xlsx) som har en icke-äkta OLE-bild. OLE-objektet är egentligen ett Microsoft Word-dokument men exemplet i Excel-filen visar djurbilden istället för Microsoft Word-bilden. Men om du öppnar[output excel-fil](5115225.xlsx), kommer du att se att Microsoft Excel visar rätt OLE-bild.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
