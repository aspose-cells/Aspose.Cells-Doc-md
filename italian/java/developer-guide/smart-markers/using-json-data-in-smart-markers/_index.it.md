---
title: Utilizzo dei dati Json nei Marker Intelligenti
type: docs
weight: 30
url: /it/java/using-json-data-in-smart-markers/
---

## **Perché usare i dati Json nei Marker Intelligenti**
Perché usare i dati JSON come dati originali per i Marker Intelligenti?
JSON (JavaScript Object Notation) è un formato di scambio dati leggero e leggibile dall’uomo, ideale per strutturare dati gerarchici. Ecco perché è adatto come dato originale per i marker intelligenti (sostituzioni dinamiche che si auto-compilano in fogli di calcolo, documenti o dashboard):

1. Supporto a dati strutturati e gerarchici
JSON supporta nativamente oggetti e array annidati (ad esempio, { "utente": { "nome": "Alice", "ordini": [ ... ] } }). I marker intelligenti possono attraversare questa gerarchia (ad esempio, {{utente.ordini[0].prezzo}}), rendendo facile mappare dati complessi ai modelli.

2. Independentemente dal linguaggio e dalla piattaforma
I parser JSON sono disponibili in quasi tutti i linguaggi di programmazione (Python, JavaScript, Java, ecc.). Strumenti come Excel Power Query, Google Apps Script o piattaforme senza codice (ad esempio Airtable) integrano facilmente JSON.

3. Compatibile con API
La maggior parte delle API moderne (ad esempio REST, GraphQL) restituisce dati in formato JSON. I marker intelligenti possono consumare direttamente JSON live dai servizi web, consentendo aggiornamenti dati in tempo reale (ad esempio prezzi azionari, meteo).

4. Leggibile dall'uomo e facilmente debugabile
La struttura semplice del testo di JSON è facile da: Validare (ad esempio, usando JSONLint). Modificare manualmente o tramite script. Debuggare quando si mappa i dati ai marker.

5. Scalabilità e flessibilità
Aggiungere/rimuovere campi in JSON senza rompere i marker intelligenti esistenti (se i campi opzionali sono gestiti correttamente). Supporta vari tipi di dati: stringhe, numeri, booleani, array e oggetti.

6. Compatibilità con l'ecosistema
Funziona con strumenti di dati moderni: Databases: MongoDB, PostgreSQL (JSONB), ecc. Strumenti di automazione: Zapier, Integromat. Data pipeline: Apache NiFi, Talend.

## **Utilizzo del modello annidato di Excel con dati JSON**
Aspose.Cells for Java supporta dati JSON nei marker intelligenti, i dati JSON possono essere annidati gerarchicamente. Si prega di controllare [file modello](smartmarker.xlsx), [file JSON](smartmarker.json) e lo screenshot del file Excel generato con il seguente codice.

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data.java" >}}


## **Utilizzo del modello di subtotale di Excel con dati JSON**
Aspose.Cells for Java supporta dati JSON nei marker intelligenti, i dati JSON possono essere annidati gerarchicamente. Sono stati usati i subtotali per le statistiche dei dati nel modello Excel. Si prega di controllare [file modello](jsonExcelTemplate.xlsx), [file JSON](jsonData.json) e lo screenshot del file Excel generato con il seguente codice.

|**Il primo foglio del file jsonExcelTemplate.xlsx che mostra i marker intelligenti.**|
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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data-Subtotal.java" >}}

{{< app/cells/assistant language="java" >}}
