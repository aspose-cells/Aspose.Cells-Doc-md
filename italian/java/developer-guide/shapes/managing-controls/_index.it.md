---
title: Gestione dei controlli
type: docs
weight: 120
url: /it/java/managing-controls/
---
## **introduzione**

Gli sviluppatori possono aggiungere diversi oggetti di disegno come caselle di testo, caselle di controllo, pulsanti di opzione, caselle combinate, etichette, pulsanti, linee, rettangoli, archi, ovali, caselle di selezione, barre di scorrimento, caselle di gruppo ecc. Aspose.Cells fornisce lo spazio dei nomi Aspose.Cells.Drawing che contiene tutti gli oggetti di disegno. Tuttavia, ci sono alcuni oggetti o forme di disegno che non sono ancora supportati. Creare questi oggetti di disegno in un foglio di calcolo del progettista utilizzando Microsoft Excel e quindi importare il foglio di calcolo del progettista in Aspose.Cells. Aspose.Cells consente di caricare questi oggetti di disegno da un foglio di calcolo del progettista e scriverli in un file generato.

## **Aggiunta del controllo TextBox al foglio di lavoro**

Un modo per evidenziare informazioni importanti in un report consiste nell'utilizzare una casella di testo. Ad esempio, aggiungi del testo per evidenziare il nome dell'azienda o per indicare la regione geografica con le vendite più alte ecc. Aspose.Cells fornisce la classe TextBoxes, utilizzata per aggiungere una nuova casella di testo alla raccolta. C'è un'altra classe,[**Casella di testo**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox), che rappresenta una casella di testo utilizzata per definire tutti i tipi di impostazioni. Ha alcuni membri importanti:

-  Il[**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) metodo restituisce a[**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame) oggetto utilizzato per regolare il contenuto della casella di testo.
-  Il[**setPlacement**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) metodo specifica il tipo di posizionamento.
-  Il[**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) metodo specifica gli attributi del carattere.
-  Il[**addHyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String)) aggiunge un collegamento ipertestuale per la casella di testo.
-  Il[**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) resi di proprietà[**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat) oggetto utilizzato per impostare il formato di riempimento per la casella di testo.
-  Il[**LineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat) proprietà restituisce il[**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat) oggetto solitamente utilizzato per definire lo stile e lo spessore della riga della casella di testo.
-  Il[**impostaTesto**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text)metodo specifica il testo di input per la casella di testo.

L'esempio seguente crea due caselle di testo nel primo foglio di lavoro della cartella di lavoro. La prima casella di testo è ben fornita con diverse impostazioni di formato. Il secondo è semplice.

Il seguente output viene generato eseguendo il codice:

**Nel foglio di lavoro vengono create due caselle di testo** 

