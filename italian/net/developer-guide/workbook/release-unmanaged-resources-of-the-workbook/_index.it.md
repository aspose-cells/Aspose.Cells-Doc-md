---
title: Rilascia le risorse non gestite del libro di lavoro
type: docs
weight: 310
url: /it/net/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce il metodo [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) per rilasciare le risorse non gestite dell'oggetto [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Il modello di smaltimento viene utilizzato solo per gli oggetti che accedono a risorse non gestite, come gestori di file e di pipe, gestori di registro, gestori di attesa o puntatori a blocchi di memoria non gestita. Questo perché il garbage collector è molto efficiente nel recuperare gli oggetti gestiti inutilizzati, ma non è in grado di recuperare gli oggetti non gestiti.

{{% /alert %}}

L'oggetto [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ora implementa l'interfaccia *System.IDisposable* che ha un unico metodo [**Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose). Puoi chiamare direttamente il metodo [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) oppure puoi utilizzare l'istruzione *Using* per chiamare questo metodo automaticamente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
