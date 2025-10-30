---
title: Importazione intelligente e posizionamento dei dati con Smart markers in Python tramite java
linktitle: Marcatori intelligenti
type: docs
weight: 10
url: /it/python-java/using-smart-markers/
description: Importazione intelligente e posizionamento dei dati secondo i file Excel di modello con Aspose.Cells per Python tramite la libreria java.
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
- **sposta** - Sposta in basso o a destra, creando righe o colonne extra per adattarsi ai dati. Il parametro di spostamento funziona allo stesso modo di Microsoft Excel. Ad esempio in Microsoft Excel, quando selezioni un intervallo di celle, fai clic con il pulsante destro del mouse e selezioni **Inserisci** e specifica **sposta celle in basso**, **sposta celle a destra** e altre opzioni. In breve, il parametro **sposta** svolge la stessa funzione per i marcatori intelligenti verticali/normale (dall'alto in basso) o orizzontali (da sinistra a destra).
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

È molto facile elaborare i marcatori intelligenti. Ecco uno snippet di codice in Python via Java, che mostra come fare.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "SmartMarker-SimpleProcess.py" >}}


