---
title: Gestione dei controlli
type: docs
weight: 150
url: /it/net/managing-controls/
---
## **introduzione**

Gli sviluppatori possono aggiungere diversi oggetti di disegno come caselle di testo, caselle di controllo, pulsanti di opzione, caselle combinate, etichette, pulsanti, linee, rettangoli, archi, ovali, caselle di selezione, barre di scorrimento, caselle di gruppo ecc. Aspose.Cells fornisce lo spazio dei nomi Aspose.Cells.Drawing che contiene tutti gli oggetti di disegno. Tuttavia, ci sono alcuni oggetti o forme di disegno che non sono ancora supportati. Creare questi oggetti di disegno in un foglio di calcolo del designer utilizzando Microsoft Excel e quindi importare il foglio di calcolo del designer in Aspose.Cells. Aspose.Cells consente di caricare questi oggetti di disegno da un foglio di calcolo del designer e scriverli in un file generato.

## **Aggiunta di un controllo casella di testo a un foglio di lavoro**

 Un modo per evidenziare informazioni importanti in un report consiste nell'utilizzare una casella di testo. Ad esempio, aggiungi del testo per evidenziare il nome dell'azienda o per indicare la regione geografica con le maggiori vendite ecc. Aspose.Cells fornisce il[**Collezione Casella di testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection) class, utilizzato per aggiungere una nuova casella di testo alla raccolta. C'è un'altra classe,[**Casella di testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox), che rappresenta una casella di testo utilizzata per definire tutti i tipi di impostazioni. Ha alcuni membri importanti:

-  Il[**Cornice di testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) restituzione della proprietà a[**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe) oggetto utilizzato per regolare il contenuto della casella di testo.
-  Il[**Posizionamento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) proprietà specifica il tipo di posizionamento.
-  Il[**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) proprietà specifica gli attributi del carattere.
-  Il[**Aggiungicollegamento ipertestuale**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink)Il metodo aggiunge un collegamento ipertestuale per la casella di testo.
-  Il[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) proprietà restituisce un[**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat) oggetto utilizzato per impostare il formato di riempimento per la casella di testo.
-  Il[**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) proprietà restituisce il[**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat) oggetto solitamente utilizzato per definire lo stile e lo spessore della riga della casella di testo.
-  Il[**Testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) La proprietà specifica il testo di input per la casella di testo.

L'esempio seguente crea due caselle di testo nel primo foglio di lavoro della cartella di lavoro. La prima casella di testo è ben fornita con diverse impostazioni di formato. Il secondo è semplice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Manipolazione dei controlli della casella di testo nei fogli di calcolo di Designer**

 Aspose.Cells consente inoltre di accedere alle caselle di testo nei fogli di lavoro del designer e di manipolarle. Utilizzare il[**Foglio di lavoro.Caselle di testo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) property per ottenere la raccolta di caselle di testo nel foglio.

L'esempio seguente utilizza il file Microsoft Excel creato nell'esempio precedente. Ottiene le stringhe di testo delle due caselle di testo e modifica il testo della seconda casella di testo per salvare il file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **Aggiunta di un controllo casella di controllo a un foglio di lavoro**

Le caselle di controllo sono utili se si desidera fornire a un utente un modo per scegliere tra due opzioni, come true o false; sì o no. Aspose.Cells consente di utilizzare le caselle di controllo nei fogli di lavoro. Ad esempio, potresti aver sviluppato un foglio di lavoro per la proiezione finanziaria in cui puoi tenere conto di una particolare acquisizione o meno. In questo caso, potresti voler inserire una casella di controllo nella parte superiore del foglio di lavoro. È quindi possibile collegare lo stato di questa casella di controllo a un'altra cella, in modo che se la casella di controllo è selezionata, il valore della cella sia True; se non è selezionato, il valore della cella è False.

### **Utilizzo di Microsoft Excel**

Per posizionare un controllo casella di controllo nel foglio di lavoro, attenersi alla seguente procedura:

