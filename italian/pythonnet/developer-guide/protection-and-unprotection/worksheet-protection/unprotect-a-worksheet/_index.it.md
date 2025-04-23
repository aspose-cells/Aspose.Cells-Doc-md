---
title: Disproteggere un foglio di lavoro
type: docs
weight: 20
url: /it/python-net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Se uno sviluppatore ha bisogno di rimuovere la protezione da un foglio di lavoro protetto in fase di esecuzione per poter apportare alcune modifiche al file? Questo può essere facilmente fatto con Aspose.Cells per Python via .NET.

{{% /alert %}}

## **Sblocca un foglio di lavoro**

### **Utilizzando Microsoft Excel**

Per rimuovere la protezione da un foglio di lavoro:

Dal menu **Strumenti**, seleziona **Protezione** seguito da **Disproteggi foglio**. La protezione verrà rimossa a meno che il foglio di lavoro sia protetto da password. In questo caso, compare un dialogo per la password. Inserisci la password e il foglio di lavoro verrà disprotetto.

### **Rimuovere la protezione da un foglio semplicemente protetto utilizzando Aspose.Cells per Python via .NET**

Un foglio di lavoro può essere disprotetto chiamando il metodo [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).
Un foglio di lavoro semplicemente protetto è uno che non è protetto da una password. Tali fogli di lavoro possono essere disprotetti chiamando il metodo [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) senza passare un parametro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingSimplyProtectedWorksheet-1.py" >}}

### **Rimuovere la protezione da un foglio di lavoro protetto da password utilizzando Aspose.Cells per Python via .NET**

Un foglio di lavoro protetto da password è uno protetto da una password. Tali fogli di lavoro possono essere disprotetti chiamando una versione sovraccaricata del metodo [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/unprotect/) che prende la password come parametro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingPasswordProtectedWorksheet-1.py" >}}

