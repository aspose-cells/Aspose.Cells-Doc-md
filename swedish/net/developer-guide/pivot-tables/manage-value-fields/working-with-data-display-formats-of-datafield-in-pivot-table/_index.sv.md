---
title: Att arbeta med dataformat för datarad i pivottabell
type: docs
weight: 140
url: /sv/net/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells stöder alla dataradens dataformat.

{{% /alert %}}

## **Alternativ för "Rangordna minsta till största" och "Rangordna största till minsta" i displayformat**

ASpose.Cells ger möjlighet att ställa in displayformatalternativet för pivottabellfält. För detta tillhandahåller API:en egenskapen [**PivotField.ShowValuesSetting.CalculationType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotshowvaluessetting/calculationtype/). För att rangordna största till minsta kan du ställa in egenskapen [**PivotField.ShowValuesSetting.CalculationType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotshowvaluessetting/calculationtype/) till [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfielddatadisplayformat). Följande kodsnutt demonstrerar inställning av displayformatalternativen.

Provfil och utdatafiler kan laddas ner här för att testa provkoden:

[Käll-Excel-fil](101089332.xlsx)

[Utdata Excel-fil](101089333.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTables-PivotTableDataDisplayFormatRanking-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
