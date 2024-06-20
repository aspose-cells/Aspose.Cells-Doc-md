---
title: Elenco delle formule
type: docs
weight: 10
url: /it/reportingservices/formula-list/
---

**Campi del report**

|**Imposta Nome** |**Nome Formula**|**Descrizione**|
| :- | :- | :- |
|Campi globali |TempoEsecuzione |La data e l'ora in cui il report è iniziato ad eseguire.|
| | ReportServerUrl | URL del server dei report su cui viene eseguito il report. |
| | ReportName | Il nome del report come è memorizzato nel database del server dei report. |
| | ReportFolder | Il percorso completo alla cartella che contiene il report. Questo non include l'URL del server dei report. |
| Utente | IDUtente | L'ID dell'utente che esegue il report. |
| | Lingua | L'ID della lingua dell'utente che esegue il report. |
**Campi del report**

| **Nome Set** | **Descrizione** |
| :- | :- |
|Parameters |La raccolta Parametri contiene i parametri del report all'interno del report. I parametri possono essere passati alle query, utilizzati nei filtri o utilizzati in altre funzioni che modificano l'aspetto del report in base al parametro. |
| Campi | La raccolta Campi contiene i campi all'interno dell'insieme di dati corrente. |
| InsiemeDati ||
**Operatori**
Gli operatori aritmetici vengono utilizzati per combinare numeri, variabili numeriche, campi numerici e funzioni numeriche per ottenere un altro numero. Gli operatori di confronto sono normalmente utilizzati per confrontare gli operandi per una condizione in una struttura di controllo come un'istruzione If. Gli operatori booleani vengono tipicamente utilizzati con gli operatori di confronto per generare condizioni per le strutture di controllo.

| **Nome Set** | **Nome Formula** | **Descrizione** |
| :- | :- | :- |
| Aritmetica | ^ | Esponenziazione, ad esempio 2^3. |
| | * | Moltiplicazione, ad esempio 2*3. |
| | / | Divisione, ad esempio 2/3. |
| | \\ | Divisione intera, ad esempio 2\\3. |
| | Mod | Modulo, ad esempio 4 Mod 3. |
| | + | Addizione, ad esempio 4 + 3. |
| | - | Sottrazione, ad esempio 4 - 3. |
|Confronto |< |Minore di, ad esempio 4 < 3 falso. |
| |<= |Minore di o uguale, ad esempio 4 <= 3 falso. |
| |> |Maggiore di, ad esempio 4 > 3 vero. |
| |>= |Maggiore di o uguale, ad esempio 4 >= 3 vero. |
| |= |Uguale, ad esempio 4 = 3 falso. |
| |<> |Diverso, ad esempio 4 <> 3 vero. |
| |Like |Confronta una stringa con un modello. Ad esempio risultato = stringa like modello. |
| |È |Confronta due variabili di riferimento agli oggetti, ad esempio asp è aspose. |
|Concatenazione |& |Genera una concatenazione di stringhe di due espressioni. |
| |+ |Aggiunge due numeri o restituisce il valore positivo di un'espressione numerica. Può anche essere utilizzato per concatenare due espressioni di stringhe. |
|Logico/Bitwise |And |Esegue una congiunzione logica su due espressioni booleane, o una congiunzione bit a bit su due espressioni numeriche. |
| |Not |Esegue la negazione logica su un'espressione booleana, o la negazione bit a bit su un'espressione numerica. |
| |Or |Esegue una disgiunzione logica su due espressioni booleane, o una disgiunzione bit a bit su due espressioni numeriche. |
| |Xor |Esegue un'esclusione logica su due espressioni booleane, o un'esclusione bit a bit su due espressioni numeriche. |
| |AndAlso |Esegue una congiunzione logica a circuito breve su due espressioni. |
| |OrElse |Esegue una disgiunzione logica inclusiva a circuito breve su due espressioni. |
Bit Shift |>> |Esegue uno spostamento a sinistra aritmetico su un modello di bit. |
| |<< |Esegue uno spostamento a destra aritmetico su un modello di bit. |

