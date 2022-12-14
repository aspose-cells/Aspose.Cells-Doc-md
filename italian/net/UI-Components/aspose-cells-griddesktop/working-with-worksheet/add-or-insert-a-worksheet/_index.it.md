---
title: Aggiungi o inserisci un foglio di lavoro
type: docs
weight: 20
url: /it/net/add-or-insert-a-worksheet/
---
{{% alert color="primary" %}} 

In questo argomento verranno illustrate le tecniche per aggiungere o inserire fogli di lavoro in un file Excel utilizzando Aspose.Cells.GridDesktop. La differenza tra l'aggiunta e l'inserimento di fogli di lavoro è che, inoltre, un foglio di lavoro viene semplicemente aggiunto alla fine della raccolta di fogli di lavoro del file Excel, tuttavia l'inserimento significa aggiungere un foglio di lavoro in una posizione specifica nella raccolta di fogli di lavoro.

{{% /alert %}} 
## **Aggiunta di un foglio di lavoro**
Per aggiungere un foglio di lavoro utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

1. Aggiungere il controllo Aspose.Cells.GridDesktop a un modulo.
1. Chiamare il metodo Add della raccolta Worksheet nel controllo GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Sono disponibili molte versioni di overload del metodo Add. Utilizzando la versione sovraccaricata sopra, ad esempio, un foglio di lavoro viene aggiunto al file Excel con un nome di foglio predefinito. Usando altre versioni di overload del metodo Add, è possibile definire il nome come mostrato di seguito nell'esempio.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **Inserimento di un foglio di lavoro**
Per inserire un foglio di lavoro utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

1. Aggiungere il controllo Aspose.Cells.GridDesktop a un form.
1. Chiamare il metodo Insert della raccolta Worksheets nel controllo GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Microsoft Excel (97-2003 XLS) supporta fogli Excel con un massimo di 65.536 righe e 256 colonne. Aspose.Cells.GridDesktop segue gli stessi standard. Nel controllo Aspose.Cells.GridDesktop, gli sviluppatori possono aggiungere o inserire fogli di lavoro con più righe e colonne rispetto al limite standard, ma quando tentano di salvare i dati Grid in un file Excel, verrà generata un'eccezione. Significa che solo i dati contenuti nelle 65.536 righe e 256 colonne possono essere salvati in un file XLS di Excel utilizzando Aspose.Cells.GridDesktop, se si utilizza il formato di file XLSX (MS Excel 2007/2010), tuttavia non esiste tale limitazione.

{{% /alert %}}
