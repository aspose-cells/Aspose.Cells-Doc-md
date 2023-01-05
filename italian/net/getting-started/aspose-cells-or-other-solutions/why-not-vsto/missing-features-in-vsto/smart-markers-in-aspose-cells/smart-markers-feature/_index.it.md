---
title: Funzione marcatori intelligenti
type: docs
weight: 30
url: /it/net/smart-markers-feature/
---
**Marcatori intelligenti** vengono utilizzati per consentire a Aspose.Cells di sapere quali informazioni inserire in un foglio di calcolo Excel Designer Microsoft. I marcatori intelligenti consentono di creare modelli che contengono solo informazioni e formattazioni specifiche.
## **Foglio di calcolo per designer e marcatori intelligenti**
I fogli di calcolo per designer sono file Excel standard che contengono formattazione visiva, formule e marcatori intelligenti. Possono contenere marcatori intelligenti che fanno riferimento a una o più origini dati, ad esempio informazioni da un progetto e informazioni per i contatti correlati. I marcatori intelligenti vengono scritti nelle celle in cui desideri le informazioni.

Tutti i marcatori intelligenti iniziano con &=. Un esempio di indicatore di dati è &=Party.FullName. Se l'indicatore di dati restituisce più di un elemento, ad esempio una riga completa, le righe successive vengono spostate automaticamente verso il basso per fare spazio a tutte le nuove informazioni. Pertanto subtotali e totali possono essere posizionati sulla riga immediatamente dopo l'indicatore di dati per eseguire calcoli basati sui dati inseriti. Per effettuare calcoli sulle righe inserite, utilizzare le formule dinamiche.

 I marcatori intelligenti sono costituiti da**fonte di dati** e**nome del campo**parti per la maggior parte delle informazioni. Informazioni speciali possono anche essere passate con variabili e array di variabili. Le variabili riempiono sempre solo una cella mentre gli array di variabili possono riempirne diverse. Utilizzare un solo marcatore di dati per cella. Gli smart marker inutilizzati vengono rimossi.

Il marcatore intelligente può anche contenere parametri. I parametri consentono di modificare la disposizione delle informazioni. Vengono aggiunti alla fine del marcatore intelligente tra parentesi come elenco separato da virgole.
### **Opzioni marcatore intelligente**
- &=DataSource.FieldName
- &=Origine dati.Nome campo
- &=$NomeVariabile
- &=$VariabileArray
- &==DynamicFormula
- &=&=Ripeti Formula Dinamica
### **Parametri**
Sono ammessi i seguenti parametri:

- noadd - Non aggiunge righe extra per adattare i dati.
- skip:n - Salta n numero di righe per ogni riga di dati.
- ascendente:n o discendente:n - Ordina i dati in marcatori intelligenti. Se n è 1, la colonna è la prima chiave dell'ordinatore. I dati vengono ordinati dopo l'elaborazione dell'origine dati. Ad esempio &=Tabella1.Campo3(crescente:1).
- orizzontale - Scrivi i dati da sinistra a destra, invece che dall'alto verso il basso.
- numerico - Converti testo in numero se possibile. Supportato solo nella versione .NET.
- shift - Sposta in basso oa destra, creando righe o colonne aggiuntive per adattare i dati. Il parametro shift funziona allo stesso modo di Microsoft Excel. Ad esempio in MS Excel, quando si seleziona un intervallo di celle, fare clic con il pulsante destro del mouse e selezionare Inserisci e specificare sposta le celle in basso, sposta le celle a destra e altre opzioni. In breve, il parametro shift svolge la stessa funzione per gli smart marker verticali/normali (dall'alto verso il basso) o orizzontali (da sinistra a destra).
- copystyle - Copia lo stile della cella di base in tutte le celle in quella colonna.

 I parametri**noadd** e skip possono essere combinati per inserire dati su righe alternate. Poiché il modello viene elaborato dal basso verso l'alto, è necessario aggiungere noadd sulla prima riga per evitare l'inserimento di righe aggiuntive prima della riga alternativa.
