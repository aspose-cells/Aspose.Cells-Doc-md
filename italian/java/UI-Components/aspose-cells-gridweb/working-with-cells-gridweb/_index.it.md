---
title: Lavorare con le celle GridWeb
type: docs
weight: 50
url: /it/java/working-with-cells-gridweb/
---

## **Accesso alle celle nel foglio di lavoro**
Questo argomento discute delle celle, esaminando la caratteristica più basilare di GridWeb: l'accesso alle celle.

Ogni foglio di lavoro contiene un oggetto GridCells, una raccolta di oggetti GridCell. Un oggetto GridCell rappresenta una cella in Aspose.Cells.GridWeb. È possibile accedere a qualsiasi cella utilizzando GridWeb. Ci sono due metodi preferiti:

- [Accesso alla cella per nome](/cells/it/java/working-with-cells-gridweb/).
- [Accesso alla cella per indici di riga e colonna](/cells/it/java/working-with-cells-gridweb/).

Di seguito, viene discusso ogni approccio.
### **Utilizzo del nome della cella**
Tutte le celle hanno un nome univoco. Ad esempio, A1, A2, B1, B2, ecc. Aspose.Cells.GridWeb consente agli sviluppatori di accedere a qualsiasi cella desiderata utilizzando il nome della cella. Basta passare il nome della cella (come indice) alla collezione GridCells del GridWorksheet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **Utilizzo degli indici di riga e colonna**
Una cella può anche essere riconosciuta dalla sua posizione in termini di indici di riga e colonna. Basta passare gli indici di riga e colonna di una cella alla collezione GridCells del GridWorksheet. Questo approccio è più veloce rispetto a quello precedente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Accesso e modifica del valore di una cella**
[Accesso alle celle nel foglio di lavoro](/cells/it/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) discusso l'accesso alle celle. Questo argomento estende quella discussione per mostrare come accedere e modificare i valori della cella utilizzando l'API GridWeb.
### **Accesso e modifica del valore di una cella**
#### **Valori stringa**
Prima di accedere e modificare il valore di una cella, è necessario sapere come accedere alle celle. Per i dettagli sui diversi approcci per l'accesso alle celle, fare riferimento a [Accesso alle celle nel foglio di lavoro](/cells/it/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

Ogni cella ha una proprietà chiamata getStringValue(). Una volta che una cella è stata accessa, gli sviluppatori possono accedere al metodo getStringValue() per accedere al valore della stringa della cella.

{{% alert color="primary" %}} 

IMPORTANTE: Cinque tipi di valori (Booleano, int, double, DateTime e stringa) possono essere memorizzati nelle celle, ma il/i metodo/i getValue()/setValue() possono essere utilizzati solo per accedere/modificare il valore dell'oggetto.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **Tutti i tipi di valori**
Aspose.Cells.GridWeb fornisce anche un metodo speciale, putValue, per ogni cella. Con questo metodo, è possibile inserire o modificare qualsiasi tipo di valore (Booleano, int, double, DateTime e stringa) in una cella.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



