---
title: Automatisk uppdatering av OLE objekt via Microsoft Excel med Golang via C++
linktitle: Automatisk uppdatering av OLE objekt
type: docs
weight: 270
url: /sv/go-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Lär dig att automatiskt uppdatera OLE objekt i Microsoft Excel med Aspose.Cells och Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller egenskapen [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/go-cpp/oleobject/getautoload/) för att fräscha upp OLE-objektet när Excel-filen öppnas i Microsoft Excel. På grund av denna egenskap visas rätt OLE-bild genererad av Microsoft Excel.

{{% /alert %}}

Följande exempelprogram laddar den [exempel Excel-fil](5115231.xlsx) som har en icke-virtuell OLE-bild. OLE-objektet är egentligen ett Microsoft Word-dokument, men exempel-Excel-filen visar djurbilden istället för Microsoft Word-bilden. Men om du öppnar [utgångs-Excel-filen](5115225.xlsx), kommer du att se att Microsoft Excel visar rätt OLE-bild.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutomaticallyRefreshOleObjectViaMicrosoftExcelUsingAsposeCells.go" >}}
