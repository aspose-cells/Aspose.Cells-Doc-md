---
title: Lavorare con i fogli di lavoro di GridWeb
type: docs
weight: 30
url: /it/java/working-with-worksheets-gridweb/
---

## **Accesso ai fogli di lavoro**

Questo argomento discute dell'accesso ai fogli di lavoro del controllo GridWeb. Possiamo anche chiamare questi fogli di lavoro web perché appartengono a GridWeb e vengono utilizzati nelle applicazioni web.

Tutti i fogli di lavoro contenuti nel controllo GridWeb sono memorizzati in una GridWorksheetCollection del controllo GridWeb. È semplice accedere a un particolare foglio di lavoro tramite il suo indice di foglio.

Gli sviluppatori possono accedere a un foglio di lavoro specifico specificando il suo indice di foglio come dimostrato di seguito nell'esempio di codice snippet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **Rimozione di un foglio di lavoro**

Questo argomento fornisce brevi informazioni sulla rimozione dei fogli di lavoro dai file di Microsoft Excel utilizzando l'API GridWeb. Rimuovere un foglio di lavoro specificando il suo indice di foglio.

Gli sviluppatori possono rimuovere un foglio di lavoro specifico specificando il suo indice di foglio utilizzando il metodo removeAt della collezione GridWorksheetCollection come dimostrato di seguito nell'esempio di codice snippet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **Aggiunta di fogli di lavoro**

I fogli di lavoro sono parte integrante di GridWeb. Tutti i dati sono gestiti e memorizzati sotto forma di fogli di lavoro. GridWeb consente agli sviluppatori di aggiungere uno o più fogli di lavoro al controllo Aspose.Cells.GridWeb. Questo argomento mostra approcci semplici per aggiungere fogli di lavoro a GridWeb.

### **Senza specificare il nome del foglio**

Il modo più semplice per aggiungere un foglio di lavoro a Aspose.Cells.GridWeb è chiamare il metodo add della classe GridWorksheetCollection nel controllo GridWeb. Questo crea fogli di lavoro che utilizzano nomi predefiniti (cioè Foglio1, Foglio2, Foglio3 e così via) e li aggiunge al controllo GridWeb.

**Output: è stato aggiunto un foglio di lavoro con un nome predefinito a GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **Con nome del foglio specificato**

Per aggiungere un foglio di lavoro con un nome specifico al controllo GridWeb anziché utilizzare lo schema di denominazione predefinito, chiamare una versione sovraccaricata del metodo add che richiede la stringa specificata SheetName. Ad esempio, l'esempio seguente aggiunge un foglio di lavoro chiamato Fattura.

**Output: è stato aggiunto un foglio di lavoro con un nome specificato a GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

