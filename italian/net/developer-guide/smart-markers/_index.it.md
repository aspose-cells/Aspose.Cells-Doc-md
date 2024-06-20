---
title: Importazione e posizionamento intelligenti dei dati con marcatori intelligenti
linktitle: Marcatori intelligenti
type: docs
weight: 190
url: /it/net/using-smart-markers/
description: Importazione e posizionamento intelligenti dei dati secondo i file Excel di modello con la libreria Aspose.Cells.
---


## **Introduzione**
I **marcatori intelligenti** vengono utilizzati per far conoscere ad Aspose.Cells quali informazioni inserire in un foglio di calcolo di progettazione di Microsoft Excel. I marcatori intelligenti ti consentono di creare modelli che contengono solo informazioni specifiche e formattazione.
## **Foglio di calcolo di progettazione e Marcatori intelligenti**
I fogli di calcolo di progettazione sono file Excel standard che contengono formattazioni visive, formule e marcatori intelligenti. Possono contenere marcatori intelligenti che fanno riferimento a una o più origini di dati, come informazioni provenienti da un progetto e informazioni per contatti correlati. I marcatori intelligenti vengono scritti nelle celle in cui si desidera inserire le informazioni.

Tutti i marker smart iniziano con &=. Un esempio di un marker dati è &=Party.FullName. Se il marker dati produce più di un elemento, ad esempio, una riga completa, allora le righe successive vengono spostate automaticamente verso il basso per fare spazio alle nuove informazioni. Pertanto, i subtotali e i totali possono essere posizionati sulla riga immediatamente dopo il marker dati per effettuare calcoli basati sui dati inseriti. Per effettuare calcoli sulle righe inserite, utilizzare **formule dinamiche**.

I marker smart consistono principalmente nelle parti **origine dei dati** e **nome del campo** per la maggior parte delle informazioni. Informazioni speciali possono anche essere passate con variabili e array di variabili. Le variabili riempiono sempre solo una cella, mentre gli array di variabili possono riempire diverse celle. Utilizzare solo un marker dati per cella. I marker smart non utilizzati vengono rimossi.

Il marker smart può anche contenere parametri. I parametri ti consentono di modificare come le informazioni sono organizzate. Vengono aggiunti alla fine del marker smart tra parentesi come elenco separato da virgola.
### **Opzioni del Marker Smart**
&=OrigineDati.NomeCampo 
&=[Origine Dati].[Nome Campo] 
&=$NomeVariabile 
&=$ArrayVariabili 
&==FormulaDinamica 
&=&=RipetiFormulaDinamica
### **Parametri**
Sono consentiti i seguenti parametri:

