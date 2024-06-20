---
title: Funzionalità Smart Markers
type: docs
weight: 30
url: /it/net/smart-markers-feature/
---

**Smart markers** vengono utilizzati per informare Aspose.Cells su quale informazione inserire in un foglio di calcolo del designer di Microsoft Excel. I smart markers consentono di creare modelli che contengono solo informazioni specifiche e formattazione.
## **Foglio di calcolo di progettazione e Marcatori intelligenti**
I fogli di calcolo di progettazione sono file Excel standard che contengono formattazioni visive, formule e marcatori intelligenti. Possono contenere marcatori intelligenti che fanno riferimento a una o più origini di dati, come informazioni provenienti da un progetto e informazioni per contatti correlati. I marcatori intelligenti vengono scritti nelle celle in cui si desidera inserire le informazioni.

Tutti i smart markers iniziano con &=. Un esempio di un marcatore dati è &=Party.Fullname. Se il marcatore dati risulta in più di un elemento, ad esempio una riga completa, le righe successive vengono spostate in basso automaticamente per fare spazio a tutte le nuove informazioni. Pertanto subtotali e totali possono essere posizionati sulla riga immediatamente dopo il marcatore dati per effettuare calcoli basati sui dati inseriti. Per effettuare calcoli sulle righe inserite, utilizzare formule dinamiche.

I marker smart consistono principalmente nelle parti **origine dei dati** e **nome del campo** per la maggior parte delle informazioni. Informazioni speciali possono anche essere passate con variabili e array di variabili. Le variabili riempiono sempre solo una cella, mentre gli array di variabili possono riempire diverse celle. Utilizzare solo un marker dati per cella. I marker smart non utilizzati vengono rimossi.

Il marcatore intelligente può anche contenere parametri. I parametri permettono di modificare come le informazioni verranno disposte. Sono aggiunti alla fine del marcatore intelligente tra parentesi come elenco separato da virgole.
### **Opzioni del Marker Smart**
- &=SorgenteDati.NomeCampo
- &=Sorgente Dati.Nome Campo
- &=$VariableName
- &=$VariableArray
- &==DynamicFormula
- &=&=RepeatDynamicFormula
### **Parametri**
Sono consentiti i seguenti parametri:

- noadd - Non aggiungere righe aggiuntive per adattare i dati.
- salta:n - Salta n numero di righe per ogni riga di dati.
- ascendente:n o discendente:n - Ordina i dati nei marcatore intelligenti. Se n è 1, allora la colonna è la prima chiave del classificatore. I dati vengono ordinati dopo aver elaborato la sorgente di dati. E.g &=Tabella1.Campo3(ascendente:1).
- orizzontale - Scrivi i dati da sinistra a destra, anziché dall'alto in basso.
- numerico - Converti il testo in numero se possibile. Supportato solo nella versione .NET.
- sposta - Sposta in basso o a destra, creando righe o colonne aggiuntive per adattare i dati. Il parametro di spostamento funziona allo stesso modo di Microsoft Excel. Ad esempio in MS Excel, quando si seleziona un intervallo di celle, fare clic con il pulsante destro del mouse e selezionare Inserisci e specificare lo spostamento delle celle in basso, a destra e altre opzioni. In breve, il parametro di spostamento svolge la stessa funzione per i marcatore intelligenti verticali/normale (dall'alto in basso) o orizzontali (da sinistra a destra).
- copiarelostile - Copia lo stile della cella di base a tutte le celle di quella colonna.

I parametri **noadd** e skip possono essere combinati per inserire i dati su righe alternate. Poiché il modello viene elaborato dal basso verso l'alto, è necessario aggiungere noadd sulla prima riga per evitare che vengano inserite righe extra prima della riga alternata.
