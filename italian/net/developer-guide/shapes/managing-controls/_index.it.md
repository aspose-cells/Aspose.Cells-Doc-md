---
title: Gestione dei controlli
type: docs
weight: 150
url: /it/net/managing-controls/
---

## **Introduzione**

Gli sviluppatori possono aggiungere diversi oggetti di disegno come caselle di testo, caselle di controllo, pulsanti di opzione, menu a discesa, etichette, pulsanti, linee, rettangoli, archi, ovali, spinner, barre di scorrimento, gruppi, ecc. Aspose.Cells fornisce lo spazio dei nomi Aspose.Cells.Drawing che contiene tutti gli oggetti di disegno. Tuttavia, alcuni oggetti di disegno o forme non sono ancora supportati. Creare questi oggetti di disegno in un foglio di calcolo del designer usando Microsoft Excel e quindi importare il foglio di calcolo del designer in Aspose.Cells. Aspose.Cells consente di caricare questi oggetti di disegno da un foglio di calcolo del designer e scriverli in un file generato.

## **Aggiunta di un controllo casella di testo a un foglio di calcolo**

Un modo per evidenziare informazioni importanti in un report è utilizzare una casella di testo. Ad esempio, aggiungere testo per evidenziare il nome dell'azienda o per indicare la regione geografica con le vendite più alte, ecc. Aspose.Cells fornisce la classe [**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection), utilizzata per aggiungere una nuova casella di testo alla collezione. C'è anche un'altra classe, [**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox), che rappresenta una casella di testo utilizzata per definire tutti i tipi di impostazioni. Ha alcuni membri importanti:

- La proprietà [**TextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) restituisce un oggetto [**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe) utilizzato per regolare i contenuti della casella di testo.
- La proprietà [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) specifica il tipo di posizionamento.
- La proprietà [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) specifica gli attributi del font.
- Il metodo [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) aggiunge un collegamento ipertestuale per la casella di testo.
- La proprietà [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) restituisce un oggetto [**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat) utilizzato per impostare il formato di riempimento per la casella di testo.
- La proprietà [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) restituisce l'oggetto [**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat) di solito usato per lo stile e lo spessore della linea della casella di testo.
- La proprietà [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) specifica il testo di input per la casella di testo.

Nell'esempio seguente vengono create due caselle di testo nel primo foglio di lavoro del documento. La prima casella di testo è ben arredata con diverse impostazioni di formato. La seconda è semplice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Manipolazione dei controlli casella di testo nei fogli di calcolo progettati**

Aspose.Cells consente anche di accedere alle caselle di testo nei fogli di lavoro del designer e manipolarle. Utilizzare la proprietà [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) per ottenere la raccolta delle caselle di testo nel foglio.

Nell'esempio seguente viene utilizzato il file Microsoft Excel che abbiamo creato nell'esempio precedente. Ottiene le stringhe di testo delle due caselle di testo e modifica il testo della seconda casella di testo per salvare il file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **Aggiunta di un controllo casella di controllo a un foglio di calcolo**

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

Aspose.Cells fornisce la classe [**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection), che viene utilizzata per aggiungere una nuova casella di controllo alla raccolta. C'è un'altra classe, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox), che rappresenta una casella di controllo. Ha alcuni membri importanti:

- La proprietà [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) specifica una cella che è collegata alla casella di controllo.
- La proprietà [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) specifica la stringa di testo associata alla casella di controllo. È l'etichetta della casella di controllo.
- La proprietà [**Value**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) specifica se la casella di controllo è selezionata o meno.

L'esempio seguente mostra come aggiungere una casella di controllo al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **Aggiungere un controllo pulsante di opzione al foglio di lavoro**

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

La classe [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**AddRadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton), che viene utilizzato per aggiungere un controllo pulsante di opzione a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton). La classe [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) rappresenta un pulsante di opzione. Ha alcuni membri importanti:

- La proprietà [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) specifica una cella che è collegata al pulsante di opzione.
- La proprietà [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) specifica la stringa di testo associata al pulsante di opzione. È l'etichetta del pulsante di opzione.
- La proprietà [**IsChecked**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) specifica se il pulsante di opzione è selezionato o meno.
- La proprietà [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) specifica il formato di riempimento del pulsante di opzione.
- La proprietà [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) specifica gli stili di formato della linea del pulsante di opzione.

