---
title: Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område
description: Lär dig hur man ändrar datakällan för ett diagram till ett måldokument samtidigt som du kopierar rader eller ett område i Aspose.Cells för Python via .NET. Vår guide visar hur man uppdaterar diagrammets dataintervall och länkar det till måldokumentet, så att de kopierade raderna eller området återspeglas korrekt i diagrammet.
keywords: Aspose.Cells för Python via .NET, diagrammering, datakälla, måldokument, rader, område, kopiering, uppdatering, dataintervall, länkning.
type: docs
weight: 440
url: /sv/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Möjliga användningsscenario**

När du kopierar rader eller område som innehåller diagram till ett nytt kalkylblad ändras inte diagrammets datakälla. Till exempel, om diagrammets datakälla är =Sheet1!$A$1:$B$4, kommer datakällan att förbli densamma efter att rader eller område har kopierats till ett nytt kalkylblad, det refererar fortfarande till det gamla kalkylbladet Sheet1. Detta är också beteendet i Microsoft Excel. Men om du vill att den ska hänvisa till det nya destinationskalkylbladet, använd egenskapen [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet) och ställ in den till **true** när du använder metoden [**Cells.copy_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows). Nu om ditt destinationskalkylblad är DestSheet, kommer datakällan för ditt diagram att ändras från =Sheet1!$A$1:$B$4 till =DestSheet!$A$1:$B$4.

## **Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område**

Följande kodexempel förklarar användningen av egenskapen [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet) när du kopierar rader eller område som innehåller diagram till ett nytt kalkylblad. Koden använder den [exempel på Excel-fil](5113699.xlsx) och genererar den [utdata-excel-filen](5113697.xlsx).

![todo:image_alt_text](1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartDataSource-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
