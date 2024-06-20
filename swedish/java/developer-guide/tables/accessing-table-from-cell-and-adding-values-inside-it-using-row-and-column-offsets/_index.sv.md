---
title: Få åtkomst till tabell från cell och lägg till värden inuti den med hjälp av rad och kolumnförflyttningar
type: docs
weight: 110
url: /sv/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalt sett lägger du till värden inuti tabellen eller listobjektet med hjälp av [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean))-metoden. Men ibland kan du behöva lägga till värden inuti tabellen eller listobjektet med rad- och kolumnförflyttningar.

För att få åtkomst till tabell eller listobjekt från en cell, använd [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--)-metoden. Och för att lägga till värden inuti den med hjälp av rad- och kolumnförflyttningar, använd [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object))-metoden.

{{% /alert %}}

## Exempel

### Skärmbilder som jämför käll- och utdatafiler

Följande skärmbild visar den käll-Excel-filen som används i koden. Den innehåller den tomma tabellen och markerar cellen D5 som ligger inuti tabellen. Vi kommer att få åtkomst till denna tabell från cellen D5 med hjälp av [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--)-metoden och sedan lägga till värden inuti den med hjälp av både [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean))- och [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object))-metoderna.

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

Följande skärmbild visar den genererade utdata-Excel-filen av koden. Som du kan se har cellen D5 ett värde och cellen F6, som ligger vid förflyttning 2,2 inuti tabellen, har ett värde.

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Java-kod för att få åtkomst till tabell från cell och lägga till värden inuti den med hjälp av rad- och kolumnförflyttningar

Följande provkod laddar den angivna källan Excel-filen som visas i skärmdumpen ovan och lägger till värden inne i tabellen och genererar den resulterande Excel-filen som visas ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