L'esempio seguente mostra come aggiungere pulsanti di opzione a un foglio di lavoro. L'esempio aggiunge tre pulsanti di opzione che rappresentano gruppi di età.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

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

La classe [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**AddComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox), che serve per aggiungere un controllo casella combinata a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox). La classe [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) rappresenta una casella combinata. Ha alcuni membri importanti:

- La proprietà [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) specifica una cella collegata alla casella combinata.
- La proprietà [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) specifica l'intervallo di celle del foglio di lavoro utilizzato per riempire la casella combinata.
- La proprietà [**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) specifica il numero di righe dell'elenco visualizzate nella parte a discesa di una casella combinata.
- La proprietà [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) indica se la casella combinata ha una ombreggiatura 3D.

L'esempio seguente mostra come aggiungere una casella combinata al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **Aggiunta del Controllo Etichetta a un Foglio di Lavoro**

Le etichette sono un modo per fornire informazioni agli utenti sui contenuti di un foglio di calcolo. Aspose.Cells rende possibile aggiungere e manipolare etichette in un foglio di lavoro. La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**AddLabel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel), utilizzato per aggiungere un controllo etichetta al foglio di lavoro. Il metodo restituisce un oggetto [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label). La classe [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) rappresenta un'etichetta nel foglio di lavoro. Ha alcuni membri importanti:

- Il metodo [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) specifica una stringa di didascalia dell'etichetta.
- Il metodo [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) specifica il [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), il modo in cui l'etichetta è collegata alle celle nel foglio di lavoro.

Nell'esempio seguente viene mostrato come aggiungere un'etichetta al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

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

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox), che viene utilizzato per aggiungere un controllo casella di selezione a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox). La classe [**ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) rappresenta una casella di selezione. Ha alcuni membri importanti:

- Il metodo [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) specifica una cella collegata alla casella di selezione.
- Il metodo [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) specifica l'intervallo di celle nel foglio di lavoro utilizzato per riempire la casella di selezione.
- Il metodo [**SelectionType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype) specifica la modalità di selezione della casella di selezione.
- Il metodo [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) indica se la casella di selezione ha un'ombreggiatura 3D.

Nell'esempio seguente viene mostrato come aggiungere una casella di selezione al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

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

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**AddButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton), utilizzato per aggiungere un controllo pulsante al foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button). La classe [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) rappresenta un pulsante. Ha alcuni membri importanti:

- La proprietà [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) specifica la didascalia del pulsante.
- La proprietà [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) specifica gli attributi del carattere per l'etichetta del controllo del pulsante.
- La proprietà [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) specifica il [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), il modo in cui il pulsante è collegato alle celle nel foglio di lavoro.
- La proprietà [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) aggiunge un collegamento ipertestuale per il controllo del pulsante. Facendo clic sul pulsante si passerà all'URL correlato.

L'esempio seguente mostra come aggiungere un pulsante al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **Aggiunta del controllo linea al foglio di lavoro**

### **Utilizzando Microsoft Excel**

1. Sulla barra degli strumenti **Disegno**, fare clic su **Forme automatiche**, puntare su **Linee** e selezionare lo stile della linea desiderato.
1. Trascinare per disegnare la linea.
1. Eseguire una o entrambe le seguenti azioni:
   1. Per vincolare la linea a disegnare a angoli di 15 gradi dal punto di inizio, tenere premuto SHIFT mentre si trascina.
   1. Per allungare la linea in direzioni opposte dal primo punto di estremità, tenere premuto CTRL mentre si trascina.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline), utilizzato per aggiungere una forma di linea al foglio di lavoro. Il metodo restituisce un oggetto [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape). La classe [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) rappresenta una linea. Ha alcuni membri importanti:

- Il metodo [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) specifica il formato di una riga.
- Il metodo [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) specifica il [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), il modo in cui la riga è collegata alle celle nel foglio di lavoro.

L'esempio seguente mostra come aggiungere righe al foglio di lavoro. Crea tre righe con stili diversi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **Aggiunta di una testa di freccia a una linea**

