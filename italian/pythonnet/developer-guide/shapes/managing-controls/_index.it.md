---
title: Gestione dei controlli
type: docs
weight: 150
url: /it/python-net/managing-controls/
---

## **Introduzione**

Gli sviluppatori possono aggiungere diversi oggetti di disegno come caselle di testo, caselle di controllo, pulsanti di opzione, combobox, etichette, pulsanti, linee, rettangoli, archi, ovals, spinner, barre di scorrimento, gruppi, ecc. Aspose.Cells per Python via .NET fornisce lo spazio dei nomi Aspose.Cells.Drawing che contiene tutti gli oggetti di disegno. Tuttavia, ci sono alcuni oggetti di disegno o forme che non sono ancora supportati. Crea questi oggetti di disegno in un foglio di calcolo di progettazione usando Microsoft Excel e poi importa il foglio di calcolo di progettazione in Aspose.Cells. Aspose.Cells per Python via .NET ti permette di caricare questi oggetti di disegno da un foglio di calcolo di progettazione e scriverli in un file generato.

## **Aggiunta di un controllo casella di testo a un foglio di calcolo**

Un modo per evidenziare informazioni importanti in un rapporto è usare una casella di testo. Ad esempio, aggiungi testo per evidenziare il nome dell'azienda o per indicare la regione geografica con le vendite più alte. Aspose.Cells per Python via .NET fornisce la classe [**TextBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textboxcollection), utilizzata per aggiungere una nuova casella di testo alla collezione. Esiste un'altra classe, [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox), che rappresenta una casella di testo usata per definire tutti i tipi di impostazioni. Ha alcuni membri importanti:

- La proprietà [**text_frame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_frame) restituisce un oggetto [**MsoTextFrame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msotextframe) utilizzato per regolare i contenuti della casella di testo.
- La proprietà [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) specifica il tipo di posizionamento.
- La proprietà [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) specifica gli attributi del font.
- Il metodo [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) aggiunge un collegamento ipertestuale per la casella di testo.
- La proprietà [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) restituisce un oggetto [**MsoFillFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msofillformat) utilizzato per impostare il formato di riempimento per la casella di testo.
- La proprietà [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) restituisce l'oggetto [**MsoLineFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msolineformat) di solito usato per lo stile e lo spessore della linea della casella di testo.
- La proprietà [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) specifica il testo di input per la casella di testo.

Nell'esempio seguente vengono create due caselle di testo nel primo foglio di lavoro del documento. La prima casella di testo è ben arredata con diverse impostazioni di formato. La seconda è semplice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingTextBoxControl-1.py" >}}

## **Manipolazione dei controlli casella di testo nei fogli di calcolo progettati**

Aspose.Cells per Python via .NET permette anche di accedere alle caselle di testo nei fogli di progettazione e manipolarle. Usa la proprietà [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/text_boxes) per ottenere la collezione di caselle di testo nel foglio.

Nell'esempio seguente viene utilizzato il file Microsoft Excel che abbiamo creato nell'esempio precedente. Ottiene le stringhe di testo delle due caselle di testo e modifica il testo della seconda casella di testo per salvare il file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-ManipulatingTextBoxControls-1.py" >}}

## **Aggiunta di un controllo casella di controllo a un foglio di calcolo**

Le caselle di controllo sono utili se si desidera fornire all'utente un modo per scegliere tra due opzioni, come vero o falso; sì o no. Aspose.Cells per Python via .NET consente di usare le caselle di controllo nei fogli di lavoro. Ad esempio, potresti aver sviluppato un foglio di proiezioni finanziarie in cui puoi considerare o meno una certa acquisizione. In questo caso, potresti voler inserire una casella di controllo in alto nel foglio di lavoro. Puoi poi collegare lo stato di questa casella di controllo a un'altra cella, in modo che se la casella è selezionata, il valore della cella sia Vero; se non è selezionata, il valore sia Falso.

### **Utilizzando Microsoft Excel**

Per inserire un controllo casella di controllo nel foglio di lavoro, seguire questi passaggi:

1. Assicurarsi che la barra degli strumenti Moduli sia visualizzata.
1. Fare clic sul pulsante **Casella di controllo** sulla barra degli strumenti Moduli.
1. Nella tua area di lavoro, fare clic e trascinare per definire il rettangolo che conterrà la casella di controllo e l'etichetta accanto alla casella di controllo.
1. Una volta inserita la casella di controllo, spostare il cursore del mouse nell'area dell'etichetta e modificare l'etichetta.
1. Nel campo **Collegamento cella**, specificare l'indirizzo della cella a cui questa casella di controllo dovrebbe essere collegata.
1. Fare clic su **OK**.

### **Usando Aspose.Cells per Python via .NET**

Aspose.Cells per Python via .NET fornisce la classe [**CheckBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkboxcollection), utilizzata per aggiungere una nuova casella di controllo alla raccolta. C'è un'altra classe, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox), che rappresenta una casella di controllo. Ha alcuni membri importanti:

- La proprietà [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) specifica una cella che è collegata alla casella di controllo.
- La proprietà [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) specifica la stringa di testo associata alla casella di controllo. È l'etichetta della casella di controllo.
- La proprietà [**value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox/value) specifica se la casella di controllo è selezionata o meno.

L'esempio seguente mostra come aggiungere una casella di controllo al foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingCheckBoxControl-1.py" >}}

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

### **Usando Aspose.Cells per Python via .NET**

La classe [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_radio_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_radio_button), che viene utilizzato per aggiungere un controllo pulsante di opzione a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton). La classe [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton) rappresenta un pulsante di opzione. Ha alcuni membri importanti:

- La proprietà [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) specifica una cella che è collegata al pulsante di opzione.
- La proprietà [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) specifica la stringa di testo associata al pulsante di opzione. È l'etichetta del pulsante di opzione.
- La proprietà [**is_checked**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton/is_checked) specifica se il pulsante di opzione è selezionato o meno.
- La proprietà [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) specifica il formato di riempimento del pulsante di opzione.
- La proprietà [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) specifica gli stili di formato della linea del pulsante di opzione.

L'esempio seguente mostra come aggiungere pulsanti di opzione a un foglio di lavoro. L'esempio aggiunge tre pulsanti di opzione che rappresentano gruppi di età.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRadioButtonControl-1.py" >}}

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

### **Usando Aspose.Cells per Python via .NET**

La classe [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_combo_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_combo_box), che serve per aggiungere un controllo casella combinata a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox). La classe [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) rappresenta una casella combinata. Ha alcuni membri importanti:

- La proprietà [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) specifica una cella collegata alla casella combinata.
- La proprietà [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) specifica l'intervallo di celle del foglio di lavoro utilizzato per riempire la casella combinata.
- La proprietà [**drop_down_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/drop_down_lines) specifica il numero di righe dell'elenco visualizzate nella parte a discesa di una casella combinata.
- La proprietà [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/shadow) indica se la casella combinata ha una ombreggiatura 3D.

L'esempio seguente mostra come aggiungere una casella combinata al foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingComboBoxControl-1.py" >}}

## **Aggiunta del Controllo Etichetta a un Foglio di Lavoro**

Le etichette sono un mezzo per fornire agli utenti informazioni sul contenuto di un foglio di calcolo. Aspose.Cells per Python via .NET rende possibile aggiungere e manipolare etichette in un foglio di lavoro. La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) offre un metodo chiamato [**add_label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label), usato per aggiungere un controllo etichetta al foglio di lavoro. Il metodo restituisce un oggetto [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label). La classe [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) rappresenta un'etichetta nel foglio di lavoro. Ha alcuni membri importanti:

- Il metodo [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) specifica una stringa di didascalia dell'etichetta.
- Il metodo [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) specifica il [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), il modo in cui l'etichetta è collegata alle celle nel foglio di lavoro.

Nell'esempio seguente viene mostrato come aggiungere un'etichetta al foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLabelControl-1.py" >}}

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

### **Usando Aspose.Cells per Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_list_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_list_box), che viene utilizzato per aggiungere un controllo casella di selezione a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox). La classe [**ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox) rappresenta una casella di selezione. Ha alcuni membri importanti:

- Il metodo [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) specifica una cella collegata alla casella di selezione.
- Il metodo [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) specifica l'intervallo di celle nel foglio di lavoro utilizzato per riempire la casella di selezione.
- Il metodo [**selection_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/selection_type) specifica la modalità di selezione della casella di selezione.
- Il metodo [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/shadow) indica se la casella di selezione ha un'ombreggiatura 3D.