1. Assicurati che la barra degli strumenti Moduli sia visualizzata.
1.  Clicca il**Casella di controllo** strumento sulla barra degli strumenti Moduli.
1. Nell'area del foglio di lavoro, fare clic e trascinare per definire il rettangolo che conterrà la casella di controllo e l'etichetta accanto alla casella di controllo.
1. Una volta posizionata la casella di controllo, spostare il cursore del mouse nell'area dell'etichetta e modificare l'etichetta.
1.  Nel**Cell Collegamento**campo, specificare l'indirizzo della cella a cui collegare questa casella di controllo.
1.  Clicca su**OK**.

### **Utilizzando Aspose.Cells**

 Aspose.Cells fornisce il[**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection) class, che viene utilizzata per aggiungere una nuova casella di controllo alla raccolta. C'è un'altra classe,[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox), che rappresenta una casella di controllo. Ha alcuni membri importanti:

-  Il[**Cella collegata**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La proprietà specifica una cella collegata alla casella di controllo.
-  Il[**Testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) La proprietà specifica la stringa di testo associata alla casella di controllo. È l'etichetta della casella di controllo.
-  Il[**Valore**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) La proprietà specifica se la casella di controllo è selezionata o meno.

L'esempio seguente mostra come aggiungere una casella di controllo al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **Aggiunta del controllo del pulsante di opzione al foglio di lavoro**

Un pulsante di opzione, o pulsante di opzione, è un controllo costituito da una casella rotonda. L'utente prende la sua decisione selezionando la casella rotonda. Un pulsante radio è solitamente, se non sempre, accompagnato da altri. Tali pulsanti di opzione appaiono e si comportano come un gruppo. L'utente decide quale pulsante è valido selezionandone solo uno. Quando l'utente fa clic su un pulsante, viene riempito. Quando viene selezionato un pulsante nel gruppo, i pulsanti dello stesso gruppo sono vuoti.

### **Utilizzo di Microsoft Excel**

Per posizionare un controllo Pulsante di opzione nel foglio di lavoro, attenersi alla seguente procedura:

1.  Assicurati di**Le forme** viene visualizzata la barra degli strumenti.
1.  Clicca il**Pulsante di opzione** attrezzo.
1. Nel foglio di lavoro, fare clic e trascinare per definire il rettangolo che conterrà il pulsante di opzione e l'etichetta accanto al pulsante di opzione.
1. Una volta posizionato il pulsante di opzione nel foglio di lavoro, spostare il cursore del mouse nell'area dell'etichetta e modificare l'etichetta.
1.  Nel**Cell Collegamento** campo, specificare l'indirizzo della cella a cui questo pulsante di opzione deve essere collegato.
1.  Clic**OK**.

### **Utilizzando Aspose.Cells**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**Aggiungi pulsante radio**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton) , utilizzato per aggiungere un controllo pulsante di opzione a un foglio di lavoro. Il metodo restituisce un[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) oggetto. La classe[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton)rappresenta un pulsante di opzione. Ha alcuni membri importanti:

-  Il[**Cella collegata**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La proprietà specifica una cella che è collegata al pulsante di opzione.
-  Il[**Testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) La proprietà specifica la stringa di testo associata al pulsante di opzione. È l'etichetta del pulsante di opzione.
-  Il[**È verificato**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) La proprietà specifica se il pulsante di opzione è selezionato o meno.
-  Il[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) La proprietà specifica il formato di riempimento del pulsante di opzione.
-  Il[**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) La proprietà specifica gli stili del formato di linea del pulsante di opzione.

L'esempio seguente mostra come aggiungere pulsanti di opzione a un foglio di lavoro. L'esempio aggiunge tre pulsanti di opzione che rappresentano i gruppi di età.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

## **Aggiunta di un controllo casella combinata a un foglio di lavoro**

Per semplificare l'immissione dei dati o per limitare le voci a determinati elementi definiti dall'utente, è possibile creare una casella combinata o un elenco a discesa di voci valide compilato da celle in altre parti del foglio di lavoro. Quando crei un elenco a discesa per una cella, viene visualizzata una freccia accanto a tale cella. Per immettere informazioni in tale cella, fare clic sulla freccia e quindi sulla voce desiderata.

### **Utilizzo di Microsoft Excel**

Per inserire un controllo casella combinata nel foglio di lavoro, attenersi alla seguente procedura:

1.  Assicurati di**Le forme** viene visualizzata la barra degli strumenti.
1.  Clicca sul**Combo box** attrezzo.
1. Nell'area del foglio di lavoro, fare clic e trascinare per definire il rettangolo che conterrà la casella combinata.
1.  Una volta inserita la casella combinata nel foglio di lavoro, fare clic con il pulsante destro del mouse sul controllo per fare clic**Controllo del formato** e specificare l'intervallo di input.
1.  Nel**Cell Collegamento** campo, specificare l'indirizzo della cella a cui collegare questa casella combinata.
1.  Clicca su**OK**.

### **Utilizzando Aspose.Cells**

 Il[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**AggiungiComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox) , utilizzato per aggiungere un controllo casella combinata a un foglio di lavoro. Il metodo restituisce un[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) oggetto. La classe[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) rappresenta una casella combinata. Ha alcuni membri importanti:

-  Il[**Cella collegata**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La proprietà specifica una cella collegata alla casella combinata.
-  Il[**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) La proprietà specifica l'intervallo di celle del foglio di lavoro utilizzato per riempire la casella combinata.
-  Il[**DropDownLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines)La proprietà specifica il numero di righe dell'elenco visualizzate nella parte a discesa di una casella combinata.
-  Il[**Ombra**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) La proprietà indica se la casella combinata ha l'ombreggiatura 3D.

L'esempio seguente mostra come aggiungere una casella combinata al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **Aggiunta di un controllo etichetta a un foglio di lavoro**

 Le etichette sono un mezzo per fornire agli utenti informazioni sui contenuti di un foglio di calcolo. Aspose.Cells consente di aggiungere e manipolare etichette in un foglio di lavoro. Il[**Collezione Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**Aggiungi etichetta**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel) , utilizzato per aggiungere un controllo etichetta al foglio di lavoro. Il metodo restituisce a[**Etichetta**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) oggetto. La classe[**Etichetta**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) rappresenta un'etichetta nel foglio di lavoro. Ha alcuni membri importanti:

-  Il[**Testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) metodo specifica la stringa di didascalia di un'etichetta.
-  Il[**Posizionamento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) metodo specifica il[**Tipo di posizionamento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), il modo in cui l'etichetta è attaccata alle celle nel foglio di lavoro.

L'esempio seguente mostra come aggiungere un'etichetta al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

## **Aggiunta di un controllo casella di riepilogo a un foglio di lavoro**

Un controllo casella di riepilogo crea un controllo elenco che consente la selezione di uno o più elementi.

### **Utilizzo di Microsoft Excel**

Per posizionare un controllo casella di riepilogo in un foglio di lavoro:

1.  Assicurati di**Le forme** viene visualizzata la barra degli strumenti.
1.  Clicca sul**Casella di riepilogo** attrezzo.
1. Nell'area del foglio di lavoro, fare clic e trascinare per definire il rettangolo che conterrà la casella di riepilogo.
1.  Una volta inserita la casella di riepilogo nel foglio di lavoro, fare clic con il pulsante destro del mouse sul controllo per fare clic**Controllo del formato** e specificare l'intervallo di input.
1.  Nel**Cell Collegamento**specificare l'indirizzo della cella a cui collegare questa casella di riepilogo e impostare l'attributo Tipo di selezione (Singola, Multi, Estendi)
1.  Clic**OK**.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox) , utilizzato per aggiungere un controllo casella di riepilogo a un foglio di lavoro. Il metodo restituisce a[**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) oggetto. La classe[**Casella di riepilogo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) rappresenta una casella di riepilogo. Ha alcuni membri importanti:

-  Il[**Cella collegata**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)metodo specifica una cella collegata alla casella di riepilogo.
-  Il[**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) metodo specifica l'intervallo di celle del foglio di lavoro utilizzato per riempire la casella di riepilogo.
-  Il[**Tipo di selezione**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype) metodo specifica la modalità di selezione della casella di riepilogo.
-  Il[**Ombra**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) Il metodo indica se la casella di riepilogo dispone di ombreggiatura 3D.

L'esempio seguente mostra come aggiungere una casella di riepilogo al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **Aggiunta di controllo pulsante a un foglio di lavoro**

pulsanti sono utili per eseguire alcune azioni. A volte è utile assegnare una macro VBA al pulsante o assegnare un collegamento ipertestuale per aprire una pagina web.

### **Utilizzo di Microsoft Excel**

Per posizionare un controllo pulsante nel foglio di lavoro:

1.  Assicurati di**Le forme** viene visualizzata la barra degli strumenti.
1.  Clicca sul**Pulsante** attrezzo.
1. Nell'area del foglio di lavoro, fare clic e trascinare per definire il rettangolo che conterrà il pulsante.
1.  Una volta inserita la casella di riepilogo nel foglio di lavoro, fare clic con il pulsante destro del mouse sul controllo e selezionare**Controllo del formato**, quindi specificare una macro VBA e gli attributi relativi a carattere, allineamento, dimensione, margine ecc.
1.  Clicca su**OK**.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**Pulsante Aggiungi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton) , utilizzato per aggiungere un controllo pulsante al foglio di lavoro. Il metodo restituisce un[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) oggetto. La classe[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) rappresenta un pulsante. Ha alcuni membri importanti:

-  Il[**Testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) La proprietà specifica la didascalia del pulsante.
-  Il[**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) La proprietà specifica gli attributi del carattere per l'etichetta del controllo pulsante.
-  Il[**Posizionamento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) proprietà specifica il[**Tipo di posizionamento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), il modo in cui il pulsante è collegato alle celle nel foglio di lavoro.
-  Il[**Aggiungicollegamento ipertestuale**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) La proprietà aggiunge un collegamento ipertestuale per il controllo pulsante. Facendo clic sul pulsante si accederà all'URL correlato.

L'esempio seguente mostra come aggiungere un pulsante al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **Aggiunta del controllo di linea al foglio di lavoro**

### **Utilizzo di Microsoft Excel**

1.  Sul**Disegno** barra degli strumenti, fare clic su**AutoForme** , indicare**Linee**e selezionare lo stile di linea desiderato.
1. Trascina per tracciare la linea.
1. Eseguire una o entrambe le seguenti operazioni:
 1. Per vincolare la linea a tracciare angoli di 15 gradi dal suo punto iniziale, tieni premuto MAIUSC mentre trascini.
 1. Per allungare la linea in direzioni opposte rispetto al primo punto finale, tieni premuto CTRL mentre trascini.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline) che viene utilizzato per aggiungere una forma di linea al foglio di lavoro. Il metodo restituisce a[**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) oggetto. La classe[**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) rappresenta una linea. Ha alcuni membri importanti:

-  Il[**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) metodo specifica il formato di una riga.
-  Il[**Posizionamento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) metodo specifica il[**Tipo di posizionamento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), il modo in cui la linea è collegata alle celle nel foglio di lavoro.

L'esempio seguente mostra come aggiungere righe al foglio di lavoro. Crea tre linee con stili diversi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **Aggiunta di una punta di freccia a una linea**

Aspose.Cells consente anche di disegnare linee di frecce. È possibile aggiungere una freccia a una riga e formattare la riga. Ad esempio, puoi modificare il colore della linea o specificare lo spessore e lo stile della linea.

L'esempio seguente mostra come aggiungere una freccia a una linea.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **Aggiunta di un controllo rettangolo a un foglio di lavoro**

Aspose.Cells ti consente di disegnare forme rettangolari nei tuoi fogli di lavoro. Puoi creare un rettangolo, un quadrato, ecc. Puoi anche formattare il colore di riempimento e il colore della linea del bordo del controllo. Ad esempio, puoi cambiare il colore del rettangolo, impostare il colore dell'ombreggiatura, specificare il peso e lo stile del rettangolo per le tue necessità.

### **Utilizzo di Microsoft Excel**

1.  Sul**Disegno** barra degli strumenti, fare clic su**Rettangolo**.
1. Trascina per disegnare il rettangolo.
1. Eseguire una o entrambe le seguenti operazioni:
 1. Per vincolare il rettangolo a disegnare un quadrato dal suo punto iniziale, tieni premuto MAIUSC mentre trascini.
 1. Per disegnare un rettangolo da un punto centrale, tieni premuto CTRL mentre trascini.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**AggiungiRettangolo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle) , utilizzato per aggiungere una forma rettangolare a un foglio di lavoro. Il metodo ritorna[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) oggetto. La classe[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) rappresenta un rettangolo. Ha alcuni membri importanti:

