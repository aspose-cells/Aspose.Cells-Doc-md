---
title: Lavorare con i fogli di lavoro GridWeb
type: docs
weight: 30
url: /it/java/working-with-worksheets-gridweb/
---
## **Accesso ai fogli di lavoro**

Questo argomento illustra l'accesso ai fogli di lavoro del controllo GridWeb. Possiamo anche chiamare questi fogli di lavoro fogli di lavoro Web perché appartengono a GridWeb e vengono utilizzati nelle applicazioni Web.

Tutti i fogli di lavoro contenuti nel controllo GridWeb vengono archiviati in un oggetto GridWorksheetCollection del controllo GridWeb. È semplice accedere a un particolare foglio di lavoro tramite il relativo indice del foglio.

Gli sviluppatori possono accedere a un foglio di lavoro specifico specificandone l'indice del foglio, come illustrato di seguito nel frammento di codice di esempio.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **Rimozione di un foglio di lavoro**

In questo argomento vengono fornite brevi informazioni sulla rimozione dei fogli di lavoro dai file Excel Microsoft utilizzando GridWeb API. Rimuovere un foglio di lavoro specificandone l'indice del foglio.

Gli sviluppatori possono rimuovere un foglio di lavoro specifico specificandone l'indice del foglio utilizzando il metodo removeAt della raccolta GridWorksheetCollection, come illustrato di seguito nel frammento di codice di esempio.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **Aggiunta di fogli di lavoro**

I fogli di lavoro sono parte integrante di GridWeb. Tutti i dati vengono gestiti e archiviati sotto forma di fogli di lavoro. GridWeb consente agli sviluppatori di aggiungere uno o più fogli di lavoro al controllo Aspose.Cells.GridWeb. Questo argomento illustra approcci semplici per l'aggiunta di fogli di lavoro a GridWeb.

### **Senza specificare il nome del foglio**

Il modo più semplice per aggiungere un foglio di lavoro a Aspose.Cells.GridWeb consiste nel chiamare il metodo add della classe GridWorksheetCollection nel controllo GridWeb. Questo crea fogli di lavoro che utilizzano nomi predefiniti (ovvero Foglio1, Foglio2, Foglio3 e così via) e li aggiunge al controllo GridWeb.

**Output: un foglio di lavoro con nome predefinito è stato aggiunto a GridWeb** 

