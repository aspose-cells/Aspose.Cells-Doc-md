---
title: Aggiungi o inserisci un foglio di lavoro
type: docs
weight: 20
url: /it/net/aspose-cells-griddesktop/add-or-insert-a-worksheet/
keywords: GridDesktop,inserisci,foglio di lavoro,inserisci foglio di lavoro
description: Questo articolo introduce come aggiungere o inserire un foglio di lavoro in GridDesktop.
---

{{% alert color="primary" %}} 

In questo argomento, discuteremo le tecniche per aggiungere o inserire fogli di lavoro in un file Excel utilizzando Aspose.Cells.GridDesktop. La differenza tra aggiungere e inserire fogli di lavoro è che inoltre, un foglio di lavoro viene semplicemente aggiunto alla fine della raccolta dei fogli di lavoro del file Excel, mentre l'inserimento significa aggiungere un foglio di lavoro in una posizione specifica nella raccolta dei fogli di lavoro.

{{% /alert %}} 
## **Aggiunta di un Foglio di Lavoro**
Per aggiungere un foglio di lavoro utilizzando Aspose.Cells.GridDesktop, seguire i passaggi di seguito:

1. Aggiungi il controllo Aspose.Cells.GridDesktop a un modulo.
1. Chiama il metodo Aggiungi della raccolta di fogli di lavoro nel controllo GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Sono disponibili molte versioni sovraccaricate del metodo Aggiungi. Utilizzando la versione sovraccarica sopra, ad esempio, viene aggiunto un foglio di lavoro al file Excel con un nome predefinito. Utilizzando altre versioni sovraccaricate del metodo Aggiungi, è possibile definire il nome come mostrato di seguito nell'esempio.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **Inserimento di un foglio di lavoro**
Per inserire un foglio di lavoro utilizzando Aspose.Cells.GridDesktop, seguire i passaggi di seguito:

1. Aggiungere il controllo Aspose.Cells.GridDesktop a un modulo.
1. Chiama il metodo Inserisci della raccolta di fogli di lavoro nel controllo GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Microsoft Excel (97-2003 XLS) supporta fogli di Excel con fino a 65.536 righe e 256 colonne. Aspose.Cells.GridDesktop segue gli stessi standard. Nel controllo Aspose.Cells.GridDesktop, gli sviluppatori possono aggiungere o inserire fogli di lavoro con più righe e colonne rispetto al limite standard, ma quando cercano di salvare i dati della griglia in un file Excel, verrà generata un'eccezione. Ciò significa che solo i dati contenuti nelle 65.536 righe e 256 colonne possono essere salvati in un file Excel XLS utilizzando Aspose.Cells.GridDesktop, se si utilizza il formato di file XLSX (MS Excel 2007/2010), non c'è tale limitazione.

{{% /alert %}}
