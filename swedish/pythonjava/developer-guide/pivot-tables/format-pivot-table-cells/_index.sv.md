---
title: Format pivottabell Cells
type: docs
weight: 20
url: /sv/python-java/format-pivot-table-cells/
---
{{% alert color="primary" %}}

 Ibland vill du formatera pivottabellceller. Till exempel vill du använda en bakgrundsfärg på pivottabellceller. Aspose.Cells tillhandahåller två metoder[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ) och[**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)), som du kan använda för detta ändamål.

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ) tillämpar stilen på hela pivottabellen medan[**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) tillämpar stilen på en enskild cell i pivottabellen.

{{% /alert %}}

Följande exempelkod formaterar hela pivottabellen med en ljusblå färg och formaterar sedan den andra tabellraden gul.

**Ingångspivottabellen, innan koden exekveras**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**Utdatapivottabellen, efter exekvering av koden**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
