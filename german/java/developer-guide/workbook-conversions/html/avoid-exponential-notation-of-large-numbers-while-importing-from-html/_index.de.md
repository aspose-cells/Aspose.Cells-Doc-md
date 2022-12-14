---
title: Vermeiden Sie beim Import aus HTML die Exponentialschreibweise großer Zahlen
type: docs
weight: 600
url: /de/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}} 

Manchmal enthält Ihr HTML-Code Zahlen wie 1234567890123456, die länger als 15 Ziffern sind, und wenn Sie Ihren HTML-Code in eine Excel-Datei importieren, werden diese Zahlen in Exponentialschreibweise wie 1,23457E+15 umgewandelt. Wenn Sie möchten, dass Ihre Zahl unverändert importiert und nicht in Exponentialschreibweise umgewandelt wird, verwenden Sie bitte[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) Eigenschaft und legen Sie sie fest**Stimmt** beim Laden Ihres HTML.

{{% /alert %}} 
## **Vermeiden Sie beim Import aus HTML die Exponentialschreibweise großer Zahlen**
 Der folgende Beispielcode erläutert die Verwendung von[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)Eigentum. Die Zahl wird so importiert, wie sie ist, ohne sie in Exponentialschreibweise umzuwandeln.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
