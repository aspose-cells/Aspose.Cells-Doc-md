---
title: Lavorare con Cells GridWeb
type: docs
weight: 50
url: /it/java/working-with-cells-gridweb/
---
## **Accesso a Cells nel foglio di lavoro**
Questo argomento discute le celle, esaminando la funzionalità più basilare di GridWeb: l'accesso alle celle.

Ogni foglio di lavoro contiene un oggetto GridCells, una raccolta di oggetti GridCell. Un oggetto GridCell rappresenta una cella in Aspose.Cells.GridWeb. È possibile accedere a qualsiasi cella utilizzando GridWeb. Ci sono due metodi preferiti:

- [Accesso alla cella per nome](/cells/it/java/working-with-cells-gridweb/).
- [Accesso alla cella tramite indici di riga e colonna](/cells/it/java/working-with-cells-gridweb/).

Di seguito viene discusso ciascun approccio.
### **Utilizzando il nome Cell**
Tutte le celle hanno un nome univoco. Ad esempio, A1, A2, B1, B2, ecc. Aspose.Cells.GridWeb consente agli sviluppatori di accedere a qualsiasi cella desiderata utilizzando il nome della cella. Basta passare il nome della cella (come indice) alla raccolta GridCells di GridWorksheet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **Utilizzo degli indici di riga e colonna**
Una cella può anche essere riconosciuta dalla sua posizione in termini di indici di riga e colonna. Basta passare gli indici di riga e colonna di una cella alla raccolta GridCells di GridWorksheet. Questo approccio è più veloce di quello precedente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Accesso e modifica del valore di un numero Cell**
[Accesso a Cells nel foglio di lavoro](/cells/it/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) discusso l'accesso alle celle. Questo argomento estende tale discussione per mostrare come accedere e modificare i valori delle celle utilizzando GridWeb API.
### **Accesso e modifica del valore di un Cell**
#### **Valori stringa**
 Prima di accedere e modificare il valore di una cella, è necessario sapere come accedere alle celle. Per dettagli sui diversi approcci per l'accesso alle celle, fare riferimento a[Accesso a Cells nel foglio di lavoro](/cells/it/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

Ogni cella ha una proprietà denominata getStringValue(). Una volta effettuato l'accesso a una cella, gli sviluppatori possono accedere al metodo getStringValue() per accedere al valore della stringa della cella.

{{% alert color="primary" %}} 

IMPORTANTE: cinque tipi di valori (Boolean, int, double, DateTime e string) possono essere memorizzati nelle celle, ma i metodi getValue()/setValue() possono essere utilizzati solo per accedere/modificare il valore dell'oggetto.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **Tutti i tipi di valori**
Aspose.Cells.GridWeb fornisce anche un metodo speciale, putValue, per ogni cella. Con questo metodo è possibile inserire o modificare qualsiasi tipo di valore (Boolean, int, double, DateTime e string) in una cella.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



