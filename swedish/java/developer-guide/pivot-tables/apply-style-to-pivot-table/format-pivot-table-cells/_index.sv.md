---
title: Formatera pivot tabellceller
type: docs
weight: 20
url: /sv/java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

Ibland vill du formatera pivottabellceller. Till exempel vill du tillämpa en bakgrundsfärg på pivottabellceller. Aspose.Cells tillhandahåller två metoder [**PivotTable.formatAll()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll-com.aspose.cells.Style-) och [**PivotTable.format()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#format-int-int-com.aspose.cells.Style-), som du kan använda för detta ändamål.

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll-com.aspose.cells.Style-) tillämpar stilen på hela pivottabellen medan [**PivotTable.format()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#format-int-int-com.aspose.cells.Style-) tillämpar stilen på en enskild cell i pivottabellen.

{{% /alert %}}

Följande kodexempel formaterar hela pivottabellen med en ljusblå färg och formaterar sedan den andra tabellraden gul.

**Ingångsförändringstabellen, innan koden körs**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**Utstegsförändringstabellen, efter att koden har utförts**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FormatPivotTableCells-FormatPivotTableCells.java" >}}
{{< app/cells/assistant language="java" >}}
