---
title: Hämta cellsträngvärde med och utan formatering med Golang via C++
linktitle: Hämta cellsträngvärde
type: docs
weight: 240
url: /sv/go-cpp/get-cell-string-value-with-and-without-formatting/
description: Lär dig att hämta cellsträngvärde med och utan formatering via API Aspose.Cells for C++.
keywords: Hämta cellsträngvärde med och utan formatering, hämta cellsträngvärde med och utan formatering, erhåll cellsträngvärde med och utan formatering
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller en metod [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) som kan användas för att få cellens strängvärde med eller utan formatering. Anta att du har en cell med värdet 0,012345 och att du har formaterat den för att bara visa två decimaler. Den kommer då att visas som 0,01 i Excel. Du kan hämta strängvärden både som 0,01 och som 0,012345 med hjälp av [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/)-metoden. Den tar [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) enum som parameter, som har följande värden:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

Följande exempelkod förklarar användningen av [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) metoden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellStringValueWithAndWithoutFormatting.go" >}}
