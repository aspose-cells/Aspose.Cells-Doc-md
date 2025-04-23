---
title: Freigeben unbeaufsichtigter Ressourcen der Arbeitsmappe
type: docs
weight: 310
url: /de/net/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Methode [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) zur Freigabe der nicht verwalteten Ressourcen des Objekts [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) an. Das Freigabemuster wird nur für Objekte verwendet, die auf nicht verwaltete Ressourcen zugreifen, wie Datei- und Pipe-Handles, Registrierungshandles, Wartehandles oder Zeiger auf Blöcke nicht verwalteten Speichers. Dies liegt daran, dass der Garbage-Collector sehr effizient beim Freigeben nicht verwendeter verwalteter Objekte ist, aber nicht verwaltete Objekte nicht freigeben kann.

{{% /alert %}}

Das [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Objekt implementiert jetzt das *System.IDisposable*-Interface, das eine einzelne Methode [**Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) hat. Sie können entweder direkt die Methode [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) aufrufen oder Sie können die *Using*-Anweisung verwenden, um diese Methode automatisch aufzurufen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
{{< app/cells/assistant language="csharp" >}}
