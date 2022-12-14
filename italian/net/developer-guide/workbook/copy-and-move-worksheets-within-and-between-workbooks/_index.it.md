---
title: Copia e sposta i fogli di lavoro all'interno e tra le cartelle di lavoro
type: docs
weight: 80
url: /it/net/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

volte, hai bisogno di un numero di fogli di lavoro con formattazione e immissione dati comuni. Ad esempio, se lavori con budget trimestrali, potresti voler creare una cartella di lavoro con fogli che contengono le stesse intestazioni di colonna, intestazioni di riga e formule. C'è un modo per farlo: creando un foglio e poi copiandolo tre volte.

Aspose.Cells supporta la copia o lo spostamento di fogli di lavoro all'interno o tra cartelle di lavoro. Fogli di lavoro inclusi dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti vengono copiati con il massimo grado di precisione.

{{% /alert %}}

## **Copiare e spostare fogli di lavoro**

### **Copia di un foglio di lavoro all'interno di una cartella di lavoro**

I passaggi iniziali sono gli stessi per tutti gli esempi.

1. Crea due cartelle di lavoro con alcuni dati in Microsoft Excel. Ai fini di questo esempio, abbiamo creato due nuove cartelle di lavoro in Microsoft Excel e inserito alcuni dati nei fogli di lavoro.

- FirstWorkbook.xlsx (3 fogli di lavoro).
- SecondWorkbook.xlsx (1 foglio di lavoro).

1. Scarica e installa Aspose.Cells:
   1. [Scarica Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. Installalo sul tuo computer di sviluppo.
 Tutto[Aspose](http://www.aspose.com/) i componenti, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e si limita a inserire filigrane nei documenti prodotti.
1. Crea un progetto:
 1. Avviare Visual Studio.Net.
 1. Creare una nuova applicazione console.
1. Aggiungi riferimenti:
 1. Aggiungere al progetto un riferimento a Aspose.Cells.
 Ad esempio, aggiungi un riferimento a ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Copia il foglio di lavoro all'interno di una cartella di lavoro
 Il primo esempio copia il primo foglio di lavoro (Copia) all'interno di FirstWorkbook.xlsx.

Quando si esegue il codice, il foglio di lavoro denominato Copy viene copiato all'interno di FirstWorkbook.xlsx con il nome Last Sheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **Spostamento di un foglio di lavoro all'interno di una cartella di lavoro**

Il codice seguente mostra come spostare un foglio di lavoro da una posizione in una cartella di lavoro a un'altra. L'esecuzione del codice sposta il foglio di lavoro denominato Sposta dall'indice 1 all'indice 2 in FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **Copia di un foglio di lavoro tra cartelle di lavoro**

L'esecuzione del codice copia il foglio di lavoro denominato Copy is in SecondWorkbook.xlsx con il nome Sheet2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **Spostare un foglio di lavoro tra cartelle di lavoro**

L'esecuzione del codice sposta il foglio di lavoro denominato Sposta da FirstWorkbook.xlsx a SecondWorkbook.xlsx con il nome Sheet3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
