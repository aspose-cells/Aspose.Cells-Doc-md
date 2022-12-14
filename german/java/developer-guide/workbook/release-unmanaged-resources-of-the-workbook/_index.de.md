---
title: Geben Sie nicht verwaltete Ressourcen der Arbeitsmappe frei
type: docs
weight: 290
url: /de/java/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}} 

 Aspose.Cells bietet[Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\) )-Methode zum Freigeben der nicht verwalteten Ressourcen der[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)Objekt. Das Dispose-Muster wird nur für Objekte verwendet, die auf nicht verwaltete Ressourcen zugreifen, z. B. Datei- und Pipe-Handles, Registrierungshandles, Wait-Handles oder Zeiger auf Blöcke von nicht verwaltetem Speicher. Dies liegt daran, dass der Garbage Collector beim Zurückgewinnen nicht verwendeter verwalteter Objekte sehr effizient ist, aber nicht in der Lage ist, nicht verwaltete Objekte zurückzugewinnen.

{{% /alert %}} 
## **Geben Sie nicht verwaltete Ressourcen der Arbeitsmappe frei**
Der folgende Beispielcode zeigt, wie Sie die verwenden[Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
