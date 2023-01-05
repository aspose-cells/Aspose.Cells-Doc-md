---
title: Rimuovere la protezione di un foglio di lavoro
type: docs
weight: 20
url: /it/net/unprotect-a-worksheet/
---
{{% alert color="primary" %}}

Se uno sviluppatore deve rimuovere la protezione da un foglio di lavoro protetto in fase di esecuzione in modo da poter apportare alcune modifiche al file? Questo può essere fatto facilmente con Aspose.Cells.

{{% /alert %}}

## **Rimuovere la protezione di un foglio di lavoro**

### **Utilizzando Microsoft Excel**

Per rimuovere la protezione da un foglio di lavoro:

 Dal**Utensili** menù, selezionare**Protezione** seguito da**Foglio non protetto**. La protezione verrà rimossa a meno che il foglio di lavoro non sia protetto da password. In questo caso, una finestra di dialogo richiede la password. Immettere la password e il foglio di lavoro non sarà protetto.

### **Rimozione della protezione di un foglio di lavoro semplicemente protetto utilizzando Aspose.Cells**

 Un foglio di lavoro può essere non protetto chiamando il metodo[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe'[**Non protetto**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)metodo.
 Un foglio di lavoro semplicemente protetto è uno che non è protetto da una password. Tali fogli di lavoro possono essere non protetti chiamando il metodo[**Non protetto**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)metodo senza passare un parametro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Rimozione della protezione di un foglio di lavoro protetto da password utilizzando Aspose.Cells**

Un foglio di lavoro protetto da password è protetto da una password. Tali fogli di lavoro possono essere non protetti chiamando una versione di overload di[**Non protetto**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1)metodo che accetta la password come parametro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
