---
title: Zellzeichenfolgenwert mit Formatstrategie abrufen
type: docs
weight: 240
url: /de/python-net/get-cell-string-value-with-format-strategy/
description: Erfahren Sie, wie Sie den Zellzeichenfolgenwert mit und ohne Formatierung über die Aspose.Cells für Python via .NET API abrufen.
keywords: Python Excel Bibliothek, Python Zellzeichenfolgenwert mit und ohne Formatierung abrufen, Python Zellzeichenfolgenwert mit und ohne Formatierung abrufen, Python Zellzeichenfolgenwert mit und ohne Formatierung abrufen
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET bietet eine Methode [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/), die verwendet werden kann, um den Zeichenfolgenwert der Zelle mit oder ohne Formatierung abzurufen. Nehmen wir an, Sie haben eine Zelle mit dem Wert 0,012345 und Sie haben sie formatiert, um nur zwei Dezimalstellen anzuzeigen. Sie wird dann in Excel als 0,01 angezeigt. Sie können Zeichenfolgenwerte sowohl als 0,01 als auch als 0,012345 mithilfe der Methode [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) abrufen. Sie erfordert ein [**CellValueFormatStrategy**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvalueformatstrategy/)-Enum als Parameter, das die folgenden Werte enthält

- CellValueFormatStrategy.CELL_STYLE
- CellValueFormatStrategy.DISPLAY_STYLE
- CellValueFormatStrategy.DISPLAY_STRING
- CellValueFormatStrategy.NONE

{{% /alert %}}

Der folgende Beispielcode erläutert die Verwendung der [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/)-Methode.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetStringValueWithOrWithoutFormatting.py" >}}
{{< app/cells/assistant language="python-net" >}}
