---
title: Come Usare il Parametro Range in SmartMarkers
type: docs
weight: 10
url: /it/net/how-to-use-range-parameter-in-smart-markers/
---

## **Perché Usare il Parametro Range in Smart Markers**
Il parametro range in SmartMarkers viene usato per controllare con precisione dove e come vengono posizionati i dati in un modello Excel quando si popola con dati da una sorgente (ad esempio, JSON, database). Aiuta a gestire l'output di dati dinamici, specialmente quando si tratta di array di lunghezza variabile o raggruppamenti complessi.

1. Controllare la Collocazione dei Dati ed Evitare Sovrapposizioni: Quando le sorgenti dati contengono array dinamici (ad esempio, numero variabile di elementi per record), il parametro range assicura che i dati siano popolati all’interno di un intervallo Excel definito, prevenendo il traboccamento in celle o sezioni adiacenti.

2. Gestire Formule di Array Dinamiche: Per operazioni come la trasposizione di array dinamici (ad esempio, &=TRANSPOSE(DataArray)), il parametro range garantisce che l’output si adatti alla dimensione effettiva dei dati senza lasciare valori residui (ad esempio, zeri in campi vuoti) dalle operazioni precedenti.

3. Supportare Raggruppamenti e Dati Gerarchici: Quando i dati richiedono raggruppamenti (ad esempio, strutture JSON annidate), il parametro range aiuta a definire le aree di output gerarchiche. Per esempio, raggruppare record sotto una categoria principale senza aggiustamenti manuali delle righe. Senza un range definito, SmartMarkers potrebbe fallire nel rappresentare accuratamente relazioni annidate, specialmente se le sorgenti dati non hanno gerarchie esplicite.

4. Migliorare la Progettazione del Modello e la Coerenza: Specificando i range, gli utenti garantiscono che formattazione, formule e bordi siano applicati in modo coerente all’area di output. Questo evita problemi come stili incoerenti delle celle o formule rotte nei report generati.

5. Ottimizzare le Prestazioni e l’Ordinamento dei Dati: Il parametro range consente agli strumenti di pre-ordinare le sorgenti dati prima di popolare i modelli, assicurando che i dati raggruppati appaiano nell’ordine corretto.

## **Come Usare il Parametro Range in SmartMarkers**
A volte, è necessario ordinare ed eseguire altre operazioni su un intervallo in SmartMarkers. Aspose.Cells permette di usare il parametro range in SmartMarkers. Si prega di controllare il [file modello](range.xlsx), [file JSON](range.json) e lo screenshot dell’Excel generato con il seguente codice.

|**Il primo foglio di lavoro del file range.xlsx che mostra gli smart markers.**|
| :- |
|![todo:image_alt_text](range_template.png)|

|**Lo screenshot del file Excel di output.**|
| :- |
|![todo:image_alt_text](range_result.png)|

Dati json come segue:
```json data
{
  "Groups": [
    {
      "Materials": [
        { 
	        "Name": "BBB", 
	        "DSSection": { "Name": "Item B" } 
	      },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item C" }
        },
        {
          "Name": "AAA",
          "DSSection": { "Name": "Item A" }
        },        
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        { 
	        "Name": "AAA", 
	        "DSSection": { "Name": "Item C" } 
        }
      ]
    }
  ]
}
```
L'esempio seguente mostra come funziona.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Range-Parameter.cs" >}}
{{< app/cells/assistant language="csharp" >}}
