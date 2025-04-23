---
title: Copiare e Spostare Fogli di Lavoro All interno e Tra Workbooks
type: docs
weight: 80
url: /it/python-net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

A volte è necessario un numero di fogli di lavoro con formattazione comune e inserimento dati. Ad esempio, se lavori con i bilanci trimestrali, potresti voler creare un foglio con fogli che contengono gli stessi titoli di colonna, titoli di riga e formule. C'è un modo per farlo: creando un foglio e poi copiandolo tre volte.

Aspose.Cells per Python via .NET supporta la copia o lo spostamento di fogli di lavoro all’interno o tra workbook. I fogli di lavoro, inclusi dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti, vengono copiati con il massimo livello di precisione.

{{% /alert %}}

## **Copia e Sposta Fogli di Lavoro**

### **Copiare un foglio di lavoro all'interno di un libro di lavoro**

I passaggi iniziali sono gli stessi per tutti gli esempi.

1. Creare due libri di lavoro con alcuni dati in Microsoft Excel. A fini di questo esempio, abbiamo creato due nuovi libri di lavoro in Microsoft Excel e inserito alcuni dati nei fogli di lavoro.

- FirstWorkbook.xlsx (3 fogli di lavoro).
- SecondWorkbook.xlsx (1 foglio di lavoro).

1. Scarica e installa Aspose.Cells for Python via .NET:
   1. [Scarica Aspose.Cells per Python via .NET](https://downloads.aspose.com/cells/python-net).
   1. Installalo sul tuo computer di sviluppo.
      Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.
1. Crea un progetto e aggiungi riferimenti:   
1. Copia il foglio di lavoro all'interno di un workbook
   Il primo esempio copia il primo foglio di lavoro (Copia) all'interno di FirstWorkbook.xlsx.

Quando si esegue il codice, il foglio di lavoro chiamato Copia viene copiato all'interno di FirstWorkbook.xlsx con il nome Ultimo foglio.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheets.py" >}}

### **Spostamento di un foglio di lavoro all'interno di un workbook**

Il codice sottostante mostra come spostare un foglio di lavoro da una posizione all'interno di un workbook a un'altra. Eseguendo il codice sposta il foglio di lavoro chiamato Spostare dall'indice 1 all'indice 2 in FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheets.py" >}}

### **Copia un Foglio di Lavoro tra i Workbooks**

Eseguendo il codice viene copiato il foglio di lavoro chiamato Copia in SecondWorkbook.xlsx con il nome Foglio2.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.py" >}}

### **Spostare un foglio di lavoro tra i Workbooks**

Eseguendo il codice sposta il foglio di lavoro chiamato Spostare da FirstWorkbook.xlsx a SecondWorkbook.xlsx con il nome Foglio3.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.py" >}}