-  Il[**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) La proprietà specifica gli attributi del formato di linea di un rettangolo.
-  Il[**Posizionamento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) proprietà specifica il[**Tipo di posizionamento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), il modo in cui il rettangolo è collegato alle celle nel foglio di lavoro.
-  Il[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) La proprietà specifica gli stili del formato di riempimento di un rettangolo.

L'esempio seguente mostra come aggiungere un rettangolo al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **Aggiunta del controllo dell'arco al foglio di lavoro**

Aspose.Cells ti consente di disegnare forme ad arco nei tuoi fogli di lavoro. Puoi creare archi semplici e pieni. Puoi formattare il colore di riempimento e il colore della linea del bordo del controllo. Ad esempio, puoi specificare / modificare il colore dell'arco, impostare il colore dell'ombreggiatura, specificare il peso e lo stile della forma per le tue necessità.

### **Utilizzo di Microsoft Excel**

1.  Sul**Disegno** barra degli strumenti, fare clic su**Arco** nel**AutoForme**.
1. Trascina per disegnare l'arco.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**AggiungiArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc) , che viene utilizzato per aggiungere una forma ad arco a un foglio di lavoro. Il metodo restituisce un[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) oggetto. La classe[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape)rappresenta un arco. Ha alcuni membri importanti:

