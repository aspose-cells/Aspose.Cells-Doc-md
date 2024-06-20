---
title: Gestione dei controlli
type: docs
weight: 120
url: /it/java/managing-controls/
---

## **Introduzione**

Gli sviluppatori possono aggiungere diversi oggetti di disegno come caselle di testo, caselle di controllo, pulsanti di opzione, menu a discesa, etichette, pulsanti, linee, rettangoli, archi, ovali, spinner, barre di scorrimento, gruppi, ecc. Aspose.Cells fornisce lo spazio dei nomi Aspose.Cells.Drawing che contiene tutti gli oggetti di disegno. Tuttavia, alcuni oggetti di disegno o forme non sono ancora supportati. Creare questi oggetti di disegno in un foglio di calcolo del designer usando Microsoft Excel e quindi importare il foglio di calcolo del designer in Aspose.Cells. Aspose.Cells consente di caricare questi oggetti di disegno da un foglio di calcolo del designer e scriverli in un file generato.

## **Aggiunta del controllo casella di testo al foglio di lavoro**

Un modo per sottolineare informazioni importanti in un report è utilizzare una casella di testo. Ad esempio, aggiungere del testo per evidenziare il nome dell'azienda o per indicare la regione geografica con le vendite più elevate, ecc. Aspose.Cells fornisce la classe TextBoxes, utilizzata per aggiungere una nuova casella di testo alla collezione. C'è un'altra classe, [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox), che rappresenta una casella di testo utilizzata per definire tutti i tipi di impostazioni. Ha alcuni membri importanti:

- Il metodo [**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) restituisce un oggetto [**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame) utilizzato per regolare i contenuti della casella di testo.
- Il metodo [**setPlacement**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) specifica il tipo di posizionamento.
- Il metodo [**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) specifica gli attributi del carattere.
- Il metodo [**addHyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String)) aggiunge un collegamento ipertestuale per la casella di testo.
- La proprietà [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) restituisce un oggetto [**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat) usato per impostare il formato di riempimento per la casella di testo.
- La proprietà [**LineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat) restituisce l'oggetto [**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat) di solito usato per lo stile e lo spessore della linea della casella di testo.
- Il metodo [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text) specifica il testo di input per la casella di testo.

Nell'esempio seguente vengono create due caselle di testo nel primo foglio di lavoro del documento. La prima casella di testo è ben arredata con diverse impostazioni di formato. La seconda è semplice.

L'output seguente è generato eseguendo il codice:

**Sono state create due caselle di testo nel foglio di lavoro** 

![todo:image_alt_text](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **Manipolazione dei controlli casella di testo nel foglio di lavoro del designer**

Aspose.Cells consente anche di accedere alle caselle di testo nei fogli di lavoro del designer e manipolarle. Utilizzare la proprietà [**Worksheet.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) per ottenere la raccolta delle caselle di testo nel foglio.

L'esempio seguente utilizza il file di Microsoft Excel - tsttextboxes.xls - che abbiamo creato nell'esempio precedente. Ottiene le stringhe di testo delle due caselle di testo e cambia il testo della seconda casella di testo per salvare il file.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **Aggiunta del controllo casella di controllo al foglio di lavoro**

Le caselle di controllo sono utili se si desidera fornire un modo per consentire all'utente di scegliere tra due opzioni, ad esempio vero o falso; sì o no. Aspose.Cells consente di utilizzare caselle di controllo nei fogli di lavoro. Ad esempio, è possibile avere sviluppato un foglio di lavoro di proiezione finanziaria nel quale è possibile contabilizzare o meno un'acquisizione specifica. In questo caso, potrebbe essere opportuno posizionare una casella di controllo nella parte superiore del foglio di lavoro. È quindi possibile collegare lo stato di questa casella di controllo a un'altra cella, in modo che se la casella di controllo è selezionata, il valore della cella è Vero; se non è selezionata, il valore della cella è Falso.

### **Utilizzando Microsoft Excel**

Per inserire un controllo casella di controllo nel foglio di lavoro, seguire questi passaggi:

1. Assicurarsi che la barra degli strumenti Moduli sia visualizzata.
1. Fare clic sul pulsante **Casella di controllo** sulla barra degli strumenti Moduli.
1. Nella tua area di lavoro, fare clic e trascinare per definire il rettangolo che conterrà la casella di controllo e l'etichetta accanto alla casella di controllo.
1. Una volta inserita la casella di controllo, spostare il cursore del mouse nell'area dell'etichetta e modificare l'etichetta.
1. Nel campo **Collegamento cella**, specificare l'indirizzo della cella a cui questa casella di controllo dovrebbe essere collegata.
1. Fare clic su **OK**.

### **Usare Aspose.Cells**

Aspose.Cells fornisce la classe [**CheckBoxCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection), che viene utilizzata per aggiungere una nuova casella di controllo alla raccolta. C'è un'altra classe, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox), che rappresenta una casella di controllo. Ha alcuni membri importanti:

