---
title: Få åtkomst till tabell från cell och lägg till värden inuti den med hjälp av rad och kolumnförflyttningar
type: docs
weight: 230
url: /sv/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalt sett lägger du till värden inuti tabellen eller listobjektet med hjälp av [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)-metoden. Men ibland kan du behöva lägga till värden inuti tabellen eller listobjektet med rad- och kolumnförflyttningar.

För att komma åt tabellen eller listobjektet från en cell, använd [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable)-metoden. För att lägga till värden inuti den med hjälp av rad- och kolumnförskjutningar, använd [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue)-metoden.

{{% /alert %}}

Följande skärmbild visar den käll-Excel-filen som används i koden. Den innehåller den tomma tabellen och markerar cellen D5 som ligger inuti tabellen. Vi kommer att få åtkomst till denna tabell från cellen D5 med hjälp av [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable)-metoden och sedan lägga till värden inuti den med hjälp av både [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)- och [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue)-metoderna.

## Exempel

### Skärmbilder som jämför käll- och utdatafiler

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

Följande skärmbild visar den genererade utdata-Excel-filen av koden. Som du kan se har cellen D5 ett värde och cellen F6, som ligger vid förflyttning 2,2 inuti tabellen, har ett värde.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### C#-kod för att komma åt tabell från cell och lägga till värden inuti den med hjälp av rad- och kolumnförskjutningar

Följande provkod laddar den angivna källan Excel-filen som visas i skärmdumpen ovan och lägger till värden inne i tabellen och genererar den resulterande Excel-filen som visas ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
