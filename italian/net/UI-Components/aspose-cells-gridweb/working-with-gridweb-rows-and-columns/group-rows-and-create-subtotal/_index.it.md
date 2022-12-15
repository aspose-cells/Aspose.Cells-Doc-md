---
title: Raggruppa righe e crea subtotale
type: docs
weight: 70
url: /it/net/group-rows-and-create-subtotal/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb può creare uno schema per i tuoi dati. Ciò consente di mostrare e nascondere i livelli di dettaglio facendo clic sui simboli di contorno "+" e "-" per visualizzare solo le righe che forniscono riepiloghi o intestazioni per le sezioni in un foglio di lavoro. È possibile utilizzare i simboli per visualizzare i dettagli sotto un singolo riepilogo o titolo.

 Quando si raggruppano le righe, è importante selezionare solo le righe di dettaglio che compongono il gruppo. Non includere la riga di riepilogo correlata. Ad esempio, se la riga 6 contiene i totali per i dati nelle righe da 3 a 5, selezionare solo le righe da 3 a 5 per definire il gruppo. Il controllo Aspose.Cells.GridWeb visualizza il**mostra i dettagli** (+) e**nascondere dettaglio** (-) simboli accanto alle intestazioni di riga che specificano i gruppi nel foglio di lavoro.

Aspose.Cells.GridWeb consente inoltre di creare subtotali basati su qualsiasi campo di dati. Un subtotale non è necessariamente una somma: può essere una media, un conteggio, un minimo, un massimo o un altro calcolo statistico.

Questo argomento illustra il raggruppamento di righe e la creazione di subtotali tramite l'API Aspose.Cells.GridWeb. Gli sviluppatori possono raggruppare righe con qualsiasi livello di nidificazione e creare facilmente subtotali.

{{% /alert %}} 
## **Raggruppamento di righe**
Per raggruppare un numero specifico di righe:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un Web Form.
1. Accedi a un foglio di lavoro.
1. Seleziona il numero desiderato di celle nelle righe.
1. Raggruppa le righe.

Quando le righe sono raggruppate, viene visualizzato un pulsante espandi/comprimi nella parte superiore della riga di riepilogo delle righe. È possibile modificare l'impostazione della direzione. La proprietà WebWorksheet.IsSummaryRowBelow è una proprietà booleana. Impostalo su false (predefinito) e la riga di riepilogo sarà sopra le righe di dettaglio. Impostalo su true e la riga di riepilogo sarà sotto le righe di dettaglio. Fare clic sul pulsante Espandi/Comprimi per espandere o comprimere le righe raggruppate.

L'esempio seguente raggruppa le righe dalla seconda alla decima riga.

**Righe di raggruppamento** 

![cose da fare:immagine_alt_testo](group-rows-and-create-subtotal_1.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **Nidificazione di righe raggruppate**
Puoi creare livelli di organizzazione mentre raggruppi un insieme di righe. È possibile raggruppare le righe tra le righe raggruppate. L'esempio seguente mostra l'annidamento di righe raggruppate.

**Righe di raggruppamento** 

![cose da fare:immagine_alt_testo](group-rows-and-create-subtotal_2.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **Processo interno: come funziona il controllo?**
Ogni riga del foglio ha un numero di contorno. Il valore predefinito del numero di struttura è zero. Ogni volta che si raggruppano le righe, il numero di struttura viene aumentato di 1. È possibile ottenere il numero di struttura chiamando il metodo GridWorksheet.Cells.GetRowOutlineLevel().
## **Separa righe**
Aspose.Cells.GridWeb consente di separare le righe raggruppate.

Per separare un numero specifico di righe:

1. Selezionare un numero di celle nelle righe del foglio di lavoro da separare.
1. Separa le righe.

L'esempio seguente separa le righe dalla seconda alla decima riga.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

Quando si chiama il metodo GridWorksheet.Cells.UngroupRows(), il numero di struttura delle righe raggruppate viene impostato su zero.

{{% /alert %}} 
## **Creazione di subtotale**
La funzione di totale parziale del controllo può raggruppare le righe nel foglio con una colonna specificata e calcolare il riepilogo delle colonne. Aspose.Cells.GridWeb può calcolare automaticamente i valori subtotali per un elenco. Quando si implementano i totali parziali, il controllo delinea l'elenco in modo da poter visualizzare e nascondere le righe di dettaglio per ogni totale parziale. Prima di aggiungere i subtotali, ordina in base al campo su cui desideri eseguire il subtotale. Per creare totali parziali, utilizzare qualsiasi versione del metodo WebWorksheet.CreateSubtotal sottoposto a overload.



{{< highlight "java" >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[]subtotalColumnIndexList

);

{{< /highlight >}}
### **Elenco dei parametri**

|**No.**|**Nome parametro**|**Descrizione**|
|:- |:- |:- |
|1|columnNameRowIndex|L'indice di riga della riga del nome di colonna.|
|2|dataRows|Il numero delle righe di dati.|
|3|groupByColumnIndex|L'indice di colonna della colonna da raggruppare.|
|4|subtotaleFunzione|L'enumerazione del tipo di funzione subtotale.|
|5|subtotaleColumnIndexList|Gli indici di colonna di cui eseguire il subtotale.|
### **Elenco delle funzioni di riepilogo**
Esistono diversi tipi di funzioni di riepilogo supportate dall'enumerazione {[SubtotalFunction}}:

|**No.**|**Nome funzione**|**Descrizione**|
|:- |:- |:- |
|1|MEDIA|Calcola la media dei valori.|
|2|CONTARE|Conta i valori numerici nelle celle.|
|3|CONTA|Conta i dati non numerici nelle celle.|
|4|MASSIMO|Calcola il valore più grande.|
|5|MIN|Calcola il valore più piccolo.|
|6|PRODOTTO|Calcola il prodotto dei valori.|
|7|SOMMA|Calcola la somma dei valori.|
L'esempio seguente genera i subtotali che calcolano i valori non numerici raggruppati in base alla seconda colonna del foglio di lavoro.

**Subtotali** 

![cose da fare:immagine_alt_testo](group-rows-and-create-subtotal_3.png)



{{< highlight "java" >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[]{ 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **Rimozione del subtotale**
Per rimuovere un totale parziale, utilizzare il metodo WebWorksheet.RemoveSubtotal. L'esempio seguente rimuove i subtotali.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **Informazioni sulla funzione SUBTOTALE**
Il controllo GridWeb utilizza la funzione formula SUBTOTAL per calcolare il valore del subtotale.

Sintassi: SUBTOTALE(num_funzione, ref1, ref2, ...)

function_num è un numero che specifica il tipo di funzione utilizzata nel calcolo del subtotale.

|**1**|**MEDIA**|
|:- |:- |
|2|CONTARE|
|3|CONTA|
|4|MASSIMO|
|5|MIN|
|6|PRODOTTO|
|7|SOMMA|
ref1, ref2, sono le aree da subtotare. Se ref1, ref2, ... contengono altre funzioni di subtotale, le celle di riferimento vengono ignorate per evitare calcoli duplicati.
