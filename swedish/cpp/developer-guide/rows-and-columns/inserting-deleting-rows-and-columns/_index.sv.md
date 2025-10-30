---
title: Infoga, ta bort rader och kolumner
type: docs
weight: 40
url: /sv/cpp/inserting-deleting-rows-and-columns/
---

## **Introduktion**
Oavsett om en ny arbetsbok skapas från grunden eller om man arbetar i en befintlig arbetsbok kan det vara nödvändigt att lägga till extra rader eller kolumner för att rymma mer data. Tvärtom kan det också vara nödvändigt att ta bort rader eller kolumner från specificerade positioner i arbetsboken. För att uppfylla dessa krav tillhandahåller Aspose.Cells en mycket enkel uppsättning klasser och metoder, som diskuteras nedan.
### **Hantera rader och kolumner**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en samling [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller en samling [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) som representerar alla celler på kalkylarket.

Samlingen [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) tillhandahåller flera metoder för att hantera rader och kolumner i ett kalkylblad. Några av dessa diskuteras nedan.

{{% alert color="primary" %}} 

När rader eller kolumner läggs till skiftas innehållet i kalkylbladet neråt eller åt höger, och om rader eller kolumner tas bort skiftas innehållet uppåt eller åt vänster.

{{% /alert %}} 
#### **Infoga en rad**
Infoga en rad i kalkylarket på valfri plats genom att anropa metoden [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) i samlingen [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Metoden [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) tar indexet för raden där den nya raden ska infogas.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


#### **Infoga flera rader**
För att infoga flera rader i ett kalkylblad, anropa metoden [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) i samlingen [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Metoden [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) tar två parametrar:

- Radindex, index för raden från vilken de nya raderna ska infogas.
- Antal rader, det totala antalet rader som ska infogas.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


#### **Ta bort flera rader**
För att ta bort flera rader från ett kalkylblad, anropa metoden [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) i samlingen [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Metoden [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) tar två parametrar:

- Radindex, index för raden från vilken raderna ska tas bort.
- Antal rader, det totala antalet rader som ska tas bort.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


#### **Infoga en kolumn**
Utvecklare kan också infoga en kolumn i kalkylarket på valfri plats genom att anropa metoden [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) i samlingen [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Metoden [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) tar indexet för kolumnen där den nya kolumnen ska infogas.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


#### **Ta bort en kolumn**
För att ta bort en kolumn från kalkylarket på valfri plats, anropa metoden [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) i samlingen [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Metoden [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) tar indexet för kolumnen som ska tas bort.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
