---
title: Copia e sposta fogli di lavoro all’interno e tra i workbook con Golang tramite C++
linktitle: Copia e sposta fogli di lavoro
type: docs
weight: 80
url: /it/go-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Impara come copiare e spostare fogli di lavoro all’interno e tra i workbook Excel utilizzando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte è necessario avere più fogli di lavoro con formattazione e inserimento dati comuni. Ad esempio, se lavori con budget trimestrali, potresti voler creare un workbook con fogli che contengono gli stessi intestazioni di colonna, intestazioni di riga e formule. Esiste un modo per farlo: creando un foglio e poi copiandolo più volte.

Aspose.Cells supporta la copia o lo spostamento dei fogli di lavoro all'interno o tra i workbook. I fogli di lavoro, compresi dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti, vengono copiati con il massimo grado di precisione.

{{% /alert %}}

## **Copia e Sposta Fogli di Lavoro**

### **Copiare un foglio di lavoro all'interno di un libro di lavoro**

I passaggi iniziali sono gli stessi per tutti gli esempi:

1. Crea due workbook con alcuni dati in Microsoft Excel. Per questo esempio, abbiamo creato due nuovi workbook in Excel e inserito alcuni dati nei fogli:
   - FirstWorkbook.xlsx (3 fogli di lavoro)
   - SecondWorkbook.xlsx (1 foglio di lavoro)

1. Scarica e installa Aspose.Cells:
   1. [Scarica Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/)
   1. Installa sul computer di sviluppo

1. Crea un progetto:
   1. Crea un nuovo progetto C++ nel tuo IDE preferito

1. Aggiungi riferimenti:
   1. Aggiungi la libreria Aspose.Cells for C++ al tuo progetto

1. Copia il foglio di lavoro all'interno di un workbook
   Il primo esempio copia il primo foglio di lavoro (Copia) all'interno di FirstWorkbook.xlsx.

Quando si esegue il codice, il foglio di lavoro chiamato Copia viene copiato all'interno di FirstWorkbook.xlsx con il nome Ultimo foglio.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks.go" >}}
### **Spostamento di un foglio di lavoro all'interno di un workbook**

Il codice sottostante mostra come spostare un foglio di lavoro da una posizione all'interno di un workbook a un'altra. Eseguendo il codice sposta il foglio di lavoro chiamato Spostare dall'indice 1 all'indice 2 in FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-1.go" >}}
### **Copia un Foglio di Lavoro tra i Workbooks**

Eseguendo il codice, viene copiato il foglio di lavoro chiamato Copy in SecondWorkbook.xlsx con il nome Sheet2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-2.go" >}}
### **Spostare un foglio di lavoro tra i Workbooks**

Eseguendo il codice sposta il foglio di lavoro chiamato Spostare da FirstWorkbook.xlsx a SecondWorkbook.xlsx con il nome Foglio3.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-3.go" >}}
