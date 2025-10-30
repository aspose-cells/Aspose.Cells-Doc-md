---
title: Jobba med Data Display Formats i DataField i pivottabell med Golang via C++
linktitle: Arbeta med datavisningsformat för DataField i pivottabell
type: docs
weight: 140
url: /sv/go-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Lär dig hur du arbetar med datavisningsformat för DataField i pivottabell med hjälp av Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells stöder alla dataradens dataformat.

{{% /alert %}}

## **"Rank Smallest to Largest" och "Rank Largest to Smallest" displayformatalternativ**

Aspose.Cells ger möjlighet att ställa in displayformatalternativ för pivottfälten. För detta tillhandahåller API:n egenskapen [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/). För att ranka störst till minst kan du ställa in egenskapen [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/) till [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/). Följande kodavsnitt visar hur du ställer in displayformatalternativen.

Provfil och utdatafiler kan laddas ner här för att testa provkoden:

[Käll-Excel-fil](101089332.xlsx)

[Utdata Excel-fil](101089333.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithDataDisplayFormatsOfDatafieldInPivotTable.go" >}}
