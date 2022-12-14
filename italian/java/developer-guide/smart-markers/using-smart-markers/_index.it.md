---
title: Utilizzo di marcatori intelligenti
type: docs
weight: 40
url: /it/java/using-smart-markers/
---
## **introduzione**

{{% alert color="primary" %}}

**Marcatori intelligenti** vengono utilizzati per far sapere a Aspose.Cells quali informazioni inserire in un Microsoft Excel[foglio di calcolo del progettista](/cells/it/java/what-is-a-designer-spreadsheet/). I marcatori intelligenti ti consentono di creare modelli che contengono solo informazioni e formattazione rilevanti.

{{% /alert %}}

## **Foglio di calcolo per designer e marcatori intelligenti**

fogli di calcolo per designer sono file Excel standard che contengono formattazione visiva, formule e marcatori intelligenti. Possono contenere marcatori intelligenti che fanno riferimento a una o più origini dati, ad esempio informazioni da un progetto e informazioni per i contatti correlati. I marcatori intelligenti vengono scritti nelle celle in cui desideri informazioni.

 Tutti i marcatori intelligenti iniziano con &=. Un esempio di indicatore di dati è &=Party.FullName. Se l'indicatore di dati restituisce più di un elemento, ad esempio una riga completa, le righe successive vengono spostate automaticamente verso il basso per fare spazio alle nuove informazioni. Pertanto i totali parziali e i totali possono essere posizionati sulla riga immediatamente dopo l'indicatore di dati per eseguire calcoli basati sui dati inseriti. Per eseguire calcoli sulle righe inserite, utilizzare[formule dinamiche](/cells/it/java/using-smart-markers/#dynamic-formulas).

 I marcatori intelligenti sono costituiti da**fonte di dati** e**nome del campo**parti per la maggior parte delle informazioni. Informazioni speciali possono anche essere passate con variabili e array di variabili. Le variabili riempiono sempre solo una cella mentre gli array di variabili possono riempirne diverse. Utilizzare un solo marcatore di dati per cella. Gli smart marker inutilizzati vengono rimossi.

Un marcatore intelligente può anche contenere parametri. I parametri consentono di modificare la disposizione delle informazioni. Vengono aggiunti alla fine dell'indicatore intelligente tra parentesi come elenco separato da virgole.

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
- *crescente:n o discendente:n - Ordina i dati in marcatori intelligenti. Se n è 1, la colonna è la prima chiave dell'ordinatore. I dati vengono ordinati dopo l'elaborazione dell'origine dati. Ad esempio: &=Tabella1.Campo3(crescente:1).
- **orizzontale** - Scrivi i dati da sinistra a destra, invece che dall'alto verso il basso.
- **numerico** - Converti testo in numero, se possibile.
- **spostare** - Sposta in basso oa destra, creando righe o colonne extra per adattare i dati. Il parametro shift funziona allo stesso modo di Microsoft Excel. Ad esempio in Microsoft Excel, quando selezioni un intervallo di celle, fai clic con il pulsante destro del mouse e seleziona**Inserire** e specificare**spostare le celle verso il basso**, **sposta le celle a destra** e altre opzioni. In breve, il parametro shift svolge la stessa funzione per gli smart marker verticali/normali (dall'alto verso il basso) o orizzontali (da sinistra a destra).
- **fagiolo** - Indica che l'origine dati è un semplice POJO. Supportato solo nel Java API.

parametri noadd e skip possono essere combinati per inserire dati su righe alternate. Poiché il modello viene elaborato dal basso verso l'alto, è necessario aggiungere noadd sulla prima riga per evitare che vengano inserite righe aggiuntive prima della riga alternativa.

Se hai più parametri, separali con una virgola, ma senza spazio: parametroA,parametroB,parametroC

Gli screenshot seguenti mostrano come inserire i dati su ogni altra riga.

![cose da fare:immagine_alt_testo](using-smart-markers_1.png)

**diventa...**

![cose da fare:immagine_alt_testo](using-smart-markers_2.png)

### **Formule dinamiche**

Le formule dinamiche consentono di inserire formule di Excel nelle celle anche quando la formula fa riferimento a righe che verranno inserite durante il processo di esportazione. Le formule dinamiche possono ripetersi per ogni riga inserita o utilizzare solo la cella in cui è posizionato l'indicatore di dati.

Le formule dinamiche consentono le seguenti opzioni aggiuntive:

- r - Numero di riga corrente.
- 2, -1 - Offset rispetto al numero di riga corrente.

Di seguito viene illustrata una formula dinamica ripetuta e il foglio di lavoro di Excel risultante.

![cose da fare:immagine_alt_testo](using-smart-markers_3.png)

**diventa…**

![cose da fare:immagine_alt_testo](using-smart-markers_4.png)

Cell C1 contiene la formula =A1*B1, C2 contiene = A2*SI2 e DO3 = LA3*SI3.

È molto facile elaborare i marcatori intelligenti. Il seguente frammento di codice mostra come è fatto.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **Utilizzo di array di variabili**

Il codice di esempio seguente mostra come utilizzare le matrici di variabili negli indicatori intelligenti. Inseriamo dinamicamente un marcatore di matrice variabile nella cella A1 del primo foglio di lavoro della cartella di lavoro che contiene una stringa di valori che impostiamo per il marcatore, elaboriamo i marcatori per riempire i dati nelle celle contro il marcatore. Infine, salviamo il file Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **Raggruppamento dei dati**

In alcuni report di Excel potrebbe essere necessario suddividere i dati in gruppi per facilitarne la lettura e l'analisi. Uno degli scopi principali per suddividere i dati in gruppi è eseguire calcoli (eseguire operazioni di riepilogo) su ogni gruppo di record.

marcatori intelligenti Aspose.Cells consentono di raggruppare i dati per set di campi e posizionare righe di riepilogo tra set di dati o gruppi di dati. Ad esempio, se si raggruppano i dati per Customers.CustomerID, è possibile aggiungere un record di riepilogo ogni volta che il gruppo cambia.

### **Parametri**

Di seguito sono riportati alcuni parametri degli indicatori intelligenti utilizzati per raggruppare i dati.

#### **gruppo:normale/unisci/ripeti**

Supportiamo tre tipi di gruppo tra cui puoi scegliere.

- **normale** - Il valore raggruppa per campo/i non viene ripetuto per i record corrispondenti nella colonna; vengono invece stampati una volta per gruppo di dati.
- **unire** - Lo stesso comportamento del parametro normale, tranne per il fatto che unisce le celle nel gruppo/i campo/i per ogni gruppo impostato.
- **ripetere** - Il valore raggruppa per campo/i viene ripetuto per i record corrispondenti.

Ad esempio: &=Clienti.IDCliente(gruppo:unione)

#### **Salta**

Salta un numero specifico di righe dopo ogni gruppo.

Ad esempio &=Employees.EmployeeID(group:normal,skip:1)

#### **subtotaleN**

Esegue un'operazione di riepilogo per i dati di un campo specificato relativi a un raggruppamento per campo. La N rappresenta i numeri compresi tra 1 e 11 che specificano la funzione utilizzata durante il calcolo dei subtotali all'interno di un elenco di dati. (1=MEDIA, 2=COUNT, 3=COUNTA, 4=MAX, 5=MIN,...9=SOMMA ecc.) Fare riferimento al riferimento Subtotale nella guida di Excel Microsoft per ulteriori dettagli.

Il formato in realtà indica come:
subtotalN:Ref dove Ref fa riferimento al gruppo per colonna.

Per esempio,

-  &=Products.Units(subtotal9:Products.ProductID) specifica la funzione di riepilogo su**Unità** campo rispetto al**Numero identificativo del prodotto** campo nel**Prodotti** tavolo.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) specifica la funzione di riepilogo su**Col3** raggruppamento di campi per**col.1** sul tavolo**Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) specifica la funzione di riepilogo su**Colonna D** raggruppamento di campi per**Colonna A** e**Colonna B** in tavola**Tabella 1**.

