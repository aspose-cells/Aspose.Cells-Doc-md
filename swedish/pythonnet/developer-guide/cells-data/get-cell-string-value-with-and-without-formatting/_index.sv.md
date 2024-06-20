---
title: Hämta cellsträngvärde med formatstrategi
type: docs
weight: 240
url: /sv/python-net/get-cell-string-value-with-format-strategy/
description: Lär dig hur man hämtar cellsträngvärde med och utan formatering genom Aspose.Cells för Python via .NET API.
keywords: Python Excel Library, Python Hämta cellsträngvärde med och utan formatering, Python Hämta cellsträngvärde med och utan formatering, Python Skaffa cellsträngvärde med och utan formatering
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET tillhandahåller en metod [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) som kan användas för att få cellens strängvärde med eller utan formatering. Anta att du har en cell med värdet 0.012345 och du har formaterat den för att endast visa två decimaler. Det kommer sedan att visas som 0.01 i Excel. Du kan hämta strängvärden både som 0,01 och som 0.012345 med hjälp av metoden [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/). Den tar [**CellValueFormatStrategy**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvalueformatstrategy/) enum som parameter som har följande värden

- CellValueFormatStrategy.CELL_STYLE
- CellValueFormatStrategy.DISPLAY_STYLE
- CellValueFormatStrategy.DISPLAY_STRING
- CellValueFormatStrategy.NONE

{{% /alert %}}

Följande exempelkod förklarar användningen av [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) metoden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetStringValueWithOrWithoutFormatting.py" >}}
