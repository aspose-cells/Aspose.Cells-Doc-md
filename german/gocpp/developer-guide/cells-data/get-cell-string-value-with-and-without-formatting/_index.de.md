---
title: Zellstring Wert mit und ohne Formatierung mit Golang über C++ abrufen
linktitle: Cell String Wert abrufen
type: docs
weight: 240
url: /de/go-cpp/get-cell-string-value-with-and-without-formatting/
description: Lernen Sie, wie Sie den Cell String Wert mit und ohne Formatierung über die Aspose.Cells for C++ API abrufen.
keywords: Zellenzeichenfolgenwert mit und ohne Formatierung abrufen, Zellenzeichenfolgenwert mit und ohne Formatierung abrufen, Zellenzeichenfolgenwert mit und ohne Formatierung erhalten
---

{{% alert color="primary" %}}

Aspose.Cells bietet eine Methode [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/), um den String-Wert der Zelle mit oder ohne Formatierung zu erhalten. Angenommen, Sie haben eine Zelle mit dem Wert 0.012345 und haben sie so formatiert, dass nur zwei Dezimalstellen angezeigt werden. Es wird dann in Excel als 0.01 angezeigt. Sie können String-Werte sowohl als 0.01 als auch als 0.012345 mit der Methode [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) abrufen. Diese Methode akzeptiert den Enum [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) als Parameter, der folgende Werte hat:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

Der folgende Beispielcode erläutert die Verwendung der [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/)-Methode.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellStringValueWithAndWithoutFormatting.go" >}}