![cose da fare:immagine_alt_testo](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **Manipolazione dei controlli della casella di testo nei fogli di calcolo di Designer**

 Aspose.Cells consente inoltre di accedere alle caselle di testo nei fogli di lavoro del designer e di manipolarle. Utilizzare il[**Foglio di lavoro.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) property per ottenere la raccolta di caselle di testo nel foglio.

L'esempio seguente utilizza il file Excel Microsoft – tsttextboxes.xls – creato nell'esempio precedente. Ottiene le stringhe di testo delle due caselle di testo e modifica il testo della seconda casella di testo per salvare il file.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **Aggiunta del controllo CheckBox al foglio di lavoro**

Le caselle di controllo sono utili se si desidera fornire a un utente un modo per scegliere tra due opzioni, come true o false; sì o no. Aspose.Cells consente di utilizzare le caselle di controllo nei fogli di lavoro. Ad esempio, potresti aver sviluppato un foglio di lavoro per la proiezione finanziaria in cui puoi tenere conto di una particolare acquisizione o meno. In questo caso, potresti voler inserire una casella di controllo nella parte superiore del foglio di lavoro. È quindi possibile collegare lo stato di questa casella di controllo a un'altra cella, in modo che se la casella di controllo è selezionata, il valore della cella sia True; se non è selezionato, il valore della cella è False.

### **Utilizzando Microsoft Excel**

Per posizionare un controllo casella di controllo nel foglio di lavoro, attenersi alla seguente procedura:

1. Assicurati che la barra degli strumenti Moduli sia visualizzata.
1.  Clicca il**Casella di controllo** strumento sulla barra degli strumenti Moduli.
1. Nell'area del foglio di lavoro, fare clic e trascinare per definire il rettangolo che conterrà la casella di controllo e l'etichetta accanto alla casella di controllo.
1. Una volta posizionata la casella di controllo, spostare il cursore del mouse nell'area dell'etichetta e modificare l'etichetta.
1.  Nel**Cell Collegamento**campo, specificare l'indirizzo della cella a cui collegare questa casella di controllo.
1.  Clicca su**OK**.

### **Utilizzando Aspose.Cells**

 Aspose.Cells fornisce il[**CheckBoxCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection) class, che viene utilizzata per aggiungere una nuova casella di controllo alla raccolta. C'è un'altra classe,[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox), che rappresenta una casella di controllo. Ha alcuni membri importanti:

-  Il[**setCella Collegata**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell) metodo specifica una cella che è collegata alla casella di controllo.
-  Il[**impostaTesto**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text) metodo specifica la stringa di testo associata alla casella di controllo. È l'etichetta della casella di controllo.
-  Il[**valore impostato**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value) metodo specifica se la casella di controllo è selezionata o meno.

L'esempio seguente mostra come aggiungere una casella di controllo al foglio di lavoro. L'output seguente viene generato dopo l'esecuzione del codice.

**Una casella di controllo viene aggiunta al foglio di lavoro** 

![cose da fare:immagine_alt_testo](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **Aggiunta del controllo RadioButton al foglio di lavoro**

Un pulsante di opzione, o pulsante di opzione, è un controllo costituito da una casella rotonda. L'utente prende la sua decisione selezionando la casella rotonda. Un pulsante radio è solitamente, se non sempre, accompagnato da altri. Tali pulsanti di opzione appaiono e si comportano come un gruppo. L'utente decide quale pulsante è valido selezionandone solo uno. Quando l'utente fa clic su un pulsante, viene riempito. Quando viene selezionato un pulsante nel gruppo, i pulsanti dello stesso gruppo sono vuoti.

### **Utilizzando Microsoft Excel**

Per posizionare un controllo Pulsante di opzione nel foglio di lavoro, attenersi alla seguente procedura:

1.  Assicurati di**Le forme** viene visualizzata la barra degli strumenti.
1.  Clicca il**Pulsante di opzione** attrezzo.
1. Nel foglio di lavoro, fare clic e trascinare per definire il rettangolo che conterrà il pulsante di opzione e l'etichetta accanto al pulsante di opzione.
1. Una volta posizionato il pulsante di opzione nel foglio di lavoro, spostare il cursore del mouse nell'area dell'etichetta e modificare l'etichetta.
1.  Nel**Cell Collegamento** campo, specificare l'indirizzo della cella a cui questo pulsante di opzione deve essere collegato.
1.  Clic**OK**.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)class fornisce un metodo denominato addShape che può essere utilizzato per aggiungere un controllo pulsante di opzione a un foglio di lavoro. Il metodo può restituire un oggetto RadioButton. La classe RadioButton rappresenta un pulsante di opzione. Ha alcuni membri importanti:

- Il metodo setLinkedCell specifica una cella collegata al pulsante di opzione.
- Il metodo setText specifica la stringa di testo associata al pulsante di opzione. È l'etichetta del pulsante di opzione.
- La proprietà Checked specifica se il pulsante di opzione è selezionato o meno.
- Il metodo setFillFormat specifica il formato di riempimento del pulsante di opzione.
- Il metodo setLineFormat specifica gli stili del formato di linea del pulsante di opzione.

L'esempio seguente mostra come aggiungere pulsanti di opzione a un foglio di lavoro. L'esempio aggiunge tre pulsanti di opzione che rappresentano i gruppi di età. Il seguente output verrebbe generato dopo l'esecuzione del codice.

**Alcuni RadioButton vengono aggiunti al foglio di lavoro** 

![cose da fare:immagine_alt_testo](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

## **Aggiunta di un controllo casella combinata a un foglio di lavoro**

Per semplificare l'immissione dei dati o per limitare le voci a determinati elementi definiti dall'utente, è possibile creare una casella combinata o un elenco a discesa di voci valide compilato da celle in altre parti del foglio di lavoro. Quando crei un elenco a discesa per una cella, viene visualizzata una freccia accanto a tale cella. Per immettere informazioni in tale cella, fare clic sulla freccia e quindi sulla voce desiderata.

### **Utilizzando Microsoft Excel**

Per inserire un controllo casella combinata nel foglio di lavoro, attenersi alla seguente procedura:

1.  Assicurati di**Le forme** viene visualizzata la barra degli strumenti.
1.  Clicca sul**Combo box** attrezzo.
1. Nell'area del foglio di lavoro, fare clic e trascinare per definire il rettangolo che conterrà la casella combinata.
1.  Una volta inserita la casella combinata nel foglio di lavoro, fare clic con il pulsante destro del mouse sul controllo per fare clic**Controllo del formato** e specificare l'intervallo di input.
1.  Nel**Cell Collegamento** campo, specificare l'indirizzo della cella a cui collegare questa casella combinata.
1.  Clicca su**OK**.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)class fornisce un metodo denominato addShape, che può essere utilizzato per aggiungere un controllo casella combinata al foglio di lavoro. Il metodo può restituire un oggetto ComboBox. La classe ComboBox rappresenta una casella combinata. Ha alcuni membri importanti:

- Il metodo setLinkedCell specifica una cella collegata alla casella combinata.
- Il metodo setInputRange specifica l'intervallo di celle del foglio di lavoro utilizzato per riempire la casella combinata.
- Il metodo setDropDownLines specifica il numero di righe di elenco visualizzate nella parte a discesa di una casella combinata.
- Il metodo setShadow indica se la casella combinata dispone di ombreggiatura 3D.

L'esempio seguente mostra come aggiungere una casella combinata al foglio di lavoro. Il seguente output viene generato durante l'esecuzione del codice.

**Una casella combinata viene aggiunta al foglio di lavoro** 

![cose da fare:immagine_alt_testo](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **Aggiunta di un controllo etichetta a un foglio di lavoro**

 Le etichette sono un mezzo per fornire agli utenti informazioni sui contenuti di un foglio di calcolo. Aspose.Cells consente di aggiungere e manipolare etichette in un foglio di lavoro. Il[**Collezione Shape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)class fornisce un metodo denominato addShape, utilizzato per aggiungere un controllo etichetta al foglio di lavoro. Il metodo restituisce un oggetto Label. La classe Label rappresenta un'etichetta nel foglio di lavoro. Ha alcuni membri importanti:

- Il metodo setText specifica la stringa della didascalia di un'etichetta.
- Il metodo setPlacement specifica il PlacementType, il modo in cui l'etichetta è allegata alle celle nel foglio di lavoro.

L'esempio seguente mostra come aggiungere un'etichetta al foglio di lavoro. Il seguente output viene generato durante l'esecuzione del codice.

**Un'etichetta viene aggiunta nel foglio di lavoro**

![cose da fare:immagine_alt_testo](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

## **Aggiunta di un controllo casella di riepilogo a un foglio di lavoro**

Un controllo casella di riepilogo crea un controllo elenco che consente la selezione di uno o più elementi.

### **Utilizzando Microsoft Excel**

Per posizionare un controllo casella di riepilogo in un foglio di lavoro:

1.  Assicurati di**Le forme** viene visualizzata la barra degli strumenti.
1.  Clicca sul**Casella di riepilogo** attrezzo.
1. Nell'area del foglio di lavoro, fare clic e trascinare per definire il rettangolo che conterrà la casella di riepilogo.
1.  Una volta inserita la casella di riepilogo nel foglio di lavoro, fare clic con il pulsante destro del mouse sul controllo per fare clic**Controllo del formato** e specificare l'intervallo di input.
1.  Nel**Cell Collegamento**specificare l'indirizzo della cella a cui collegare questa casella di riepilogo e impostare l'attributo Tipo di selezione (Singola, Multi, Estendi)
1.  Clic**OK**.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class fornisce un metodo denominato addShape, utilizzato per aggiungere un controllo casella di riepilogo a un foglio di lavoro. Il metodo restituisce un oggetto ListBox. La classe ListBox rappresenta una casella di riepilogo. Ha alcuni membri importanti:

- Il metodo setLinkedCell specifica una cella collegata alla casella di riepilogo.
- Il metodo setInputRange specifica l'intervallo di celle del foglio di lavoro utilizzato per riempire la casella di riepilogo.
- Il metodo setSelectionType specifica la modalità di selezione della casella di riepilogo.
- Il metodo setShadow indica se la casella di riepilogo dispone di ombreggiatura 3D.

L'esempio seguente mostra come aggiungere una casella di riepilogo al foglio di lavoro. Il seguente output viene generato durante l'esecuzione del codice.

**Una casella di riepilogo viene aggiunta al foglio di lavoro** 

![cose da fare:immagine_alt_testo](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

## **Aggiunta di controllo pulsante a un foglio di lavoro**

pulsanti sono utili per eseguire alcune azioni. A volte è utile assegnare una macro VBA al pulsante o assegnare un collegamento ipertestuale per aprire una pagina web.

### **Utilizzando Microsoft Excel**

Per posizionare un controllo pulsante nel foglio di lavoro:

1.  Assicurati di**Le forme** viene visualizzata la barra degli strumenti.
1.  Clicca sul**Pulsante** attrezzo.
1. Nell'area del foglio di lavoro, fare clic e trascinare per definire il rettangolo che conterrà il pulsante.
1.  Una volta inserita la casella di riepilogo nel foglio di lavoro, fare clic con il pulsante destro del mouse sul controllo e selezionare**Controllo del formato**, quindi specificare una macro VBA e gli attributi relativi a carattere, allineamento, dimensione, margine ecc.
1.  Clicca su**OK**.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class fornisce un metodo denominato addShape, utilizzato per aggiungere un controllo pulsante al foglio di lavoro. Il metodo può restituire un oggetto Button. La classe Button rappresenta un pulsante. Ha alcuni membri importanti:

- Il metodo setText specifica la didascalia del pulsante.
- Il metodo setPlacement specifica il PlacementType, il modo in cui il pulsante è collegato alle celle nel foglio di lavoro.
- Il metodo addHyperlink aggiunge un collegamento ipertestuale per il controllo pulsante. Facendo clic sul pulsante si accederà all'URL correlato.

L'esempio seguente mostra come aggiungere un pulsante al foglio di lavoro. Il seguente output viene generato durante l'esecuzione del codice

**Un pulsante viene aggiunto nel foglio di lavoro**

![cose da fare:immagine_alt_testo](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **Aggiunta del controllo di linea a un foglio di lavoro**

Aspose.Cells ti consente di disegnare forme automatiche nei tuoi fogli di lavoro. Puoi creare una linea con facilità. Puoi anche formattare la linea. Ad esempio, puoi cambiare il colore della linea, specificare il peso e lo stile della linea per le tue necessità.

### **Utilizzando Microsoft Excel**

1.  Sul**Disegno** barra degli strumenti, fare clic su**AutoForme** , indicare**Linee**e selezionare lo stile di linea desiderato.
1. Trascina per tracciare la linea.
1. Eseguire una o entrambe le seguenti operazioni:
 1. Per vincolare la linea a tracciare angoli di 15 gradi dal suo punto iniziale, tieni premuto MAIUSC mentre trascini.
 1. Per allungare la linea in direzioni opposte rispetto al primo punto finale, tieni premuto CTRL mentre trascini.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)class fornisce un metodo denominato addShape, che viene utilizzato per aggiungere una forma di linea al foglio di lavoro. Il metodo può restituire un oggetto LineShape. La classe LineShape rappresenta una linea. Ha alcuni membri importanti:

- Il metodo setDashStyle specifica il formato di una riga.
- Il metodo setPlacement specifica PlacementType, il modo in cui la linea è collegata alle celle nel foglio di lavoro.

L'esempio seguente mostra come aggiungere righe al foglio di lavoro. Crea tre linee con stili diversi. L'output seguente viene generato dopo l'esecuzione del codice

**Alcune righe vengono aggiunte al foglio di lavoro** 

![cose da fare:immagine_alt_testo](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **Aggiunta di una freccia a una linea**

Aspose.Cells consente anche di disegnare linee di frecce. È possibile aggiungere una freccia a una riga e formattare la riga. Ad esempio, puoi modificare il colore della linea o specificare lo spessore e lo stile della linea.

L'esempio seguente mostra come aggiungere una freccia a una linea. Il seguente output viene generato durante l'esecuzione del codice.

**Nel foglio di lavoro viene aggiunta una linea con la punta della freccia** 

![cose da fare:immagine_alt_testo](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **Aggiunta di un controllo rettangolo a un foglio di lavoro**

Aspose.Cells ti consente di disegnare forme rettangolari nei tuoi fogli di lavoro. Puoi creare un rettangolo, un quadrato, ecc. Puoi anche formattare il colore di riempimento e il colore della linea del bordo del controllo. Ad esempio, puoi cambiare il colore del rettangolo, impostare il colore dell'ombreggiatura, specificare il peso e lo stile del rettangolo per le tue necessità.

### **Utilizzando Microsoft Excel**

1.  Sul**Disegno** barra degli strumenti, fare clic su**Rettangolo**.
1. Trascina per disegnare il rettangolo.
1. Eseguire una o entrambe le seguenti operazioni:
 1. Per vincolare il rettangolo a disegnare un quadrato dal suo punto iniziale, tieni premuto MAIUSC mentre trascini.
 1. Per disegnare un rettangolo da un punto centrale, tieni premuto CTRL mentre trascini.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class fornisce un metodo denominato addShape, che viene utilizzato per aggiungere una forma rettangolare a un foglio di lavoro. Il metodo può restituire un oggetto RectangleShape. La classe RectangleShape rappresenta un rettangolo. Ha alcuni membri importanti:

- Il metodo setLineFormat specifica gli attributi del formato di linea di un rettangolo.
- Il metodo setPlacement specifica il PlacementType, il modo in cui il rettangolo è attaccato alle celle nel foglio di lavoro.
- La proprietà FillFormat specifica gli stili del formato di riempimento di un rettangolo.

L'esempio seguente mostra come aggiungere un rettangolo al foglio di lavoro. Il seguente output viene generato durante l'esecuzione del codice.

**Un rettangolo viene aggiunto nel foglio di lavoro** 

![cose da fare:immagine_alt_testo](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **Aggiunta del controllo dell'arco al foglio di lavoro**

Aspose.Cells ti consente di disegnare forme ad arco nei tuoi fogli di lavoro. Puoi creare archi semplici e pieni. Puoi formattare il colore di riempimento e il colore della linea del bordo del controllo. Ad esempio, puoi specificare / modificare il colore dell'arco, impostare il colore dell'ombreggiatura, specificare il peso e lo stile della forma per le tue necessità.

### **Utilizzando Microsoft Excel**

1.  Sul**Disegno** barra degli strumenti, fare clic su**Arco** nel**AutoForme**.
1. Trascina per disegnare l'arco.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class fornisce un metodo denominato addShape, che viene utilizzato per aggiungere una forma ad arco al foglio di lavoro. Il metodo può restituire un oggetto ArcShape. La classe ArcShape rappresenta un arco. Ha alcuni membri importanti:

- Il metodo setLineFormat specifica gli attributi del formato linea di una forma ad arco.
- Il metodo setPlacement specifica il PlacementType, il modo in cui l'arco è collegato alle celle nel foglio di lavoro.
- La proprietà FillFormat specifica gli stili del formato di riempimento della forma.

L'esempio seguente mostra come aggiungere forme ad arco al foglio di lavoro. L'esempio crea due forme ad arco: una è piena e l'altra è semplice. Il seguente output viene generato durante l'esecuzione del codice

**Due forme ad arco vengono aggiunte al foglio di lavoro** 

![cose da fare:immagine_alt_testo](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **Aggiunta del controllo ovale a un foglio di lavoro**

Aspose.Cells consente di disegnare forme ovali nei fogli di lavoro. Crea forme ovali semplici e piene e formatta il colore di riempimento e il colore della linea del bordo del controllo. Ad esempio, puoi specificare / modificare il colore dell'ovale, impostare il colore dell'ombreggiatura, specificare il peso e lo stile della forma.

### **Utilizzando Microsoft Excel**

1.  Sul**Disegno** barra degli strumenti, fare clic su**Ovale** .
1. Trascina per disegnare l'ovale.
1. Eseguire una o entrambe le seguenti operazioni:
 1. Per vincolare l'ovale a disegnare un cerchio dal suo punto iniziale, tieni premuto MAIUSC mentre trascini.
1. Per disegnare un ovale da un punto centrale, tieni premuto CTRL mentre trascini.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class fornisce un metodo denominato addShape, che viene utilizzato per aggiungere una forma ovale a un foglio di lavoro. Il metodo può restituire un oggetto Oval. La classe Oval rappresenta una forma ovale. Ha alcuni membri importanti:

- Il metodo setLineFormat specifica gli attributi del formato della linea di una forma ovale.
-  Il metodo setPlacement specifica il**Tipo di posizionamento** , il modo in cui l'ovale è collegato alle celle nel foglio di lavoro.
- La proprietà FillFormat specifica gli stili del formato di riempimento della forma.

L'esempio seguente mostra come aggiungere forme ovali al foglio di lavoro. L'esempio crea due forme ovali: una è un ovale pieno, l'altra è un semplice cerchio. Il seguente output viene generato durante l'esecuzione del codice.

**Nel foglio di lavoro vengono aggiunte due forme ovali** 

![cose da fare:immagine_alt_testo](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **Argomenti avanzati**
- [Aggiungi controlli ActiveX utilizzando Aspose.Cells](/cells/it/java/add-activex-controls-using-aspose-cells/)
- [Rimuovere il controllo ActiveX](/cells/it/java/remove-activex-control/)
