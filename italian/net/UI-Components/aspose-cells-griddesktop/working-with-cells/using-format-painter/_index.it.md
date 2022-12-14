---
title: Utilizzo di Copia formato
type: docs
weight: 80
url: /it/net/using-format-painter/
---
{{% alert color="primary" %}} 

Format painter è la caratteristica di MS Excel che è stata adattata in Aspose.Cells.GridDesktop. È una caratteristica molto bella. Per coloro che non hanno ancora utilizzato questa funzione, Format Painter consente agli utenti di applicare le impostazioni di formattazione di qualsiasi cella attiva a un'altra cella. L'implementazione di questa funzione è molto semplice. In questo argomento tratteremo anche questo.

{{% /alert %}} 
## **Utilizzo di Copia formato**
 La caratteristica di**Formato pittore** richiede agli utenti di selezionare una cella le cui impostazioni di formattazione si desidera applicare su altre celle e quindi chiamare**StartFormatPainter** metodo**GrigliaDesktop**. Ci sono due modalità di format painter come segue:

- **Utilizzo di Format Painter una volta**
- **Usare Copia formato sempre**
### **Utilizzo di Format Painter una volta**
 Se gli sviluppatori desiderano utilizzare la funzionalità di format painter solo una volta per applicare le impostazioni di formattazione di una cella focalizzata a una singola cella, possono farlo chiamando**StartFormatPainter** metodo e passando a**falso** valore ad esso. Questo**falso** value proibirà per sempre al format painter di dipingere.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **Usare Copia formato sempre**
Usare format painter è sempre una caratteristica utile quando abbiamo bisogno di applicare le impostazioni di formattazione su più di una cella. Gli sviluppatori possono ottenere questa funzione semplicemente chiamando**StartFormatPainter** metodo e passando a**VERO** valore ad esso.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


 Questo tipo di pittore di formati continua a dipingere per sempre a meno che non lo fermiamo. Quindi, per impedire sempre al format painter di dipingere, possiamo semplicemente chiamare**EndFormatPainter** metodo di**GrigliaDesktop**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
