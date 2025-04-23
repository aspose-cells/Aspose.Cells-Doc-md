---
title: Infoga, ta bort rader och kolumner
type: docs
weight: 40
url: /sv/go-cpp/inserting-deleting-rows-and-columns/
---

## **Introduktion**

Oavsett om en ny arbetsbok skapas från grunden eller om man arbetar i en befintlig arbetsbok kan det vara nödvändigt att lägga till extra rader eller kolumner för att rymma mer data. Tvärtom kan det också vara nödvändigt att ta bort rader eller kolumner från specificerade positioner i arbetsboken. För att uppfylla dessa krav tillhandahåller Aspose.Cells en mycket enkel uppsättning klasser och metoder, som diskuteras nedan.

### **Hantera rader och kolumner**

Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) klassen innehåller en [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) samling som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad är representerat av [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) klassen. [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) klassen ger en [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samling som representerar alla celler i arbetsbladet.

[Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingen ger flera metoder för att hantera rader och kolumner i ett arbetsblad. Några av dessa diskuteras nedan.

{{% alert color="primary" %}}

När rader eller kolumner läggs till skiftas innehållet i kalkylbladet neråt eller åt höger, och om rader eller kolumner tas bort skiftas innehållet uppåt eller åt vänster.

{{% /alert %}}

Infoga en rad i arbetsbladet på valfri plats genom att anropa [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) metoden i [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingen. [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) metoden tar indexet av raden där den nya raden ska infogas.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertRow.go" >}}

#### **Infoga flera rader**

För att infoga flera rader i ett arbetsblad, anropa [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrows_int_int/) metoden i [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingen. [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrowinsertrows_int_ints/) metoden tar två parametrar:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingMultipleRows.go" >}}

#### **Ta bort flera rader**

För att ta bort flera rader från ett arbetsblad, anropa [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) metoden i [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingen. [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) metoden tar två parametrar:

- Radindex, index för raden från vilken raderna ska tas bort.
- Antal rader, det totala antalet rader som ska tas bort.

#### **Infoga en kolumn**

Utvecklare kan även infoga en kolumn i arbetsbladet på valfri plats genom att anropa [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) metoden i [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingen. [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) metoden tar indexet för kolumnen där den nya kolumnen ska infogas.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertColumn.go" >}}

För att ta bort en kolumn från arbetsbladet på valfri plats, anropa [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) metoden i [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingen. [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) metoden tar indexet för kolumnen som ska tas bort.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteColumn.go" >}}
