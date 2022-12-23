---
title: Converti una tabella di Excel in un intervallo di dati
type: docs
weight: 10
url: /it/python-java/convert-an-excel-table-to-a-range-of-data/
---
## **Converti una tabella di Excel in un intervallo di dati**
Aspose.Cells for Python via Java offre la possibilità di convertire la tabella Excel in un intervallo di dati. Per questo, lo API fornisce il[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\) ) metodo. Il seguente frammento di codice illustra l'uso di[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) metodo per convertire una tabella di Excel in un intervallo di dati.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Converti una tabella di Excel in un intervallo con le opzioni**
Puoi fornire opzioni aggiuntive durante la conversione di una tabella in un intervallo con il[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) classe. Puoi passare un'istanza di[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)classe al[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) per specificare opzioni aggiuntive. Il seguente frammento di codice illustra l'uso di[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)class per impostare l'ultimo indice di riga della tabella. La formattazione della tabella verrà mantenuta fino all'indice di riga specificato e il resto della formattazione verrà rimosso.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
