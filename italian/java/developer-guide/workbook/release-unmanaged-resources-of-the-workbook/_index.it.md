---
title: Rilascia le risorse non gestite del libro di lavoro
type: docs
weight: 290
url: /it/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells fornisce il metodo [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) per rilasciare le risorse non gestite dell'oggetto Workbook. Il modello di dispose è utilizzato solo per gli oggetti che accedono a risorse non gestite, come handle di file e pipe, handle del registro, handle di attesa o puntatori a blocchi di memoria non gestita. Ciò è dovuto al fatto che il raccoglitore di spazzatura è molto efficiente nel recuperare gli oggetti gestiti inutilizzati, ma non è in grado di recuperare gli oggetti non gestiti.

{{% /alert %}} 
## **Rilasciare le risorse non gestite del libro di lavoro**
Il seguente codice di esempio mostra come fare uso del metodo [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
