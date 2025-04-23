---
title: Smart import och placering av data med Smarta markörer
linktitle: Smarta markörer
type: docs
weight: 190
url: /sv/net/using-smart-markers/
description: Smartt importera och placera data enligt mallexcelfiler med Aspose.Cells biblioteket.
---


## **Introduktion**
**Smart markers** används för att låta Aspose.Cells veta vilken information som ska placeras i en Microsoft Excel-designmall. Smarta markörer gör det möjligt att skapa mallar som endast innehåller specifik information och formatering.
## **Designer Spreadsheet & Smart Markers**
Designer kalkylblad är standard Excel-filer som innehåller visuell formatering, formler och smarta markörer. De kan innehålla smarta markörer som refererar till en eller flera datakällor, såsom information från ett projekt och information för relaterade kontakter. Smarta markörer skrivs in i cellerna där du vill ha informationen.

Alla smarta markörer börjar med &=. Ett exempel på en datamarkör är &=Party.FullName. Om datamarkören resulterar i mer än en post, till exempel en komplett rad, flyttas följande rader ned automatiskt för att ge plats för den nya informationen. På så sätt kan delsummor och totaler placeras på raden omedelbart efter datamarkören för att göra beräkningar baserade på den infogade datan. Använd **dynamiska formler** för att göra beräkningar på de infogade raderna.

Smart markers består av **datakälla** och **fältnamn** för de flesta uppgifter. Speciell information kan också skickas med variabler och variabelmatriser. Variabler fyller alltid bara en cell medan variabelmatriser kan fylla flera. Använd endast en datamarkör per cell. Oanvända smart markers tas bort.

Smarta markörer kan också innehålla parametrar. Parametrar gör det möjligt att modifiera hur informationen layoutas. De läggs till i slutet av den smarta markören inom parentes som en kommateckenavgränsad lista.
### **Smart Marker-alternativ**
&=DataSource.FieldName 
&=[Data Source].[Field Name] 
&=$VariableName 
&=$VariableArray 
&==Dynamisk formula 
&=&=UpprepaDynamiskFormula
### **Parametrar**
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
### **Dynamiska formler**
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

## **Användning av variabla Arrayer**
Följande exempelkod visar hur man använder variabla matriser i Smart Markers. Vi placerar en variabel matrismarkör i cell A1 i den första kalkylbladet i arbetsboken dynamiskt som innehåller en sträng av värden som vi sätter för markören, bearbetar markörerna för att fylla data i cellerna mot markören. Till sist sparar vi Excelfilen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **Gruppering av data**
I vissa Excel-rapporter kan du behöva bryta upp datan i grupper för att göra det lättare att läsa och analysera. Ett av de primära syftena med att bryta upp data i grupper är att köra beräkningar (utföra sammanfattande operationer) på varje grupp av poster.

Aspose.Cells smarta markörer gör det möjligt att gruppera data efter fält och placera sammanfattande rader mellan databaser eller datagrupper. Till exempel, om data grupperas efter Kunder.KundID, kan du lägga till en sammanfattande post varje gång gruppen ändras.
### **Parametrar**
Här är några av de smarta markörsparametrar som används för att gruppera data.
#### **group:normal/merge/repeat**
Vi stödjer tre typer av grupper som du kan välja mellan.

- **normal** - Gruppera efter fält(s) värde upprepas inte för de motsvarande posterna i kolumnen; istället skrivs de ut en gång per datagrupp.
- **merge** - Samma beteende som för normalparametern, förutom att den slår samman cellerna i grupperingsfält(en) för varje gruppsats.
- **repeat** - Gruppera efter fält(s) värde upprepas för de motsvarande posterna.

Till exempel: &=Customers.CustomerID(group:merge)
#### **skip**
Hoppar ett angivet antal rader efter varje grupp.

Till exempel, &=Employees.EmployeeID(group:normal,skip:1)
#### **subtotalN**
Utför en sammanfattande operation för ett specificerat fältdata relaterat till ett grupperingsfält. N står för nummer mellan 1 och 11 som anger den funktion som används vid beräkning av delsummor inom en lista över data. (1=MEDDELVÄRDE, 2=RÄKNA, 3=RÄKNAA, 4=MAX, 5=MIN,...9=SUMMA osv.) Se delsummareferensen i Microsoft Excels hjälp för ytterligare detaljer.

Formatet anges faktiskt som:
delsummaN:Ref där Ref avser grupperingskolumnen.

Till exempel,

- &=Products.Units(delsumma9:Products.ProductID) anger sammanfattningsfunktion för fältet **Units** med avseende på fältet **ProductID** i tabellen **Products**.
- &=Tabx.Col3(delsumma9:Tabx.Col1) anger sammanfattningsfunktion för fältet **Col3** grupperat efter **Col1** i tabellen **Tabx**.
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) specificerar summeringsfunktion för fältet **ColumnD** grupperat efter **ColumnA** och **ColumnB** i tabellen **Table1**.

Det här exemplet visar några av gruppfunktionerna i aktion. Det använder Microsoft Access-databasen Northwind.mdb och extraherar data från tabellen som heter "Order Details". Vi skapar en designerfil som heter SmartMarker_Designer.xls i Microsoft Excel och placerar smarta markörer i olika celler i kalkylbladen. Markörerna bearbetas för att fylla i kalkylbladen. Data placeras och organiseras efter ett gruppfält.

