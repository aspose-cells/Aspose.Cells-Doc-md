---
title: Hämta Cell String Value med och utan formatering
type: docs
weight: 240
url: /sv/net/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells tillhandahåller en metod[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) som kan användas för att få strängvärdet för cellen med eller utan någon formatering. Anta att du har en cell med värdet 0,012345 och du har formaterat den så att den endast visar två decimaler. Det kommer då att visas som 0.01 i Excel. Du kan hämta strängvärden både som 0,01 och som 0,012345 med hjälp av[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) metod. Det tar[**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)enum som en parameter som har följande värden

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

 Följande exempelkod förklarar användningen av[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)metod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
