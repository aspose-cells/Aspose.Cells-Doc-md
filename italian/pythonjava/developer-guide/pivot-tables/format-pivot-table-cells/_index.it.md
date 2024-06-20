---
title: Formattare le celle della tabella pivot
type: docs
weight: 20
url: /it/python-java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

A volte si desidera formattare le celle della tabella pivot. Ad esempio, si desidera applicare un colore di sfondo alle celle della tabella pivot. Aspose.Cells fornisce due metodi [**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) e [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)), che è possibile utilizzare a questo scopo.

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) applica lo stile all'intera tabella pivot mentre [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) applica lo stile a una singola cella della tabella pivot.

{{% /alert %}}

Il codice di esempio seguente formatta l'intera tabella pivot con un colore blu chiaro e poi formatta la seconda riga della tabella con il colore giallo.

**La tabella pivot di input, prima di eseguire il codice**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**La tabella pivot in uscita, dopo l'esecuzione del codice**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