Aspose.Cells ti consente anche di disegnare linee con punta a freccia. È possibile aggiungere una punta a freccia a una linea e formattare la linea. Ad esempio, puoi cambiare il colore della linea o specificare lo spessore e lo stile della linea.

L'esempio seguente mostra come aggiungere una testa di freccia a una linea.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **Aggiunta del controllo Rettangolo in un foglio di lavoro**

Aspose.Cells ti consente di disegnare forme rettangolari nei tuoi fogli di lavoro. Puoi creare un rettangolo, un quadrato, ecc. Ti è anche consentito formattare il colore di riempimento e il colore della linea di bordo del controllo. Ad esempio, puoi cambiare il colore del rettangolo, impostare il colore di sfondo, specificare lo spessore e lo stile del rettangolo per le tue esigenze.

### **Utilizzando Microsoft Excel**

1. Sulla barra degli strumenti **Disegno**, fare clic su **Rettangolo**.
1. Trascina per disegnare il rettangolo.
1. Eseguire una o entrambe le seguenti azioni:
   1. Per vincolare il rettangolo e disegnare un quadrato dal suo punto iniziale, premere il tasto MAIUSC mentre trascini.
   1. Per disegnare un rettangolo da un punto centrale, premere il tasto CTRL mentre trascini.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**AddRectangle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle), che viene utilizzato per aggiungere una forma rettangolare a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape). La classe [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) rappresenta un rettangolo. Ha alcuni membri importanti:

- La proprietà [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) specifica gli attributi del formato della linea di un rettangolo.
- La proprietà [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) specifica il [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), il modo in cui il rettangolo è collegato alle celle nel foglio di lavoro.
- La proprietà [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) specifica gli stili di formato del riempimento di un rettangolo.

L'esempio seguente mostra come aggiungere un rettangolo al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **Aggiunta del controllo Arco al foglio di lavoro**

Aspose.Cells ti consente di disegnare forme ad arco nei tuoi fogli di lavoro. Puoi creare archi semplici e riempiti. Ti è consentito formattare il colore di riempimento e il colore della linea di bordo del controllo. Ad esempio, puoi specificare/cambiare il colore dell'arco, impostare il colore di sfondo, specificare lo spessore e lo stile della forma per le tue esigenze.

### **Utilizzando Microsoft Excel**

1. Sulla barra degli strumenti **Disegno**, fare clic su **Arco** in **Forme automatiche**.
1. Trascina per disegnare l'arco.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**AddArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc), che viene utilizzato per aggiungere una forma ad arco a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape). La classe [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) rappresenta un arco. Ha alcuni membri importanti:

- La proprietà [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) specifica gli attributi del formato della linea di una forma ad arco.
- La proprietà [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) specifica il [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), il modo in cui l'arco è collegato alle celle nel foglio di lavoro.
- La proprietà [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) specifica gli stili del formato di riempimento della forma.
- La proprietà [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) specifica l'indice della riga dell'angolo in basso a destra.
- La proprietà [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) specifica l'indice della colonna dell'angolo in basso a destra.

L'esempio seguente mostra come aggiungere forme ad arco al foglio di lavoro. L'esempio crea due forme ad arco: una è riempita e l'altra è semplice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **Aggiunta del controllo ovale a un foglio di lavoro**

Aspose.Cells consente di disegnare forme ovali nei fogli di lavoro. Creare forme ovali semplici e riempite e formattare il colore di riempimento e il colore della linea di bordo del controllo. Ad esempio, è possibile specificare / cambiare il colore dell'ovale, impostare il colore dell'ombreggiatura, specificare il peso e lo stile della forma.

### **Utilizzando Microsoft Excel**

- Nella barra degli strumenti *Disegno*, fare clic su *Ovale*.
- Trascina per disegnare l'ovale.
- Fare uno o entrambi i seguenti:
- Per vincolare l'ovale nel disegnare un cerchio dal suo punto di partenza, tenere premuto SHIFT mentre trascini.
- Per disegnare un ovale da un punto centrale, tenere premuto CTRL mentre trascini.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**AddOval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval), che viene utilizzato per aggiungere una forma ovale a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval). La classe [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) rappresenta una forma ovale. Ha alcuni membri importanti:

- La proprietà [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) specifica gli attributi del formato della linea di una forma ovale.
- La proprietà [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) specifica il [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), il modo in cui l'ovale è collegato alle celle nel foglio di lavoro.
- La proprietà [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) specifica gli stili del formato di riempimento della forma.
- La proprietà [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) specifica l'indice della riga dell'angolo in basso a destra.
- La proprietà [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) specifica l'indice della colonna dell'angolo in basso a destra.

L'esempio seguente mostra come aggiungere forme ovali al foglio di lavoro. L'esempio crea due forme ovali: una è una forma ovale piena, l'altra è un semplice cerchio.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **Aggiunta del controllo Spinner al foglio di lavoro**

Una casella di testo è un riquadro di testo collegato a un pulsante (chiamato pulsante di scorrimento) composto da una freccia su e una freccia giù che è possibile fare clic per modificare incrementalmente il valore nella casella di testo. Utilizzando le caselle di testo, è possibile vedere come le modifiche all'input del modello finanziario altereranno gli output del modello. È possibile collegare un pulsante di scorrimento a una cella di input specifica. Quando si fa clic sulla freccia su o giù sul pulsante di scorrimento, il valore intero nella cella di input mirata aumenta o diminuisce. *Aspose.Cells* consente di creare spinner nei fogli di lavoro.

### **Utilizzando Microsoft Excel**

Per inserire un controllo casella di scorrimento nel tuo foglio di lavoro:

- Assicurati che la barra degli strumenti *Forme* sia visualizzata.
- Fare clic sull'opzione *Spinner*.
- Nell'area del foglio di lavoro, fare clic e trascinare per definire il rettangolo che conterrà lo spinner.
- Una volta inserito lo spinner nel foglio di lavoro, fare clic con il pulsante destro del mouse sul controllo e fare clic su *Formatta controllo* e specificare i valori massimo, minimo e incrementale.
- Nel campo *Collegamento cella* specificare l'indirizzo della cella a cui dovrebbe essere collegata questa casella di scorrimento.
- Fare clic su *OK*.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**AddSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner), che viene utilizzato per aggiungere un controllo casella di scorrimento a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner). La classe [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) rappresenta una casella di scorrimento. Ha alcuni membri importanti:

- La proprietà [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) specifica una cella collegata alla casella di scorrimento.
- La proprietà [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) specifica il valore massimo per l'intervallo della casella di scorrimento.
- La proprietà [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) specifica il valore minimo per l'intervallo della casella di scorrimento.
- La proprietà [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) specifica l'importo del valore con cui viene incrementato uno spinner a una riga di scorrimento.
- La proprietà [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) indica se la casella di scorrimento ha ombreggiature 3D.
- La proprietà [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) specifica il valore corrente della casella di scorrimento.

L'esempio seguente mostra come aggiungere una casella di scorrimento al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **Aggiunta di un controllo barra di scorrimento a un foglio di lavoro**

Un controllo barra di scorrimento viene utilizzato per aiutare a selezionare dati in un foglio di lavoro in modo simile a un controllo spin box. Aggiungendo il controllo a un foglio di lavoro e collegandolo a una cella, è possibile restituire un valore numerico per la posizione corrente del controllo.

### **Utilizzando Microsoft Excel**

- Per aggiungere una barra di scorrimento in Excel 2003 e nelle versioni precedenti, fare clic sul pulsante *Barra di scorrimento* nella barra degli strumenti *Forme*, e quindi creare una barra di scorrimento che copra le celle da B2 a B6 in altezza e sia larga circa un quarto della larghezza della colonna.
- Per aggiungere una barra di scorrimento in Excel 2007, fare clic sulla scheda *Sviluppatore*, fare clic su *Inserisci* e quindi fare clic su *Barra di scorrimento* nella sezione Controlli modulo.
- Fare clic con il pulsante destro del mouse sulla barra di scorrimento e quindi fare clic su *Formato controllo*.
- Immettere le seguenti informazioni e fare clic su *OK*:
  - Nella casella *Valore corrente*, digitare 1.
  - Nella casella *Valore minimo*, digitare 1. Questo valore limita la parte superiore della barra di scorrimento al primo elemento nella lista.
  - Nella casella *Valore massimo*, digitare 20. Questo numero specifica il numero massimo di voci nella lista.
  - Nella casella *Cambiamento incrementale*, digitare 1. Questo valore controlla quanti numeri il controllo barra di scorrimento incrementa il valore corrente.
  - Nella casella *Cambio pagina*, digitare 5. Questa voce controlla di quanto verrà incrementato il valore corrente se si fa clic all'interno della barra di scorrimento su uno dei lati della casella di scorrimento.
  - Per inserire un valore numerico nella cella G1 (a seconda dell'elemento selezionato nell'elenco), digitare G1 nella casella *Collegamento cella*.