- Il metodo [**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell) specifica una cella a cui è collegata la casella di controllo.
- Il metodo [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text) specifica la stringa di testo associata alla casella di controllo. È l'etichetta della casella di controllo.
- Il metodo [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value) specifica se la casella di controllo è selezionata o meno.

L'esempio seguente mostra come aggiungere una casella di controllo al foglio di lavoro. L'output sottostante è generato dopo l'esecuzione del codice.

**Una casella di controllo è stata aggiunta nel foglio di lavoro** 

![todo:image_alt_text](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **Aggiunta del controllo pulsante di opzione al foglio di lavoro**

Un pulsante radio, o un pulsante di opzione, è un controllo composto da una casella rotonda. L'utente prende la sua decisione selezionando la casella rotonda. Un pulsante radio è di solito, se non sempre, accompagnato da altri. Tali pulsanti radio appaiono e si comportano come un gruppo. L'utente decide quale pulsante è valido selezionandone solo uno. Quando l'utente fa clic su un pulsante, viene riempito. Quando un pulsante nel gruppo è selezionato, i pulsanti dello stesso gruppo sono vuoti.

### **Utilizzando Microsoft Excel**

Per inserire un controllo Radio Button nel tuo foglio di lavoro, segui questi passaggi:

1. Assicurati che la barra degli strumenti **Form** sia visualizzata.
1. Clicca sullo strumento **Pulsante di Opzione**.
1. Nel foglio di lavoro, clicca e trascina per definire il rettangolo che conterrà il pulsante di opzione e l'etichetta accanto al pulsante di opzione.
1. Una volta che il pulsante radio è stato posizionato nel foglio di lavoro, sposta il cursore del mouse nell'area dell'etichetta e cambia l'etichetta.
1. Nel campo **Collegamento cella**, specifica l'indirizzo della cella a cui questo radio button dovrebbe essere collegato.
1. Fai clic su **OK**.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fornisce un metodo chiamato addShape che può essere utilizzato per aggiungere un controllo radio button a un foglio di lavoro. Il metodo potrebbe restituire un oggetto RadioButton. La classe RadioButton rappresenta un pulsante di opzione. Ha alcuni membri importanti:

- Il metodo setLinkedCell specifica una cella che è collegata al radio button.
- Il metodo setText specifica la stringa di testo associata al radio button. È l'etichetta del radio button.
- La proprietà Checked specifica se il radio button è selezionato o no.
- Il metodo setFillFormat specifica il formato di riempimento del radio button.
- Il metodo setLineFormat specifica gli stili del formato della linea del pulsante di opzione.

Nell'esempio seguente viene mostrato come aggiungere i radio button a un foglio di lavoro. L'esempio aggiunge tre radio button che rappresentano gruppi di età. L'output seguente sarebbe generato dopo aver eseguito il codice.

**Alcuni RadioButtons sono aggiunti nel foglio di lavoro** 

![todo:image_alt_text](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

## **Aggiungere un Controllo Combo Box a un Foglio di Lavoro**

Per rendere più semplice l'inserimento dei dati, o per limitare le voci a determinati elementi definiti da te, puoi creare una casella combinata, o una lista a discesa di voci valide che è compilata da celle altrove nel foglio di lavoro. Quando crei una lista a discesa per una cella, viene visualizzata una freccia accanto a quella cella. Per inserire informazioni in quella cella, clicca sulla freccia e poi sulla voce che desideri.

### **Utilizzando Microsoft Excel**

Per inserire un controllo casella combinata nel tuo foglio di lavoro, segui questi passaggi:

1. Assicurati che la barra degli strumenti **Form** sia visualizzata.
1. Clicca sullo strumento **Casella Combinata**.
1. Nella tua area di lavoro, clicca e trascina per definire il rettangolo che conterrà la casella combinata.
1. Una volta che la casella combinata è posizionata nel foglio di lavoro, fare clic con il pulsante destro del mouse sul controllo per fare clic su **Formato Controllo** e specificare l'intervallo di input.
1. Nel campo **Collegamento Cella**, specificare l'indirizzo della cella a cui questa casella combinata dovrebbe essere collegata.
1. Fare clic su **OK**.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fornisce un metodo chiamato addShape, che può essere utilizzato per aggiungere un controllo casella combinata al foglio di lavoro. Il metodo può restituire l'oggetto ComboBox. La classe ComboBox rappresenta una casella combinata. Ha alcuni membri importanti:

- Il metodo setLinkedCell specifica una cella collegata alla casella combinata.
- Il metodo setInputRange specifica l'intervallo di celle del foglio di lavoro utilizzato per riempire la casella combinata.
- Il metodo setDropDownLines specifica il numero di righe di elenco visualizzate nella parte a discesa di una casella combinata.
- Il metodo setShadow indica se la casella combinata ha un'ombreggiatura 3D.

Nell'esempio seguente viene mostrato come aggiungere una casella combinata al foglio di lavoro. L'output seguente viene generato durante l'esecuzione del codice.

**È stata aggiunta una casella combinata nel foglio di lavoro** 

![todo:image_alt_text](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **Aggiunta del Controllo Etichetta a un Foglio di Lavoro**

Le etichette sono un modo per fornire agli utenti informazioni sui contenuti di un foglio di calcolo. Aspose.Cells consente di aggiungere e manipolare etichette in un foglio di lavoro. La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fornisce un metodo chiamato addShape, utilizzato per aggiungere un controllo etichetta al foglio di lavoro. Il metodo restituisce un oggetto Label. La classe Label rappresenta un'etichetta nel foglio di lavoro. Ha alcuni membri importanti:

- Il metodo setText specifica una stringa di didascalia per l'etichetta.
- Il metodo setPlacement specifica il tipo di inserimento PlacementType, il modo in cui l'etichetta è collegata alle celle nel foglio di lavoro.

Nell'esempio seguente viene mostrato come aggiungere un'etichetta al foglio di lavoro. L'output seguente viene generato durante l'esecuzione del codice.

**È stata aggiunta un'etichetta nel foglio di lavoro**

![todo:image_alt_text](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

## **Aggiunta di un Controllo Casella Elenco a un Foglio di Lavoro**

Un controllo casella elenco crea un controllo elenco che consente la selezione di uno o più elementi.

### **Utilizzando Microsoft Excel**

Per posizionare un controllo casella elenco in un foglio di lavoro:

1. Assicurati che la barra degli strumenti **Form** sia visualizzata.
1. Fare clic sullo strumento **Casella Elenco**.
1. Nella tua area di lavoro, fare clic e trascinare per definire il rettangolo che conterrà la casella di selezione.
1. Una volta posizionata la casella di selezione nel foglio di lavoro, fare clic con il tasto destro sul controllo per fare clic su **Formato controllo** e specificare l'intervallo di input.
1. Nel campo **Collegamento cella**, specificare l'indirizzo della cella a cui questa casella di selezione deve essere collegata e impostare l'attributo del tipo di selezione (Singola, Multipla, Estesa).
1. Fai clic su **OK**.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fornisce un metodo chiamato addForma, che viene utilizzato per aggiungere un controllo casella di selezione a un foglio di lavoro. Il metodo restituisce un oggetto ListBox. La classe ListBox rappresenta una casella di selezione. Ha alcuni membri importanti:

- Il metodo setLinkedCell specifica una cella che è collegata alla casella di selezione.
- Il metodo setInputRange specifica l'intervallo di celle del foglio di lavoro utilizzato per riempire la casella di selezione.
- Il metodo setSelectionType specifica la modalità di selezione della casella di selezione.
- Il metodo setShadow indica se la casella di selezione ha ombreggiatura 3D.

Nell'esempio seguente viene mostrato come aggiungere una casella di selezione al foglio di lavoro. L'output seguente viene generato durante l'esecuzione del codice.

**Una casella di selezione è stata aggiunta nel foglio di lavoro** 

![todo:image_alt_text](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

## **Aggiunta del controllo Pulsante a un foglio di lavoro**

I pulsanti sono utili per eseguire alcune azioni. A volte è utile assegnare un Macro VBA al pulsante o assegnare un collegamento ipertestuale per aprire una pagina web.

### **Utilizzando Microsoft Excel**

Per inserire un controllo pulsante nel tuo foglio di lavoro:

1. Assicurati che la barra degli strumenti **Form** sia visualizzata.
1. Fare clic sullo strumento **Pulsante**.
1. Nella tua area di lavoro, fare clic e trascinare per definire il rettangolo che conterrà il pulsante.
1. Una volta posizionata la casella di selezione nel foglio di lavoro, fare clic con il tasto destro sul controllo e selezionare **Formato controllo**, quindi specificare un Macro VBA e attributi relativi al carattere, all'allineamento, alla dimensione, al margine, ecc.
1. Fare clic su **OK**.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fornisce un metodo chiamato addForma, utilizzato per aggiungere un controllo pulsante al foglio di lavoro. Il metodo potrebbe restituire un oggetto Pulsante. La classe Pulsante rappresenta un pulsante. Ha alcuni membri importanti:

- Il metodo setText specifica la didascalia del pulsante.
- Il metodo setPlacement specifica il PlacementType, il modo in cui il pulsante è collegato alle celle nel foglio di lavoro.
- Il metodo addHyperlink aggiunge un collegamento ipertestuale per il controllo del pulsante. Cliccando sul pulsante si verrà indirizzati all'URL correlato.

L'esempio seguente mostra come aggiungere un pulsante al foglio di lavoro. L'output seguente viene generato durante l'esecuzione del codice

**Un pulsante viene aggiunto nel foglio di lavoro**

![todo:image_alt_text](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **Aggiunta di un controllo Linea a un Foglio di Lavoro**

Aspose.Cells ti consente di disegnare autoshape nei tuoi fogli di lavoro. Puoi creare una linea con facilità. Ti è anche consentito formattare la linea. Ad esempio, puoi cambiare il colore della linea, specificare lo spessore e lo stile della linea secondo le tue esigenze.

### **Utilizzando Microsoft Excel**

1. Sulla barra degli strumenti **Disegno**, fare clic su **Forme automatiche**, puntare su **Linee** e selezionare lo stile della linea desiderato.
1. Trascinare per disegnare la linea.
1. Eseguire una o entrambe le seguenti azioni:
   1. Per vincolare la linea a disegnare a angoli di 15 gradi dal punto di inizio, tenere premuto SHIFT mentre si trascina.
   1. Per allungare la linea in direzioni opposte dal primo punto di estremità, tenere premuto CTRL mentre si trascina.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fornisce un metodo denominato addShape, che viene utilizzato per aggiungere una forma di linea al foglio di lavoro. Il metodo può restituire un oggetto LineShape. La classe LineShape rappresenta una linea. Ha alcuni membri importanti:

- Il metodo setDashStyle specifica il formato di una linea.
- Il metodo setPlacement specifica il PlacementType, il modo in cui la linea è collegata alle celle nel foglio di lavoro.

L'esempio seguente mostra come aggiungere linee al foglio di lavoro. Crea tre linee con stili diversi. L'output seguente viene generato dopo l'esecuzione del codice

**Alcune linee sono aggiunte nel foglio di lavoro** 

![todo:image_alt_text](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **Aggiunta di una Punta a Freccia a una Linea**

Aspose.Cells ti consente anche di disegnare linee con punta a freccia. È possibile aggiungere una punta a freccia a una linea e formattare la linea. Ad esempio, puoi cambiare il colore della linea o specificare lo spessore e lo stile della linea.

L'esempio seguente mostra come aggiungere una punta a freccia a una linea. L'output seguente viene generato durante l'esecuzione del codice.

**È stata aggiunta una linea con un capo di freccia nel foglio di lavoro** 

![todo:image_alt_text](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **Aggiunta del controllo Rettangolo in un foglio di lavoro**

Aspose.Cells ti consente di disegnare forme rettangolari nei tuoi fogli di lavoro. Puoi creare un rettangolo, un quadrato, ecc. Ti è anche consentito formattare il colore di riempimento e il colore della linea di bordo del controllo. Ad esempio, puoi cambiare il colore del rettangolo, impostare il colore di sfondo, specificare lo spessore e lo stile del rettangolo per le tue esigenze.

### **Utilizzando Microsoft Excel**

1. Sulla barra degli strumenti **Disegno**, fare clic su **Rettangolo**.
1. Trascina per disegnare il rettangolo.
1. Eseguire una o entrambe le seguenti azioni:
   1. Per vincolare il rettangolo e disegnare un quadrato dal suo punto iniziale, premere il tasto MAIUSC mentre trascini.
   1. Per disegnare un rettangolo da un punto centrale, premere il tasto CTRL mentre trascini.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fornisce un metodo chiamato addShape, che viene utilizzato per aggiungere una forma rettangolare a un foglio di lavoro. Il metodo può restituire un oggetto RectangleShape. La classe RectangleShape rappresenta un rettangolo. Ha alcuni membri importanti:

- Il metodo setLineFormat specifica gli attributi del formato della linea di un rettangolo.
- Il metodo setPlacement specifica il PlacementType, il modo in cui il rettangolo è collegato alle celle nel foglio di lavoro.
- La proprietà FillFormat specifica gli stili di formato di riempimento di un rettangolo.

Nell'esempio seguente viene mostrato come aggiungere un rettangolo al foglio di lavoro. Viene generato il seguente output durante l'esecuzione del codice.

**È stato aggiunto un rettangolo nel foglio di lavoro** 

![todo:image_alt_text](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **Aggiunta del controllo Arco al foglio di lavoro**

Aspose.Cells ti consente di disegnare forme ad arco nei tuoi fogli di lavoro. Puoi creare archi semplici e riempiti. Ti è consentito formattare il colore di riempimento e il colore della linea di bordo del controllo. Ad esempio, puoi specificare/cambiare il colore dell'arco, impostare il colore di sfondo, specificare lo spessore e lo stile della forma per le tue esigenze.

### **Utilizzando Microsoft Excel**

1. Sulla barra degli strumenti **Disegno**, fare clic su **Arco** in **Forme automatiche**.
1. Trascina per disegnare l'arco.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fornisce un metodo chiamato addShape, che viene utilizzato per aggiungere una forma ad arco al foglio di lavoro. Il metodo può restituire un oggetto ArcShape. La classe ArcShape rappresenta un arco. Ha alcuni membri importanti:

- Il metodo setLineFormat specifica gli attributi del formato della linea di un arco.
- Il metodo setPlacement specifica il PlacementType, il modo in cui l'arco è collegato alle celle nel foglio di lavoro.
- La proprietà FillFormat specifica gli stili del formato di riempimento della forma.

Nell'esempio seguente viene mostrato come aggiungere forme ad arco al foglio di lavoro. L'esempio crea due forme ad arco: una è riempita e l'altra è semplice. L'output seguente viene generato durante l'esecuzione del codice

**Vengono aggiunte due forme ad arco al foglio di lavoro** 

![todo:image_alt_text](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **Aggiunta del controllo ovale a un foglio di lavoro**

Aspose.Cells consente di disegnare forme ovali nei fogli di lavoro. Creare forme ovali semplici e riempite e formattare il colore di riempimento e il colore della linea di bordo del controllo. Ad esempio, è possibile specificare / cambiare il colore dell'ovale, impostare il colore dell'ombreggiatura, specificare il peso e lo stile della forma.

### **Utilizzando Microsoft Excel**

1. Sulla barra degli strumenti **Disegno**, fare clic su **Ovale**.
1. Trascina per disegnare l'ovale.
1. Eseguire una o entrambe le seguenti azioni:
   1. Per limitare l'ovale a disegnare un cerchio dal suo punto di inizio, tenere premuto MAIUSC mentre si trascina.
   1. Per disegnare un ovale da un punto centrale, tenere premuto CTRL mentre si trascina.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fornisce un metodo chiamato addShape, che viene utilizzato per aggiungere un'ovale a un foglio di lavoro. Il metodo può restituire un oggetto Oval. La classe Oval rappresenta una forma ovale. Ha alcuni membri importanti:

- Il metodo setLineFormat specifica gli attributi del formato linee di una forma ovale.
- Il metodo setPlacement specifica il **PlacementType**, il modo in cui l'ovale è allegato alle celle nel foglio di lavoro.
- La proprietà FillFormat specifica gli stili del formato di riempimento della forma.

Nell'esempio seguente viene mostrato come aggiungere forme ovali al foglio di lavoro. L'esempio crea due forme ovali: una è ovale riempito, l'altra è un semplice cerchio. Viene generato l'output seguente durante l'esecuzione del codice.

**Vengono aggiunte due forme ovali al foglio di lavoro** 

![todo:image_alt_text](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **Argomenti avanzati**
- [Aggiungi controlli ActiveX utilizzando Aspose.Cells](/cells/it/java/add-activex-controls-using-aspose-cells/)
- [Rimuovi controllo ActiveX](/cells/it/java/remove-activex-control/)
