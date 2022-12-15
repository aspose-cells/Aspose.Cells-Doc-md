---
title: Elenco delle formule
type: docs
weight: 10
url: /it/reportingservices/formula-list/
---
**Campi del rapporto**

|**Imposta nome** |**Nome formula**|**Descrizione**|
|:- |:- |:- |
| Campi globali| Tempo di esecuzione|La data e l'ora in cui è iniziata l'esecuzione del rapporto.|
|| ReportServerUrl| L'URL del server di report in cui viene eseguito il report.|
|| ReportName| Il nome del report archiviato nel database del server di report.|
|| Segnalacartella| Il percorso completo della cartella contenente il rapporto. Questo non include l'URL del server di report.|
| Utente| ID utente| L'ID dell'utente che esegue il rapporto.|
|| Lingua| L'ID lingua dell'utente che esegue il rapporto.|
**Campi del rapporto**

|**Imposta nome**|**Descrizione**|
|:- |:- |
| Parametri| La raccolta Parameters contiene i parametri del report all'interno del report. I parametri possono essere passati alle query, utilizzati nei filtri o utilizzati in altre funzioni che alterano l'aspetto del report in base al parametro.|
| Campi| La raccolta Fields contiene i campi all'interno del set di dati corrente.|
| Set di dati||
**Operatori**
Gli operatori aritmetici vengono utilizzati per combinare numeri, variabili numeriche, campi numerici e funzioni numeriche per ottenere un altro numero. Gli operatori di confronto vengono generalmente utilizzati per confrontare gli operandi per una condizione in una struttura di controllo come un'istruzione If. Gli operatori booleani vengono in genere utilizzati con gli operatori di confronto per generare condizioni per le strutture di controllo.

|**Imposta nome**|**Nome della formula**|**Descrizione**|
|:- |:- |:- |
| Aritmetica|^ | Esponenziazione, ad esempio 2^3.|
||* | Moltiplicazione, ad esempio 2*3.|
||/ | Divisione, ad esempio 2/3.|
||\\\ | Divisione intera, ad esempio 2\\\3.|
|| mod| Modulo, ad esempio 4 Mod 3.|
||+ | Addizione, ad esempio 4 + 3.|
||- | Sottrazione, ad esempio 4 – 3.|
| Confronto|< | Meno di, ad esempio 4< 3 false. |
||<= | Minore o uguale, ad esempio 4<= 3 false. |
||> | Maggiore di, ad esempio 4 > 3 true.|
||>= | Maggiore o uguale, ad esempio 4 >= 3 true.|
||= | Uguale, ad esempio 4 = 3 falso.|
||<> | Non uguale, ad esempio 4<> 3 vero.|
|| Piace|Confronta una stringa con un modello. Ad esempio result = string Like pattern.|
|| È| Confronta due variabili di riferimento oggetto, ad esempio asp Is aspose.|
| Concatenazione|& | Genera una concatenazione di stringhe di due espressioni.|
||+ | Somma due numeri o restituisce il valore positivo di un'espressione numerica. Può anche essere utilizzato per concatenare due espressioni stringa.|
| Logico/bit per bit| E| Esegue una congiunzione logica su due espressioni booleane o una congiunzione bit per bit su due espressioni numeriche.|
|| Non| Esegue la negazione logica su un'espressione booleana o la negazione bit per bit su un'espressione numerica.|
|| O| Esegue una disgiunzione logica su due espressioni booleane o una disgiunzione bit per bit su due espressioni numeriche.|
|| Xor| Esegue un'esclusione logica su due espressioni booleane o un'esclusione bit per bit su due espressioni numeriche.|
|| E anche| Esegue la congiunzione logica di cortocircuito su due espressioni.|
|| O altro|Esegue la disgiunzione logica inclusiva di cortocircuito su due espressioni.|
| Spostamento bit|>> | Esegue uno spostamento aritmetico a sinistra su un modello di bit.|
||<< | Esegue uno spostamento aritmetico a destra su un modello di bit.|