- Fare clic su qualsiasi cella in modo che la barra di scorrimento non sia selezionata.

Quando si fa clic sul controllo su o giù nella barra di scorrimento, la cella G1 viene aggiornata con un numero che indica il valore corrente della barra di scorrimento aumentato o diminuito del cambio incrementale della barra di scorrimento.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**AddScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar), che viene utilizzato per aggiungere un controllo barra di scorrimento al foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar). La classe [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) rappresenta una barra di scorrimento. Ha alcuni membri importanti:

- La proprietà [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) specifica una cella collegata alla barra di scorrimento.
- La proprietà [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) specifica il valore massimo per l'intervallo della barra di scorrimento.
- La proprietà [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) specifica il valore minimo per l'intervallo della barra di scorrimento.
- La proprietà [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) specifica l'ammontare del valore per il quale una barra di scorrimento viene incrementata di uno scroll di riga.
- La proprietà [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) indica se la barra di scorrimento ha un ombreggiatura 3D.
- La proprietà [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) specifica il valore corrente della barra di scorrimento.
- La proprietà [**PageChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange) specifica di quanto verrà incrementato il valore corrente se si fa clic all'interno della barra di scorrimento su uno dei due lati della casella di scorrimento.

L'esempio seguente mostra come aggiungere una barra di scorrimento al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **Aggiunta di un controllo GroupBox ai controlli di gruppo in un foglio di lavoro**

A volte è necessario implementare pulsanti di opzione o altri controlli che appartengono a un certo gruppo, è possibile farlo includendo un controllo group box o un rettangolo. Uno di questi due oggetti funzionerebbe come delimitatore del gruppo. Dopo aver aggiunto una di queste forme, è possibile aggiungere due o più pulsanti di opzione o altri oggetti di gruppo.

### **Utilizzando Microsoft Excel**

Per inserire un controllo di group box nel foglio di lavoro e inserire i controlli al suo interno:

- Per avviare un modulo, nel menu principale, fare clic su *Visualizza*, seguito da *Barre degli strumenti* e *Moduli*.
- Sulla barra degli strumenti *Moduli*, fare clic su *GroupBox* e disegnare un rettangolo sul foglio di lavoro.
- Digitare una stringa di didascalia per la casella.
- Sulla barra degli strumenti *Moduli*, fare clic su *Pulsante di opzione* e fare clic all'interno del *GroupBox* appena sotto la stringa di didascalia.
- Dalla barra degli strumenti *Moduli* nuovamente, fare clic su *Pulsante di opzione* e fare clic all'interno del *GroupBox* sotto il primo pulsante di opzione.
- Ancora una volta sulla barra degli strumenti *Moduli*, fare clic su *Pulsante di opzione* e fare clic all'interno del *GroupBox* sotto il pulsante di opzione precedente.

### **Usare Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**AddGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox), che viene utilizzato per aggiungere un controllo di group box al foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox). Inoltre, il metodo [**Group**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) della classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) raggruppa le forme, prende un array [**Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) come parametro e restituisce un oggetto [**GroupShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape). La classe [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) rappresenta una casella di gruppo. Ha alcuni membri importanti:

- La proprietà [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) specifica la stringa di didascalia della casella di gruppo.
- La proprietà [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) indica se la casella di gruppo ha sfumature in 3D.

L'esempio seguente mostra come aggiungere una casella di gruppo e raggruppare i controlli nel foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **Argomenti avanzati**
- [Aggiungi controlli ActiveX utilizzando Aspose.Cells](/cells/it/net/add-activex-controls-using-aspose-cells/)
- [Rimuovi controllo ActiveX](/cells/it/net/remove-activex-control/)
- [Aggiorna il controllo ComboBox ActiveX](/cells/it/net/update-activex-combobox-control/)
