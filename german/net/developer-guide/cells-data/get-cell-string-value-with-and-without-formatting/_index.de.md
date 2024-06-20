---
title: Zellenzeichenfolgenwert mit und ohne Formatierung abrufen
type: docs
weight: 240
url: /de/net/get-cell-string-value-with-and-without-formatting/
description: Erfahren Sie, wie Sie den Zellenzeichenfolgenwert mit und ohne Formatierung mithilfe der Aspose.Cells for .NET API abrufen.
keywords: Zellenzeichenfolgenwert mit und ohne Formatierung abrufen, Zellenzeichenfolgenwert mit und ohne Formatierung abrufen, Zellenzeichenfolgenwert mit und ohne Formatierung erhalten
---

{{% alert color="primary" %}}

Aspose.Cells bietet eine Methode [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue), die verwendet werden kann, um den Zeichenfolgenwert der Zelle mit oder ohne Formatierung zu erhalten. Angenommen, Sie haben eine Zelle mit dem Wert 0,012345 und haben sie formatiert, um nur zwei Dezimalstellen anzuzeigen. Sie wird dann als 0,01 in Excel angezeigt. Sie können Zeichenfolgenwerte sowohl als 0,01 als auch als 0,012345 mithilfe der [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)-Methode abrufen. Sie akzeptiert das [**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy/)-Enum als Parameter, das folgende Werte hat

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Der folgende Beispielcode erläutert die Verwendung der [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)-Methode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
