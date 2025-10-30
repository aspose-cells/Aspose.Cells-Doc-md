---
title: Parametri Smart Marker
type: docs
weight: 30
url: /it/net/smart-marker-parameters/
---

## **Foglio di calcolo di progettazione e Marcatori intelligenti**
I fogli di calcolo di progettazione sono file Excel standard che contengono formattazioni visive, formule e marcatori intelligenti. Possono contenere marcatori intelligenti che fanno riferimento a una o più origini di dati, come informazioni provenienti da un progetto e informazioni per contatti correlati. I marcatori intelligenti vengono scritti nelle celle in cui si desidera inserire le informazioni.

Tutti i marker smart iniziano con &=. Un esempio di un marker dati è &=Party.FullName. Se il marker dati produce più di un elemento, ad esempio, una riga completa, allora le righe successive vengono spostate automaticamente verso il basso per fare spazio alle nuove informazioni. Pertanto, i subtotali e i totali possono essere posizionati sulla riga immediatamente dopo il marker dati per effettuare calcoli basati sui dati inseriti. Per effettuare calcoli sulle righe inserite, utilizzare **formule dinamiche**.

I marker smart consistono principalmente nelle parti **origine dei dati** e **nome del campo** per la maggior parte delle informazioni. Informazioni speciali possono anche essere passate con variabili e array di variabili. Le variabili riempiono sempre solo una cella, mentre gli array di variabili possono riempire diverse celle. Utilizzare solo un marker dati per cella. I marker smart non utilizzati vengono rimossi.

Il marker smart può anche contenere parametri. I parametri ti consentono di modificare come le informazioni sono organizzate. Vengono aggiunti alla fine del marker smart tra parentesi come elenco separato da virgola.

## **Opzioni del Marker Smart**

```csharp
&=DataSource.FieldName 
&=[Data Source].[Field Name] 
&=$VariableName 
&=$VariableArray 
&==DynamicFormula 
&=&=RepeatDynamicFormula
```
## **Parametri Smart Marker**
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

## **Formule dinamiche**
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

## **Come Usare Formule Dinamiche e Variabili in SmartMarkers**
A volte, è necessario usare formule dinamiche e variabili in SmartMarkers. Per formule dinamiche, aggiungi il carattere speciale (~) come separatore. Aspose.Cells permette di usare formule dinamiche e variabili in SmartMarkers. Si prega di controllare il [file modello](template.xlsx), [file JSON](employees-data.json) e lo screenshot dell’Excel generato con il seguente codice.

|**Il primo foglio di lavoro del file template.xlsx che mostra le variabili.**|
| :- |
|![todo:image_alt_text](template_variables.png)|

|**Il secondo foglio di lavoro del file template.xlsx che mostra gli smart markers.**|
| :- |
|![todo:image_alt_text](template_data.png)|

|**Lo screenshot del file Excel di output.**|
| :- |
|![todo:image_alt_text](template_result.png)|

Dati json come segue:
```json data
{
  "RootData": {
    "Directors": [
      {
        "FirstName": "director first 1",
        "id": "director id 1",
        "LastName": "director last 1",
        "MiddleName": "director middle 1",
        "Reportees": [
          {
            "City": "aaa city",
            "Department": "aaa department",
            "FirstName": "first aaa",
            "GST": "Yes",
            "id": "aaa",
            "ITR": "No",
            "LastName": "last aaa",
            "MiddleName": "middle aaa"
          },
          {
            "City": "bbb city",
            "Department": "bbb department",
            "FirstName": "first bbb",
            "GST": "Yes",
            "id": "bbb",
            "ITR": "Yes",
            "LastName": "last bbb",
            "MiddleName": "middle bbb"
          },
          {
            "City": "ccc city",
            "Department": "ccc department",
            "FirstName": "first ccc",
            "GST": "No",
            "id": "ccc",
            "ITR": "No",
            "LastName": "last ccc",
            "MiddleName": "middle ccc"
          },
          {
            "City": "ddd city",
            "Department": "ddd department",
            "FirstName": "first ddd",
            "GST": "No",
            "id": "ddd",
            "ITR": "No",
            "LastName": "last ddd",
            "MiddleName": "middle ddd"
          },
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "No",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          }
        ]
      },
      {
        "FirstName": "director first 2",
        "id": "director id 2",
        "LastName": "director last 2",
        "MiddleName": "director middle 2",
        "Reportees": [
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "Yes",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          },
          {
            "City": "fff city",
            "Department": "fff department",
            "FirstName": "first fff",
            "GST": "No",
            "id": "fff",
            "ITR": "No",
            "LastName": "last fff",
            "MiddleName": "middle fff"
          }
        ]
      }
    ],
    "DOB": "2025-02-28",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111",
	"CtcPerEmployee": 100000,
	"CountOfEmployees": 132
  }
}
```
L'esempio seguente mostra come funziona.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-DynamicFormula-And-Variables.cs" >}}