-  Il[**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) La proprietà specifica gli attributi del formato linea di una forma ad arco.
-  Il[**Posizionamento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) proprietà specifica il[**Tipo di posizionamento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), il modo in cui l'arco è collegato alle celle nel foglio di lavoro.
-  Il[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) La proprietà specifica gli stili del formato di riempimento della forma.
-  Il[**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) La proprietà specifica l'indice della riga nell'angolo inferiore destro.
-  Il[**Colonna in basso a destra**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) La proprietà specifica l'indice della colonna nell'angolo inferiore destro.

L'esempio seguente mostra come aggiungere forme ad arco al foglio di lavoro. L'esempio crea due forme ad arco: una è piena e l'altra è semplice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **Aggiunta del controllo ovale a un foglio di lavoro**

Aspose.Cells consente di disegnare forme ovali nei fogli di lavoro. Crea forme ovali semplici e piene e formatta il colore di riempimento e il colore della linea del bordo del controllo. Ad esempio, puoi specificare / modificare il colore dell'ovale, impostare il colore dell'ombreggiatura, specificare il peso e lo stile della forma.

### **Utilizzo di Microsoft Excel**

-  Sul*Disegno* barra degli strumenti, fare clic su*Ovale*.
- Trascina per disegnare l'ovale.
- Eseguire una o entrambe le seguenti operazioni:
- Per vincolare l'ovale a disegnare un cerchio dal suo punto iniziale, tieni premuto MAIUSC mentre trascini.
- Per disegnare un ovale da un punto centrale, tieni premuto CTRL mentre trascini.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**AggiungiOvale**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval) , utilizzato per aggiungere una forma ovale a un foglio di lavoro. Il metodo restituisce un[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) oggetto. La classe[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) rappresenta una forma ovale. Ha alcuni membri importanti:

-  Il[**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) La proprietà specifica gli attributi del formato della linea di una forma ovale.
-  Il[**Posizionamento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) proprietà specifica il[**Tipo di posizionamento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)il modo in cui l'ovale è collegato alle celle nel foglio di lavoro.
-  Il[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) La proprietà specifica gli stili del formato di riempimento della forma.
-  Il[**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) La proprietà specifica l'indice della riga nell'angolo inferiore destro.
-  Il[**Colonna in basso a destra**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) La proprietà specifica l'indice della colonna nell'angolo inferiore destro.

