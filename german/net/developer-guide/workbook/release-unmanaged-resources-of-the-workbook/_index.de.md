---
title: Geben Sie nicht verwaltete Ressourcen der Arbeitsmappe frei
type: docs
weight: 310
url: /de/net/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}}

 Aspose.Cells bietet[**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) Methode zum Freigeben der nicht verwalteten Ressourcen der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Objekt. Das Dispose-Muster wird nur für Objekte verwendet, die auf nicht verwaltete Ressourcen zugreifen, z. B. Datei- und Pipe-Handles, Registrierungshandles, Wait-Handles oder Zeiger auf Blöcke von nicht verwaltetem Speicher. Dies liegt daran, dass der Garbage Collector beim Zurückgewinnen nicht verwendeter verwalteter Objekte sehr effizient ist, aber nicht in der Lage ist, nicht verwaltete Objekte zurückzugewinnen.

{{% /alert %}}

[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Objekt implementiert jetzt die*System.IDisposable* Schnittstelle, die eine einzige Methode hat[**Entsorgen()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) . Sie können entweder direkt anrufen[**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) Methode oder Sie können die verwenden*Verwenden*-Anweisung, um diese Methode automatisch aufzurufen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
