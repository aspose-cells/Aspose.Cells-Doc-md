---
title: Come Usare il Parametro if e le Variabili in SmartMarkers
type: docs
weight: 10
url: /it/net/how-to-use-if-parameter-and-Variables-in-smart-markers/
---

## **Perché Usare il Parametro if e le Variabili in Smart Markers**
Smart Markers sono strumenti potenti usati in vari contesti. L'uso di parametri e variabili all'interno di Smart Markers ne aumenta significativamente la flessibilità, l'efficienza e le funzionalità.

1. Gestione Dinamica dei Dati e Flessibilità: Parametri e variabili permettono agli Smart Markers di gestire i dati in modo dinamico, adattandosi a input variabili senza richiedere modifiche manuali al modello o al codice.
2. Controllo sul Comportamento e le Operazioni: I parametri regolano il comportamento degli Smart Markers, consentendo operazioni come raggruppamento, ordinamento, subtotali e formattazione condizionale.
3. Supporto aStrutture Dati Complesse: Le variabili permettono agli Smart Markers di lavorare con sorgenti di dati complesse, inclusi array, oggetti e dati multidimensionali.
4. Efficienza e Automazione: Parametri e variabili automatizzano compiti ripetitivi, riducendo sforzo manuale ed errori potenziali.
5. Logica Condizionale e Filtraggio: Sebbene limitati in alcuni contesti, parametri e variabili possono implementare logiche condizionali.
6. Personalizzazione e Interazione con l'Utente: Le variabili consentono input utente per personalizzare dinamicamente il comportamento degli Smart Marker.
7. Ottimizzazione delle Prestazioni: I parametri aiutano a ottimizzare le prestazioni controllando come i dati vengono elaborati.


## **Come Usare il Parametro if e le Variabili in SmartMarkers**
A volte, è necessario aggiungere una condizione if ai parametri variabili in SmartMarkers. Aspose.Cells rende possibile usare il parametro if e le variabili in SmartMarkers. Verifica il [file modello](template.xlsx), il [file json](data.json) e lo screenshot del file Excel generato con il seguente codice.

|**Il primo foglio del file template.xlsx mostra le variabili.**|
| :- |
|![todo:image_alt_text](variables.png)|

|**Il secondo foglio del file template.xlsx mostra gli smart markers.**|
| :- |
|![todo:image_alt_text](template.png)|

|**Lo screenshot del file Excel di output.**|
| :- |
|![todo:image_alt_text](result.png)|

Dati json come segue:
```json data
{
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
    "DOB": "2025-02-08",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111"
}
```
L'esempio seguente mostra come funziona.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-If-Parameter-And-Variables.cs" >}}

{{< app/cells/assistant language="csharp" >}}