Designfilen har två kalkylblad. På första kalkylbladet placerar vi smarta markörer med gruppindata som visas i skärmbilden nedan. Tre smarta markörer (med gruppfunktioner) placeras:
&=[Order Details].OrderID(group:merge,skip:1),
&=[Order Details].Quantity(subtotal9:Order Details.OrderID), and
&=[Order Details].UnitPrice(subtotal9:Order Details.OrderID) läggs in i A5, B5 och C5 respektive.

|**Det första kalkylbladet i filen SmartMarker_Designer.xls, komplett med smarta markörer**|
| :- |
|![todo:image_alt_text](using-smart-markers_5.png)|
I det andra kalkylbladet i designerfilen lägger vi till några fler smarta markörer enligt figuren nedan. Vi placerar följande smarta markörer:
&=[Order Details].OrderID(group:normal),
&=[Order Details].Quantity,
&=[Order Details].UnitPrice,
&=&=B(r)*C(r), and
&=subtotal9:Order Details.OrderID in i A5, B5, C5, D5 och C6 respektive.

|**Det andra kalkylbladet i filen SmartMarker_Designer.xls som visar blandade smarta markörer.**|
| :- |
|![todo:image_alt_text](using-smart-markers_6.png)|
Här är den källkod som används i exemplet.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Om du behöver lägga till dina egna anpassade etiketter till Summeringsrader eller om du vill sammanfoga fältnamnet med en etikett, t.ex. "Subtotal av Orders", tillhandahåller Aspose.Cells attributen Label och LabelPosition, så att du kan placera dina egna anpassade etiketter i Smarta Markörer medan du sammanfogar med Subtotalrader i grupperad data. Se dokumentet om hur man lägger till anpassade etiketter att sammanfoga med Subtotalrader i Smarta Markörer för din referens.

{{% /alert %}} 
## **Använda anonyma typer eller anpassade objekt**
Aspose.Cells stöder också anonyma typer eller anpassade objekt i smarta markörer. Exemplet nedan visar hur detta fungerar. För att importera data från dynamiska objekt med hjälp av Smarta Markörer, besök följande artikel:

[Importering från dynamiskt objekt som datakälla](/cells/sv/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **Bildmarkörer**
Aspose.Cells smarta markörer stödjer också bildmarkörer. Den här sektionen visar dig hur du sätter in bilder med hjälp av smarta markörer.
### **Bildparametrar**
Smarta markörsparametrar för hantering av bilder.

- **Bild:FitToCell** - Justera automatiskt bilden till cellens radhöjd och kolumnbredd.
- **Bild:SkalaN** - Skala höjd och bredd till N procent.
- **Picture:Width:Nin&Height:Nin** - Rendera bilden N tum hög och N tum bred. Du kan också specificera vänster och övre positioner (i punkter).

Här är den källkod som används i exemplet.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **Användning av inbäddade objekt**
Aspose.Cells stödjer inbäddade objekt i smarta markörer, de inbäddade objekten bör vara enkla. Vi använder en enkel mallfil. Se den designer-kalkylblad som innehåller några inbäddade smarta markörer.

|**Det första kalkylbladet i filen SM_NestedObjects.xlsx som visar inbäddade smarta markörer.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
Exemplet nedan visar hur detta fungerar.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}

## **Användning av JSON-data**
Aspose.Cells stöder json-data i smarta markörer, json-data kan vara hierarkiskt nästlad. Kontrollera gärna [mallfilen](smartmarker.xlsx), [json-filen](smartmarker.json) och skärmbilden av den genererade Excel-filen med följande kod.

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

## **Användning av generisk lista som inbäddat objekt**
Aspose.Cells stöder nu även användning av generiska listor som inbäddade objekt. Var god kontrollera skärmbilden av den genererade Excel-filen med följande kod. Som du kan se på skärmbilden innehåller ett lärarobjekt flera inbäddade studentobjekt.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **Användning av HTML-egenskapen hos Smart Markers**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **Inte rad för rad**
Den nuvarande standardbehandlingsmetoden är att behandla smartmaker rad för rad. Men ibland behöver smartmarkörer för samma datatabell behandlas tillsammans, oavsett 
om de är i samma rad eller inte, då måste du ange en angiven omfattning "_CellsSmartMarkers" och ange  WorkbookDesigner.LineByLine som falsk innan du anropar behandlingen.

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **Få meddelanden när data sammanfogas med smarta markörer**
Ibland kan det vara nödvändigt att få notifieringar om cellreferens eller den särskilda Smart Marker som behandlas innan färdigställandet. Detta kan uppnås med hjälp av egenskapen WorkbookDesigner.CallBack och ISmartMarkerCallBack

## **Fortsatta ämnen**
- [Lägg till anonymt eller anpassat objekt i SmartMarkers](/cells/sv/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Automatiskt fylla i Smart Marker-data till andra kalkylblad om datan är för stor](/cells/sv/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formatering av Smart Markers](/cells/sv/net/formatting-smart-markers/)
- [Få meddelanden när data sammanfogas med smarta markörer](/cells/sv/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Ange anpassad datakälla för WorkbookDesigner](/cells/sv/net/set-custom-datasource-for-workbookdesigner/)
- [Visa ledande apostrofer i celler](/cells/sv/net/show-leading-apostrophe-in-cells/)
- [Använda Formelparameter i Smart Marker-fält](/cells/sv/net/using-formula-parameter-in-smart-marker-field/)
- [Använda bildenkoder vid gruppering av data i Smart Markers](/cells/sv/net/using-image-markers-while-grouping-data-in-smart-markers/)


{{< app/cells/assistant language="csharp" >}}
