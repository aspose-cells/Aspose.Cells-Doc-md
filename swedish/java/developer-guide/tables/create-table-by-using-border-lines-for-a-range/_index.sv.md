---
title: Skapa tabell genom att använda kantlinjer för ett område
type: docs
weight: 50
url: /sv/java/create-table-by-using-border-lines-for-a-range/
description: Hur man skapar en tabell med intervall genom att använda kantlinjer. Aspose.Cells för Java tillhandahåller ett lättanvänt API som kan användas för att lägga till gränser till ett intervall.
keywords: create table, range to table, range to table excel, excel range to table, range to table with borders, how to create table from range, convert range to table, excel convert range to table, excel create table, range to table java 
---
{{% alert color="primary" %}}

 Ibland vill du skapa en tabell genom att lägga till kantlinjer för en**Räckvidd**/**CellArea** baserat på adressen till de celler du har. Du kan använda[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean) ) metod för att skapa ett cellintervall. De[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean) ) metod returnerar en[**Räckvidd**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) objekt. Du kan skapa en[**Stil**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objekt och ange gränserna (överst, vänster, botten, höger) alternativen i enlighet med detta. Senare kan du få cellerna i[**Räckvidd**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)och tillämpa önskad formatering på cellerna.

{{% /alert %}}

 Följande exempel visar hur man skapar en[**Räckvidd**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)och ange gränslinjerna för intervallcellerna.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

Efter att ha kört ovanstående kod kan vi ha den genererade excel-filen som innehåller den formaterade tabellen; här är skärmdumpen av filen.

![todo:image_alt_text](create-table-by-using-border-lines-for-a-range_1.png)