Nell'esempio seguente viene mostrato come aggiungere una casella di selezione al foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingListBoxControl-1.py" >}}

## **Aggiunta del controllo Pulsante a un foglio di lavoro**

I pulsanti sono utili per eseguire alcune azioni. A volte è utile assegnare un Macro VBA al pulsante o assegnare un collegamento ipertestuale per aprire una pagina web.

### **Utilizzando Microsoft Excel**

Per inserire un controllo pulsante nel tuo foglio di lavoro:

1. Assicurati che la barra degli strumenti **Form** sia visualizzata.
1. Fare clic sullo strumento **Pulsante**.
1. Nella tua area di lavoro, fare clic e trascinare per definire il rettangolo che conterrà il pulsante.
1. Una volta posizionata la casella di selezione nel foglio di lavoro, fare clic con il tasto destro sul controllo e selezionare **Formato controllo**, quindi specificare un Macro VBA e attributi relativi al carattere, all'allineamento, alla dimensione, al margine, ecc.
1. Fare clic su **OK**.

### **Usando Aspose.Cells per Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_button), utilizzato per aggiungere un controllo pulsante al foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button). La classe [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button) rappresenta un pulsante. Ha alcuni membri importanti:

- La proprietà [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) specifica la didascalia del pulsante.
- La proprietà [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) specifica gli attributi del carattere per l'etichetta del controllo del pulsante.
- La proprietà [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) specifica il [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), il modo in cui il pulsante è collegato alle celle nel foglio di lavoro.
- La proprietà [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) aggiunge un collegamento ipertestuale per il controllo del pulsante. Facendo clic sul pulsante si passerà all'URL correlato.

L'esempio seguente mostra come aggiungere un pulsante al foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingButtonControl-1.py" >}}

## **Aggiunta del controllo linea al foglio di lavoro**

### **Utilizzando Microsoft Excel**

1. Sulla barra degli strumenti **Disegno**, fare clic su **Forme automatiche**, puntare su **Linee** e selezionare lo stile della linea desiderato.
1. Trascinare per disegnare la linea.
1. Eseguire una o entrambe le seguenti azioni:
   1. Per vincolare la linea a disegnare a angoli di 15 gradi dal punto di inizio, tenere premuto SHIFT mentre si trascina.
   1. Per allungare la linea in direzioni opposte dal primo punto di estremità, tenere premuto CTRL mentre si trascina.

### **Usando Aspose.Cells per Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line), utilizzato per aggiungere una forma di linea al foglio di lavoro. Il metodo restituisce un oggetto [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape). La classe [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) rappresenta una linea. Ha alcuni membri importanti:

- Il metodo [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) specifica il formato di una riga.
- Il metodo [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) specifica il [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), il modo in cui la riga è collegata alle celle nel foglio di lavoro.

L'esempio seguente mostra come aggiungere righe al foglio di lavoro. Crea tre righe con stili diversi.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLineControl-1.py" >}}

### **Aggiunta di una testa di freccia a una linea**

Aspose.Cells per Python via .NET consente anche di disegnare linee a freccia. È possibile aggiungere una testa di freccia a una linea e formattare la linea stessa. Ad esempio, puoi cambiare il colore della linea, o specificare lo spessore e lo stile della linea.

L'esempio seguente mostra come aggiungere una testa di freccia a una linea.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddinganArrowHead-1.py" >}}

## **Aggiunta del controllo Rettangolo in un foglio di lavoro**

Aspose.Cells per Python via .NET ti permette di disegnare forme rettangolari nei tuoi fogli di lavoro. Puoi creare un rettangolo, quadrato, ecc. È anche consentito formattare il colore di riempimento e il colore del bordo del controllo. Ad esempio, puoi cambiare il colore del rettangolo, impostare il colore di ombreggiatura, specificare lo spessore e lo stile del rettangolo secondo le tue esigenze.

### **Utilizzando Microsoft Excel**

1. Sulla barra degli strumenti **Disegno**, fare clic su **Rettangolo**.
1. Trascina per disegnare il rettangolo.
1. Eseguire una o entrambe le seguenti azioni:
   1. Per vincolare il rettangolo e disegnare un quadrato dal suo punto iniziale, premere il tasto MAIUSC mentre trascini.
   1. Per disegnare un rettangolo da un punto centrale, premere il tasto CTRL mentre trascini.