L'esempio seguente mostra come aggiungere forme ovali al foglio di lavoro. L'esempio crea due forme ovali: una è un ovale pieno, l'altra è un semplice cerchio.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **Aggiunta del controllo Spinner al foglio di lavoro**

 Una casella di selezione è una casella di testo associata a un pulsante (denominato pulsante di selezione) costituita da una freccia su e una freccia giù su cui fare clic per modificare in modo incrementale il valore nella casella di testo. Usando le caselle di selezione, puoi vedere come le modifiche di input al tuo modello finanziario altereranno gli output del modello. Puoi collegare un pulsante di selezione a una specifica cella di input. Mentre fai clic sulla freccia su o giù sul pulsante di selezione, il valore intero nella cella di input di destinazione aumenta o diminuisce.*Aspose.Cells* ti consente di creare filatori nei tuoi fogli di lavoro.

### **Utilizzo di Microsoft Excel**

Per posizionare un controllo casella di selezione nel foglio di lavoro:

-  Assicurati di*Le forme* viene visualizzata la barra degli strumenti.
-  Clicca il*Filatore* attrezzo.
- Nell'area del tuo foglio di lavoro, fai clic e trascina per definire il rettangolo che conterrà la trottola.
- Una volta inserito lo spinner nel foglio di lavoro, fare clic con il pulsante destro del mouse sul controllo e fare clic*Controllo del formato* e specificare i valori massimo, minimo e incrementale.
-  Nel*Cell Collegamento* specificare l'indirizzo della cella a cui collegare questa spin box.
-  Clicca su*OK*.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**Aggiungi Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner) , utilizzato per aggiungere un controllo casella di selezione a un foglio di lavoro. Il metodo restituisce un[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) oggetto. La classe[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) rappresenta una casella numerica. Ha alcuni membri importanti:

-  Il[**Cella collegata**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La proprietà specifica una cella che è collegata alla casella numerica.
-  Il[**Massimo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) La proprietà specifica il valore massimo per l'intervallo della casella di selezione.
-  Il[**min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) La proprietà specifica il valore minimo per l'intervallo della casella di selezione.
-  Il[**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) La proprietà specifica l'importo del valore per il quale uno spinner viene incrementato di una riga di scorrimento.
-  Il[**Ombra**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) La proprietà indica se la casella numerica ha l'ombreggiatura 3D.
-  Il[**Valore corrente**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) La proprietà specifica il valore corrente della casella numerica.

L'esempio seguente mostra come aggiungere una casella numerica al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **Aggiunta del controllo della barra di scorrimento a un foglio di lavoro**

Un controllo barra di scorrimento viene utilizzato per selezionare i dati in un foglio di lavoro in modo simile a un controllo casella di selezione. Aggiungendo il controllo a un foglio di lavoro e collegandolo a una cella, è possibile restituire un valore numerico per la posizione corrente del controllo.

### **Utilizzo di Microsoft Excel**

-  Per aggiungere una barra di scorrimento in Excel 2003 e nelle versioni precedenti, fare clic su*Barra di scorrimento* pulsante sul*Le forme* barra degli strumenti, quindi creare una barra di scorrimento che copra le celle B2:B6 in altezza e sia circa un quarto della larghezza della colonna.
-  Per aggiungere una barra di scorrimento in Excel 2007, fare clic su*Sviluppatore* scheda, fare clic*Inserire* e quindi fare clic su*Barra di scorrimento* nella sezione Controlli modulo.
-  Fare clic con il pulsante destro del mouse sulla barra di scorrimento, quindi fare clic*Controllo del formato*.
-  Digitare le seguenti informazioni e fare clic*OK*:
 - Nel*Valore corrente* scatola, tipo 1.
 - Nel*Valore minimo* casella, digitare 1. Questo valore restringe la parte superiore della barra di scorrimento al primo elemento dell'elenco.
 - Nel*Valore massimo* casella, digitare 20. Questo numero specifica il numero massimo di voci nell'elenco.
 - Nel*Cambio incrementale*casella, digitare 1. Questo valore controlla di quanti numeri il controllo della barra di scorrimento incrementa il valore corrente.
 - Nel*Cambio pagina* casella, digitare 5. Questa voce controlla di quanto verrà incrementato il valore corrente se si fa clic all'interno della barra di scorrimento su entrambi i lati della casella di scorrimento.
 - Per inserire un valore numerico nella cella G1 (a seconda dell'elemento selezionato nell'elenco), digitare G1 nel*Cell collegamento* scatola.
- Fare clic su qualsiasi cella in modo che la barra di scorrimento non sia selezionata.

Quando si fa clic sul controllo su o giù sulla barra di scorrimento, la cella G1 viene aggiornata a un numero che indica il valore corrente della barra di scorrimento più o meno la modifica incrementale della barra di scorrimento.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**AggiungiScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar) , utilizzato per aggiungere un controllo barra di scorrimento al foglio di lavoro. Il metodo restituisce un[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) oggetto. La classe[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) rappresenta una barra di scorrimento. Ha alcuni membri importanti:

-  Il[**Cella collegata**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La proprietà specifica una cella collegata alla barra di scorrimento.
-  Il[**Massimo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) La proprietà specifica il valore massimo per l'intervallo della barra di scorrimento.
-  Il[**min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min)specifica il valore minimo per l'intervallo della barra di scorrimento.
-  Il[**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) specifica la quantità di valore per la quale una barra di scorrimento viene incrementata di una riga di scorrimento.
-  Il[**Ombra**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) La proprietà indica se la barra di scorrimento ha l'ombreggiatura 3D.
-  Il[**Valore corrente**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) La proprietà specifica il valore corrente della barra di scorrimento.
-  Il[**Cambio pagina**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange) La proprietà specifica di quanto verrà incrementato il valore corrente se si fa clic all'interno della barra di scorrimento su entrambi i lati della casella di scorrimento.

L'esempio seguente mostra come aggiungere una barra di scorrimento al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **Aggiunta del controllo GroupBox ai controlli di gruppo in un foglio di lavoro**

A volte è necessario implementare pulsanti di opzione o altri controlli che appartengono a un determinato gruppo, è possibile implementare includendo una casella di gruppo o un controllo rettangolo. Ognuno di questi due oggetti fungerebbe da delimitatore del gruppo. Dopo aver aggiunto una di queste forme, puoi aggiungere due o più pulsanti di opzione o altri oggetti di gruppo.

### **Utilizzo di Microsoft Excel**

Per posizionare un controllo casella di gruppo nel foglio di lavoro e inserire i controlli al suo interno:

- Per avviare un modulo, nel menu principale, fare clic su*Visualizzazione* , seguito da*Barre degli strumenti* e*Le forme*.
-  Sul*Le forme* barra degli strumenti, fare clic su*Casella di gruppo* e disegna un rettangolo sul foglio di lavoro.
- Digita una stringa di didascalia per la casella.
-  Sul*Le forme* barra degli strumenti, fare clic su*Pulsante di opzione* e fare clic all'interno del*Casella di gruppo* appena sotto la stringa della didascalia.
-  Dal*Le forme* di nuovo sulla barra degli strumenti, fare clic su*Pulsante di opzione* e fare clic all'interno del*Casella di gruppo* sotto il primo pulsante di opzione.
-  Ancora una volta sul*Le forme* barra degli strumenti, fare clic su*Pulsante di opzione* e fare clic all'interno del*Casella di gruppo* sotto il pulsante di opzione precedente.

### **Utilizzando Aspose.Cells**

 Il[**Collezione Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**AddGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox) , utilizzato per aggiungere un controllo casella di gruppo al foglio di lavoro. Il metodo restituisce un[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) oggetto. Inoltre, il[**Gruppo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) metodo del[**Collezione Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class raggruppa le forme, ci vuole a[**Forma**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) array come parametro e restituisce a[**GroupShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape) oggetto. La classe[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) rappresenta una casella di gruppo. Ha alcuni membri importanti:

-  Il[**Testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) La proprietà specifica la stringa di didascalia della casella di gruppo.
-  Il[**Ombra**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) La proprietà indica se la casella di gruppo ha l'ombreggiatura 3D.

L'esempio seguente mostra come aggiungere una casella di gruppo e raggruppare i controlli nel foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **Argomenti avanzati**
- [Aggiungi controlli ActiveX utilizzando Aspose.Cells](/cells/it/net/add-activex-controls-using-aspose-cells/)
- [Rimuovere il controllo ActiveX](/cells/it/net/remove-activex-control/)
- [Aggiorna controllo ComboBox ActiveX](/cells/it/net/update-activex-combobox-control/)
