---
title: Zellenzeichenfolgenwert mit und ohne Formatierung abrufen
type: docs
weight: 240
url: /de/nodejs-cpp/get-cell-string-value-with-and-without-formatting/
description: Erfahren Sie, wie Sie den Zell Stringwert mit und ohne Formatierung über die API Aspose.Cells for Node.js via C++ abrufen.
keywords: Zell Stringwert mit und ohne Formatierung in Node.js via C++, Zell Stringwert mit und ohne Formatierung in Node.js via C++, Zell Stringwert mit und ohne Formatierung in Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells stellt eine Methode [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) bereit, die verwendet werden kann, um den String-Wert der Zelle mit oder ohne Formatierung abzurufen. Angenommen, Sie haben eine Zelle mit dem Wert 0.012345 und haben diese so formatiert, dass nur zwei Dezimalstellen angezeigt werden. In Excel wird sie dann als 0.01 angezeigt. Sie können String-Werte sowohl als 0.01 als auch als 0.012345 mit der Methode [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) abrufen. Sie akzeptiert den [**CellValueFormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/cellvalueformatstrategy/)-enum als Parameter, der die folgenden Werte hat.

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Der folgende Beispielcode erklärt die Verwendung der [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--)-Methode.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-GetCellStringWithOrWithoutFormatting.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
