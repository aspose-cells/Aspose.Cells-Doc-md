---
title: Hur man grupperar data i Smart Markers
type: docs
weight: 30
url: /sv/net/how-to-group-data-in-smart-markers/
---

## **Möjliga användningsscenario**
I vissa Excel-rapporter kan du behöva bryta upp datan i grupper för att göra det lättare att läsa och analysera. Ett av de primära syftena med att bryta upp data i grupper är att köra beräkningar (utföra sammanfattande operationer) på varje grupp av poster.

Aspose.Cells smarta markörer gör det möjligt att gruppera data efter fält och placera sammanfattande rader mellan databaser eller datagrupper. Till exempel, om data grupperas efter Kunder.KundID, kan du lägga till en sammanfattande post varje gång gruppen ändras.

## **Parametrar för datagruppering i Smart Markers**
Här är några av de smarta markörsparametrar som används för att gruppera data.
### **group:normal/merge/repeat**
Vi stödjer tre typer av grupper som du kan välja mellan.

- **normal** - Gruppera efter fält(s) värde upprepas inte för de motsvarande posterna i kolumnen; istället skrivs de ut en gång per datagrupp.
- **merge** - Samma beteende som för normalparametern, förutom att den slår samman cellerna i grupperingsfält(en) för varje gruppsats.
- **repeat** - Gruppera efter fält(s) värde upprepas för de motsvarande posterna.

Till exempel: &=Customers.CustomerID(group:merge)
### **skip**
Hoppar ett angivet antal rader efter varje grupp.

Till exempel, &=Employees.EmployeeID(group:normal,skip:1)
### **subtotalN**
Utför en sammanfattande operation för ett specificerat fältdata relaterat till ett grupperingsfält. N står för nummer mellan 1 och 11 som anger den funktion som används vid beräkning av delsummor inom en lista över data. (1=MEDDELVÄRDE, 2=RÄKNA, 3=RÄKNAA, 4=MAX, 5=MIN,...9=SUMMA osv.) Se delsummareferensen i Microsoft Excels hjälp för ytterligare detaljer.

Formatet anges faktiskt som:
delsummaN:Ref där Ref avser grupperingskolumnen.

Till exempel,

- &=Products.Units(delsumma9:Products.ProductID) anger sammanfattningsfunktion för fältet **Units** med avseende på fältet **ProductID** i tabellen **Products**.
- &=Tabx.Col3(delsumma9:Tabx.Col1) anger sammanfattningsfunktion för fältet **Col3** grupperat efter **Col1** i tabellen **Tabx**.
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) specificerar summeringsfunktion för fältet **ColumnD** grupperat efter **ColumnA** och **ColumnB** i tabellen **Table1**.

## **Hur man grupperar data i Smart Markers**

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
