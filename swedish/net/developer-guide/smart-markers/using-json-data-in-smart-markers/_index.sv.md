---
title: Smart import av JSON till Excel med Smart Markers
type: docs
weight: 30
url: /sv/net/how-to-import-json-into-excel-with-smart-markers/
alias: [/net/using-json-data-in-smart-markers/]
---

## **Varför använda JSON-data för Smart Markers**
Varför använda JSON-data som ursprungsdata för Smart Markers?
JSON (JavaScript Object Notation) är ett lättviktigt, människoläsbart datautbytesformat som är idealiskt för att strukturera hierarkiska data. Här är varför det passar bra som ursprungsdata för smarta markörer (dynamiska platshållare som automatiskt fyller i kalkylblad, dokument eller dashboards):

1. Stöd för strukturerad och hierarkisk data
JSON stöder naturligt inbäddade objekt och arrayer (t.ex., { "användare": { "namn": "Alice", "beställningar": [ ... ] } }). Smart markörer kan traversera denna hierarki (t.ex., {{användare.beställningar[0].pris}}), vilket gör det enkelt att mappa komplex data till mallar.

2. Plattform- och språkoberoende
JSON-parsers finns i praktiskt taget alla programmeringsspråk (Python, JavaScript, Java, etc.). Verktyg som Excel Power Query, Google Apps Script eller no-code plattformar (t.ex., Airtable) importerar sömlöst JSON.

3. API-vänligt
De flesta moderna API:er (t.ex., REST, GraphQL) returnerar data i JSON-format. Smart markörer kan direkt konsumera live JSON från webbtjänster och möjliggöra uppdateringar i realtid (t.ex., aktiekurser, väder).

4. Människoläsbart och felsökningsbart
JSON:s snälla textstruktur är lätt att: Validera (t.ex., med JSONLint). Redigera manuellt eller via skript. Felsöka vid mappning av data till markörer.

5. Skalbarhet och flexibilitet
Lägg till eller ta bort fält i JSON utan att bryta befintliga smarta markörer (om frivilliga fält hanteras smidigt). Stöd för olika datatyper: strängar, nummer, Boolean, arrayer och objekt.

6. Ekosystemkompatibilitet
Fungerar med moderna dataverktyg: databaser: MongoDB, PostgreSQL (JSONB), etc. Automatiseringsverktyg: Zapier, Integromat. Data pipelines: Apache NiFi, Talend.

## **Användning av Excel inbäddad mall med JSON-data**
Aspose.Cells for .NET stöder json-data i smartmarkörer, json-data kan vara invävda hierarkiskt. Vänligen kontrollera [mallfil](smartmarker.xlsx), [json-fil](smartmarker.json) och skärmbilden av den utskrivna Excel-filen genererad med följande kod.

|**Den första arbetsbladet i smartmarker.xlsx-filen visar smarta markörer.**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**Skärmbild av utdata Excel-fil.**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

Json-data enligt följande:
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
Exemplet nedan visar hur detta fungerar.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data.cs" >}}


## **Använder Excel Subtotal-mall med JSON-data**
Aspose.Cells for .NET stöder json-data i smartmarkörer, json-data kan vara invävda hierarkiskt. Subtotal användes för datasammanställning i Excel-mallen. Vänligen kontrollera [mallfil](jsonExcelTemplate.xlsx), [json-fil](jsonData.json) och skärmbilden av den utskrivna Excel-filen genererad med följande kod.

|**Det första arket i jsonExcelTemplate.xlsx visar smartmarkörer.**|
| :- |
|![todo:image_alt_text](jsontemplate2.png)|

|**Skärmbild av utdata Excel-fil.**|
| :- |
|![todo:image_alt_text](jsonresult2.png)|

Json-data enligt följande:
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
Exemplet nedan visar hur detta fungerar.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data-Subtotal.cs" >}}

{{< app/cells/assistant language="csharp" >}}
