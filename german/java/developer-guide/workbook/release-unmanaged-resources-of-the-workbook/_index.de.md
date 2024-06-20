---
title: Freigeben unbeaufsichtigter Ressourcen der Arbeitsmappe
type: docs
weight: 290
url: /de/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells stellt die Methode [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) bereit, um die unbeaufsichtigten Ressourcen des [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)-Objekts freizugeben. Das Dispose-Muster wird nur für Objekte verwendet, die unbeaufsichtigte Ressourcen wie Datei- und Pipe-Handles, Registrierungshandles, Wartehandles oder Zeiger auf Blöcke unbeaufsichtigten Speichers zugreifen. Dies liegt daran, dass der Garbage-Collector sehr effizient beim Wiederherstellen unbeachteter verwalteter Objekte ist, jedoch nicht in der Lage ist, unbeaufsichtigte Objekte wiederherzustellen.

{{% /alert %}} 
## **Freigeben unbeaufsichtigter Ressourcen der Arbeitsmappe**
Der folgende Beispielscode zeigt, wie die Methode [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) verwendet wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
