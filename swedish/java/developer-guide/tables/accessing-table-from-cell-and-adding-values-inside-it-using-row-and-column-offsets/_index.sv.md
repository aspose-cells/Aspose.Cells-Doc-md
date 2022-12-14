---
title: Få åtkomst till tabell från Cell och lägga till värden i den med hjälp av rad- och kolumnförskjutningar
type: docs
weight: 110
url: /sv/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Normalt lägger du till värden inuti tabell- eller listobjektet med hjälp av[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) metod. Men ibland kan du behöva lägga till värden i tabell- eller listobjektet med hjälp av rad- och kolumnförskjutningar.

För att komma åt tabell- eller listobjekt från en cell, använd[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) metod. Och för att lägga till värden inuti den med hjälp av rad- och kolumnförskjutningar, använd[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) metod.

{{% /alert %}}

## Exempel

### Skärmdumpar som jämför käll- och utdatafiler

 Följande skärmdump visar källfilen för Excel som används i koden. Den innehåller den tomma tabellen och markerar cellen D5 som ligger inuti tabellen. Vi kommer åt den här tabellen från cell D5 med hjälp av[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) och lägg sedan till värdena i den med båda[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean) ) och[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) metoder.

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

Följande skärmdump visar utdata Excel-filen som genereras av koden. Som du kan se har cell D5 ett värde och cell F6 som är vid offset 2,2 i tabellen har ett värde.

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Java-kod för att komma åt tabell från cell och för att lägga till värden inuti den med hjälp av rad- och kolumnförskjutningar

Följande exempelkod laddar källfilen för Excel som visas i skärmdumpen ovan och lägger till värden i tabellen och genererar utdata Excel-filen som visas ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
