---
title: Convertire una tabella Excel in un intervallo di dati
type: docs
weight: 10
url: /it/python-java/convert-an-excel-table-to-a-range-of-data/
---

## **Convertire una tabella Excel in un intervallo di dati**
Aspose.Cells for Python via Java fornisce l'opzione di convertire una tabella Excel in un intervallo di dati. A questo scopo, l'API fornisce il metodo [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)). Il seguente frammento di codice dimostra l'uso del metodo [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) per convertire una tabella Excel in un intervallo di dati.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Convertire una tabella Excel in un intervallo con opzioni**
È possibile fornire ulteriori opzioni durante la conversione di una tabella in un intervallo con la classe [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions). È possibile passare un'istanza della classe [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) al metodo [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) per specificare opzioni aggiuntive. Il seguente frammento di codice dimostra l'uso della classe [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) per impostare l'indice dell'ultima riga della tabella. La formattazione della tabella verrà mantenuta fino all'indice di riga specificato e il resto della formattazione verrà rimossa.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