### **Usando Aspose.Cells per Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle), che viene utilizzato per aggiungere una forma rettangolare a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape). La classe [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape) rappresenta un rettangolo. Ha alcuni membri importanti:

- La proprietà [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) specifica gli attributi del formato della linea di un rettangolo.
- La proprietà [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) specifica il [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), il modo in cui il rettangolo è collegato alle celle nel foglio di lavoro.
- La proprietà [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) specifica gli stili di formato del riempimento di un rettangolo.

L'esempio seguente mostra come aggiungere un rettangolo al foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRectangleControl-1.py" >}}

## **Aggiunta del controllo Arco al foglio di lavoro**

Aspose.Cells per Python via .NET permette di disegnare forme ad arco nei tuoi fogli di lavoro. Puoi creare archi semplici e pieni. È consentito formattare il colore di riempimento e il colore del bordo della forma. Ad esempio, puoi specificare / cambiare il colore dell'arco, impostare il colore di ombreggiatura, specificare lo spessore e lo stile della forma secondo le tue esigenze.

### **Utilizzando Microsoft Excel**

1. Sulla barra degli strumenti **Disegno**, fare clic su **Arco** in **Forme automatiche**.
1. Trascina per disegnare l'arco.

### **Usando Aspose.Cells per Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_arc**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_arc), che viene utilizzato per aggiungere una forma ad arco a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape). La classe [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape) rappresenta un arco. Ha alcuni membri importanti:

- La proprietà [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) specifica gli attributi del formato della linea di una forma ad arco.
- La proprietà [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) specifica il [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), il modo in cui l'arco è collegato alle celle nel foglio di lavoro.
- La proprietà [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) specifica gli stili del formato di riempimento della forma.
- La proprietà [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) specifica l'indice della riga dell'angolo in basso a destra.
- La proprietà [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) specifica l'indice della colonna dell'angolo in basso a destra.

L'esempio seguente mostra come aggiungere forme ad arco al foglio di lavoro. L'esempio crea due forme ad arco: una è riempita e l'altra è semplice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingArcControl-1.py" >}}

## **Aggiunta del controllo ovale a un foglio di lavoro**

Aspose.Cells per Python via .NET consente di disegnare forme ovali nei fogli di lavoro. Crea forme ovali semplici e piene e formatta il colore di riempimento e il colore del bordo della forma. Ad esempio, puoi specificare / cambiare il colore dell'ovale, impostare il colore di ombreggiatura, specificare lo spessore e lo stile della forma.

### **Utilizzando Microsoft Excel**

- Nella barra degli strumenti *Disegno*, fare clic su *Ovale*.
- Trascina per disegnare l'ovale.
- Fare uno o entrambi i seguenti:
- Per vincolare l'ovale nel disegnare un cerchio dal suo punto di partenza, tenere premuto SHIFT mentre trascini.
- Per disegnare un ovale da un punto centrale, tenere premuto CTRL mentre trascini.

### **Usando Aspose.Cells per Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_oval), che viene utilizzato per aggiungere una forma ovale a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval). La classe [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval) rappresenta una forma ovale. Ha alcuni membri importanti:

- La proprietà [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) specifica gli attributi del formato della linea di una forma ovale.
- La proprietà [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) specifica il [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), il modo in cui l'ovale è collegato alle celle nel foglio di lavoro.
- La proprietà [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) specifica gli stili del formato di riempimento della forma.
- La proprietà [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) specifica l'indice della riga dell'angolo in basso a destra.
- La proprietà [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) specifica l'indice della colonna dell'angolo in basso a destra.

L'esempio seguente mostra come aggiungere forme ovali al foglio di lavoro. L'esempio crea due forme ovali: una è una forma ovale piena, l'altra è un semplice cerchio.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingOvalControl-1.py" >}}

## **Aggiunta del controllo Spinner al foglio di lavoro**

