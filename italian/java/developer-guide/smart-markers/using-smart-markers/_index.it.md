---
title: Utilizzo degli indicatori intelligenti
type: docs
weight: 40
url: /it/java/using-smart-markers/
---
##  **introduzione**

{{% alert color="primary" %}}

**Marcatori intelligenti** vengono utilizzati per far sapere a Aspose.Cells quali informazioni inserire in un file Excel Microsoft[foglio di calcolo del progettista](/cells/it/java/what-is-a-designer-spreadsheet/). I marcatori intelligenti ti consentono di creare modelli che contengono solo informazioni e formattazioni rilevanti.

{{% /alert %}}

##  **Foglio di calcolo del designer e pennarelli intelligenti**

I fogli di calcolo di Designer sono file Excel standard che contengono formattazione visiva, formule e indicatori intelligenti. Possono contenere indicatori intelligenti che fanno riferimento a una o più origini dati, ad esempio informazioni da un progetto e informazioni per i contatti correlati. Gli indicatori intelligenti vengono scritti nelle celle in cui desideri informazioni.

Tutti gli indicatori intelligenti iniziano con &=. Un esempio di indicatore di dati è &=Party.FullName. Se l'indicatore dati restituisce più di un elemento, ad esempio una riga completa, le righe successive vengono spostate automaticamente verso il basso per fare spazio alle nuove informazioni. Pertanto i totali parziali e i totali possono essere posizionati sulla riga immediatamente dopo l'indicatore dei dati per effettuare calcoli basati sui dati inseriti. Per effettuare calcoli sulle righe inserite, utilizzare[formule dinamiche](/cells/it/java/using-smart-markers/#dynamic-formulas).

 I marcatori intelligenti sono costituiti da**fonte di dati** E**nome del campo** parti per la maggior parte delle informazioni. Informazioni speciali possono anche essere passate con variabili e array di variabili. Le variabili riempiono sempre solo una cella mentre gli array di variabili possono riempirne diverse. Utilizzare solo un indicatore di dati per cella. I marcatori intelligenti non utilizzati vengono rimossi.

Un marcatore intelligente può contenere anche parametri. I parametri consentono di modificare la modalità di presentazione delle informazioni. Vengono aggiunti alla fine dell'indicatore intelligente tra parentesi come elenco separato da virgole.

###  **Opzioni marcatore intelligente**

&=Originedati.NomeCampo
&=[Origine dati].[Nome campo]
&=$NomeVariabile
&=$ArrayVariabile
&==Formula dinamica
&=&=RipetiFormulaDinamica

###  **Parametri**

Sono ammessi i seguenti parametri:

- **non aggiungere** - Non aggiungere righe aggiuntive per adattare i dati.
- **salta: n** - Salta n numero di righe per ogni riga di dati.
- *ascendente:n o discendente:n - Ordina i dati negli indicatori intelligenti. Se n è 1, allora la colonna è la prima chiave del sorter. I dati vengono ordinati dopo l'elaborazione dell'origine dati. Ad esempio: &=Tabella1.Campo3(ascendente:1).
- **orizzontale** - Scrivi i dati da sinistra a destra, anziché dall'alto verso il basso.
- **numerico** - Converti il testo in numero, se possibile.
- **spostare** - Sposta verso il basso o verso destra, creando righe o colonne aggiuntive per adattare i dati. Il parametro di spostamento funziona allo stesso modo di Microsoft Excel. Ad esempio in Microsoft Excel, quando selezioni un intervallo di celle, fai clic con il pulsante destro del mouse e seleziona**Inserire** e specificare**sposta le celle verso il basso**, **sposta le celle verso destra** e altre opzioni. In breve, il parametro di spostamento svolge la stessa funzione per i marcatori intelligenti verticali/normali (dall'alto verso il basso) o orizzontali (da sinistra a destra).
- **fagiolo** - Indica che l'origine dati è un semplice POJO. Supportato solo nello Java API.

I parametri noadd e skip possono essere combinati per inserire dati su righe alternate. Poiché il modello viene elaborato dal basso verso l'alto, è necessario aggiungere noadd alla prima riga per evitare che vengano inserite righe aggiuntive prima della riga alternativa.

Se disponi di più parametri, separali con una virgola, ma senza spazi: parametroA,parametroB,parametroC

Le schermate seguenti mostrano come inserire dati su ogni altra riga.

![cose da fare:immagine_alt_testo](using-smart-markers_1.png)

**diventa...**

![cose da fare:immagine_alt_testo](using-smart-markers_2.png)

###  **Formule dinamiche**

Le formule dinamiche consentono di inserire formule Excel nelle celle anche quando la formula fa riferimento a righe che verranno inserite durante il processo di esportazione. Le formule dinamiche possono ripetersi per ogni riga inserita o utilizzare solo la cella in cui è posizionato l'indicatore dati.

Le formule dinamiche consentono le seguenti opzioni aggiuntive:

- r - Numero della riga corrente.
- 2, -1 - Offset al numero di riga corrente.

Di seguito viene illustrata una formula dinamica ripetuta e il foglio di lavoro Excel risultante.

![cose da fare:immagine_alt_testo](using-smart-markers_3.png)

**diventa…**

![cose da fare:immagine_alt_testo](using-smart-markers_4.png)

Cell C1 contiene la formula =A1*B1, C2 contiene = A2*B2 e C3 = A3*B3.

 È molto semplice elaborare i marcatori intelligenti. Il seguente codice di esempio mostra come utilizzare le formule dinamiche negli indicatori intelligenti. Carichiamo il[file modello](templateDynamicFormulas.xlsx) e creare dati di test, elaborare i marcatori per inserire i dati nelle celle rispetto al marcatore.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

##  **Utilizzo di array di variabili**

Il codice di esempio seguente mostra come utilizzare matrici di variabili negli indicatori intelligenti. Inseriamo dinamicamente un marcatore di matrice variabile nella cella A1 del primo foglio di lavoro della cartella di lavoro che contiene una stringa di valori che impostiamo per il marcatore, elaboriamo i marcatori per riempire i dati nelle celle contro il marcatore. Infine, salviamo il file Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

##  **Raggruppamento dei dati**

In alcuni report Excel potrebbe essere necessario suddividere i dati in gruppi per facilitarne la lettura e l'analisi. Uno degli scopi principali della suddivisione dei dati in gruppi è eseguire calcoli (eseguire operazioni di riepilogo) su ciascun gruppo di record.

Aspose.Cells I marcatori intelligenti consentono di raggruppare i dati per set di campi e posizionare righe di riepilogo tra set di dati o gruppi di dati. Ad esempio, se si raggruppano i dati per Clienti.IDCliente, è possibile aggiungere un record di riepilogo ogni volta che il gruppo cambia.

###  **Parametri**

Di seguito sono riportati alcuni parametri dei marcatori intelligenti utilizzati per raggruppare i dati.

####  **gruppo:normale/unisci/ripeti**

Supportiamo tre tipi di gruppo tra cui puoi scegliere.

- **normale** - Il valore del campo(i) raggruppato per non viene ripetuto per i record corrispondenti nella colonna; vengono invece stampati una volta per gruppo di dati.
- **unire** - Lo stesso comportamento del parametro normale, tranne per il fatto che unisce le celle nel gruppo per campo/i per ciascun gruppo impostato.
- **ripetere** - Il valore del gruppo per campo(i) viene ripetuto per i record corrispondenti.

Ad esempio: &=Clienti.IDCliente(gruppo:unisci)

####  **saltare**

Salta un numero specifico di righe dopo ciascun gruppo.

Ad esempio &=Dipendenti.IDDipendente(gruppo:normale,salta:1)

####  **subtotaleN**

Esegue un'operazione di riepilogo per i dati di un campo specificato relativi a un raggruppamento per campo. La N rappresenta i numeri compresi tra 1 e 11 che specificano la funzione utilizzata durante il calcolo dei totali parziali all'interno di un elenco di dati. (1=MEDIA, 2=COUNT, 3=COUNTA, 4=MAX, 5=MIN,...9=SOMMA ecc.) Fare riferimento al riferimento al totale parziale nella guida di Excel Microsoft per ulteriori dettagli.

Il formato in realtà afferma come:
subtotaleN:Rif dove Rif si riferisce al gruppo per colonna.

Per esempio,

-  &=Products.Units(subtotal9:Products.ProductID) specifica la funzione di riepilogo su**Unità** campo rispetto a**Codice prodotto** campo nel**Prodotti** tavolo.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) specifica la funzione di riepilogo su**Col3** raggruppamento di campi per**Col1** nella tabella *Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) specifica la funzione di riepilogo su**ColonnaD** raggruppamento di campi per**ColonnaA** E**ColonnaB** nella tabella *Tabella1**.

