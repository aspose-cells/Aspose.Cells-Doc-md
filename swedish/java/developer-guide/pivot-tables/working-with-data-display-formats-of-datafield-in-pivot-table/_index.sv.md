---
title: Att arbeta med dataformat för datarad i pivottabell
type: docs
weight: 150
url: /sv/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells stöder alla dataradens dataformat.

{{% /alert %}}

## **Alternativ för "Rangordna minsta till största" och "Rangordna största till minsta" i displayformat**

Aspose.Cells tillhandahåller möjligheten att ange datapresentationformatet för pivotfält. För detta tillhandahåller API:et [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) egenskapen. För att rangera störst till minst kan du ange [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) egenskapen till [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK_LARGEST_TO_SMALLEST). Följande kodsnutt visar hur du anger datapresentationformatalternativen.

Provfil och utdatafiler kan laddas ner här för att testa provkoden:

[Käll-Excel-fil](PivotTableSample.xlsx)

[Utdata-Excel-fil](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