Il metodo add() restituisce l'indice del nuovo foglio di lavoro che può essere utilizzato per accedere all'istanza di questo foglio di lavoro. Per ulteriori dettagli su come accedere ai fogli di lavoro, leggere [Accesso ai fogli di lavoro](/cells/it/java/lavorare-con-i-fogli-di-lavoro-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Rinomina un foglio di lavoro**

Rinominare un foglio di lavoro può essere molto utile quando si lavora con molti fogli di lavoro in GridWeb e si decide di cambiarne i nomi per renderli più significativi. Ad esempio, un foglio contenente una fattura può essere rinominato Fattura invece di Foglio1. Questo argomento descrive questa funzionalità semplice ma utile.

### **Rinomina un foglio di lavoro**

Tutte le schede contengono una proprietà Name che permette agli sviluppatori di accedere o modificare i nomi delle schede. Per rinominare una scheda:

1. Accedere a una scheda dalla GridWorksheetCollection.
1. Rinominare la scheda selezionata.

{{% alert color="primary" %}}

Per ulteriori dettagli su come accedere ai fogli di lavoro in Aspose.Cells.GridWeb, fare riferimento a [Accesso ai fogli di lavoro](/cells/it/java/lavorare-con-i-fogli-di-lavoro-gridweb/#lavorareconfoglidilavorogridweb-accederefoglidilavoro).

{{% /alert %}}

Prima di eseguire il codice, la scheda ha un nome predefinito, come ad esempio Sheet1.

**File di input: una scheda con un nome predefinito Sheet1** 

![todo:image_alt_text](working-with-worksheets-gridweb_3.png)

Dopo aver eseguito il codice, il foglio di lavoro viene rinominato Fattura.

**Output: il foglio di lavoro viene rinominato Fattura** 

![todo:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **Copiare un Foglio di Lavoro**

[Aggiunta di fogli di lavoro](/cells/it/java/lavorare-con-i-fogli-di-lavoro-gridweb/#lavorareconfoglidilavorogridweb-aggiuntafoglidilavoro) descrive come aggiungere nuovi fogli di lavoro a GridWeb. È anche possibile aggiungere una copia (o replica) di un altro foglio di lavoro al controllo Aspose.Cells.GridWeb. Questa funzionalità può essere utile quando è necessario avere dati identici o simili in un foglio di lavoro diverso. In questo caso, è più facile copiare un foglio di lavoro esistente e aggiungerlo ad Aspose.Cells.GridWeb come nuovo foglio di lavoro anziché crearlo da zero.

### **Utilizzo dell'indice del foglio**

Il codice di esempio sottostante mostra come aggiungere una copia di un foglio di lavoro al controllo GridWeb specificando l'indice del foglio di lavoro nel metodo addCopy di GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **Utilizzo del nome del foglio**
Il codice di esempio sottostante mostra come aggiungere una copia di un foglio di lavoro al controllo GridWeb specificando il nome del foglio di lavoro nel metodo addCopy di GridWorksheetCollection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

Il metodo addCopy restituisce l'indice del nuovo foglio di lavoro che può essere utilizzato per accedere all'istanza del foglio di lavoro. Per ulteriori dettagli su come accedere ai fogli di lavoro, leggere [Accesso ai fogli di lavoro](/cells/it/java/lavorare-con-i-fogli-di-lavoro-gridweb/#lavorareconfoglidilavorogridweb-accederefoglidilavoro).

{{% /alert %}}

## **Lavorare con i Riferimenti Nominati**

Normalmente, etichette di colonne e righe vengono utilizzate per fare riferimento in modo univoco alle celle. Tuttavia, è possibile creare nomi descrittivi per rappresentare celle, intervalli di celle, formule o valori costanti.

La parola **nome** può riferirsi a una stringa di caratteri che rappresenta una cella, un intervallo di celle, una formula o un valore costante. Ad esempio, utilizzare nomi facili da capire, come Prodotti, per fare riferimento a intervalli difficili da comprendere, come Vendite!C20:C30.

Le etichette possono essere utilizzate in formule che fanno riferimento ai dati sullo stesso foglio; se si desidera rappresentare un intervallo su un altro foglio, è possibile utilizzare un nome. **Intervalli nominati** è una delle funzionalità più potenti di Microsoft Excel.

Gli utenti possono assegnare un nome a un intervallo e utilizzare tale nome nelle formule. Aspose.Cells.GridWeb supporta questa funzionalità.

### **Aggiunta/Riferimento degli Intervalli Nominati nelle Formule**

Il controllo GridWeb fornisce due classi (GridName e GridNameCollection) per lavorare con intervalli nominati.

Il seguente frammento di codice ti aiuterà a capire come utilizzarli.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **Gestione dei Commenti nel Foglio di Lavoro**

Questo argomento discute l'aggiunta, l'accesso e la rimozione dei commenti dai fogli di lavoro. I commenti sono utili per aggiungere note o informazioni utili per gli utenti che lavoreranno sul foglio. Gli sviluppatori hanno la flessibilità di aggiungere commenti a qualsiasi cella del foglio di lavoro.

### **Lavorare con i commenti**

#### **Aggiunta di commenti**

Per aggiungere un commento al foglio di lavoro, seguire i passaggi seguenti:

1. Aggiungi il controllo Aspose.Cells.GridWeb al modulo Web.
1. Accedi al foglio di lavoro a cui si stanno aggiungendo commenti.
1. Aggiungi un commento a una cella.
1. Imposta una nota per il nuovo commento.

**Un commento è stato aggiunto al foglio di lavoro** 

![todo:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **Accesso ai commenti**

Per accedere a un commento:

1. Accedere alla cella che contiene il commento.
1. Ottenere il riferimento della cella.
1. Passare il riferimento alla raccolta Comment per accedere al commento.
1. Ora è possibile modificare le proprietà del commento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **Rimozione dei commenti**

Per rimuovere un commento:

1. Accedere alla cella come spiegato sopra.
1. Utilizzare il metodo removeAt della raccolta Comment per rimuovere il commento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **Gestione degli Ipercollegamenti nella scheda**

Questo argomento discute quali tipi di collegamenti ipertestuali sono supportati in Aspose.Cells.GridWeb e come gestirli programmaticamente. I collegamenti ipertestuali possono essere utilizzati sia per creare collegamenti a URL web sia per eseguire un postback a un server.

### **Tipi di Collegamenti Ipotestuali**

I seguenti collegamenti ipertestuali sono supportati da Aspose.Cells.GridWeb:

- Collegamenti ipertestuali URL per il testo, collegamenti ipertestuali URL applicati al testo.
- Collegamenti ipertestuali URL per le immagini, collegamenti ipertestuali URL applicati alle immagini.

#### **Collegamenti ipertestuali URL per il testo**

L'esempio qui sotto aggiunge due collegamenti ipertestuali a una scheda. Uno ha un target _blank mentre l'altro è impostato su _parent.

![todo:image_alt_text](working-with-worksheets-gridweb_6.png)

**Output: collegamenti ipertestuali di testo aggiunti al foglio di lavoro**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **Collegamenti ipertestuali URL per le immagini**

L'esempio qui sotto aggiunge un collegamento ipertestuale URL a un foglio di lavoro.

![todo:image_alt_text](working-with-worksheets-gridweb_7.png)

**Output: collegamento ipertestuale per l'immagine aggiunto al foglio di lavoro**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **Ordinamento dati**

L'ordinamento è una funzionalità molto preziosa quando si tratta di elaborazione dati. I dati non ordinati sono un problema per gli utenti quando cercano informazioni specifiche. Aspose.Cells.GridWeb supporta potenti funzionalità di ordinamento. Questo argomento discute l'ordinamento dei dati utilizzando l'API Aspose.Cells.GridWeb.

Aspose.Cells.GridWeb consente ai programmatori di ordinare i dati in orizzontale e verticale in modo che sia possibile ordinare i dati dall'alto verso il basso o da sinistra a destra.

### **Dall'alto al basso**

Per ordinare i dati in orientamento dall'alto al basso:

1. Aggiungi il controllo Aspose.Cells.GridWeb al tuo modulo web.
1. Accedi al foglio di lavoro che desideri ordinare.
1. Ordina il range di dati in qualsiasi ordine (crescente o decrescente). Assicurati di selezionare l'orientamento dall'alto verso il basso.

L'esempio qui sotto ordina i dati in due colonne (ID Studente e Nome Studente) di un foglio di lavoro in ordine ascendente. Solo dodici righe di due colonne sono ordinate in orientamento dall'alto verso il basso.

Prima di applicare il codice, il foglio di lavoro contiene dati non ordinati.

**Input: dati non ordinati** 

![todo:image_alt_text](working-with-worksheets-gridweb_8.png)

Dopo l'esecuzione del codice, i dati sono ordinati in ordine crescente.

**Output: dati ordinati dall'alto verso il basso in ordine ascendente** 

![todo:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **Da sinistra a destra**

Per ordinare i dati da sinistra a destra:

1. Aggiungi il controllo Aspose.Cells.GridWeb al tuo modulo web.
1. Accedi al foglio di lavoro che desideri ordinare.
1. Ordina il range di dati in qualsiasi ordine (crescente o decrescente). Assicurati di selezionare da sinistra a destra.

L'esempio qui sotto ordina i dati in due righe (ID Studente e Nome Studente) in ordine ascendente. Solo due righe di quattro colonne sono ordinate da sinistra a destra.

Prima di applicare il codice, il foglio di lavoro contiene dati non ordinati.

**Input: dati non ordinati prima dell'esecuzione del frammento di codice** 

![todo:image_alt_text](working-with-worksheets-gridweb_10.png)

Dopo l'esecuzione del codice, i dati sono ordinati in ordine crescente.

**Output: dati ordinati da sinistra a destra in ordine ascendente** 

![todo:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **Ricerca e Sostituzione**

Uno dei modi più veloci per apportare modifiche ripetitive in un ampio foglio di calcolo è utilizzare la funzione di ricerca e sostituzione. La ricerca ti permette di individuare una stringa di testo o dati e la sostituzione la sostituisce con un nuovo valore. Aspose.Cells.GridWeb fornisce questa funzionalità. Consente di cercare e sostituire con una specifica stringa di testo o valore nel lato client della scheda attraverso una semplice finestra di dialogo. Consente anche di cercare dati parziali.

### **La finestra di dialogo Ricerca/Sostituzione**

Ci sono due modi per aprire la finestra di dialogo Ricerca/Sostituzione:

1. Quando il controllo è attivo, premere **CTRL+F** per aprire la finestra di dialogo, o premere il tasto **CTRL+R** per aprire la finestra di dialogo con il pulsante **Sostituisci** abilitato.
1. Spostare il cursore nell'area della cella nella scheda, quindi fare clic con il pulsante destro del mouse. Selezionare **Ricerca** o **Sostituisci** dal menu.

**Selezione di Ricerca**

![todo:image_alt_text](working-with-worksheets-gridweb_12.png)

Viene visualizzata una finestra di ricerca e sostituzione.

**La finestra di dialogo Ricerca/Sostituzione**

![todo:image_alt_text](working-with-worksheets-gridweb_13.png)

**Usando Trova**

Per cercare:

1. Apri la finestra Trova/Sostituisci.
1. Digitare la stringa che si desidera cercare nel campo Trova cosa.
1. Fare clic su Trova avanti per cercare.

La prossima cella che corrisponde alla tua condizione di ricerca viene evidenziata.

{{% alert color="primary" %}}

Se il criterio di ricerca non viene trovato, viene visualizzata una finestra di dialogo per informarti.

{{% /alert %}}

### **Opzioni di Ricerca**

Ci sono alcune opzioni di ricerca che puoi personalizzare nella finestra di dialogo. La tabella sottostante le elenca.

|**N.**|**Nome opzione**|**Descrizione**|
| :- | :- | :- |
|1|Corrispondenza maiuscolo/minuscolo|Indica se utilizzare il case sensitive nella ricerca.|
|2|Corrispondenza parola intera|Indica se corrispondere l'intera parola nella ricerca.|
|3|Ricerca in su|Indica se la ricerca verrà fatta dal basso verso l'alto.|
|4|Espressione regolare|Quando selezionato, il controllo tratterà la stringa nel campo Trova cosa come un'espressione regolare nel processo di ricerca.|
|5|Trova in Formule/Valori|Quando si seleziona Formule, il controllo corrisponderà alla formula o al valore non formattato delle celle se la formula o il valore non formattato è presente. Quando si seleziona Valori, il controllo corrisponderà solo al valore visualizzato delle celle.|

### **Usando Sostituisci**

Per sostituire testo o valori:

1. Apri la finestra di dialogo Trova/Sostituisci premendo **CTRL+F**, o seleziona fare clic con il pulsante destro del mouse su una cella e poi seleziona **Trova** prima di fare clic su **Sostituisci**.
1. Digitare la stringa di sostituzione nel campo **Sostituisci con**.
1. Fai clic su **Sostituisci**.

Per sostituire il testo:

1. Apri la finestra di dialogo.
1. Immettere il testo che si desidera trovare nel campo **Trova cosa**, e il testo che si desidera sostituire nel campo **Sostituisci con**.
1. Sostituisci una singola occorrenza facendo clic su **Trova successivo** seguito da **Sostituisci**.
1. Se sei sicuro del contenuto del foglio di lavoro, fai clic su **Sostituisci tutto**.

{{% alert color="primary" %}}

Se il foglio di lavoro non è in modalità di modifica, il pulsante **Sostituisci** non viene visualizzato.

{{% /alert %}}

## Aggiungi/Rimuovi collegamenti ipertestuali dal lato client

Aspose.Cells GridWeb supporta ora l'aggiunta e la rimozione di collegamenti ipertestuali dal lato client. A questo scopo, l'API fornisce le funzioni "addCelllink" e "delCelllink". I seguenti frammenti di codice dimostrano l'aggiunta e la rimozione di collegamenti ipertestuali dal lato client in GridWeb.

### Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

È anche possibile collegarsi a un foglio utilizzando il seguente frammento di codice.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## Aggiorna le impostazioni del carattere dal lato client

Aspose.Cells GridWeb supporta ora la modifica delle impostazioni del carattere dal lato client. A questo scopo, l'API fornisce le seguenti funzioni

- **updateCellFontStyle**: Parametri - r/i/b/ib per regolare/corsivo/grassetto/corsivo&&grassetto
- **updateCellFontSize**: Parametri - nome carattere, ecc. 'Sistema'
- **updateCellFontName**: Parametri - dimensione carattere, ecc. '12pt'
- **updateCellFontColor**: Parametri - nessuno/u/l/ul/ per nessuno/sottolineato/barrato/sottolineato&&barrato
- **updateCellFontLine**: Parametri - colore html come #aa22ee o nome del colore ben noto come verde, rosso,...
- **updateCellBackGroundColor**: Parametri - colore html come #aa22ee o nome di colore ben noto come verde, rosso, ...

Il seguente frammento di codice dimostra come modificare le impostazioni del font dal lato client in GridWeb.

### Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## Aggiungi/Rimuovi Commenti Dal Lato Client

Aspose.Cells GridWeb supporta ora l'aggiunta e la rimozione di commenti dal lato client. A tal scopo, l'API fornisce le funzioni "addcomments" e "delcomments". Il seguente frammento di codice dimostra come aggiungere e rimuovere commenti dal lato client in GridWeb.

### Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## Mostra bottoni per Aggiungere/Rimuovere Fogli di Lavoro

Aspose.Cells GridWeb ora supporta l'aggiunta e la rimozione di fogli usando i pulsanti nella barra degli strumenti. Per rendere visibili i pulsanti sul frontend, è necessario impostare **GridWeb1.ShowAddButton** su **true**. Il seguente snippet di codice dimostra l'aggiunta dei pulsanti Aggiungi/Rimuovi alla barra degli strumenti di GridWeb.

### Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
