---
title: Vermeiden, dass große Zahlen in exponentialer Notation angezeigt werden, beim Import aus HTML mit Golang via C++
linktitle: Verhindern Sie die Exponentialnotation großer Zahlen beim Importieren aus HTML
type: docs
weight: 10
url: /de/go-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Lernen Sie, wie man die exponentielle Notation großer Zahlen beim Import aus HTML mit Aspose.Cells for C++ vermeidet.
---

{{% alert color="primary" %}}

Manchmal enthält Ihr HTML Zahlen wie 1234567890123456, die länger als 15 Ziffern sind, und wenn Sie Ihr HTML in eine Excel-Datei importieren, werden diese Zahlen in die exponentielle Notation umgewandelt, z.B. 1.23457E+15. Wenn Sie möchten, dass Ihre Nummer so importiert wird, wie sie ist, ohne in die exponentielle Notation umgewandelt zu werden, verwenden Sie bitte die [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/)-Eigenschaft und setzen sie auf **true**, während Sie Ihr HTML laden.

{{% /alert %}}

Der folgende Beispielcode erklärt die Verwendung der [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/)-Eigenschaft. Die API importiert die Nummer so, wie sie ist, ohne sie in die exponentielle Notation umzuwandeln.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AvoidExponentialNotationOfLargeNumbersWhileImportingFromHtml.go" >}}
