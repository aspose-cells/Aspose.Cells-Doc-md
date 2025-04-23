---
title: Rilascia le risorse non gestite del libro di lavoro
type: docs
weight: 290
url: /it/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells fornisce il metodo [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) per rilasciare le risorse non gestite dell’oggetto [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Il pattern dispose viene utilizzato solo per oggetti che accedono a risorse non gestite, come handle di file e pipe, handle del registro, handle di attesa o puntatori a blocchi di memoria non gestita. Questo perché il garbage collector è molto efficiente nel riappropriarsi di oggetti gestiti inutilizzati, ma non può riappropriarsi di oggetti non gestiti.

{{% /alert %}} 
## **Rilasciare le risorse non gestite del libro di lavoro**
Il seguente esempio di codice mostra come usare il metodo [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
{{< app/cells/assistant language="java" >}}
