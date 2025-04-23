---
title: Disproteggere un foglio di lavoro
type: docs
weight: 20
url: /it/net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Se uno sviluppatore ha bisogno di rimuovere la protezione da un foglio di lavoro protetto durante l'esecuzione in modo che alcune modifiche possano essere apportate al file? Questo può essere facilmente fatto con Aspose.Cells.

{{% /alert %}}

## **Sblocca un foglio di lavoro**

### **Utilizzando Microsoft Excel**

Per rimuovere la protezione da un foglio di lavoro:

Dal menu **Strumenti**, seleziona **Protezione** seguito da **Disproteggi foglio**. La protezione verrà rimossa a meno che il foglio di lavoro sia protetto da password. In questo caso, compare un dialogo per la password. Inserisci la password e il foglio di lavoro verrà disprotetto.

### **Disproteggere un foglio di lavoro semplicemente protetto utilizzando Aspose.Cells**

Un foglio di lavoro può essere disprotetto chiamando il metodo [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).
Un foglio di lavoro semplicemente protetto è uno che non è protetto da una password. Tali fogli di lavoro possono essere disprotetti chiamando il metodo [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) senza passare un parametro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Disproteggere un foglio di lavoro protetto da password utilizzando Aspose.Cells**

Un foglio di lavoro protetto da password è uno protetto da una password. Tali fogli di lavoro possono essere disprotetti chiamando una versione sovraccaricata del metodo [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1) che prende la password come parametro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
