---
title: Verhindern Sie die Exponentialnotation großer Zahlen beim Importieren aus HTML
type: docs
weight: 600
url: /de/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}} 

Manchmal enthält Ihr HTML Zahlen wie 1234567890123456, die länger als 15 Ziffern sind, und wenn Sie Ihr HTML in eine Excel-Datei importieren, werden diese Zahlen in Exponentialnotation wie 1.23457E+15 umgewandelt. Wenn Sie möchten, dass Ihre Zahl so importiert wird, wie sie ist und nicht in Exponentialnotation umgewandelt wird, verwenden Sie bitte die [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)-Eigenschaft und setzen Sie sie beim Laden Ihres HTML auf **true**.

{{% /alert %}} 
## **Verhindern Sie die Exponentialnotation großer Zahlen beim Importieren aus HTML**
Der folgende Beispielcode erläutert die Verwendung der Eigenschaft [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision). Es importiert die Zahl so, wie sie ist, ohne sie in Exponentialnotation umzuwandeln.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
{{< app/cells/assistant language="java" >}}
