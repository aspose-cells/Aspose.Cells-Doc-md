---
title: Få åtkomst till tabell från Cell och lägga till värden i den med hjälp av rad- och kolumnförskjutningar
type: docs
weight: 230
url: /sv/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Normalt lägger du till värden inuti tabell- eller listobjektet med hjälp av[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)metod. Men ibland kan du behöva lägga till värden i tabell- eller listobjektet med hjälp av rad- och kolumnförskjutningar.

För att komma åt tabell- eller listobjekt från en cell, använd[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) metod. För att lägga till värden inuti den med hjälp av rad- och kolumnoffset, använd[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) metod.

{{% /alert %}}

 Följande skärmdump visar källfilen för Excel som används i koden. Den innehåller den tomma tabellen och markerar cellen D5 som ligger inuti tabellen. Vi kommer åt den här tabellen från cell D5 med hjälp av[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) och lägg sedan till värdena i den med båda[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) och[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue)metoder.

## Exempel

### Skärmdumpar som jämför käll- och utdatafiler

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
|:- |

Följande skärmdump visar utdata Excel-filen som genereras av koden. Som du kan se har cell D5 ett värde och cell F6 som är vid offset 2,2 i tabellen har ett värde.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
|:- |

### C#-kod för att komma åt tabell från cell och för att lägga till värden inuti den med hjälp av rad- och kolumnförskjutningar

Följande exempelkod laddar källfilen för Excel som visas i skärmdumpen ovan och lägger till värden i tabellen och genererar utdata Excel-filen som visas ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
