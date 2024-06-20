---
title: Usa il copia formato
type: docs
weight: 80
url: /it/net/aspose-cells-griddesktop/use-format-painter/
keywords: GridDesktop,format painter
description: Questo articolo introduce il copia formato in GridDesktop.
---

{{% alert color="primary" %}} 

Copia formato è la funzione di MS Excel che è stata adattata in Aspose.Cells.GridDesktop. È una funzione molto utile. Per coloro che non hanno ancora utilizzato questa funzionalità, il copia formato consente agli utenti di applicare le impostazioni di formattazione di qualsiasi cella focalizzata su un'altra cella. L'implementazione di questa funzionalità è molto semplice. In questo argomento ne parleremo anche.

{{% /alert %}} 
## **Utilizzo del copia formato**
La funzionalità del **Copia formato** richiede agli utenti di selezionare una cella le cui impostazioni di formattazione si desidera applicare ad altre celle e quindi chiamare il metodo **StartFormatPainter** di **GridDesktop**. Ci sono due modalità di copia formato come segue:

- **Utilizzo del copia formato una volta**
- **Utilizzo del copia formato sempre**
### **Utilizzo del copia formato una volta**
Se gli sviluppatori vogliono utilizzare la funzionalità del formato pittore solo una volta per applicare le impostazioni di formattazione di una cella focalizzata a una singola cella, possono farlo chiamando il metodo **StartFormatPainter** e passando un valore **false** ad esso. Questo valore **false** impedirà al formato pittore di dipingere per sempre.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **Usare sempre il formato pittore**
Utilizzare sempre il formato pittore è una funzionalità utile quando abbiamo bisogno di applicare le impostazioni di formattazione su più di una cella. Gli sviluppatori possono ottenere questa funzionalità chiamando semplicemente il metodo **StartFormatPainter** e passando un valore **true** ad esso.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


Questo tipo di formato pittore continua a dipingere per sempre a meno che non lo fermiamo. Quindi, per impedire al formato pittore di dipingere sempre, possiamo semplicemente chiamare il metodo **EndFormatPainter** di **GridDesktop**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
