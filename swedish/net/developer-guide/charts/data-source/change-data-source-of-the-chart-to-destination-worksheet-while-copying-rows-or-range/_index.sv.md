---
title: Ändra datakälla för diagrammet till målarbetsblad medan du kopierar rader eller intervall
description: Lär dig hur du ändrar datakällan för ett diagram till ett målarbetsblad medan du kopierar rader eller ett intervall i Aspose.Cells for .NET. Vår guide visar dig hur du uppdaterar diagrammets dataintervall och länkar det till målarbetsbladet, och säkerställer att de kopierade raderna resp. intervallet återspeglas korrekt i diagrammet.
keywords: Aspose.Cells for .NET, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.
type: docs
weight: 440
url: /sv/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
##  **Möjliga användningsscenarier**

När du kopierar rader eller intervall som innehåller diagram till ett nytt kalkylblad, ändras inte datakällan för diagrammet. Till exempel, om datakällan för diagrammet är =Sheet1!$A$1:$B$4, efter kopiering av rader eller intervall till nytt kalkylblad, kommer datakällan att förbli densamma, dvs. =Sheet1!$A$1:$B$4. Det hänvisar fortfarande till det gamla kalkylbladet, dvs. Sheet1. Detta är också beteendet i Microsoft Excel. Men om du vill att det ska referera till det nya destinationsarbetsbladet, använd[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)egendom och ställ in den på**Sann** medan du ringer till[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)metod. Om ditt målark är DestSheet kommer datakällan för ditt diagram att ändras från =Sheet1!$A$1:$B$4 till =DestSheet!$A$1:$B$4.

##  **Ändra datakälla för diagrammet till målarbetsblad medan du kopierar rader eller intervall**

Följande exempelkod förklarar användningen av[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) egenskap medan du kopierar rader eller intervall som innehåller diagram till ett nytt kalkylblad. Koden använder[exempel på excel-fil](5113699.xlsx) och genererar[output excel-fil](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