![cose da fare:immagine_alt_testo](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **Con il nome del foglio specificato**

Per aggiungere un foglio di lavoro con un nome specifico al controllo GridWeb anziché utilizzare lo schema di denominazione predefinito, chiamare una versione di overload del metodo add che accetta la stringa specificata SheetName. Ad esempio, l'esempio seguente aggiunge un foglio di lavoro denominato Invoice.

**Output: un foglio di lavoro con un nome specificato è stato aggiunto a GridWeb** 

![cose da fare:immagine_alt_testo](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

 Il metodo add() restituisce l'indice del nuovo foglio di lavoro che può essere utilizzato per accedere all'istanza di questo foglio di lavoro. Per maggiori dettagli su come accedere ai fogli di lavoro, leggi[Accesso ai fogli di lavoro](/cells/it/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Rinominare un foglio di lavoro**

Rinominare un foglio di lavoro può essere molto utile quando si lavora con molti fogli di lavoro in GridWeb e si decide di cambiarne i nomi per renderli più significativi. Ad esempio, un foglio di lavoro contenente una fattura può essere rinominato Fattura anziché Foglio1. Questo argomento descrive questa funzione semplice ma utile.

### **Rinominare un foglio di lavoro**

Tutti i fogli di lavoro contengono una proprietà Name che consente agli sviluppatori di accedere o modificare i nomi dei fogli di lavoro. Per rinominare un foglio di lavoro:

1. Accedere a un foglio di lavoro da GridWorksheetCollection.
1. Rinominare il foglio di lavoro selezionato.

{{% alert color="primary" %}}

 Per maggiori dettagli su come accedere ai fogli di lavoro in Aspose.Cells.GridWeb, fare riferimento a[Accesso ai fogli di lavoro](/cells/it/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

Prima di eseguire il codice, il foglio di lavoro ha un nome predefinito, ad esempio Foglio1.

**File di input: un foglio di lavoro con un nome predefinito Foglio1** 

![cose da fare:immagine_alt_testo](working-with-worksheets-gridweb_3.png)

Dopo aver eseguito il codice, il foglio di lavoro viene rinominato Invoice.

**Output: il foglio di lavoro viene rinominato Fattura** 

![cose da fare:immagine_alt_testo](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **Copiare un foglio di lavoro**

[Aggiunta di fogli di lavoro](/cells/it/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)descrive come aggiungere nuovi fogli di lavoro a GridWeb. È anche possibile aggiungere una copia (o replica) di un altro foglio di lavoro al controllo Aspose.Cells.GridWeb. Questa funzione può essere utile quando dati identici o simili in un foglio di lavoro sono richiesti anche in un altro foglio di lavoro. In tal caso, è più semplice copiare un foglio di lavoro esistente e aggiungerlo a Aspose.Cells.GridWeb come nuovo foglio di lavoro anziché crearlo da zero.

### **Utilizzo dell'indice del foglio**

Il codice di esempio seguente mostra come aggiungere una copia di un foglio di lavoro al controllo GridWeb specificando l'indice del foglio di lavoro nel metodo addCopy di GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **Utilizzo del nome del foglio**
Il codice di esempio seguente mostra come aggiungere una copia di un foglio di lavoro al controllo GridWeb specificando il nome del foglio di lavoro nel metodo addCopy di GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

 Il metodo addCopy restituisce l'indice del foglio di lavoro appena aggiunto che può essere utilizzato per accedere all'istanza del foglio di lavoro. Per maggiori dettagli su come accedere ai fogli di lavoro, leggi[Accesso ai fogli di lavoro](/cells/it/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Utilizzo di intervalli denominati**

Normalmente, le etichette di colonna e riga vengono utilizzate per fare riferimento in modo univoco alle celle. Ma puoi creare nomi descrittivi per rappresentare celle, intervalli di celle, formule o valori costanti.

 La parola**nome** può fare riferimento a una stringa di caratteri che rappresenta una cella, un intervallo di celle, una formula o un valore costante. Ad esempio, utilizza nomi di facile comprensione, come Prodotti, per fare riferimento a intervalli di difficile comprensione, come Vendite!C20:C30.

 Le etichette possono essere utilizzate in formule che fanno riferimento a dati sullo stesso foglio di lavoro; se vuoi rappresentare un intervallo su un altro foglio di lavoro, puoi usare un nome.**Intervalli denominati** è una delle funzionalità più potenti di Microsoft Excel.

Gli utenti possono assegnare un nome a un intervallo e utilizzare tale nome nelle formule. Aspose.Cells.GridWeb supporta questa funzione.

### **Aggiunta/riferimento a intervalli denominati nelle formule**

Il controllo GridWeb fornisce due classi (GridName e GridNameCollection) per lavorare con intervalli denominati.

Il seguente frammento di codice ti aiuterà a capire come usarli.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **Gestione dei commenti nel foglio di lavoro**

Questo argomento illustra l'aggiunta, l'accesso e la rimozione di commenti dai fogli di lavoro. I commenti sono utili per aggiungere note o informazioni utili per gli utenti che lavoreranno con il foglio. Gli sviluppatori hanno la flessibilità di aggiungere commenti a qualsiasi cella del foglio di lavoro.

### **Lavorare con i commenti**

#### **Aggiunta di commenti**

Per aggiungere un commento al foglio di lavoro, procedi nel seguente modo:

1. Aggiungere il controllo Aspose.Cells.GridWeb al Web Form.
1. Accedi al foglio di lavoro a cui stai aggiungendo commenti.
1. Aggiungi un commento a una cella.
1. Imposta una nota per il nuovo commento.

**È stato aggiunto un commento al foglio di lavoro** 

![cose da fare:immagine_alt_testo](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **Accesso ai commenti**

Per accedere a un commento:

1. Accedi alla cella che contiene il commento.
1. Ottieni il riferimento della cella.
1. Passare il riferimento alla raccolta Comment per accedere al commento.
1. Ora è possibile modificare le proprietà del commento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **Rimozione di commenti**

Per rimuovere un commento:

1. Accedi alla cella come spiegato sopra.
1. Utilizzare il metodo removeAt della raccolta Comment per rimuovere il commento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **Gestione dei collegamenti ipertestuali nel foglio di lavoro**

Questo argomento illustra quali tipi di collegamenti ipertestuali sono supportati in Aspose.Cells.GridWeb e come gestirli a livello di codice. I collegamenti ipertestuali possono essere utilizzati per creare collegamenti a URL Web o per eseguire il postback su un server.

### **Tipi di collegamenti ipertestuali**

I seguenti collegamenti ipertestuali sono supportati da Aspose.Cells.GridWeb:

- Collegamenti ipertestuali URL di testo, collegamenti ipertestuali URL applicati al testo.
- Collegamenti ipertestuali URL immagine, collegamenti ipertestuali URL applicati alle immagini.

#### **Collegamenti ipertestuali URL di testo**

 L'esempio seguente aggiunge due collegamenti ipertestuali a un foglio di lavoro. Uno ha un_ bersaglio vuoto mentre l'altro è impostato su_genitore.

![cose da fare:immagine_alt_testo](working-with-worksheets-gridweb_6.png)

**Output: collegamenti ipertestuali di testo aggiunti al foglio di lavoro**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **Collegamenti ipertestuali dell'URL dell'immagine**

L'esempio seguente aggiunge il collegamento ipertestuale dell'URL dell'immagine a un foglio di lavoro.

![cose da fare:immagine_alt_testo](working-with-worksheets-gridweb_7.png)

**Output: collegamento ipertestuale dell'immagine aggiunto al foglio di lavoro**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **Ordinamento dei dati**

L'ordinamento è una caratteristica molto preziosa quando si tratta di elaborazione dei dati. I dati non ordinati sono una seccatura per gli utenti durante la ricerca di informazioni specifiche. Aspose.Cells.GridWeb supporta potenti funzionalità di ordinamento. Questo argomento illustra l'ordinamento dei dati utilizzando Aspose.Cells.GridWeb API.

Aspose.Cells.GridWeb consente agli sviluppatori di ordinare i dati orizzontalmente e verticalmente in modo che gli sviluppatori possano ordinare i dati dall'alto verso il basso o da sinistra a destra.

### **Da cima a fondo**

Per ordinare i dati dall'alto verso il basso:

1. Aggiungere il controllo Aspose.Cells.GridWeb al Web Form.
1. Accedi al foglio di lavoro che desideri ordinare.
1. Ordina l'intervallo di dati in qualsiasi ordine (crescente o decrescente). Assicurati di selezionare l'orientamento dall'alto verso il basso.

L'esempio seguente ordina i dati in due colonne (ID studente e Nome studente) di un foglio di lavoro in ordine crescente. Solo dodici righe di due colonne sono ordinate dall'alto verso il basso.

Prima di applicare il codice, il foglio di lavoro contiene dati non ordinati.

**Input: dati non ordinati** 

![cose da fare:immagine_alt_testo](working-with-worksheets-gridweb_8.png)

Dopo aver eseguito il codice, i dati vengono ordinati in ordine crescente.

**Output: dati ordinati dall'alto verso il basso in ordine crescente** 

![cose da fare:immagine_alt_testo](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **Da sinistra a destra**

Per ordinare i dati da sinistra a destra:

1. Aggiungere il controllo Aspose.Cells.GridWeb al Web Form.
1. Accedi al foglio di lavoro che desideri ordinare.
1. Ordina l'intervallo di dati in qualsiasi ordine (crescente o decrescente). Assicurati di selezionare da sinistra a destra.

L'esempio seguente ordina i dati in due righe (ID studente e Nome studente) in ordine crescente. Solo due righe di quattro colonne sono ordinate da sinistra a destra.

Prima di applicare il codice, il foglio di lavoro contiene dati non ordinati.

**Input: dati non ordinati prima dell'esecuzione dello snippet di codice** 

![cose da fare:immagine_alt_testo](working-with-worksheets-gridweb_10.png)

Dopo aver eseguito il codice, i dati vengono ordinati in ordine crescente.

**Output: dati ordinati da sinistra a destra in ordine crescente** 

![cose da fare:immagine_alt_testo](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **Ricerca e sostituzione**

Uno dei modi più veloci per apportare modifiche ripetitive a un foglio di calcolo di grandi dimensioni consiste nell'utilizzare la funzione Trova e sostituisci. Trova ti aiuta a individuare una stringa di testo o dati e sostituire li sostituisce con un nuovo valore. Aspose.Cells.GridWeb fornisce questa funzione. Ti consente di cercare e sostituire con una stringa di testo o un valore specifico nel lato client del foglio di lavoro tramite una semplice finestra di dialogo. Ti permette anche di cercare dati parziali.

### **La finestra di dialogo Trova/Sostituisci**

Esistono due modi per aprire la finestra di dialogo Trova/Sostituisci:

1.  Quando il controllo è attivo, premere**CTRL+F** per aprire la finestra di dialogo o premere**CTRL+R** tasto per aprire la finestra di dialogo con il**Sostituire** pulsante abilitato.
1.  Spostare il cursore sull'area della cella nel foglio di lavoro, quindi fare clic con il pulsante destro del mouse. Selezionare**Trova** o**Sostituire** dal menù.

**Selezionando Trova**

![cose da fare:immagine_alt_testo](working-with-worksheets-gridweb_12.png)

Viene visualizzata una finestra di dialogo Trova e sostituisci.

**La finestra di dialogo Trova/Sostituisci**

![cose da fare:immagine_alt_testo](working-with-worksheets-gridweb_13.png)

**Usando Trova**

Cercare:

1. Apri la finestra di dialogo Trova/Sostituisci.
1. Digita la stringa che desideri cercare nel campo Trova.
1. Fare clic su Trova successivo per eseguire la ricerca.

Viene evidenziata la cella successiva che corrisponde alla condizione di ricerca.

{{% alert color="primary" %}}

Se il tuo criterio di ricerca non viene trovato, viene visualizzata una finestra di dialogo per avvisarti.

{{% /alert %}}

### **Opzioni di ricerca**

Ci sono alcune opzioni di ricerca che puoi personalizzare nella finestra di dialogo. La tabella sottostante li elenca.

|**No.**|**Nome opzione**|**Descrizione**|
|:- |:- |:- |
|1|Caso di corrispondenza|Indica se utilizzare la distinzione tra maiuscole e minuscole nella ricerca.|
|2|Abbina parola intera|Indica se corrispondere all'intera parola nella ricerca.|
|3|Cerca in alto|Indica se la ricerca verrà eseguita dal basso verso l'alto.|
|4|Espressione regolare|Se selezionato, il controllo tratterà la stringa nella casella di testo Trova come un'espressione regolare nel processo di ricerca.|
|5|Trova in Formule/Valori|Quando si seleziona Formule, il controllo corrisponderà alla formula o al valore non formattato delle celle se la formula o il valore non formattato è presente. Quando i valori sono selezionati, il controllo corrisponderà solo al valore visualizzato delle celle.|

### **Usando Sostituisci**

Per sostituire testo o valori:

1.  Aprire la finestra di dialogo Trova/Sostituisci premendo**CTRL+F** oppure selezionare fare clic con il pulsante destro del mouse su una cella e selezionare**Trova** prima di cliccare**Sostituire**.
1.  Digitare la stringa di sostituzione nel file**Sostituirlo con**campo.
1.  Clic**Sostituire**.

Per sostituire il testo:

1. Apri la finestra di dialogo.
1.  Inserisci il testo che vuoi trovare nel file**Trovare cosa** campo e il testo che si desidera sostituire all'interno del file**Sostituirlo con** campo.
1.  Sostituisci un'occorrenza alla volta facendo clic**Trova il prossimo** seguito da**Sostituire**.
1.  Se sei molto sicuro di cosa contiene il foglio di lavoro, fai clic su**Sostituisci tutto**.

{{% alert color="primary" %}}

 Se il foglio di lavoro non è in modalità di modifica, il file**Sostituire** pulsante non viene visualizzato.

{{% /alert %}}

## Aggiungi/Rimuovi collegamenti ipertestuali dal lato client

Aspose.Cells GridWeb ora supporta l'aggiunta e la rimozione di collegamenti ipertestuali dal lato client. Per questo, lo API mette a disposizione le funzioni "addCelllink" e "delCelllink". I seguenti frammenti di codice illustrano l'aggiunta e la rimozione di collegamenti ipertestuali dal lato client in GridWeb.

### Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

Puoi anche collegarti al foglio utilizzando il seguente frammento di codice.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## Aggiorna le impostazioni dei caratteri dal lato client

Aspose.Cells GridWeb ora supporta la modifica delle impostazioni dei caratteri dal lato client. Per questo, il API fornisce le seguenti funzioni

- **updateCellFontStyle**: Params - r/i/b/ib per regolare/corsivo/grassetto/corsivo&&grassetto
- **updateCellFontSize**: Params - nome carattere, ecc. 'Sistema'
- **updateCellFontName**: Params - dimensione carattere, ecc. '12pt'
- **updateCellFontColor**: Params - nessuno/u/l/ul/ per nessuno/sottolineato/cancellato/sottolineato&&cancellato
- **updateCellFontLine**: Params - colore html come #aa22ee o nomi di colori noti come verde, rosso,...
- **updateCellBackGroundColor**: Params - colore html come #aa22ee o nomi di colori noti come verde, rosso,...

Il frammento di codice seguente illustra la modifica delle impostazioni dei caratteri dal lato client in GridWeb.

### Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## Aggiungi/Rimuovi commenti dal lato client

Aspose.Cells GridWeb ora supporta l'aggiunta e la rimozione di commenti dal lato client. Per questo lo API mette a disposizione le funzioni "aggiungicommenti" e "cancellacommenti". Il frammento di codice seguente illustra l'aggiunta e la rimozione di commenti dal lato client in GridWeb.

### Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## Mostra i pulsanti per aggiungere/rimuovere fogli di lavoro

 Aspose.Cells GridWeb ora supporta l'aggiunta e la rimozione di fogli utilizzando i pulsanti nella barra degli strumenti. Affinché i pulsanti siano visibili sul frontend, è necessario impostare**GridWeb1.ShowAddButton** a**VERO**. Il seguente frammento di codice illustra l'aggiunta di pulsanti Aggiungi/Rimuovi alla barra degli strumenti GridWeb.

### Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
