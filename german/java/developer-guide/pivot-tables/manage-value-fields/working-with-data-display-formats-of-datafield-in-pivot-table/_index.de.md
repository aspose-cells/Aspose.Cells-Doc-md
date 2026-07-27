---
title: Arbeiten mit Datenanzeigeformaten von DataField im Pivot Table
type: docs
weight: 150
url: /de/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt alle Datenanzeigeformate von DataField.

{{% /alert %}}

## **"Rang Kleinste bis Größte" und "Rang Größte bis Kleinste" Anzeigeformat-Option**

Aspose.Cells bietet die Möglichkeit, die Anzeigeformatoptionen für Pivot-Felder festzulegen. Für dies bietet die API die Eigenschaft [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat). Um von größtem zu kleinestem Rang zu sortieren, können Sie die [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) Eigenschaft auf [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK-LARGEST-TO-SMALLEST) setzen. Der folgende Codeausschnitt zeigt das Festlegen der Anzeigeformatoptionen.

Die Beispielsquell- und Ausgabedateien können hier für das Testen des Beispielcodes heruntergeladen werden:

[Quelldatei Excel](PivotTableSample.xlsx)

[Ausgabedatei Excel](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
{{< app/cells/assistant language="java" >}}
