---
title: Rimuovi un foglio di lavoro
type: docs
weight: 30
url: /it/net/remove-a-worksheet/
---
{{% alert color="primary" %}} 

In questo argomento viene illustrata la rimozione dei fogli di lavoro tramite il controllo Aspose.Cells.GridDesktop. Esistono alcuni semplici approcci per eseguire questo compito di base.

{{% /alert %}} 
## **Rimozione di un foglio di lavoro**
Per rimuovere un foglio di lavoro utilizzando il controllo Aspose.Cells.GridDesktop, procedi nel seguente modo:

1. Aggiungere il controllo Aspose.Cells.GridDesktop a un form.
1. Chiamare il metodo Remove dell'insieme Worksheets nel controllo GridDesktop.
### **Utilizzo dell'indice del foglio di lavoro**
In questo approccio, passa semplicemente l'indice del foglio di lavoro (nella raccolta dei fogli di lavoro della griglia) del foglio di lavoro da rimuovere.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Utilizzo del nome del foglio di lavoro**
Se il nome del foglio di lavoro è noto, è possibile rimuovere un foglio di lavoro specifico specificandone il nome.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Rimuovi è un metodo. Usalo per rimuovere un foglio di lavoro usando il suo indice (nella raccolta dei fogli di lavoro) o usa il metodo RemoveAt per rimuovere il foglio di lavoro usando il suo indice/nome.

{{% /alert %}}
