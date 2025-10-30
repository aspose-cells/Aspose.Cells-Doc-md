---
title: Importazione intelligente dell elemento dell array tramite Slicer in Excel con Smart Markers
type: docs
weight: 30
url: /it/net/how-to-import-array-element-by-slicer-with-smart-markers/
---

## **Perché accedere all'elemento dell'array tramite Slicer**
In FastReport's Smart Markers, l'accesso agli elementi dell'array usando uno slicer (ad esempio, [array[1..3]]) fornisce un modo conciso ed efficiente di lavorare con sottoinsiemi di dati.

1. Estrazione dati semplificata: iterare manualmente su grandi array richiede cicli e sintassi complessa. Gli slicer permettono di estrarre intervalli (subarray) in una riga. Esempio: [Products[1..5].Name] recupera i nomi dei primi 5 prodotti.
2. Reporting dinamico: generare report per slice di dati variabili (ad esempio, "Top N elementi", viste paginabili). Esempio: [Sales[0..{PageNo*10}]] carica dinamicamente le parti di dati per report multi-pagina.
3. Ottimizzazione delle prestazioni: evitare di caricare interi array in memoria. Recuperare solo gli elementi necessari. Esempio: [Logs[^10..^1]] recupera le ultime 10 voci in modo efficiente.
4. Sintassi dichiarativa: esprimi l'intento direttamente nei marcatori del template. Esempio: [Employees[3..7].Department] seleziona chiaramente i dipartimenti da gli elementi 3 a 7.
5. Integrazione con fonti di dati: funziona con array provenienti da database, JSON o codice. Esempio: associare Invoice.Items[0..2] per visualizzare i primi 3 elementi di linea.
6. Gli Slicers in Smart Markers riducono la complessità del codice, migliorano la leggibilità e ottimizzano la gestione dei dati per sottinsiemi di array. Usali quando hai bisogno di un accesso rapido basato su intervalli—ideale per paginazione, liste Top-N o visualizzazioni di dati a finestra. 

## **Come Importare Elemento di Array tramite Slicer in Excel con Smart Markers**
Aspose.Cells supporta l'accesso all'elemento dell'array tramite slicer in smart markers. Verifica il [file modello](ElementBySlicer.xlsx), il [file json](ElementBySlicer.json) e lo screenshot del file Excel generato con il seguente codice.

|**Il primo foglio di lavoro del file smartmarker.xlsx mostra smart markers.**|
| :- |
|![todo:image_alt_text](ElementBySlicer1.png)|

|**Lo screenshot del file Excel di output.**|
| :- |
|![todo:image_alt_text](ElementBySlicer2.png)|

Dati json come segue:
```json data
{
  "EntityCin": "EntityCin Test",
  "EntityName": "EntityName Test",
  "FirstName": "FirstName Test",
  "MiddleName": "MiddleName Test",
  "LastName": "LastName Test",
  "DOB": "2025-02-08",
  "SSN": "11111111",
  "Directors": [
    {
      "id": "director id 1",
      "FirstName": "director first 1",
      "MiddleName": "director middle 1",
      "LastName": "director last 1",
      "Reportees": [
        {
          "id": "aaa",
          "FirstName": "first aaa",
          "MiddleName": "middle aaa",
          "LastName": "last aaa",
          "Department": "aaa department",
          "City": "aaa city",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "bbb",
          "FirstName": "first bbb",
          "MiddleName": "middle bbb",
          "LastName": "last bbb",
          "Department": "bbb department",
          "City": "bbb city",
          "GST": "Yes",
          "ITR": "Yes"
        },
        {
          "id": "ccc",
          "FirstName": "first ccc",
          "MiddleName": "middle ccc",
          "LastName": "last ccc",
          "Department": "ccc department",
          "City": "ccc city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 2",
      "FirstName": "director first 2",
      "MiddleName": "director middle 2",
      "LastName": "director last 2",
      "Reportees": [
        {
          "id": "eee",
          "FirstName": "first eee",
          "MiddleName": "middle eee",
          "LastName": "last eee",
          "Department": "eee department",
          "City": "eee city",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff",
          "FirstName": "first fff",
          "MiddleName": "middle fff",
          "LastName": "last fff",
          "Department": "fff department",
          "City": "fff city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 3",
      "FirstName": "director first 2",
      "MiddleName": "director middle 2",
      "LastName": "director last 2",
      "Reportees": [
        {
          "id": "eee3",
          "FirstName": "first eee3",
          "MiddleName": "middle eee3",
          "LastName": "last eee3",
          "Department": "eee department3",
          "City": "eee city3",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff3",
          "FirstName": "first fff3",
          "MiddleName": "middle fff3",
          "LastName": "last fff3",
          "Department": "fff department3",
          "City": "fff city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 4",
      "FirstName": "director first 4",
      "MiddleName": "director middle 4",
      "LastName": "director last 4",
      "Reportees": [
        {
          "id": "eee4",
          "FirstName": "first eee4",
          "MiddleName": "middle eee4",
          "LastName": "last eee4",
          "Department": "eee department4",
          "City": "eee city4",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff4",
          "FirstName": "first fff4",
          "MiddleName": "middle fff4",
          "LastName": "last fff4",
          "Department": "fff department4",
          "City": "fff city4",
          "GST": "No",
          "ITR": "No"
        }
      ]
    }
  ]
}
```
L'esempio seguente mostra come funziona.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-AccessElementBySlicer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