Una casella di spin è una casella di testo collegata a un pulsante (chiamato pulsante di spin) composto da una freccia su e una freccia giù su cui cliccare per modificare incrementalmente il valore nella casella di testo. Usando le caselle di spin, puoi vedere come le modifiche di input nel tuo modello finanziario cambieranno gli output del modello. Puoi collegare un pulsante di spin a una cella di input specifica. Mentre clicchi sulla freccia su o giù sul pulsante di spin, il valore intero nella cella di input mirata aumenta o diminuisce. *Aspose.Cells per Python via .NET* permette di creare spinner nei tuoi fogli di lavoro.

### **Utilizzando Microsoft Excel**

Per inserire un controllo casella di scorrimento nel tuo foglio di lavoro:

- Assicurati che la barra degli strumenti *Forme* sia visualizzata.
- Fare clic sull'opzione *Spinner*.
- Nell'area del foglio di lavoro, fare clic e trascinare per definire il rettangolo che conterrà lo spinner.
- Una volta inserito lo spinner nel foglio di lavoro, fare clic con il pulsante destro del mouse sul controllo e fare clic su *Formatta controllo* e specificare i valori massimo, minimo e incrementale.
- Nel campo *Collegamento cella* specificare l'indirizzo della cella a cui dovrebbe essere collegata questa casella di scorrimento.
- Fare clic su *OK*.

### **Usando Aspose.Cells per Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_spinner), che viene utilizzato per aggiungere un controllo casella di scorrimento a un foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner). La classe [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner) rappresenta una casella di scorrimento. Ha alcuni membri importanti:

- La proprietà [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) specifica una cella collegata alla casella di scorrimento.
- La proprietà [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/max) specifica il valore massimo per l'intervallo della casella di scorrimento.
- La proprietà [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/min) specifica il valore minimo per l'intervallo della casella di scorrimento.
- La proprietà [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/incremental_change) specifica l'importo del valore con cui viene incrementato uno spinner a una riga di scorrimento.
- La proprietà [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/shadow) indica se la casella di scorrimento ha ombreggiature 3D.
- La proprietà [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/current_value) specifica il valore corrente della casella di scorrimento.

L'esempio seguente mostra come aggiungere una casella di scorrimento al foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingSpinnerControl-1.py" >}}

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

### **Usando Aspose.Cells per Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_scroll_bar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_scroll_bar), che viene utilizzato per aggiungere un controllo barra di scorrimento al foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar). La classe [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar) rappresenta una barra di scorrimento. Ha alcuni membri importanti:

- La proprietà [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) specifica una cella collegata alla barra di scorrimento.
- La proprietà [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/max) specifica il valore massimo per l'intervallo della barra di scorrimento.
- La proprietà [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/min) specifica il valore minimo per l'intervallo della barra di scorrimento.
- La proprietà [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/incremental_change) specifica l'ammontare del valore per il quale una barra di scorrimento viene incrementata di uno scroll di riga.
- La proprietà [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/shadow) indica se la barra di scorrimento ha un ombreggiatura 3D.
- La proprietà [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/current_value) specifica il valore corrente della barra di scorrimento.
- La proprietà [**page_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/page_change) specifica di quanto verrà incrementato il valore corrente se si fa clic all'interno della barra di scorrimento su uno dei due lati della casella di scorrimento.

L'esempio seguente mostra come aggiungere una barra di scorrimento al foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingScrollBarControl-1.py" >}}

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

### **Usando Aspose.Cells per Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_group_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_group_box), che viene utilizzato per aggiungere un controllo di group box al foglio di lavoro. Il metodo restituisce un oggetto [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox). Inoltre, il metodo [**group**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/group) della classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) raggruppa le forme, prende un array [**Shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) come parametro e restituisce un oggetto [**GroupShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape). La classe [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox) rappresenta una casella di gruppo. Ha alcuni membri importanti:

- La proprietà [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) specifica la stringa di didascalia della casella di gruppo.
- La proprietà [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox/shadow) indica se la casella di gruppo ha sfumature in 3D.

L'esempio seguente mostra come aggiungere una casella di gruppo e raggruppare i controlli nel foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingGroupBoxControl-1.py" >}}

## **Argomenti avanzati**
- [Aggiungi controlli ActiveX](/cells/it/python-net/add-activex-controls-using-aspose-cells/)
- [Rimuovi controllo ActiveX](/cells/it/python-net/remove-activex-control/)
- [Aggiorna il controllo ComboBox ActiveX](/cells/it/python-net/update-activex-combobox-control/)