Esiste anche una versione sovraccaricata del metodo putValue che può accettare qualsiasi tipo di valore in formato stringa e convertirlo automaticamente in un tipo di dati appropriato. Per realizzarlo, passa il valore booleano true a un altro parametro del metodo putValue come mostrato di seguito nell'esempio.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Aggiunta di formule allo Cells**
La caratteristica più preziosa offerta da Aspose.Cells.GridWeb è il supporto per formule o funzioni. Aspose.Cells.GridWeb ha il proprio Formula Engine che calcola le formule nei fogli di lavoro. Aspose.Cells.GridWeb supporta funzioni o formule sia integrate che definite dall'utente. Questo argomento illustra in dettaglio l'aggiunta di formule alle celle utilizzando Aspose.Cells.GridWeb API.
### **Come aggiungere e calcolare una formula?**
 È possibile aggiungere, accedere e modificare le formule nelle celle utilizzando la proprietà Formula di una cella. Aspose.Cells.GridWeb supporta formule definite dall'utente che vanno dal semplice al complesso. Tuttavia, con Aspose.Cells.GridWeb viene fornito anche un gran numero di funzioni o formule incorporate (simili a Microsoft Excel). Per vedere l'elenco completo delle funzioni integrate, fare riferimento a questo[elenco delle funzioni supportate.](/cells/it/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

La sintassi della formula deve essere compatibile con la sintassi di Excel Microsoft. Ad esempio, tutte le formule devono iniziare con un segno di uguale (=).

Per aggiungere una formula a livello di codice, Aspose.Cells.GridWeb la riconoscerà come formula anche se non si utilizza un segno **=**, ma se gli utenti finali che lavorano nella GUI devono utilizzarla.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**Formula aggiunta alla cella B3 ma non calcolata da GridWeb** 

![cose da fare:immagine_alt_testo](working-with-cells-gridweb_1.png)

Nello screenshot sopra, puoi vedere che una formula è stata aggiunta a B3 ma non è stata ancora calcolata. Per calcolare tutte le formule, chiama il metodo GridWorksheetCollection del controllo GridWeb calcolaFormula dopo aver aggiunto le formule ai fogli di lavoro come mostrato di seguito.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

 Gli utenti possono anche calcolare le formule facendo clic**Invia**.

**Facendo clic sul pulsante Invia di GridWeb** 

![cose da fare:immagine_alt_testo](working-with-cells-gridweb_2.png)

**IMPORTANTE** : se un utente fa clic su**Salva** o**Annullare** pulsanti o le schede dei fogli, tutte le formule vengono calcolate automaticamente da GridWeb.

**Risultato della formula dopo il calcolo** 

![cose da fare:immagine_alt_testo](working-with-cells-gridweb_3.png)
### **Riferimento a Cells da Altri fogli di lavoro**
Utilizzando Aspose.Cells.GridWeb, è possibile fare riferimento a valori memorizzati in diversi fogli di lavoro nelle loro formule, creando formule complesse.

La sintassi per fare riferimento a un valore di cella da un foglio di lavoro diverso è SheetName!CellName.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **Creare la convalida dei dati in una GridCell di GridWeb**
 Aspose.Cells.GridWeb consente di aggiungere**Convalida dei dati** utilizzando il metodo GridWorksheet.getValidations().add(). Usando questo metodo, devi specificare il file**Cell Gamma** . Ma se vuoi creare una convalida dei dati in un singolo GridCell, puoi farlo direttamente usando il metodo GridCell.createValidation(). Allo stesso modo, puoi rimuovere**Convalida dei dati** da un GridCell utilizzando il metodo GridCell.removeValidation().

 Il codice di esempio seguente crea a**Convalida dei dati** in una cella B3. Se inserisci un valore che non è compreso tra 20 e 40, verrà visualizzata la cella B3**errore di convalida** nella forma di**Rosso XXXX** come mostrato in questo screenshot.

![cose da fare:immagine_alt_testo](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **Creazione di pulsanti di comando personalizzati**
Aspose.Cells.GridWeb contiene pulsanti speciali come Invia, Salva e Annulla. Tutti questi pulsanti eseguono attività specifiche per Aspose.Cells.GridWeb. È anche possibile aggiungere pulsanti personalizzati che eseguono attività personalizzate. Questo argomento spiega come utilizzare questa funzione.

Il seguente codice di esempio spiega come creare un pulsante di comando personalizzato e come gestirne l'evento click. Puoi utilizzare qualsiasi icona per il tuo pulsante di comando personalizzato. A scopo illustrativo, abbiamo utilizzato questa icona immagine.

![cose da fare:immagine_alt_testo](working-with-cells-gridweb_5.png)

 Come puoi vedere nello screenshot seguente, quando l'utente fa clic sul pulsante di comando personalizzato, aggiunge un testo nella cella A1 che dice**"È stato fatto clic sul mio pulsante di comando personalizzato."**

![cose da fare:immagine_alt_testo](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **Gestione degli eventi del pulsante di comando personalizzato**
Il seguente codice di esempio spiega come eseguire la gestione degli eventi del pulsante di comando personalizzato.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **Formattazione delle celle per GridWeb**
### **Possibili scenari di utilizzo**
GridWeb ora supporta gli utenti per inserire i dati della cella in formato percentuale come 3% e i dati nella cella verranno formattati automaticamente come 3,00%. Tuttavia, dovrai impostare lo stile della cella su Percentage Format che è GridTableItemStyle.NumberType a 9 o 10. Il numero 9 formatterà il 3% come 3% ma il numero 10 formatterà il 3% come 3,00%.

{{% alert color="primary" %}} 

Se non hai impostato lo stile della cella su Formato percentuale, i dati di input 3% verranno visualizzati come 0,03.

{{% /alert %}} 
### **Immettere i dati Cell del foglio di lavoro GridWeb in formato percentuale**
Il seguente codice di esempio imposta la cella A1 GridTableItemStyle.NumberType come 10, pertanto i dati di input 3% vengono automaticamente formattati come 3,00% come mostrato nello screenshot.

![cose da fare:immagine_alt_testo](working-with-cells-gridweb_7.png)
### **Codice d'esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
