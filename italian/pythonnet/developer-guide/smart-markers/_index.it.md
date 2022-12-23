---
title: Importazione e posizionamento intelligente dei dati con i marcatori intelligenti in Python tramite .Net
linktitle: Marcatori intelligenti
type: docs
weight: 190
url: /it/python-net/using-smart-markers/
description: Importazione e posizionamento intelligente dei dati in base ai file Excel del modello con Aspose.Cells for Python tramite la libreria .Net.
---
## **introduzione**
**Marcatori intelligenti**vengono utilizzati per consentire a Aspose.Cells di sapere quali informazioni inserire in un foglio di calcolo Excel Designer Microsoft. I marcatori intelligenti consentono di creare modelli che contengono solo informazioni e formattazioni specifiche.
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
- **spostare** - Sposta in basso oa destra, creando righe o colonne extra per adattare i dati. Il parametro shift funziona allo stesso modo di Microsoft Excel. Ad esempio in Microsoft Excel, quando selezioni un intervallo di celle, fai clic con il pulsante destro del mouse e seleziona**Inserire** e specificare?**spostare le celle verso il basso**, **sposta le celle a destra** e altre opzioni. Insomma, il**spostare** Il parametro svolge la stessa funzione per gli smart marker verticali/normali (dall'alto verso il basso) o orizzontali (da sinistra a destra).
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

È molto facile elaborare i marcatori intelligenti. Quello che segue è uno snippet di codice in Python tramite .Net, che mostra come è fatto.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "SmartMarker-SimpleProcess.py" >}}


