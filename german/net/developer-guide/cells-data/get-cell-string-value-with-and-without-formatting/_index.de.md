---
title: Erhalten Sie den String-Wert Cell mit und ohne Formatierung
type: docs
weight: 240
url: /de/net/get-cell-string-value-with-and-without-formatting/
description: Erfahren Sie, wie Sie den String-Wert Cell mit und ohne Formatierung über Aspose.Cells for .NET API abrufen.
keywords: Get Cell String Value with and without Formatting, Retrieve Cell String Value with and without Formatting, Obtain Cell String Value with and without Formatting
---
{{% alert color="primary" %}}

 Aspose.Cells bietet eine Methode[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)Dies kann verwendet werden, um den Zeichenfolgenwert der Zelle mit oder ohne Formatierung abzurufen. Angenommen, Sie haben eine Zelle mit dem Wert 0,012345 und haben sie so formatiert, dass nur zwei Dezimalstellen angezeigt werden. In Excel wird dann der Wert 0,01 angezeigt. Mit dem können Sie Zeichenfolgenwerte sowohl als 0,01 als auch als 0,012345 abrufen[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) Methode. Es braucht[**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)enum als Parameter, der die folgenden Werte hat

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

 Der folgende Beispielcode erläutert die Verwendung von[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)Methode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
