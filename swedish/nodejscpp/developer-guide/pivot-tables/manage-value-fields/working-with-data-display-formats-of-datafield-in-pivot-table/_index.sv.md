---
title: Att arbeta med dataformat för datarad i pivottabell
type: docs
weight: 140
url: /sv/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ stödjer alla data visningsformat för DataField.

{{% /alert %}}

## **Alternativ för "Rangordna minsta till största" och "Rangordna största till minsta" i displayformat**

ASpose.Cells ger möjlighet att ställa in displayformatalternativet för pivottabellfält. För detta tillhandahåller API:en egenskapen [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-). För att rangordna största till minsta kan du ställa in egenskapen [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-) till [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/nodejs-cpp/pivotfielddatadisplayformat/). Följande kodsnutt demonstrerar inställning av displayformatalternativen.

Provfil och utdatafiler kan laddas ner här för att testa provkoden:

[Käll-Excel-fil](101089332.xlsx)

[Utdata Excel-fil](101089333.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTableDataDisplayFormatRanking-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
