---
title: Smart Marker parametrar
type: docs
weight: 30
url: /sv/net/smart-marker-parameters/
---

## **Designer Spreadsheet & Smart Markers**
Designer kalkylblad är standard Excel-filer som innehåller visuell formatering, formler och smarta markörer. De kan innehålla smarta markörer som refererar till en eller flera datakällor, såsom information från ett projekt och information för relaterade kontakter. Smarta markörer skrivs in i cellerna där du vill ha informationen.

Alla smarta markörer börjar med &=. Ett exempel på en datamarkör är &=Party.FullName. Om datamarkören resulterar i mer än en post, till exempel en komplett rad, flyttas följande rader ned automatiskt för att ge plats för den nya informationen. På så sätt kan delsummor och totaler placeras på raden omedelbart efter datamarkören för att göra beräkningar baserade på den infogade datan. Använd **dynamiska formler** för att göra beräkningar på de infogade raderna.

Smart markers består av **datakälla** och **fältnamn** för de flesta uppgifter. Speciell information kan också skickas med variabler och variabelmatriser. Variabler fyller alltid bara en cell medan variabelmatriser kan fylla flera. Använd endast en datamarkör per cell. Oanvända smart markers tas bort.

Smarta markörer kan också innehålla parametrar. Parametrar gör det möjligt att modifiera hur informationen layoutas. De läggs till i slutet av den smarta markören inom parentes som en kommateckenavgränsad lista.

## **Smart Marker-alternativ**

```csharp
&=DataSource.FieldName 
&=[Data Source].[Field Name] 
&=$VariableName 
&=$VariableArray 
&==DynamicFormula 
&=&=RepeatDynamicFormula
```
## **Smart Marker-parametrar**
Följande parametrar är tillåtna:

- **noadd** - Lägg inte till extra rader för att passa data.
- **skip:n** - Hoppa över n antal rader för varje datarad.
- **ascending:n** eller **descending:n** - Sortera data i smarta markörer. Om n är 1, då är kolumnen den första nyckeln för sorteraren. Datan sorteras efter bearbetningen av datakällan. Till exempel: &=Table1.Field3(ascending:1).
- **horisontell** - Skriv data från vänster till höger i stället för uppifrån och ner.
- **numerisk** - Konvertera text till nummer om möjligt.
- **skift** - Skifta ner eller åt höger, skapa extra rader eller kolumner för att passa datan. Skiftparametern fungerar på samma sätt som i Microsoft Excel. Till exempel i Microsoft Excel när du väljer en rad med celler, högerklickar och väljer **Infoga** och specificerar **skifta celler nedåt**, **skifta celler åt höger** och andra alternativ. Kort sagt fyller skiftparametern samma funktion för vertikala / normala (höjd till botten) eller horisontella (vänster till höger) smarta markörer.
- **kopierastil** - Kopiera bascellens stil till alla celler i den kolumnen.

Parametrarna noadd och skip kan kombineras för att infoga data på växelvis rader. Eftersom mallen behandlas uppifrån och ner, bör du lägga till noadd på den första raden för att undvika att extra rader infogas före den växelvisa raden.

Om du har flera parametrar, separera dem med kommatecken, men inget mellanrum: parameterA, parameterB, parameterC

Följande skärmbilder visar hur du infogar data på varannan rad.

|**Mallfil**|**Resultatfil**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|

## **Dynamiska formler**
Dynamiska formler gör det möjligt att infoga Excel-formler i celler även när formeln refererar till rader som kommer att infogas under exportprocessen. Dynamiska formler kan upprepas för varje infogad rad eller använda endast den cell där datamarkören placeras.

Dynamiska formler möjliggör följande ytterligare alternativ:

- r - Nuvarande radnummer.
- 2, -1 - Förskjutning till aktuellt radnummer.

Exempelvis:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

I den dynamiska formelmarkören betecknar "-1" förskjutningen till den nuvarande raden i kolumn B och C respektive som kommer att ställas in för divisionsoperationen, hoppa parametern är en rad. Dessutom bör vi ange följande tecken:

{{< highlight java >}}

 "~"

{{< /highlight >}}

som ett avskiljande tecken för att tillämpa ytterligare parametrar i dynamiska formler.

De följande skärmbilderna illustrerar en upprepande dynamisk formel och den resulterande Excel-arket.

|**Mallfil**|**Utdatafil**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
Cellen "C1" innehåller formeln **= A1*B1**, cellen "C2" innehåller **= A2*B2** och cellen "C3" innehåller **= A3*B3**.

Det är mycket enkelt att bearbeta smarta markörer. Följande exempelkod visar hur du använder dynamiska formler i Smart Markers. Vi laddar [mallfilen](templateDynamicFormulas.xlsx) och skapar testdata, bearbetar markörerna för att fylla i data i cellerna mot markören. 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **Hur man använder dynamiska formler och variabler i SmartMarkers**
Ibland måste du använda dynamiska formler och variabler i SmartMarkers. För dynamiska formler, lägg till tecknet (~) som separator. Aspose.Cells gör det möjligt att använda dynamiska formler och variabler i SmartMarkers. Kontrollera gärna [mallfilen](template.xlsx), [jsonfilen](employees-data.json) och skärmbilden av den genererade Excel-filen med följande kod.

|**Första arbetsbladet i template.xlsx-filen som visar variabler.**|
| :- |
|![todo:image_alt_text](template_variables.png)|

|**Andra arbetsbladet i template.xlsx-filen som visar smarta markörer.**|
| :- |
|![todo:image_alt_text](template_data.png)|

|**Skärmbild av utdata Excel-fil.**|
| :- |
|![todo:image_alt_text](template_result.png)|

Json-data enligt följande:
```json data
{
  "RootData": {
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
          },
          {
            "City": "ddd city",
            "Department": "ddd department",
            "FirstName": "first ddd",
            "GST": "No",
            "id": "ddd",
            "ITR": "No",
            "LastName": "last ddd",
            "MiddleName": "middle ddd"
          },
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "No",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
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
    "DOB": "2025-02-28",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111",
	"CtcPerEmployee": 100000,
	"CountOfEmployees": 132
  }
}
```
Exemplet nedan visar hur detta fungerar.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-DynamicFormula-And-Variables.cs" >}}