C'è anche una versione sovraccaricata del metodo putValue che può prendere qualsiasi tipo di valore in formato stringa e convertirlo automaticamente in un tipo di dati appropriato. Per farlo, passare il valore Booleano true a un altro parametro del metodo putValue come mostrato di seguito nell'esempio.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Aggiunta di formule alle celle**
La funzionalità più preziosa offerta da Aspose.Cells.GridWeb è il supporto per formule o funzioni. Aspose.Cells.GridWeb ha il suo motore di formule che calcola le formule nei fogli di lavoro. Aspose.Cells.GridWeb supporta sia funzioni o formule integrate che definite dall'utente. Questo argomento discute l'aggiunta di formule alle celle utilizzando l'API Aspose.Cells.GridWeb in dettaglio.
### **Come aggiungere e calcolare una formula?**
È possibile aggiungere, accedere e modificare formule nelle celle utilizzando la proprietà della Formula di una cella. Aspose.Cells.GridWeb supporta formule definite dall'utente che vanno da semplici a complesse. Tuttavia, un gran numero di funzioni o formule integrate (simili a Microsoft Excel) sono anche fornite con Aspose.Cells.GridWeb. Per vedere l'elenco completo delle funzioni integrate, consultare questo [elenco delle funzioni supportate.](/cells/it/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

La sintassi della formula dovrebbe essere compatibile con la sintassi di Microsoft Excel. Ad esempio, tutte le formule devono iniziare con un segno uguale (=).

Per aggiungere una formula in modo programmato, Aspose.Cells.GridWeb la riconoscerà come una formula anche se non si utilizza un segno **=**, ma se gli utenti finali che lavorano nell'interfaccia grafica devono utilizzarla.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**Formula aggiunta alla cella B3 ma non calcolata da GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

Nello screenshot sopra, puoi vedere che è stata aggiunta una formula a B3 ma non è stata ancora calcolata. Per calcolare tutte le formule, chiama il metodo calculateFormula della collezione GridWorksheet del controllo GridWeb dopo aver aggiunto le formule ai fogli di lavoro come mostrato di seguito.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

Gli utenti possono anche calcolare le formule cliccando su **Invia**.

**Cliccando sul pulsante Invia di GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**IMPORTANTE**: Se un utente clicca sui pulsanti **Salva** o **Annulla**, o sulle schede dei fogli, tutte le formule vengono calcolate automaticamente da GridWeb.

**Risultato della formula dopo il calcolo** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
### **Riferimento a celle da altri fogli di lavoro**
Utilizzando Aspose.Cells.GridWeb, è possibile fare riferimento ai valori memorizzati in fogli di lavoro diversi nelle loro formule, creando formule complesse.

La sintassi per fare riferimento a un valore di cella da un foglio di lavoro diverso è NomeFoglio!NomeCella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **Creare una convalida dei dati in una GridCell di GridWeb**
Aspose.Cells.GridWeb consente di aggiungere **Convalida dei dati** utilizzando il metodo GridWorksheet.getValidations().add(). Utilizzando questo metodo, devi specificare l'**Intervallo di celle**. Ma se vuoi creare una Convalida dei dati in una singola GridCell allora puoi farlo direttamente utilizzando il metodo GridCell.createValidation(). Allo stesso modo, puoi rimuovere la **Convalida dei dati** da una GridCell utilizzando il metodo GridCell.removeValidation().

Il seguente codice di esempio crea una **Convalida dei dati** in una cella B3. Se inserisci un valore che non è compreso tra 20 e 40, la cella B3 mostrerà un **Errore di convalida** sotto forma di **XXXX rosso** come mostrato in questo screenshot.

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **Creazione di pulsanti di comando personalizzati**
Aspose.Cells.GridWeb contiene pulsanti speciali come Invia, Salva e Annulla. Tutti questi pulsanti svolgono compiti specifici per Aspose.Cells.GridWeb. È anche possibile aggiungere pulsanti personalizzati che eseguono compiti personalizzati. Questo argomento spiega come utilizzare questa funzionalità.

Il seguente codice di esempio spiega come creare un pulsante di comando personalizzato e come gestire il suo evento di click. Puoi utilizzare qualsiasi icona per il tuo pulsante di comando personalizzato. A scopo illustrativo, abbiamo utilizzato quest'icona.

![todo:image_alt_text](working-with-cells-gridweb_5.png)

Come puoi vedere nello screenshot seguente, quando l'utente fa clic sul pulsante di comando personalizzato, viene aggiunto un testo nella cella A1 che dice **"Il mio pulsante di comando personalizzato è stato premuto."**

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **Gestione degli eventi del pulsante di comando personalizzato**
Il seguente codice di esempio spiega come gestire gli eventi del pulsante di comando personalizzato.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **Formattazione delle celle per GridWeb**
### **Possibili Scenari di Utilizzo**
GridWeb ora supporta gli utenti nell'inserire i dati della cella nel formato percentuale come 3% e i dati nella cella saranno automaticamente formattati come 3.00%. Tuttavia, sarà necessario impostare lo stile della cella nel formato percentuale, che può essere GridTableItemStyle.NumberType a 9 o 10. Il numero 9 formattarà 3% come 3%, ma il numero 10 formattarà 3% come 3.00%

{{% alert color="primary" %}} 

Se non hai impostato lo stile della cella nel formato percentuale, quindi i dati di input 3% verranno visualizzati come 0.03.

{{% /alert %}} 
### **Inserisci i dati della cella della scheda di lavoro di GridWeb nel formato percentuale**
Il seguente codice di esempio imposta la cella A1 GridTableItemStyle.NumberType come 10, pertanto i dati di input 3% verranno automaticamente formattati come 3.00% come mostrato nello screenshot.

![todo:image_alt_text](working-with-cells-gridweb_7.png)
### **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
