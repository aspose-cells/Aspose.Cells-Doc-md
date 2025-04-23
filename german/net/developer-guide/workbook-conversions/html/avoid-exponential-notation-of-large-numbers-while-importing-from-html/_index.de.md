---
title: Verhindern Sie die Exponentialnotation großer Zahlen beim Importieren aus HTML
type: docs
weight: 10
url: /de/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}}

Manchmal enthält Ihr HTML Zahlen wie 1234567890123456, die länger als 15 Stellen sind, und wenn Sie Ihr HTML in eine Excel-Datei importieren, werden diese Zahlen in die exponentielle Notation wie 1.23457E+15 umgewandelt. Wenn Sie möchten, dass Ihre Zahl wie eingegeben importiert und nicht in die exponentielle Notation umgewandelt wird, verwenden Sie bitte die [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)-Eigenschaft und setzen Sie sie beim Laden Ihres HTML auf **true**.

{{% /alert %}}

Der folgende Beispielcode erklärt die Verwendung der [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)-Eigenschaft. Die API importiert die Zahl so, wie sie ist, ohne sie in die exponentielle Notation umzuwandeln.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
