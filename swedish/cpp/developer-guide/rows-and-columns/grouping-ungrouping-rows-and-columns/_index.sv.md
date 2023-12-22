---
title: Gruppera, dela upp rader och kolumner
type: docs
weight: 30
url: /sv/cpp/grouping-ungrouping-rows-and-columns/
---
##  **Introduktion**
en Microsoft Excel-fil kan du skapa en disposition för data så att du kan visa och dölja detaljnivåer med ett enda musklick.

Klicka på *Kontursymboler**, 1,2,3, + och - för att snabbt bara visa de rader eller kolumner som ger sammanfattningar eller rubriker för avsnitt i ett kalkylblad, eller så kan du använda symbolerna för att se detaljer under en enskild sammanfattning eller rubrik.
##  **Grupphantering av rader och kolumner**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. De[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass ger en[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)samling som representerar alla celler i kalkylbladet.

 De[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)samling innehåller flera metoder för att hantera rader eller kolumner i ett kalkylblad, några av dessa diskuteras mer i detalj nedan.
###  **Gruppera rader och kolumner**
 Det är möjligt att gruppera rader eller kolumner genom att anropa[Grupprader](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) och[Gruppkolumner](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) metoder för[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)samling. Båda metoderna tar följande parametrar:

- Den första raden/kolumnindex, den första raden eller kolumnen i gruppen.
- Den sista raden/kolumnindex, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som anger om rader/kolumner ska döljas efter gruppering eller inte.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
####  **Gruppinställningar**
Microsoft Excel låter dig konfigurera gruppinställningar för att visa:

- Sammanfattningsrader nedan detalj.
- Sammanfattningskolumner till höger om detaljer.
##  **Dela upp rader och kolumner**
 För att avgruppera grupperade rader eller kolumner, anropa[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingens[Dela upp rader](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) och[Dela upp kolumner](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/)metoder. Båda metoderna tar två parametrar:

- Den första raden eller kolumnindexet, den första raden/kolumnen som ska delas upp.
- Den sista raden eller kolumnindexet, den sista raden/kolumnen som ska delas upp.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