- **noadd** - Non aggiungere righe aggiuntive per adattare i dati.
- **skip:n** - Ignora n numero di righe per ogni riga di dati.
- **ascending:n** o **descending:n** - Ordina i dati nei marker smart. Se n è 1, allora la colonna è la prima chiave dell'ordinamento. I dati sono ordinati dopo il trattamento dell'origine dati. Ad esempio: &=Tabella1.Campo3(crescente:1).
- **orizzontale** - Scrivi i dati da sinistra a destra, invece che dall'alto verso il basso.
- **numerico** - Converti il testo in numero se possibile.
- **spostamento** - Sposta verso il basso o a destra, creando righe o colonne aggiuntive per adattare i dati. Il parametro di spostamento funziona allo stesso modo di Microsoft Excel. Ad esempio in Microsoft Excel, quando selezioni un intervallo di celle, fai clic con il pulsante destro del mouse e selezioni **Inserisci** e specifica **sposta celle in basso**, **sposta celle a destra** e altre opzioni. In breve, il parametro di spostamento svolge la stessa funzione per i marker smart verticali/normali (dall'alto in basso) o orizzontali (da sinistra a destra).
- **copiastile** - Copia lo stile della cella di base in tutte le celle di quella colonna.

I parametri noadd e skip possono essere combinati per inserire dati su righe alternate. Poiché il modello viene elaborato dall'alto verso il basso, è necessario aggiungere noadd sulla prima riga per evitare che vengano inserite righe aggiuntive prima della riga alternata.

Se hai più parametri, separali con virgole, ma senza spazi: parametroA, parametroB, parametroC

Le seguenti schermate mostrano come inserire dati ogni altra riga

|**File del modello**|**File di output**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|
### **Formule dinamiche**
Le formule dinamiche ti consentono di inserire formule Excel nelle celle anche quando la formula fa riferimento a righe che saranno inserite durante il processo di esportazione. Le formule dinamiche possono ripetersi per ogni riga inserita o utilizzare solo la cella in cui è posizionato il marcatore dei dati

Le formule dinamiche consentono le seguenti opzioni aggiuntive:

- r - Numero di riga attuale
- 2, -1 - Offset al numero di riga attuale

Per esempio:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

Nel marcatore della formula dinamica, "-1" indica l'offset alla riga corrente rispettivamente nelle colonne B e C che verranno impostate per l'operazione di divisione, il parametro di skip è una riga. Inoltre, dovremmo specificare il seguente carattere:

{{< highlight java >}}

 "~"

{{< /highlight >}}

come carattere separatore per applicare ulteriori parametri nelle formule dinamiche

Le seguenti schermate illustrano una formula dinamica ripetitiva e il foglio di lavoro Excel risultante

|**File del modello**|**File di output**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
La cella "C1" contiene la formula **= A1*B1**, la cella "C2" contiene **= A2*B2** e la cella "C3" contiene **= A3*B3**

È molto semplice elaborare i marcatore intelligenti. Il seguente esempio di codice mostra come utilizzare formule dinamiche nei marcatore intelligenti. Carichiamo il [file del modello](templateDynamicFormulas.xlsx) e creiamo dati di test, elaboriamo i marcatori per riempire i dati nelle celle contro il marcatore 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **Utilizzo di Array Variabili**
Il seguente esempio di codice mostra come utilizzare array variabili nei marcatore intelligenti. Inseriamo un marcatore di array variabili nella cella A1 del primo foglio di lavoro del file Excel in modo dinamico che contiene una stringa di valori che impostiamo per il marcatore, elaboriamo i marcatori per riempire i dati nelle celle contro il marcatore. Infine, salviamo il file Excel



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **Raggruppamento dei dati**
In alcuni report Excel potrebbe essere necessario suddividere i dati in gruppi per renderli più facili da leggere e analizzare. Uno dei principali scopi per suddividere i dati in gruppi è eseguire calcoli (eseguire operazioni di riepilogo) su ciascun gruppo di record

I marcatore intelligenti di Aspose.Cells ti consentono di raggruppare i dati per campi e inserire righe di riepilogo tra i set di dati o gruppi di dati. Ad esempio, se si raggruppano i dati per Customers.CustomerID, è possibile aggiungere un record di riepilogo ogni volta che cambia il gruppo
### **Parametri**
Di seguito sono riportati alcuni dei parametri di smart marker utilizzati per raggruppare i dati.
#### **group:normal/merge/repeat**
Supportiamo tre tipi di gruppo tra cui puoi scegliere.

- **normale** - Il valore del campo di raggruppamento non viene ripetuto per i record corrispondenti nella colonna; invece vengono stampati una volta per gruppo di dati.
- **unire** - Lo stesso comportamento del parametro normale, eccetto che unisce le celle nel campo di raggruppamento per ciascun insieme di gruppi.
- **ripetere** - Il valore del campo di raggruppamento viene ripetuto per i record corrispondenti.

Ad esempio: &=Customers.CustomerID(gruppo:unire)
#### **skip**
Salta un numero specificato di righe dopo ciascun gruppo.

Ad esempio, &=Employees.EmployeeID(gruppo:normale,saltare:1)
#### **subtotalN**
Esegue un'operazione di riepilogo per un dato campo relativo a un campo di raggruppamento. La N rappresenta i numeri tra 1 e 11 che specificano la funzione utilizzata nel calcolo dei subtotali all'interno di un elenco di dati. (1=MEDIA, 2=CONTATORE, 3=CONT.VALORI, 4=MASSIMO, 5=MINIMO,...9=SOMMA ecc.) Consultare il riferimento Subtotali nell'aiuto di Microsoft Excel per ulteriori dettagli.

Il formato effettivo viene specificato come:
subtotalN:Rif dove Rif si riferisce alla colonna di raggruppamento.

Ad esempio,

- &=Products.Units(subtotal9:Products.ProductID) specifica la funzione di riepilogo sul campo **Units** rispetto al campo **ProductID** nella tabella **Products**.
- &=Tabx.Col3(subtotal9:Tabx.Col1) specifica la funzione di riepilogo sul campo **Col3** raggruppato per **Col1** nella tabella **Tabx**.
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) specifica la funzione di riepilogo sul campo **ColumnD** raggruppato per **ColumnA** e **ColumnB** nella tabella **Table1**.

