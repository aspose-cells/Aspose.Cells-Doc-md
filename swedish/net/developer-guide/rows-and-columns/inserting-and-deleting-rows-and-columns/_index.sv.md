---
title: Infoga och ta bort rader och kolumner i Excel-fil
linktitle: Infoga och ta bort rader och kolumner
type: docs
weight: 70
url: /sv/net/inserting-and-deleting-rows-and-columns/
description: Den här artikeln visar hur du infogar och tar bort rader och kolumner med Aspose.Cells for .NET API.
keywords: Aspose.Cells C# manage rows and columns, insert rows and columns, delete rows and columns
---
##  **Introduktion**

Oavsett om vi skapar ett nytt kalkylblad från början eller arbetar med ett befintligt kalkylblad, kan vi behöva lägga till extra rader eller kolumner för att ta emot mer data. Omvänt kan vi också behöva ta bort rader eller kolumner från angivna positioner i kalkylbladet.
För att uppfylla dessa krav tillhandahåller Aspose.Cells en mycket enklaste uppsättning klasser och metoder, som diskuteras nedan.

###  **Hantera rader och kolumner**

Aspose.Cells tillhandahåller en klass[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)samling som representerar alla celler i kalkylbladet.

 De[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)samling innehåller flera metoder för att hantera rader och kolumner i ett kalkylblad. Några av dessa diskuteras nedan.

{{% alert color="primary" %}}

När rader eller kolumner läggs till flyttas innehållet i kalkylbladet nedåt eller åt höger, och om rader eller kolumner tas bort flyttas innehållet uppåt eller åt vänster.

{{% /alert %}}


##  **Infoga rader och kolumner**

###  **Hur man infogar en rad**

 Infoga en rad i kalkylbladet på valfri plats genom att anropa[**Infoga rad**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling. De[**Infoga rad**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)metoden tar indexet för raden där den nya raden kommer att infogas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

###  **Hur man infogar flera rader**

 För att infoga flera rader i ett kalkylblad, anropa[**Infoga rader**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling. De[**Infoga rader**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)Metoden tar två parametrar:

- Radindex, indexet för raden varifrån de nya raderna kommer att infogas.
- Antal rader, det totala antalet rader som behöver infogas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

###  **Hur man infogar en rad med formatering**

För att infoga en rad med formateringsalternativ, använd[**Infoga rader**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)överbelastning som tar[**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) som en parameter. Ställ in[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) egendom av[**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) klass med[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Uppräkning. De[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)Enumeration har tre medlemmar enligt nedan.

- SameAsAbove: Formaterar raden på samma sätt som raden ovan.
- SameAsBelow: Formaterar raden på samma sätt som under raden.
- Rensa: Rensar formateringen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

###  **Hur man infogar en kolumn**

 Utvecklare kan också infoga en kolumn i kalkylbladet var som helst genom att anropa[**Infoga kolumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)samling. De[**Infoga kolumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)metoden tar indexet för den kolumn där den nya kolumnen kommer att infogas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

##  **Ta bort rader och kolumner**

###  **Hur man tar bort flera rader**

 För att ta bort flera rader från ett kalkylblad, anropa[**Ta bort rader**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling. De[**Ta bort rader**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)Metoden tar två parametrar:

- Radindex, indexet för raden där raderna kommer att tas bort.
- Antal rader, det totala antalet rader som behöver raderas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


###  **Hur man tar bort en kolumn**

 För att ta bort en kolumn från kalkylbladet på valfri plats, ring till[**Ta bort kolumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling. De[**Ta bort kolumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)metoden tar indexet för kolumnen att radera.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
