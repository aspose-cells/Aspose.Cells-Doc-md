---
title: Hämta cellsträngvärde med och utan formatering
type: docs
weight: 240
url: /sv/net/get-cell-string-value-with-and-without-formatting/
description: Lär dig hur du får cellsträngvärde med och utan formatering genom Aspose.Cells for .NET API.
keywords: Hämta cellsträngvärde med och utan formatering, hämta cellsträngvärde med och utan formatering, erhåll cellsträngvärde med och utan formatering
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller en metod [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) som kan användas för att få cellens strängvärde med eller utan formatering. Anta att du har en cell med värdet 0.012345 och du har formaterat den för att endast visa två decimaler. Då kommer den att visas som 0.01 i Excel. Du kan hämta strängvärden både som 0.01 och som 0.012345 med hjälp av [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) metoden. Den tar [**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy/) enum som parameter som har följande värden

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Följande exempelkod förklarar användningen av [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) metoden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
{{< app/cells/assistant language="csharp" >}}