Questo esempio mostra alcuni dei parametri di raggruppamento in azione. Utilizza il database Microsoft Access Northwind.mdb ed estrae i dati dalla tabella chiamata "Dettagli ordine". Creiamo un file designer chiamato SmartMarker_Designer.xls in Microsoft Excel e inseriamo smart marker in varie celle nei fogli di lavoro. I marker vengono elaborati per riempire i fogli di lavoro. I dati sono collocati e organizzati da un campo di raggruppamento.

Il file designer ha due fogli di lavoro. Nel primo mettiamo smart marker con parametri di raggruppamento come mostrato nello screenshot qui sotto. Sono collocati tre smart marker (con parametri di raggruppamento):
&=[Order Details].OrderID(group:merge,skip:1),
&=[Dettagli Ordine].Quantità(subtotale9:Dettagli Ordine.IDOrdine), e
&=[Dettagli Ordine].PrezzoUnitario(subtotale9:Dettagli Ordine.IDOrdine) vanno in A5, B5 e C5 rispettivamente.

|**Il primo foglio di lavoro nel file SmartMarker_Designer.xls, completo di smart markers**|
| :- |
|![todo:image_alt_text](using-smart-markers_5.png)|
Nel secondo foglio di lavoro del file del designer, inseriamo alcuni altri smart marker come mostrato nella figura sottostante. Collochiamo i seguenti smart marker:
&=[Order Details].OrderID(group:normal),
&=[Order Details].Quantity,
&=[Order Details].UnitPrice,
&=&=B(r)*C(r), e
&=subtotale9:Dettagli Ordine.IDOrdine in A5, B5, C5, D5 e C6 rispettivamente.

|**Il secondo foglio di lavoro del file SmartMarker_Designer.xls, mostrando smart markers misti.**|
| :- |
|![todo:image_alt_text](using-smart-markers_6.png)|
Qui è riportato il codice sorgente utilizzato nell'esempio.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Se hai bisogno di aggiungere le tue etichette personalizzate alle righe riepilogative o desideri concatenare il nome del campo con un'etichetta, ad esempio "Subtotale degli Ordini", Aspose.Cells fornisce gli attributi Label e LabelPosition, in modo da poter inserire le tue etichette personalizzate nei Smart Marker mentre concateni con le righe di subtotali nei dati di raggruppamento. Consulta il documento su come Aggiungere Etichette Personalizzate per Concatenare con le Righe di Subtotale nei Smart Markers per ulteriori riferimenti.

