---
title: La tua prima domanda Aspose.Cells - Hello World
type: docs
weight: 30
url: /it/net/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

Questo tutorial mostra come creare una primissima applicazione (Hello World) utilizzando Aspose.Cells' semplice API. Questa semplice applicazione crea un file Excel Microsoft con il testo 'Hello World' in una cella del foglio di lavoro specificata.

{{% /alert %}}

## **Creazione dell'applicazione Hello World**

I passaggi seguenti creano l'applicazione Hello World utilizzando Aspose.Cells API:

1.  Crea un'istanza di[Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe.
1.  Se hai una licenza, allora[applicarlo](/cells/it/net/licensing/).
 Se stai utilizzando la versione di valutazione, salta le righe di codice relative alla licenza.
1. Crea un nuovo file Excel o apri un file Excel esistente.
1. Accedi a qualsiasi cella desiderata di un foglio di lavoro nel file Excel.
1.  Inserisci le parole**Hello World!** in una cella a cui si accede.
1. Genera il file Excel Microsoft modificato.

L'implementazione dei passaggi precedenti è dimostrata negli esempi seguenti.

### **Esempio di codice: creazione di una nuova cartella di lavoro**

L'esempio seguente crea una nuova cartella di lavoro da zero, scrive Hello World! nella cella A1 del primo foglio di lavoro e salva il file Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Esempio di codice: apertura di un file esistente**

L'esempio seguente apre un file modello Excel Microsoft esistente denominato "Sample.xlsx", input "Hello World!" testo nella cella A1 nel primo foglio di lavoro e salva la cartella di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
