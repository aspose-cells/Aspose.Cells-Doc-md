---
title: Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område
description: Lär dig hur du ändrar datakällan för ett diagram till ett destinationskalkylblad samtidigt som du kopierar rader eller ett område i Aspose.Cells for .NET. Vår guide visar hur du uppdaterar diagrammets dataområde och länkar det till destinationskalkylbladet, vilket säkerställer att de kopierade raderna eller området återspeglas korrekt i diagrammet.
keywords: Aspose.Cells for .NET, diagram, datakälla, destinationskalkylblad, rader, område, kopiera, uppdatering, dataområde, länkning.
type: docs
weight: 440
url: /sv/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Möjliga användningsscenario**

När du kopierar rader eller område som innehåller diagram till ett nytt kalkylblad ändras inte diagrammets datakälla. Till exempel, om diagrammets datakälla är =Sheet1!$A$1:$B$4, kommer datakällan att förbli densamma efter att rader eller område har kopierats till ett nytt kalkylblad, det refererar fortfarande till det gamla kalkylbladet Sheet1. Detta är också beteendet i Microsoft Excel. Men om du vill att den ska hänvisa till det nya destinationskalkylbladet, använd egenskapen [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) och ställ in den till **true** när du använder metoden [**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index). Nu om ditt destinationskalkylblad är DestSheet, kommer datakällan för ditt diagram att ändras från =Sheet1!$A$1:$B$4 till =DestSheet!$A$1:$B$4.

## **Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område**

Följande kodexempel förklarar användningen av egenskapen [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) när du kopierar rader eller område som innehåller diagram till ett nytt kalkylblad. Koden använder den [exempel på Excel-fil](5113699.xlsx) och genererar den [utdata-excel-filen](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