{{% /alert %}} 
## **Utilizzo di Tipi Anonimi o Oggetti Personalizzati**
Aspose.Cells supporta anche tipi anonimi o oggetti personalizzati in smart markers. L'esempio seguente mostra come funziona. Per l'importazione di dati da oggetti dinamici utilizzando Smart Markers, visita il seguente articolo:

[Importare da oggetto dinamico come origine dati](/cells/it/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **Smart Marker per Immagini**
Gli smart marker di Aspose.Cells supportano anche i marker di immagini. Questa sezione ti mostra come inserire immagini utilizzando smart markers.
### **Parametri dell'Immagine**
Parametri smart marker per gestire le immagini.

- **Immagine: AdattaACella** - Adatta automaticamente l'immagine all'altezza della riga e alla larghezza della colonna della cella.
- **Immagine: ScalaN** - Scala altezza e larghezza al N percento.
- **Immagine: Larghezza:Npollici&Altezza:Npollici** - Rappresenta l'immagine alta N pollici e larga N pollici. È inoltre possibile specificare le posizioni Sinistra e Alto (in punti).

Qui è riportato il codice sorgente utilizzato nell'esempio.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **Utilizzo di Oggetti Annidati**
Aspose.Cells supporta oggetti annidati in smart markers, gli oggetti annidati devono essere semplici. Utilizziamo un file di modello semplice. Vedi il foglio di calcolo del designer che contiene alcuni smart markers annidati.

|**Il primo foglio di calcolo del file SM_NestedObjects.xlsx mostra smart markers annidati.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
L'esempio seguente mostra come funziona.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}
## **Utilizzo di Lista Generica come Oggetto Annidato**
Aspose.Cells ora supporta anche l'utilizzo di una lista generica come oggetto annidato. Si prega di controllare lo screenshot del file Excel di output generato con il codice sottostante. Come si può vedere nello screenshot, un oggetto Teacher contiene più oggetti Student annidati.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |




{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **Utilizzo della proprietà HTML di Smart Markers**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **Non linea per linea**
Il metodo di elaborazione predefinito attuale prevede di elaborare gli smart marker linea per linea. Ma a volte gli smart marker della stessa tabella dati devono essere elaborati insieme, indipendentemente dal fatto che siano nella stessa riga o meno, quindi è necessario specificare un intervallo con nome "_CellsSmartMarkers" e specificare WorkbookDesigner.LineByLine come falso prima di chiamare l'elaborazione. 
se sono nella stessa riga o meno, allora devi specificare un intervallo denominato "_CellsSmartMarkers" e specificare WorkbookDesigner.LineByLine come falso prima di chiamare l'elaborazione.

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **Ottenere Notifiche durante la Fusione dei Dati con Smart Markers**
A volte, potrebbe essere necessario ricevere le notifiche riguardanti il riferimento della cella o il particolare Smart Marker che viene elaborato prima del completamento. Questo può essere realizzato utilizzando la proprietà WorkbookDesigner.CallBack e ISmartMarkerCallBack

## **Argomenti avanzati**
- [Aggiunta di Oggetti Anonimi o Personalizzati in SmartMarkers](/cells/it/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Auto Popolare i Dati di Smart Marker in Altri Fogli di Lavoro se i Dati sono Troppo Numerosi](/cells/it/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formattazione Smart Markers](/cells/it/net/formatting-smart-markers/)
- [Ottenere Notifiche durante la Fusione dei Dati con Smart Markers](/cells/it/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Imposta origine dati personalizzata per WorkbookDesigner](/cells/it/net/set-custom-datasource-for-workbookdesigner/)
- [Mostra apostrofo iniziale nelle celle](/cells/it/net/show-leading-apostrophe-in-cells/)
- [Utilizzo del parametro Formula nel campo di Smart Marker](/cells/it/net/using-formula-parameter-in-smart-marker-field/)
- [Utilizzo di marcatori immagine durante la raggruppamento dei dati in Smart Markers](/cells/it/net/using-image-markers-while-grouping-data-in-smart-markers/)


