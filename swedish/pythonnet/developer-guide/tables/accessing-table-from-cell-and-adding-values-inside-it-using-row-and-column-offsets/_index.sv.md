---
title: Få åtkomst till tabell från cell och lägg till värden inuti den med hjälp av rad och kolumnförflyttningar
type: docs
weight: 230
url: /sv/python-net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalt sett lägger du till värden inuti tabellen eller listobjektet med hjälp av [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool)-metoden. Men ibland kan du behöva lägga till värden inuti tabellen eller listobjektet med rad- och kolumnförflyttningar.

För att komma åt tabellen eller listobjektet från en cell, använd [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#)-metoden. För att lägga till värden inuti den med hjälp av rad- och kolumnförskjutningar, använd [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any)-metoden.

{{% /alert %}}

Följande skärmbild visar den käll-Excel-filen som används i koden. Den innehåller den tomma tabellen och markerar cellen D5 som ligger inuti tabellen. Vi kommer att få åtkomst till denna tabell från cellen D5 med hjälp av [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#)-metoden och sedan lägga till värden inuti den med hjälp av både [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool)- och [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any)-metoderna.

## Exempel

### Skärmbilder som jämför käll- och utdatafiler

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

Följande skärmbild visar den genererade utdata-Excel-filen av koden. Som du kan se har cellen D5 ett värde och cellen F6, som ligger vid förflyttning 2,2 inuti tabellen, har ett värde.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### Python-kod för att komma åt tabell från cell och lägga till värden inuti den med rad- och kolumnförskjutningar

Följande provkod laddar den angivna källan Excel-filen som visas i skärmdumpen ovan och lägger till värden inne i tabellen och genererar den resulterande Excel-filen som visas ovan.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-AccessTableFromCellAndAddValue.py" >}}
{{< app/cells/assistant language="python-net" >}}
