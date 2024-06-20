---
title: Formatieren von Pivottabellenzellen
type: docs
weight: 20
url: /de/python-java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

Manchmal möchten Sie Pivot-Tabelle Zellen formatieren. Zum Beispiel möchten Sie eine Hintergrundfarbe auf Pivot-Tabelle Zellen anwenden. Aspose.Cells bietet zwei Methoden [**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) und [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)), die Sie zu diesem Zweck verwenden können.

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) wendet den Stil auf die gesamte Pivot-Tabelle an, während [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) den Stil auf eine einzelne Zelle der Pivot-Tabelle anwendet.

{{% /alert %}}

Der folgende Beispielcode formatiert die gesamte Pivot-Tabelle mit einer hellblauen Farbe und formatiert dann die zweite Tabellenzeile gelb.

**Der Eingabe-Pivot-Table, bevor der Code ausgeführt wird**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**Der Ausgabe-Pivot-Table, nach Ausführung des Codes**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