## **Utilizzo di oggetti nidificati**

Aspose.Cells supporta gli oggetti nidificati nei marcatori intelligenti, gli oggetti nidificati dovrebbero essere semplici.

Usiamo un semplice file modello. Guarda il foglio di calcolo del designer che contiene alcuni marcatori intelligenti nidificati.

**Il primo foglio di lavoro del file designer che mostra i marcatori intelligenti nidificati.**

![cose da fare:immagine_alt_testo](using-smart-markers_5.png)

L'esempio che segue mostra come funziona. L'esecuzione del codice seguente comporta l'output riportato di seguito.

**Il primo foglio di lavoro del file di output che mostra i dati risultanti.**

![cose da fare:immagine_alt_testo](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **Utilizzo di un elenco generico come oggetto nidificato**

Aspose.Cells ora supporta anche l'utilizzo di un elenco generico come oggetto nidificato. Si prega di controllare lo screenshot del file excel di output generato con il seguente codice. Come puoi vedere nello screenshot, un oggetto Insegnante contiene più oggetti Studente nidificati.

![cose da fare:immagine_alt_testo](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **Utilizzo della proprietà HTML degli Smart Marker**

Il seguente codice di esempio spiega l'utilizzo della proprietà HTML degli Smart Marker. Quando verrà elaborato, mostrerà "World" in "Hello World" in grassetto a causa dell'HTML \<b>etichetta.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **Ricezione di notifiche durante l'unione dei dati con i marcatori intelligenti**

 A volte, potrebbe essere necessario ricevere le notifiche sul riferimento della cella o sul particolare Smart Marker in fase di elaborazione prima del completamento. Ciò può essere ottenuto utilizzando il[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)proprietà e[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

Per il codice di esempio e la spiegazione dettagliata, vedere questo articolo.

- [Ricezione di notifiche durante l'unione dei dati con i marcatori intelligenti](/cells/it/java/getting-notifications-while-merging-data-with-smart-markers/)
