---
title: Verhindern Sie die Exponentialnotation großer Zahlen beim Importieren aus HTML
type: docs
weight: 10
url: /de/python-net/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: In diesem Thema wird gezeigt, wie Sie die exponentielle Notation großer Zahlen beim Importieren aus HTML mithilfe von Aspose.Cells für Python via NET vermeiden können.
keywords: Vermeiden Sie die exponentielle Notation großer Zahlen beim Importieren aus HTML und behalten Sie die Genauigkeit bei.
---

{{% alert color="primary" %}}

Manchmal enthält Ihr HTML Zahlen wie 1234567890123456, die länger als 15 Stellen sind, und wenn Sie Ihr HTML in eine Excel-Datei importieren, werden diese Zahlen in die exponentielle Notation wie 1.23457E+15 umgewandelt. Wenn Sie möchten, dass Ihre Zahl wie eingegeben importiert und nicht in die exponentielle Notation umgewandelt wird, verwenden Sie bitte die [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/)-Eigenschaft und setzen Sie sie beim Laden Ihres HTML auf **true**.

{{% /alert %}}

Der folgende Beispielcode erklärt die Verwendung der [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/)-Eigenschaft. Die API importiert die Zahl so, wie sie ist, ohne sie in die exponentielle Notation umzuwandeln.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AvoidExponentialNotationWhileImportingFromHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
