---
title: Rilascia le risorse non gestite della cartella di lavoro
type: docs
weight: 310
url: /it/net/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}}

 Aspose.Cells fornisce[**Cartella di lavoro.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) metodo per rilasciare le risorse non gestite del[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)oggetto. Il modello Dispose viene usato solo per oggetti che accedono a risorse non gestite, ad esempio handle di file e pipe, handle di registro, handle di attesa o puntatori a blocchi di memoria non gestita. Questo perché il Garbage Collector è molto efficiente nel recuperare oggetti gestiti inutilizzati, ma non è in grado di recuperare oggetti non gestiti.

{{% /alert %}}

[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) oggetto ora implementa il*System.IDDisposable* interfaccia che ha un unico metodo[**Disponi()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) . Puoi chiamare direttamente il[**Cartella di lavoro.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) metodo oppure è possibile utilizzare il*Usando*istruzione per chiamare questo metodo automaticamente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
