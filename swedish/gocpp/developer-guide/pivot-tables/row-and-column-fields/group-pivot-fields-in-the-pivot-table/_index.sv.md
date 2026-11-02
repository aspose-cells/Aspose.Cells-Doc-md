---
title: Gruppera pivotfält i pivottabellen med Golang via C++
linktitle: Gruppera pivotfält i pivottabellen med Golang via C++
description: Lär dig hur du grupperar pivotfält i en pivottabell med Aspose.Cells for Go via C++.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, pivottabell, pivotfält, gruppera pivotfält, GroupBy, PivotField, datumgruppering, Go
type: docs
weight: 80
url: /sv/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Microsoft Excel låter dig gruppera pivotfält **i** pivottabellen. När det finns en stor mängd data som är relaterad till ett pivotfält är det ofta användbart att gruppera dem i sektioner. Aspose.Cells tillhandahåller också den här funktionen med metoden [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/).

## **Gruppera pivotfält i pivottabellen**
Följande exempelkod läser in [exempelfilen i Excel](64716818.xlsx) och utför gruppering på det första pivotfältet med hjälp av metoden [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/). Därefter uppdateras pivottabellen, dess data beräknas och arbetsboken sparas som [utdatafilen i Excel](64716817.xlsx). Skärmbilden visar effekten av exempelkoden på exempelfilen i Excel. Som du kan se på skärmbilden är det första pivotfältet nu grupperat efter månader och kvartal.
![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupPivotFieldsInThePivotTable.go" >}}

{{< app/cells/assistant language="go" >}}