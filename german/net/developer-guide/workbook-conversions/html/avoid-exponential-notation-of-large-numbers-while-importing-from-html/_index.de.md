---
title: Vermeiden Sie beim Importieren von HTML die Exponentialschreibweise großer Zahlen
type: docs
weight: 10
url: /de/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}}

 Manchmal enthält Ihr HTML-Code Zahlen wie 1234567890123456, die länger als 15 Ziffern sind, und wenn Sie Ihre HTML in eine Excel-Datei importieren, werden diese Zahlen in Exponentialschreibweise wie 1,23457E+15 umgewandelt. Wenn Sie möchten, dass Ihre Zahl unverändert importiert und nicht in Exponentialschreibweise umgewandelt wird, verwenden Sie bitte[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) Eigenschaft und legen Sie sie fest**wahr** beim Laden Ihrer HTML.

{{% /alert %}}

 Der folgende Beispielcode erläutert die Verwendung von[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)Eigentum. Die API importiert die Zahl so, wie sie ist, ohne sie in Exponentialschreibweise umzuwandeln.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
