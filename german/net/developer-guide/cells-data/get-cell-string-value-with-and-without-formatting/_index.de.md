---
title: Holen Sie sich Cell Zeichenfolgenwert mit und ohne Formatierung
type: docs
weight: 240
url: /de/net/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells stellt eine Methode bereit[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) die verwendet werden kann, um den Zeichenfolgenwert der Zelle mit oder ohne Formatierung zu erhalten. Angenommen, Sie haben eine Zelle mit dem Wert 0,012345 und Sie haben sie so formatiert, dass nur zwei Dezimalstellen angezeigt werden. Es wird dann in Excel als 0,01 angezeigt. Sie können Zeichenfolgenwerte sowohl als 0,01 als auch als 0,012345 abrufen, indem Sie die verwenden[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) Methode. Es braucht[**CellValueFormatStrategie**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)enum als Parameter, der die folgenden Werte hat

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

 Der folgende Beispielcode erläutert die Verwendung von[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)Methode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
