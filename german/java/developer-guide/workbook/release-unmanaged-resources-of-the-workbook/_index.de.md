---
title: Freigeben unbeaufsichtigter Ressourcen der Arbeitsmappe
type: docs
weight: 290
url: /de/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells stellt die Methode [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) bereit, um die unmanaged Ressourcen des [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)-Objekts freizugeben. Das Dispose-Muster wird nur für Objekte verwendet, die auf unmanaged Ressourcen zugreifen, wie Datei- und Rohrgriffe, Registry-Handles, Wait Handles oder Zeiger auf Blöcke unmanaged Speicher. Dies liegt daran, dass der Garbage Collector sehr effizient beim Zurücknehmen ungenutzter verwalteter Objekte ist, bei unmanaged Objekten jedoch nicht.

{{% /alert %}} 
## **Freigeben unbeaufsichtigter Ressourcen der Arbeitsmappe**
Das folgende Beispiel zeigt, wie die Methode [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) verwendet wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
{{< app/cells/assistant language="java" >}}
