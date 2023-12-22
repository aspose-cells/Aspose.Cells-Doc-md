---
title: Infoga, ta bort rader och kolumner
type: docs
weight: 40
url: /sv/cpp/inserting-deleting-rows-and-columns/
---
##  **Introduktion**
Oavsett om vi skapar ett nytt kalkylblad från början eller arbetar med ett befintligt kalkylblad, kan vi behöva lägga till extra rader eller kolumner för att ta emot mer data. Omvänt kan vi också behöva ta bort rader eller kolumner från angivna positioner i kalkylbladet. För att uppfylla dessa krav tillhandahåller Aspose.Cells en mycket enklaste uppsättning klasser och metoder, som diskuteras nedan.
###  **Hantera rader och kolumner**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) , som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. De[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass ger en[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)samling som representerar alla celler i kalkylbladet.

 De[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)samling innehåller flera metoder för att hantera rader och kolumner i ett kalkylblad. Några av dessa diskuteras nedan.

{{% alert color="primary" %}} 

När rader eller kolumner läggs till flyttas innehållet i kalkylbladet nedåt eller åt höger, och om rader eller kolumner tas bort flyttas innehållet uppåt eller åt vänster.

{{% /alert %}} 
####  **Infoga en rad**
 Infoga en rad i kalkylbladet på valfri plats genom att anropa[Infoga rad](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) metod för[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling. De[Infoga rad](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)metoden tar indexet för raden där den nya raden kommer att infogas.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


####  **Infoga flera rader**
 För att infoga flera rader i ett kalkylblad, anropa[Infoga rader](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) metod för[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling. De[Infoga rader](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)Metoden tar två parametrar:

- Radindex, indexet för raden varifrån de nya raderna kommer att infogas.
- Antal rader, det totala antalet rader som behöver infogas.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


####  **Ta bort flera rader**
 För att ta bort flera rader från ett kalkylblad, anropa[Ta bort rader](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) metod för[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling. De[Ta bort rader](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)Metoden tar två parametrar:

- Radindex, indexet för raden där raderna kommer att tas bort.
- Antal rader, det totala antalet rader som behöver raderas.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


####  **Infoga en kolumn**
 Utvecklare kan också infoga en kolumn i kalkylbladet var som helst genom att anropa[Infoga kolumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) metod för[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling.[Infoga kolumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)metoden tar indexet för den kolumn där den nya kolumnen kommer att infogas.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


####  **Ta bort en kolumn**
 För att ta bort en kolumn från kalkylbladet på valfri plats, ring till[Ta bort kolumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) metod för[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling. De[Ta bort kolumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)metoden tar indexet för kolumnen att radera.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
