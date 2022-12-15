---
title: Gruppering, dela upp rader och kolumner
type: docs
weight: 30
url: /sv/cpp/grouping-ungrouping-rows-and-columns/
---
## **Introduktion**
en Microsoft Excel-fil kan du skapa en disposition för data så att du kan visa och dölja detaljnivåer med ett enda musklick.

 Klicka på**Kontursymboler**, 1,2,3, + och - för att snabbt visa bara de rader eller kolumner som ger sammanfattningar eller rubriker för avsnitt i ett kalkylblad, eller så kan du använda symbolerna för att se detaljer under en enskild sammanfattning eller rubrik.
## **Grupphantering av rader och kolumner**
 Aspose.Cells tillhandahåller en klass,[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) som representerar en Microsoft Excel-fil. De[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) klass innehåller en[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass. De[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass ger en[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)samling som representerar alla celler i kalkylbladet.

 De[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)samling innehåller flera metoder för att hantera rader eller kolumner i ett kalkylblad, några av dessa diskuteras mer i detalj nedan.
### **Gruppera rader och kolumner**
 Det är möjligt att gruppera rader eller kolumner genom att anropa[Grupprader](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a88e0180ed1a4a423e0bd3ac599ef9332) och[Gruppkolumner](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aaa14179e2a84ba5c2857f8434570d3d8) metoder för[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)samling. Båda metoderna tar följande parametrar:

- Den första raden/kolumnindex, den första raden eller kolumnen i gruppen.
- Den sista raden/kolumnindex, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som anger om rader/kolumner ska döljas efter gruppering eller inte.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns.cpp" >}}
#### **Gruppinställningar**
Microsoft Excel låter dig konfigurera gruppinställningar för att visa:

- Sammanfattningsrader nedan detalj.
- Sammanfattningskolumner till höger om detaljer.
## **Dela upp rader och kolumner**
 För att avgruppera grupperade rader eller kolumner, anropa[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) samlingens[Dela upp rader](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#adc1f6418506854ab41707bfef453ddb1) och[Dela upp kolumner](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aa3bf9a9510d4e85f68db9ebdcadc8406)metoder. Båda metoderna tar två parametrar:

- Den första raden eller kolumnindexet, den första raden/kolumnen som ska delas upp.
- Den sista raden eller kolumnindexet, den sista raden/kolumnen som ska delas upp.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns.cpp" >}}
