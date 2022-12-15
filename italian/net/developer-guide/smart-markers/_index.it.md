---
title: Importazione e posizionamento dei dati in modo intelligente con i marcatori intelligenti
linktitle: Marcatori intelligenti
type: docs
weight: 190
url: /it/net/using-smart-markers/
description: Importazione e posizionamento intelligente dei dati in base ai file Excel modello con la libreria Aspose.Cells.
---
## **introduzione**
**Marcatori intelligenti**vengono utilizzati per consentire a Aspose.Cells di sapere quali informazioni inserire in un foglio di calcolo di Microsoft Excel designer. I marcatori intelligenti consentono di creare modelli che contengono solo informazioni e formattazioni specifiche.
## **Foglio di calcolo per designer e marcatori intelligenti**
I fogli di calcolo per designer sono file Excel standard che contengono formattazione visiva, formule e marcatori intelligenti. Possono contenere marcatori intelligenti che fanno riferimento a una o più origini dati, ad esempio informazioni da un progetto e informazioni per i contatti correlati. I marcatori intelligenti vengono scritti nelle celle in cui desideri le informazioni.

 Tutti i marcatori intelligenti iniziano con &=. Un esempio di indicatore di dati è &=Party.FullName. Se l'indicatore di dati restituisce più di un elemento, ad esempio una riga completa, le righe successive vengono spostate automaticamente verso il basso per fare spazio alle nuove informazioni. Pertanto subtotali e totali possono essere posizionati sulla riga immediatamente dopo l'indicatore di dati per eseguire calcoli basati sui dati inseriti. Per eseguire calcoli sulle righe inserite, utilizzare**formule dinamiche**.

 I marcatori intelligenti sono costituiti da**fonte di dati** e**nome del campo**parti per la maggior parte delle informazioni. Informazioni speciali possono anche essere passate con variabili e array di variabili. Le variabili riempiono sempre solo una cella mentre gli array di variabili possono riempirne diverse. Utilizzare un solo marcatore di dati per cella. Gli smart marker inutilizzati vengono rimossi.

Il marcatore intelligente può anche contenere parametri. I parametri consentono di modificare la disposizione delle informazioni. Vengono aggiunti alla fine dell'indicatore intelligente tra parentesi come elenco separato da virgole.
### **Opzioni marcatore intelligente**
 &=DataSource.FieldName
 &=[Origine dati].[Nome campo]&=$NomeVariabile
 &=$VariabileArray
 &==DynamicFormula
&=&=Ripeti Formula Dinamica
### **Parametri**
Sono ammessi i seguenti parametri:

- **noadd** - Non aggiungere righe extra per adattare i dati.
- **salta: n** - Salta n numero di righe per ogni riga di dati.
- **ascendente: n** o**discendente: n** - Ordina i dati in marcatori intelligenti. Se n è 1, la colonna è la prima chiave dell'ordinatore. I dati vengono ordinati dopo l'elaborazione dell'origine dati. Ad esempio: &=Tabella1.Campo3(crescente:1).
- **orizzontale** - Scrivi i dati da sinistra a destra, invece che dall'alto verso il basso.
- **numerico** - Converti testo in numero, se possibile.
- **spostare** - Sposta in basso oa destra, creando righe o colonne extra per adattare i dati. Il parametro shift funziona allo stesso modo di Microsoft Excel. Ad esempio, in Microsoft Excel, quando selezioni un intervallo di celle, fai clic con il pulsante destro del mouse e seleziona**Inserire** e specificare**spostare le celle verso il basso**, **sposta le celle a destra** e altre opzioni. Insomma, il**spostare** Il parametro svolge la stessa funzione per gli smart marker verticali/normali (dall'alto verso il basso) o orizzontali (da sinistra a destra).
- **copystyle** - Copia lo stile della cella di base in tutte le celle di quella colonna.

parametri noadd e skip possono essere combinati per inserire dati su righe alternate. Poiché il modello viene elaborato dal basso verso l'alto, è necessario aggiungere noadd sulla prima riga per evitare l'inserimento di righe aggiuntive prima della riga alternativa.

Se hai più parametri, separali con una virgola, ma senza spazio: parametroA,parametroB,parametroC

Gli screenshot seguenti mostrano come inserire i dati su ogni altra riga.

|**File modello**|**File di uscita**|
|:- |:- |
|![cose da fare:immagine_alt_testo](using-smart-markers_1.jpg)|![cose da fare:immagine_alt_testo](using-smart-markers_2.jpg)|
### **Formule dinamiche**
Le formule dinamiche consentono di inserire formule di Excel nelle celle anche quando la formula fa riferimento a righe che verranno inserite durante il processo di esportazione. Le formule dinamiche possono ripetersi per ogni riga inserita o utilizzare solo la cella in cui è posizionato l'indicatore di dati.

Le formule dinamiche consentono le seguenti opzioni aggiuntive:

- r - Numero di riga corrente.
- 2, -1 - Offset rispetto al numero di riga corrente.

Per esempio:

{{< highlight "java" >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

Nell'indicatore di formula dinamica, "-1" indica l'offset rispetto alla riga corrente rispettivamente nelle colonne B e C che verranno impostate per l'operazione di divisione, il parametro skip è una riga. Inoltre, dovremmo specificare il seguente carattere:

{{< highlight "java" >}}

 "~"

{{< /highlight >}}

come carattere separatore per applicare ulteriori parametri nelle formule dinamiche.

Gli screenshot seguenti illustrano una formula dinamica ripetuta e il foglio di lavoro di Excel risultante.

|**File modello**|**File di uscita**|
|:- |:- |
|![cose da fare:immagine_alt_testo](using-smart-markers_3.jpg)|![cose da fare:immagine_alt_testo](using-smart-markers_4.jpg)|
 Cell "C1" contiene la formula**= A1*B1** , la cella "C2" contiene**= A2*B2** e la cella "C3" contiene**= LA3*SI3**.

È molto facile elaborare i marcatori intelligenti. Quelli che seguono sono due frammenti di codice, uno in C# e uno in VB, che mostrano come è fatto.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}
## **Utilizzo di array di variabili**
Il seguente codice di esempio mostra come utilizzare gli array di variabili negli Smart Markers. Inseriamo dinamicamente un marcatore di matrice variabile nella cella A1 del primo foglio di lavoro della cartella di lavoro che contiene una stringa di valori che impostiamo per il marcatore, elaboriamo i marcatori per riempire i dati nelle celle contro il marcatore. Infine salviamo il file Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **Raggruppamento dei dati**
In alcuni report di Excel potrebbe essere necessario suddividere i dati in gruppi per facilitarne la lettura e l'analisi. Uno degli scopi principali per suddividere i dati in gruppi è eseguire calcoli (eseguire operazioni di riepilogo) su ciascun gruppo di record.

I marcatori intelligenti Aspose.Cells consentono di raggruppare i dati per campi e posizionare righe di riepilogo tra set di dati o gruppi di dati. Ad esempio, se si raggruppano i dati per Customers.CustomerID, è possibile aggiungere un record di riepilogo ogni volta che il gruppo cambia.
### **Parametri**
Di seguito sono riportati alcuni dei parametri degli indicatori intelligenti utilizzati per raggruppare i dati.
#### **gruppo:normale/unisci/ripeti**
Supportiamo tre tipi di gruppo tra cui puoi scegliere.

- **normale** - Il valore raggruppa per campo/i non viene ripetuto per i record corrispondenti nella colonna; vengono invece stampati una volta per gruppo di dati.
- **unire** - Lo stesso comportamento del parametro normale, tranne per il fatto che unisce le celle nel gruppo/i campo/i per ogni gruppo impostato.
- **ripetere** - Il valore raggruppa per campo/i viene ripetuto per i record corrispondenti.

Ad esempio: &=Clienti.IDCliente(gruppo:unione)
#### **Salta**
Salta un numero specificato di righe dopo ogni gruppo.

Ad esempio, &=Employees.EmployeeID(group:normal,skip:1)
#### **subtotaleN**
Esegue un'operazione di riepilogo per i dati di un campo specificato relativi a un raggruppamento per campo. La N rappresenta i numeri compresi tra 1 e 11 che specificano la funzione utilizzata durante il calcolo dei subtotali all'interno di un elenco di dati. (1=MEDIA, 2=COUNT, 3=COUNTA, 4=MAX, 5=MIN,...9=SOMMA ecc.) Fare riferimento al subtotale di riferimento nella guida di Microsoft Excel per ulteriori dettagli.

Il formato in realtà indica come:
subtotalN:Ref dove Ref fa riferimento al gruppo per colonna.

Per esempio,

-  &=Products.Units(subtotal9:Products.ProductID) specifica la funzione di riepilogo su**Unità** campo rispetto al**Numero identificativo del prodotto** campo nel**Prodotti** tavolo.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) specifica la funzione di riepilogo su**Col3** raggruppamento di campi per**col.1** sul tavolo**Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) specifica la funzione di riepilogo su**Colonna D** raggruppamento di campi per**Colonna A** e**Colonna B** sul tavolo**Tabella 1**.

Questo esempio mostra alcuni dei parametri di raggruppamento in azione. Utilizza il database Microsoft Access Northwind.mdb ed estrae i dati dalla tabella denominata "Dettagli ordine". Creiamo un file designer chiamato SmartMarker_Designer.xls in Microsoft Excel e inseriamo marcatori intelligenti in varie celle nei fogli di lavoro. I marcatori vengono elaborati per riempire i fogli di lavoro. I dati vengono inseriti e organizzati da un campo di gruppo.

Il file designer ha due fogli di lavoro. Nel primo inseriamo marcatori intelligenti con parametri di raggruppamento come mostrato nello screenshot qui sotto. Vengono posizionati tre marcatori intelligenti (con parametri di raggruppamento):
&=[Dettagli ordine].IDOrdine(gruppo:unione,salta:1),
&=[Dettagli ordine].Quantità(subtotale9:Dettagli ordine.ID ordine), e
&=[Dettagli ordine].PrezzoUnità(subtotale9:Dettagli ordine.ID ordine) vanno rispettivamente in A5, B5 e C5.

|**Il primo foglio di lavoro nel file SmartMarker_Designer.xls, completo di marcatori intelligenti**|
|:- |
|![cose da fare:immagine_alt_testo](using-smart-markers_5.png)|
Nel secondo foglio di lavoro del file designer, inseriamo altri marcatori intelligenti come mostrato nella figura seguente. Posizioniamo i seguenti marcatori intelligenti:
&=[Dettagli ordine].IDOrdine(gruppo:normale),
&=[Dettagli ordine].Quantità,
&=[Dettagli ordine].UnitPrice,
&=&=B(r)*C(r), e
&=subtotale9:Dettagli ordine.ID ordine rispettivamente in A5, B5, C5, D5 e C6.

|**Il secondo foglio di lavoro del file SmartMarker_Designer.xls, che mostra marcatori intelligenti misti.**|
|:- |
|![cose da fare:immagine_alt_testo](using-smart-markers_6.png)|
Ecco il codice sorgente utilizzato nell'esempio.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Se devi aggiungere le tue etichette personalizzate alle righe Riepilogo o vuoi concatenare il nome del campo con un'etichetta, ad esempio "Subtotale degli ordini", Aspose.Cells ti fornisce gli attributi Label e LabelPosition, quindi puoi inserire le tue etichette personalizzate nello Smart Indicatori durante la concatenazione con le righe del totale parziale nel raggruppamento dei dati. Consulta il documento su come aggiungere etichette personalizzate da concatenare con le righe del totale parziale negli indicatori intelligenti come riferimento.

{{% /alert %}} 
## **Utilizzo di tipi anonimi o oggetti personalizzati**
Aspose.Cells supporta anche tipi anonimi o oggetti personalizzati nei marcatori intelligenti. L'esempio che segue mostra come funziona. Per importare dati da oggetti dinamici utilizzando gli Smart Marker, visita il seguente articolo:

[Importazione da oggetto dinamico come origine dati](/cells/it/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **Marcatori immagine**
I marcatori intelligenti Aspose.Cells supportano anche i marcatori immagine. Questa sezione mostra come inserire immagini utilizzando i marcatori intelligenti.
### **Parametri dell'immagine**
Parametri di marker intelligenti per la gestione delle immagini.

- **Immagine:FitToCell** - Adatta automaticamente l'immagine all'altezza della riga e alla larghezza della colonna della cella.
- **Immagine:ScalaN** - Ridimensiona l'altezza e la larghezza all'N percento.
- **Immagine: Larghezza: Nin e Altezza: Nin** - Rendi l'immagine alta N pollici e larga N pollici. È inoltre possibile specificare le posizioni Left e Top (in punti).

Ecco il codice sorgente utilizzato nell'esempio.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **Utilizzo di oggetti nidificati**
Aspose.Cells supporta gli oggetti nidificati nei marcatori intelligenti, gli oggetti nidificati dovrebbero essere semplici. Usiamo un semplice file modello. Guarda il foglio di calcolo del designer che contiene alcuni marcatori intelligenti nidificati.

|**Il primo foglio di lavoro del file SM_NestedObjects.xlsx che mostra i marcatori intelligenti nidificati.**|
|:- |
|![cose da fare:immagine_alt_testo](using-smart-markers_7.png)|
L'esempio che segue mostra come funziona.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}
## **Utilizzo di un elenco generico come oggetto nidificato**
Aspose.Cells ora supporta anche l'utilizzo di un elenco generico come oggetto nidificato. Si prega di controllare lo screenshot del file excel di output generato con il seguente codice. Come puoi vedere nello screenshot, un oggetto Insegnante contiene più oggetti Studente nidificati.

|![cose da fare:immagine_alt_testo](using-smart-markers_8.png)|
|:- |




{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **Utilizzo della proprietà HTML degli Smart Marker**
 Il seguente codice di esempio spiega l'uso della proprietà HTML degli Smart Marker. Quando verrà elaborato, mostrerà "Mondo" in "Hello World" in grassetto a causa dell'HTML<b>etichetta.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **Non riga per riga**
 L'attuale metodo di elaborazione predefinito consiste nell'elaborare smartmaker riga per riga. Ma a volte gli indicatori intelligenti della stessa tabella dati devono essere elaborati insieme, non importa
se sono nella stessa riga o meno, devi specificare un intervallo denominato "_CellsSmartMarkers" e specificare WorkbookDesigner.LineByLine come false prima di chiamare l'elaborazione.

|![cose da fare:immagine_alt_testo](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **Ricezione di notifiche durante l'unione dei dati con i marcatori intelligenti**
volte, potrebbe essere necessario ricevere le notifiche sul riferimento della cella o sul particolare Smart Marker in fase di elaborazione prima del completamento. Ciò può essere ottenuto utilizzando la proprietà WorkbookDesigner.CallBack e ISmartMarkerCallBack

## **Argomenti avanzati**
- [Aggiunta di oggetti anonimi o personalizzati negli SmartMarker](/cells/it/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Popola automaticamente i dati degli indicatori intelligenti in altri fogli di lavoro se i dati sono troppo grandi](/cells/it/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formattazione dei marcatori intelligenti](/cells/it/net/formatting-smart-markers/)
- [Ricezione di notifiche durante l'unione dei dati con i marcatori intelligenti](/cells/it/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Imposta DataSource personalizzato per WorkbookDesigner](/cells/it/net/set-custom-datasource-for-workbookdesigner/)
- [Mostra l'apostrofo iniziale nelle celle](/cells/it/net/show-leading-apostrophe-in-cells/)
- [Utilizzando il parametro Formula nel campo Smart Marker](/cells/it/net/using-formula-parameter-in-smart-marker-field/)
- [Utilizzo di marcatori immagine durante il raggruppamento di dati in marcatori intelligenti](/cells/it/net/using-image-markers-while-grouping-data-in-smart-markers/)


