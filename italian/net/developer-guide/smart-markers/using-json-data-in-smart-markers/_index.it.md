---
title: Importazione intelligente di JSON in Excel con Smart Markers
type: docs
weight: 30
url: /it/net/how-to-import-json-into-excel-with-smart-markers/
alias: [/net/using-json-data-in-smart-markers/]
---

## **Perché usare i dati JSON per Smart Markers**
Perché utilizzare i dati JSON come dati originali per Smart Markers?
JSON (JavaScript Object Notation) è un formato di scambio dati leggero, leggibile dall’uomo, ideale per strutturare dati gerarchici. Ecco perché è adatto come dati originali per i marker intelligenti (segnaposto dinamici che popolano automaticamente fogli di calcolo, documenti o dashboard):

1. Supporto di dati strutturati e gerarchici
JSON supporta nativamente oggetti annidati e array (ad esempio, { "utente": { "nome": "Alice", "ordini": [ ... ] } }). I marker intelligenti possono attraversare questa gerarchia (ad esempio, {{utente.ordini[0].prezzo}}), rendendo facile mappare dati complessi ai modelli.

2. Indipendente da linguaggio e piattaforma
I parser JSON esistono in praticamente tutti i linguaggi di programmazione (Python, JavaScript, Java, ecc.). Strumenti come Excel Power Query, Google Apps Script o piattaforme senza codice (ad esempio, Airtable) integrano facilmente JSON.

3. Compatibile con API
La maggior parte delle API moderne (ad esempio REST, GraphQL) restituisce dati in formato JSON. I marker intelligenti possono consumare direttamente JSON live dai servizi web, consentendo aggiornamenti in tempo reale dei dati (ad esempio, prezzi azionari, meteo).

4. Leggibile dall’uomo e facilmente debugable
La struttura in testo semplice di JSON è facile da: Validare (ad esempio, usando JSONLint). Modificare manualmente o tramite script. Debuggare quando si mappano dati ai marker.

5. Scalabilità e flessibilità
Aggiungi/rimuovi campi in JSON senza interrompere i marker intelligenti esistenti (se i campi opzionali sono gestiti con grazia). Supporta diversi tipi di dati: stringhe, numeri, booleani, array e oggetti.

6. Compatibilità con l’ecosistema
Funziona con strumenti di dati moderni: Database: MongoDB, PostgreSQL (JSONB), ecc. Strumenti di automazione: Zapier, Integromat. Pipelines di dati: Apache NiFi, Talend.

## **Utilizzo del modello annidato di Excel con dati JSON**
Aspose.Cells for .NET supporta dati JSON nei smart markers, i dati JSON possono essere annidati gerarchicamente. Si prega di verificare [file modello](smartmarker.xlsx), [file JSON](smartmarker.json) e lo screenshot del file Excel di output generato con il seguente codice.

|**Il primo foglio di lavoro del file smartmarker.xlsx mostra smart markers.**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**Lo screenshot del file Excel di output.**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

Dati json come segue:
```json data
{
    "EntityCin" : "EntityCin Test",
    "EntityName" : "EntityName Test",
    "FirstName" : "FirstName Test",
    "MiddleName" : "MiddleName Test",
    "LastName" : "LastName Test",
    "DOB" : "2025-02-08",
    "SSN" : "11111111",
    "Directors" : [
        {
            "id" : "director id 1",
            "FirstName" : "director first 1",
            "MiddleName" : "director middle 1",
            "LastName" : "director last 1",
            "Reportees" : [
                {
                    "id" : "aaa",
                    "FirstName" : "first aaa",
                    "MiddleName" : "middle aaa",
                    "LastName" : "last aaa",
                    "Department" : "aaa department",
                    "City" : "aaa city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "bbb",
                    "FirstName" : "first bbb",
                    "MiddleName" : "middle bbb",
                    "LastName" : "last bbb",
                    "Department" : "bbb department",
                    "City" : "bbb city",
                    "GST" : "Yes",
                    "ITR" : "Yes"
                },
                {
                    "id" : "ccc",
                    "FirstName" : "first ccc",
                    "MiddleName" : "middle ccc",
                    "LastName" : "last ccc",
                    "Department" : "ccc department",
                    "City" : "ccc city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        },
        {
            "id" : "director id 2",
            "FirstName" : "director first 2",
            "MiddleName" : "director middle 2",
            "LastName" : "director last 2",
            "Reportees" : [
                {
                    "id" : "eee",
                    "FirstName" : "first eee",
                    "MiddleName" : "middle eee",
                    "LastName" : "last eee",
                    "Department" : "eee department",
                    "City" : "eee city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "fff",
                    "FirstName" : "first fff",
                    "MiddleName" : "middle fff",
                    "LastName" : "last fff",
                    "Department" : "fff department",
                    "City" : "fff city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        }
    ]
}
```
L'esempio seguente mostra come funziona.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data.cs" >}}


## **Utilizzo del modello di sottototale Excel con dati JSON**
Aspose.Cells for .NET supporta dati JSON nei smart markers, i dati JSON possono essere annidati gerarchicamente. Il sottototale è stato usato per le statistiche dei dati nel modello Excel. Si prega di verificare [file modello](jsonExcelTemplate.xlsx), [file JSON](jsonData.json) e lo screenshot del file Excel di output generato con il seguente codice.

|**Il primo foglio di lavoro del file jsonExcelTemplate.xlsx mostra smart markers.**|
| :- |
|![todo:image_alt_text](jsontemplate2.png)|

|**Lo screenshot del file Excel di output.**|
| :- |
|![todo:image_alt_text](jsonresult2.png)|

Dati json come segue:
```json data
{
    "number": 10,
    "test": "test abc",
    "date": "2011-10-05T14:48:00.000Z",
    "arrayNumber": [1,2,3,4,5],
    "arrayWords": ["x1","xy2","yz3","z4"],
    "arrayOfObjects": [
      {"valNumber":12,"valString": "aa"},
      {"valNumber":15,"valString": "bb"},
      {"valNumber":1,"valString": "cc"},
      {"valNumber":20,"valString": "dd"}

    ],
    "nestedArray": [
      {"valNumber":12,"valString": "xy","nestArr": [{"val": 1,"some": "aa"}]},
      {"valNumber":15,"valString": "y","nestArr": [{"val": 2,"some": "bb"}]},
      {"valNumber":1,"valString": "yz","nestArr": [{"some": "cc"}]},
      {"valNumber":20,"valString": "z","nestArr": [{"some": "dd"}]}
    ],
  "Products": [
    { "ProductID": "A101", "ProductName": "Apples", "Units": 5 },
    { "ProductID": "A101", "ProductName": "Apples", "Units": 10 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 7 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 3 },
    { "ProductID": "C303", "ProductName": "Cherries", "Units": 8 }
  ]
}
```
L'esempio seguente mostra come funziona.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data-Subtotal.cs" >}}

{{< app/cells/assistant language="csharp" >}}
