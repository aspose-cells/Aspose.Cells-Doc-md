---
title: Infoga och ta bort rader och kolumner i Excelfil
linktitle: Infoga och ta bort rader och kolumner
type: docs
weight: 70
url: /sv/net/inserting-and-deleting-rows-and-columns/
description: Den här artikeln visar hur du infogar och tar bort rader och kolumner med hjälp av Aspose.Cells for .NET API.
keywords: Aspose.Cells C# hantera rader och kolumner, infoga rader och kolumner, ta bort rader och kolumner
---

## **Introduktion**

Oavsett om du skapar en ny arbetsbok från grunden eller arbetar med en befintlig arbetsbok kan vi behöva lägga till extra rader eller kolumner för att rymma mer data. Å andra sidan kan det också hända att vi behöver ta bort rader eller kolumner från angivna positioner i arbetsboken.
För att uppfylla dessa krav tillhandahåller Aspose.Cells en mycket enklaste uppsättning klasser och metoder, som diskuteras nedan.

### **Hantera rader och kolumner**

Aspose.Cells tillhandahåller en klass [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) samling som tillåter åtkomst till varje arbetsblad i en Excel-fil. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling som representerar alla celler i arbetsbladet.

Samlingen [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) tillhandahåller flera metoder för att hantera rader och kolumner i ett arbetsblad. Några av dessa diskuteras nedan.

{{% alert color="primary" %}}

När rader eller kolumner läggs till skiftas innehållet i kalkylbladet neråt eller åt höger, och om rader eller kolumner tas bort skiftas innehållet uppåt eller åt vänster.

{{% /alert %}}


## **Infoga rader och kolumner**

### **Hur man infogar en rad**

Infoga en rad i arbetsbladet på valfri plats genom att anropa [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)-metoden i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samlingen. Metoden [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) tar indexet för raden där den nya raden ska infogas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **Hur man infogar flera rader**

För att infoga flera rader i ett arbetsblad, ring [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)-metoden i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samlingen. Metoden [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) tar två parametrar:

- Radindex, index för raden från vilken de nya raderna ska infogas.
- Antal rader, det totala antalet rader som ska infogas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **Hur man infogar en rad med formatering**

För att infoga en rad med formateringsalternativ, använd [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)-överbelastningen som tar [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) som parameter. Ange [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)-egenskapen i [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions)-klassen med [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)-uppräkningen. [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)-uppräkningen har tre medlemmar som listas nedan.

- SammaSomOvan: Formaterar raden på samma sätt som raden ovan.
- SammaSomNedan: Formaterar raden på samma sätt som raden nedan.
- Rensa: Rensar formateringen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **Hur man infogar en kolumn**

Utvecklare kan också infoga en kolumn i arbetsbladet på valfri plats genom att anropa [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)-metoden i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samlingen. Metoden [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) tar indexet för kolumnen där den nya kolumnen ska infogas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **Ta bort rader och kolumner**

### **Hur man tar bort flera rader**

För att ta bort flera rader från ett arbetsblad, ring [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)-metoden i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samlingen. Metoden [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) tar två parametrar:

- Radindex, index för raden från vilken raderna ska tas bort.
- Antal rader, det totala antalet rader som ska tas bort.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **Hur man tar bort en kolumn**

För att ta bort en kolumn från arbetsbladet på valfri plats, ring [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)-metoden i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samlingen. Metoden [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) tar indexet för kolumnen som ska tas bort.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