##  **Utilizzo di oggetti nidificati**

Aspose.Cells supporta oggetti nidificati nei marcatori intelligenti, gli oggetti nidificati dovrebbero essere semplici.

Usiamo un semplice file modello. Consulta il foglio di calcolo del designer che contiene alcuni marcatori intelligenti nidificati.

**Il primo foglio di lavoro del file di progettazione che mostra i marcatori intelligenti nidificati.**

![cose da fare:immagine_alt_testo](using-smart-markers_5.png)

L'esempio che segue mostra come funziona. Eseguendo il codice seguente si ottiene l'output seguente.

**Il primo foglio di lavoro del file di output che mostra i dati risultanti.**

![cose da fare:immagine_alt_testo](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

##  **Utilizzo dell'elenco generico come oggetto nidificato**

Aspose.Cells ora supporta anche l'utilizzo di un elenco generico come oggetto nidificato. Controlla lo screenshot del file Excel di output generato con il seguente codice. Come puoi vedere nello screenshot, un oggetto Insegnante contiene più oggetti Studente nidificati.

![cose da fare:immagine_alt_testo](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

##  **Utilizzando la proprietà HTML degli Smart Markers**

Il seguente codice di esempio spiega l'utilizzo della proprietà HTML degli Smart Marker. Quando verrà elaborato, verrà visualizzato "Mondo" in "Hello World" in grassetto a causa di HTML \<b> etichetta.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

##  **Ricevere notifiche durante l'unione dei dati con gli indicatori intelligenti**

 A volte, potrebbe essere necessario ricevere notifiche sul riferimento di cella o sul particolare Smart Marker in fase di elaborazione prima del completamento. Ciò può essere ottenuto utilizzando il[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)proprietà e[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

Per il codice di esempio e la spiegazione dettagliata, vedere questo articolo.

- [Ricevere notifiche durante l'unione dei dati con gli indicatori intelligenti](/cells/it/java/getting-notifications-while-merging-data-with-smart-markers/)
