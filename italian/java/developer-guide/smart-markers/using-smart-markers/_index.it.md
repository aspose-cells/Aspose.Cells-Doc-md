---
title: Utilizzo degli Smart Markers
type: docs
weight: 40
url: /it/java/using-smart-markers/
---

## **Introduzione**

{{% alert color="primary" %}}

**Gli smart marker** vengono utilizzati per far sapere ad Aspose.Cells quale informazione inserire in un [foglio di calcolo del designer](/cells/it/java/what-is-a-designer-spreadsheet/) di Microsoft Excel. Gli smart marker ti consentono di creare modelli che contengono solo informazioni rilevanti e formattazione.

{{% /alert %}}

## **Foglio di calcolo di progettazione e Marcatori intelligenti**

I fogli di calcolo del designer sono file Excel standard che contengono formattazione visiva, formule e smart marker. Possono contenere smart marker che fanno riferimento a una o più origini dati, come informazioni di un progetto e informazioni per contatti correlati. Gli smart marker vengono scritti nelle celle in cui desideri le informazioni.

Tutti gli smart marker iniziano con &=. Un esempio di marcatore di dati è &=Party.FullName. Se il marcatore di dati produce più di un elemento, ad esempio una riga completa, le righe seguenti vengono spostate automaticamente per fare spazio alle nuove informazioni. Così i subtotali e i totali possono essere inseriti nella riga immediatamente dopo il marcatore di dati per effettuare calcoli basati sui dati inseriti. Per effettuare calcoli sulle righe inserite, utilizza le [formule dinamiche](/cells/it/java/using-smart-markers/#dynamic-formulas).

I marker smart consistono principalmente nelle parti **origine dei dati** e **nome del campo** per la maggior parte delle informazioni. Informazioni speciali possono anche essere passate con variabili e array di variabili. Le variabili riempiono sempre solo una cella, mentre gli array di variabili possono riempire diverse celle. Utilizzare solo un marker dati per cella. I marker smart non utilizzati vengono rimossi.

Un marcatore intelligente può anche contenere parametri. I parametri ti consentono di modificare la disposizione delle informazioni. Vengono aggiunti alla fine del marcatore intelligente tra parentesi come elenco separato da virgole.

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
- *ascendente:n o discendente:n - Ordina i dati negli smart marker. Se n è 1, allora la colonna è la prima chiave del sorter. I dati sono ordinati dopo il trattamento dell'origine dati. Ad esempio: &=Tabella1.Campo3(ascendente:1).
- **orizzontale** - Scrivi i dati da sinistra a destra, invece che dall'alto verso il basso.
- **numerico** - Converti il testo in numero se possibile.
- **spostamento** - Sposta verso il basso o a destra, creando righe o colonne aggiuntive per adattare i dati. Il parametro di spostamento funziona allo stesso modo di Microsoft Excel. Ad esempio in Microsoft Excel, quando selezioni un intervallo di celle, fai clic con il pulsante destro del mouse e selezioni **Inserisci** e specifica **sposta le celle in basso**, **sposta le celle a destra** e altre opzioni. In breve, il parametro di spostamento svolge la stessa funzione per gli smart marker verticali/normale (dall'alto in basso) o orizzontali (da sinistra a destra).
- **bean** - Indica che l'origine dati è un semplice POJO. Supportato solo nell'API Java.

I parametri noadd e skip possono essere combinati per inserire dati su righe alternate. Poiché il modello viene elaborato dall'alto verso il basso, dovresti aggiungere noadd sulla prima riga per evitare che siano inserite righe aggiuntive prima della riga alternata.

Se hai più parametri, separali con una virgola, ma senza spazi: parametroA,parametroB,parametroC

Le seguenti schermate mostrano come inserire dati ogni altra riga

![todo:image_alt_text](using-smart-markers_1.png)

**diventa...**

![todo:image_alt_text](using-smart-markers_2.png)

### **Formule dinamiche**

Le formule dinamiche ti consentono di inserire formule Excel nelle celle anche quando la formula fa riferimento a righe che saranno inserite durante il processo di esportazione. Le formule dinamiche possono ripetersi per ogni riga inserita o utilizzare solo la cella in cui è posizionato il marcatore dei dati

Le formule dinamiche consentono le seguenti opzioni aggiuntive:

- r - Numero di riga attuale
- 2, -1 - Offset al numero di riga attuale

Il seguente illustra una formula dinamica ripetitiva e il foglio di calcolo di Excel risultante.

![todo:image_alt_text](using-smart-markers_3.png)

**diventa...**

![todo:image_alt_text](using-smart-markers_4.png)

La cella C1 contiene la formula =A1*B1, C2 contiene = A2*B2 e C3 = A3*B3.

È molto semplice elaborare i marcatore intelligenti. Il seguente esempio di codice mostra come utilizzare formule dinamiche nei marcatore intelligenti. Carichiamo il [file del modello](templateDynamicFormulas.xlsx) e creiamo dati di test, elaboriamo i marcatori per riempire i dati nelle celle contro il marcatore 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **Utilizzo di Array Variabili**

Il seguente esempio di codice mostra come utilizzare matrici variabili negli Smart Marker. Inseriamo un marcatore di matrice variabile nella cella A1 del primo foglio di lavoro del libro dinamicamente che contiene una stringa di valori impostati per il marcatore, elaborare i marcatori per riempire i dati nelle celle contro il marcatore. Infine, salviamo il file Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **Raggruppamento dei dati**

In alcuni report Excel potrebbe essere necessario suddividere i dati in gruppi per renderli più facili da leggere e analizzare. Uno dei principali scopi per suddividere i dati in gruppi è eseguire calcoli (eseguire operazioni di riepilogo) su ciascun gruppo di record

Gli smart markers di Aspose.Cells ti consentono di raggruppare i dati per campi impostati e inserire righe di riepilogo tra i gruppi di dati o set di dati. Ad esempio, se raggruppi i dati per Customers.customerID, puoi aggiungere un record di riepilogo ogni volta che cambia il gruppo.

### **Parametri**

Di seguito alcuni parametri smart marker utilizzati per il raggruppamento dati.

#### **group:normal/merge/repeat**

Supportiamo tre tipi di gruppo tra cui puoi scegliere.

- **normale** - Il valore del campo di raggruppamento non viene ripetuto per i record corrispondenti nella colonna; invece vengono stampati una volta per gruppo di dati.
- **unire** - Lo stesso comportamento del parametro normale, eccetto che unisce le celle nel campo di raggruppamento per ciascun insieme di gruppi.
- **ripetere** - Il valore del campo di raggruppamento viene ripetuto per i record corrispondenti.

Ad esempio: &=Customers.CustomerID(gruppo:unire)

#### **skip**

Salta un numero specifico di righe dopo ciascun gruppo.

Ad esempio &=Dipendenti.Matricola(group:normal,skip:1)

#### **subtotalN**

Esegue un'operazione di riepilogo per un dato campo relativo a un campo di raggruppamento. La N rappresenta i numeri tra 1 e 11 che specificano la funzione utilizzata nel calcolo dei subtotali all'interno di un elenco di dati. (1=MEDIA, 2=CONTATORE, 3=CONT.VALORI, 4=MASSIMO, 5=MINIMO,...9=SOMMA ecc.) Consultare il riferimento Subtotali nell'aiuto di Microsoft Excel per ulteriori dettagli.

Il formato effettivo viene specificato come:
subtotalN:Rif dove Rif si riferisce alla colonna di raggruppamento.

Ad esempio,

- &=Products.Units(subtotal9:Products.ProductID) specifica la funzione di riepilogo sul campo **Units** rispetto al campo **ProductID** nella tabella **Products**.
- &=Tabx.Col3(subtotal9:Tabx.Col1) specifica la funzione di riepilogo sul campo **Col3** raggruppato per **Col1** nella tabella **Tabx**.
- &=Tabella1.ColonnaD(subtotal9:Tabella1.ColonnaA&Tabella1.ColonnaB) specifica la funzione di riepilogo su **ColonnaD** raggruppata per **ColonnaA** e **ColonnaB** nella tabella **Tabella1**.

## **Utilizzo di Oggetti Annidati**

Aspose.Cells supporta oggetti nidificati negli smart marker, gli oggetti nidificati dovrebbero essere semplici.

Utilizziamo un file di modello semplice. Consultare il foglio di calcolo del designer che contiene alcuni marcatori intelligenti nidificati.

**Il primo foglio di lavoro del file del designer che mostra marcatori intelligenti nidificati.**

![todo:image_alt_text](using-smart-markers_5.png)

L'esempio che segue mostra come funziona questo. Eseguendo il codice qui sotto si ottiene il risultato qui sotto.

**Il primo foglio di lavoro del file di output che mostra i dati risultanti.**

![todo:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **Utilizzo di Lista Generica come Oggetto Annidato**

Aspose.Cells ora supporta anche l'uso di un elenco generico come un oggetto nidificato. Si prega di controllare la schermata del file excel di output generato con il codice seguente. Come si può vedere nella schermata, un oggetto Teacher contiene più oggetti studenti nidificati.

![todo:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **Utilizzo della proprietà HTML di Smart Markers**

The following sample code explains the use of the HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML \<b> tag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **Ottenere Notifiche durante la Fusione dei Dati con Smart Markers**

A volte può essere necessario ricevere le notifiche sul riferimento della cella o sul particolare Smart Marker in elaborazione prima del completamento. Questo può essere ottenuto utilizzando la proprietà [**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) e [**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

Per il codice di esempio e spiegazioni dettagliate, si prega di consultare questo articolo.

- [Ottenere Notifiche durante la Fusione dei Dati con Smart Markers](/cells/it/java/getting-notifications-while-merging-data-with-smart-markers/)
{{< app/cells/assistant language="java" >}}
