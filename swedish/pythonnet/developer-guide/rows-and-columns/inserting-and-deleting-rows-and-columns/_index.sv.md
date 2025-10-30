---
title: Infoga och ta bort rader och kolumner i Excelfil
linktitle: Infoga och ta bort rader och kolumner
type: docs
weight: 70
url: /sv/python-net/inserting-and-deleting-rows-and-columns/
description: Den här artikeln visar hur man infogar och tar bort rader och kolumner med Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Aspose.Cells Python hanterar rader och kolumner, Python infoga rader och kolumner, Python ta bort rader och kolumner, Python Ta bort rader och kolumner.
---

## **Introduktion**

Oavsett om du skapar en ny arbetsbok från grunden eller arbetar med en befintlig arbetsbok kan vi behöva lägga till extra rader eller kolumner för att rymma mer data. Å andra sidan kan det också hända att vi behöver ta bort rader eller kolumner från angivna positioner i arbetsboken.
För att uppfylla dessa krav tillhandahåller Aspose.Cells for Python via .NET en mycket enkel uppsättning av klasser och metoder, som diskuteras nedan.

### **Hantera rader och kolumner**

Aspose.Cells for Python via .NET tillhandahåller en klass [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) samling som möjliggör åtkomst till varje arbetsblad i en Excel-fil. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) samling som representerar alla celler i arbetsbladet.

Samlingen [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) tillhandahåller flera metoder för att hantera rader och kolumner i ett arbetsblad. Några av dessa diskuteras nedan.

{{% alert color="primary" %}}

När rader eller kolumner läggs till skiftas innehållet i kalkylbladet neråt eller åt höger, och om rader eller kolumner tas bort skiftas innehållet uppåt eller åt vänster.

{{% /alert %}}


## **Infoga rader och kolumner**

### **Hur man infogar en rad**

Infoga en rad i arbetsbladet på valfri plats genom att anropa [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/)-metoden i [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-samlingen. Metoden [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) tar indexet för raden där den nya raden ska infogas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARow-1.py" >}}

### **Hur man infogar flera rader**

För att infoga flera rader i ett arbetsblad, ring [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int)-metoden i [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-samlingen. Metoden [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) tar två parametrar:

- Radindex, index för raden från vilken de nya raderna ska infogas.
- Antal rader, det totala antalet rader som ska infogas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.py" >}}

### **Hur man infogar en rad med formatering**

För att infoga en rad med formateringsalternativ, använd [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int-aspose.cells.InsertOptions)-överbelastningen som tar [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) som parameter. Ange [**copy_format_type**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions/copy_format_type/)-egenskapen i [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions)-klassen med [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/)-uppräkningen. [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/)-uppräkningen har tre medlemmar som listas nedan.

- SAMMA_SOM_OVAN: Formaterar raden på samma sätt som ovanstående rad.
- SAMMA_SOM_NEDAN: Formaterar raden på samma sätt som nedanstående rad.
- RENSA: Rensar formateringen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.py" >}}

### **Hur man infogar en kolumn**

Utvecklare kan också infoga en kolumn i arbetsbladet på valfri plats genom att anropa [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int)-metoden i [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-samlingen. Metoden [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) tar indexet för kolumnen där den nya kolumnen ska infogas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingAColumn-1.py" >}}

## **Ta bort rader och kolumner**

### **Hur man tar bort flera rader**

För att ta bort flera rader från ett arbetsblad, ring [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int)-metoden i [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-samlingen. Metoden [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) tar två parametrar:

- Radindex, index för raden från vilken raderna ska tas bort.
- Antal rader, det totala antalet rader som ska tas bort.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.py" >}}


### **Hur man tar bort en kolumn**

För att ta bort en kolumn från arbetsbladet på valfri plats, ring [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int)-metoden i [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-samlingen. Metoden [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) tar indexet för kolumnen som ska tas bort.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingAColumn-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
