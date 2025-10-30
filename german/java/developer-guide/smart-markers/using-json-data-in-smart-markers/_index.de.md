---
title: Verwendung von JSON Daten in Smart Markern
type: docs
weight: 30
url: /de/java/using-json-data-in-smart-markers/
---

## **Warum JSON-Daten in Smart Markern verwenden**
Warum JSON-Daten als Originaldaten für Smart Marker verwenden?
JSON (JavaScript Object Notation) ist ein leichtgewichtiges, menschenlesbares Datenformat, das ideal für die Strukturierung hierarchischer Daten ist. Hier ist, warum es gut geeignet ist als Originaldaten für Smart Marker (dynamische Platzhalter, die automatisch Tabellen, Dokumente oder Dashboards ausfüllen):

1. Unterstützung für strukturierte und hierarchische Daten
JSON unterstützt native verschachtelte Objekte und Arrays (z.B. { "user": { "name": "Alice", "orders": [ ... ] } }). Smart Marker können diese Hierarchie durchqueren (z.B. {{user.orders[0].price}}), was das Mapping komplexer Daten auf Vorlagen erleichtert.

2. Plattform- und sprachunabhängig
JSON-Parser sind in nahezu allen Programmiersprachen verfügbar (Python, JavaScript, Java usw.). Tools wie Excel Power Query, Google Apps Script oder No-Code-Plattformen (z.B. Airtable) können JSON nahtlos einlesen.

3. API-kompatibel
Die meisten modernen APIs (z.B. REST, GraphQL) liefern Daten im JSON-Format. Smart Marker können direkt Live-JSON von Webdiensten konsumieren, was Echtzeitdaten-Updates ermöglicht (z.B. Aktienkurse, Wetter).

4. Menschenlesbar und debugbar
Die Klartext-Struktur von JSON ist einfach zu validieren (z.B. mit JSONLint), manuell zu bearbeiten oder per Skript zu ändern. Beim Abbilden von Daten auf Marker kann es auch bei der Fehlersuche hilfreich sein.

5. Skalierbarkeit und Flexibilität
Felder in JSON können hinzugefügt oder entfernt werden, ohne bestehende Smart Marker zu beschädigen (wenn optionale Felder gut behandelt werden). Unterstützt vielfältige Datentypen: Strings, Nummern, Booleans, Arrays und Objekte.

6. Kompatibilität mit Ecosystemen
Funktioniert mit modernen Datenwerkzeugen: Datenbanken wie MongoDB, PostgreSQL (JSONB) etc. Automatisierungstools wie Zapier, Integromat. Datenpipelines wie Apache NiFi, Talend.

## **Verwendung von Excel Verschachteltem Template mit JSON-Daten**
Aspose.Cells for Java unterstützt JSON-Daten in Smart Markern, JSON-Daten können hierarchisch verschachtelt werden. Bitte überprüfen Sie die [Vorlagendatei](smartmarker.xlsx), [JSON-Datei](smartmarker.json) und den Screenshot der generierten Excel-Ausgabedatei mit folgendem Code.

|**Das erste Arbeitsblatt der Datei smartmarker.xlsx zeigt Smart Marker.**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**Screenshot der Ausgabedatei im Excel-Format.**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

Die JSON-Daten sind wie folgt:
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
Das folgende Beispiel zeigt, wie dies funktioniert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data.java" >}}


## **Verwendung von Excel-Subtotal-Vorlage mit JSON-Daten**
Aspose.Cells for Java unterstützt JSON-Daten in Smart Markern, JSON-Daten können hierarchisch verschachtelt werden. Subtotal wurde für Datenstatistiken in der Excel-Vorlage verwendet. Bitte überprüfen Sie die [Vorlagendatei](jsonExcelTemplate.xlsx), [JSON-Datei](jsonData.json) und den Screenshot der generierten Excel-Ausgabedatei mit folgendem Code.

|**Das erste Arbeitsblatt der jsonExcelTemplate.xlsx-Datei zeigt Smart Marker.**|
| :- |
|![todo:image_alt_text](jsontemplate2.png)|

|**Screenshot der Ausgabedatei im Excel-Format.**|
| :- |
|![todo:image_alt_text](jsonresult2.png)|

Die JSON-Daten sind wie folgt:
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
Das folgende Beispiel zeigt, wie dies funktioniert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data-Subtotal.java" >}}

{{< app/cells/assistant language="java" >}}
