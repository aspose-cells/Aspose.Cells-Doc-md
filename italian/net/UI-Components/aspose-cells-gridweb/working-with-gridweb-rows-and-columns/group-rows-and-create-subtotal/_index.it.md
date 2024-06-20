---
title: Raggruppare righe e creare subtotali
type: docs
weight: 70
url: /it/net/aspose-cells-gridweb/group-rows-and-create-subtotal/
keywords: GridWeb,subtotal,group,ungroup
description: Questo articolo introduce come raggruppare/suddividere righe/colonne e come lavorare con il subtotali in GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb può creare un sommario per i tuoi dati. Ciò ti consente di mostrare e nascondere livelli di dettaglio facendo clic sui simboli di sommario "+" e "-" per visualizzare solo le righe che forniscono riepiloghi o intestazioni per le sezioni in un foglio di lavoro. È possibile utilizzare i simboli per visualizzare i dettagli sotto un singolo riepilogo o intestazione.

Quando si raggruppano le righe, è importante selezionare solo le righe di dettaglio che compongono il gruppo. Non includere la riga di riepilogo correlata. Ad esempio, se la riga 6 contiene totali per i dati dalla riga 3 alla 5, selezionare solo dalla riga 3 alla 5 per definire il gruppo. Il controllo di Aspose.Cells.GridWeb visualizza i simboli **mostra dettagli** (+) e **nascondi dettagli** (-) accanto alle intestazioni di riga specificando i gruppi nel foglio di lavoro.

Aspose.Cells.GridWeb consente anche di creare subtotali basati su qualsiasi campo di dati. Un subtotali non è necessariamente una somma: può essere una media, conteggio, minimo, massimo o altro calcolo statistico.

Questo argomento discute il raggruppamento delle righe e la creazione dei subtotali utilizzando l'API di Aspose.Cells.GridWeb. Gli sviluppatori possono raggruppare le righe con qualsiasi livello di annidamento e creare subtotali facilmente.

{{% /alert %}} 
## **Raggruppamento righe**
Per raggruppare un numero specifico di righe:

1. Aggiungi il controllo Aspose.Cells.GridWeb a un modulo Web.
1. Accedi a un foglio di lavoro.
1. Seleziona il numero desiderato di celle nelle righe.
1. Raggruppa le righe.

Quando le righe sono raggruppate, viene visualizzato un pulsante di espansione/contrazione in cima alla riga di sommario delle righe. È possibile modificare l'impostazione di direzione. La proprietà Booleana WebWorksheet.IsSummaryRowBelow è un Booleano. Impostalo su false (predefinito) e la riga di sommario sarà sopra le righe di dettaglio. Impostalo su true e la riga di sommario sarà sotto le righe di dettaglio. Fai clic sul pulsante di espansione o contrazione per espandere o contrarre le righe raggruppate.

Nell'esempio seguente vengono raggruppate le righe dalla 2a alla 10a riga.

**Raggruppamento righe** 

![todo:image_alt_text](group-rows-and-create-subtotal_1.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **Raggruppamento nidificato di righe**
È possibile creare livelli di organizzazione durante il raggruppamento di un insieme di righe. È possibile raggruppare righe tra le righe già raggruppate. Nell'esempio seguente vengono mostrate righe raggruppate nidificate.

**Raggruppamento righe** 

![todo:image_alt_text](group-rows-and-create-subtotal_2.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **Processo interno: Come funziona il controllo?**
Ogni riga del foglio ha un numero di struttura. Il valore predefinito del numero di struttura è zero. Ogni volta che si raggruppano le righe, il numero di struttura aumenta di 1. È possibile ottenere il numero di struttura chiamando il metodo GridWorksheet.Cells.GetRowOutlineLevel().
## **Annulla raggruppamento righe**
Aspose.Cells.GridWeb ti consente di annullare il raggruppamento delle righe.

Per annullare il raggruppamento di un numero specifico di righe:

1. Seleziona un numero di celle nelle righe del foglio di lavoro da annullare.
1. Annulla il raggruppamento delle righe.

Nell'esempio seguente vengono annullate le righe dalla 2a alla 10a riga.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

Quando si chiama il metodo GridWorksheet.Cells.UngroupRows(), il numero di struttura delle righe raggruppate viene impostato a zero.

{{% /alert %}} 
## **Creazione subtotali**
La funzionalità subtotale del controllo può raggruppare le righe nel foglio con una colonna specificata e calcolare il riepilogo delle colonne. Aspose.Cells.GridWeb può calcolare automaticamente i valori subtotali per un elenco. Quando si implementano i subtotali, il controllo evidenzia l'elenco in modo da poter visualizzare e nascondere le righe di dettaglio per ciascun totale parziale. Prima di aggiungere i subtotali, ordinare sul campo su cui si desidera fare il totale parziale. Per creare i subtotali, utilizzare qualsiasi versione del metodo sovraccaricato WebWorksheet.CreateSubtotal.



{{< highlight java >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[] subtotalColumnIndexList

);

{{< /highlight >}}
### **Elenco dei parametri**

|**No.**|**Nome parametro**|**Descrizione**|
| :- | :- | :- |
|1|columnNameRowIndex| Indice di riga della riga del nome della colonna.|
| 2|dataRows| Il numero delle righe dati.|
| 3|groupByColumnIndex| L'indice di colonna della colonna da raggruppare.|
| 4|subtotalFunction| L'enumerazione del tipo di funzione parziale.|
| 5|subtotalColumnIndexList| Gli indici di colonna da sottoporre a totale parziale.|
### **Elenco delle funzioni di riepilogo**
Esistono diversi tipi di funzioni di riepilogo supportate dall'enumerazione {[SubtotalFunction}}:

|**No.**|**Nome funzione**|**Descrizione**|
| :- | :- | :- |
| 1|AVERAGE| Calcola la media dei valori.|
| 2|COUNT| Conta i valori numerici nelle celle.|
| 3|COUNTA| Conta i dati non numerici nelle celle.|
| 4|MAX| Calcola il valore più grande.|
| 5|MIN| Calcola il valore più piccolo.|
| 6|PRODUCT| Calcola il prodotto dei valori.|
| 7|SUM| Calcola la somma dei valori.|
L'esempio seguente genera i subtotali che calcolano i valori non numerici raggruppati dalla seconda colonna nel foglio di lavoro.

**Subtotali** 

![todo:image_alt_text](group-rows-and-create-subtotal_3.png)



{{< highlight java >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[] { 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **Rimozione del subtotale**
Per rimuovere un subtotale, utilizzare il metodo WebWorksheet.RemoveSubtotal. Nell'esempio seguente vengono rimossi i subtotali.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **Informazioni sulla funzione SUBTOTALE**
Il controllo GridWeb fa uso della funzione di formula SUBTOTALE per calcolare il valore del subtotale.

Sintassi: SUBTOTALE(numero_funzione, ref1, ref2, ...)

La funzione_num è un numero che specifica il tipo di funzione utilizzata nel calcolo del subtotale.

|**1**|**MEDIA**|
| :- | :- |
|2|COUNT|
|3|COUNTA|
|4|MAX|
|5|MIN|
|6|PRODUCT|
|7|SUM|
ref1, ref2, sono le aree da sottoporre a subtotali. Se ref1, ref2, ... contengono altre funzioni di subtotale, le celle referenziate vengono ignorate per evitare il calcolo duplicato.
