---
title: Smart import och placering av data med smarta markörer
linktitle: Smarta markörer
type: docs
weight: 190
url: /sv/net/using-smart-markers/
description: Smart importera och placera data som följer mallen Excel-filer med Aspose.Cells bibliotek.
---
## **Introduktion**
**Smarta markörer**används för att låta Aspose.Cells veta vilken information som ska placeras i ett Microsoft Excel-designark. Smarta markörer låter dig skapa mallar som bara innehåller specifik information och formatering.
## **Designerkalkylblad och smarta markörer**
Designer-kalkylblad är vanliga Excel-filer som innehåller visuell formatering, formler och smarta markörer. De kan innehålla smarta markörer som refererar till en eller flera datakällor, till exempel information från ett projekt och information för relaterade kontakter. Smarta markörer skrivs in i cellerna där du vill ha informationen.

 Alla smarta markörer börjar med &=. Ett exempel på en datamarkör är &=Party.FullName. Om datamarkören resulterar i mer än ett objekt, till exempel en hel rad, flyttas följande rader ned automatiskt för att ge plats åt den nya informationen. Således kan delsummor och summor placeras på raden omedelbart efter datamarkören för att göra beräkningar baserat på infogade data. För att göra beräkningar på de infogade raderna, använd**dynamiska formler**.

 Smarta markörer består av**datakälla** och**fält namn**delar för mest information. Särskild information kan också skickas med variabler och variabla arrayer. Variabler fyller alltid bara en cell medan variabla arrayer kan fylla flera. Använd endast en datamarkör per cell. Oanvända smarta markörer tas bort.

Smart markör kan också innehålla parametrar. Parametrar låter dig ändra hur informationen är upplagd. De läggs till i slutet av den smarta markören inom parentes som en kommaseparerad lista.
### **Alternativ för smarta markörer**
 &=Datakälla.Fältnamn
 &=[Datakälla].[Fältnamn]&=$VariableName
 &=$VariableArray
 &==DynamicFormula
&=&=RepeatDynamicFormula
### **Parametrar**
Följande parametrar är tillåtna:

- **noadd** - Lägg inte till extra rader för att passa data.
- **hoppa över:n** - Hoppa över n antal rader för varje rad med data.
- **stigande:n** eller**fallande:n** - Sortera data i smarta markörer. Om n är 1, är kolumnen den första nyckeln i sorteraren. Data sorteras efter bearbetning av datakällan. Till exempel: &=Tabell1.Fält3(stigande:1).
- **horisontell** - Skriv data från vänster till höger, istället för från topp till botten.
- **numerisk** - Konvertera text till nummer om möjligt.
- **flytta** - Växla nedåt eller höger, skapa extra rader eller kolumner för att passa data. Skiftparametern fungerar på samma sätt som i Microsoft Excel. Till exempel i Microsoft Excel, när du markerar ett cellintervall, högerklickar du och väljer**Föra in** och specificera**flytta ner cellerna**, **flytta celler åt höger** och andra alternativ. Kort sagt**flytta** parametern fyller samma funktion för vertikala/normala (uppifrån och ned) eller horisontella (vänster till höger) smarta markörer.
- **copystyle** - Kopiera bascellens stil till alla celler i den kolumnen.

Parametrarna noadd och skip kan kombineras för att infoga data på alternerande rader. Eftersom mallen bearbetas från botten till toppen bör du lägga till noadd på första raden för att undvika att extra rader infogas före den alternativa raden.

Om du har flera parametrar, separera dem med ett kommatecken, men inget mellanslag: parameterA,parameterB,parameterC

Följande skärmdumpar visar hur man infogar data på varannan rad.

|**Mallfil**|**Utdatafil**|
|:- |:- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|
### **Dynamiska formler**
Dynamiska formler låter dig infoga Excel-formler i celler även när formeln refererar till rader som kommer att infogas under exportprocessen. Dynamiska formler kan upprepas för varje infogat rad eller bara använda cellen där datamarkören är placerad.

Dynamiska formler tillåter följande ytterligare alternativ:

- r - Aktuellt radnummer.
- 2, -1 - Offset till aktuellt radnummer.

Till exempel:

{{< highlight "java" >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

I den dynamiska formelmarkören betecknar "-1" förskjutningen till den aktuella raden i B- respektive C-kolumner som kommer att ställas in för divisionsoperation, överhoppningsparametern är en rad. Dessutom bör vi ange följande char:

{{< highlight "java" >}}

 "~"

{{< /highlight >}}

som ett separatortecken för att tillämpa ytterligare parametrar i dynamiska formler.

Följande skärmdumpar illustrerar en återkommande dynamisk formel och det resulterande Excel-kalkylbladet.

|**Mallfil**|**OutPut-fil**|
|:- |:- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
 Cell "C1" innehåller formeln**= A1*B1** , cell "C2" innehåller**= A2*B2** och cell "C3" innehåller**= A3*B3**.

Det är väldigt enkelt att bearbeta de smarta markörerna. Vad som följer är två kodavsnitt, en i C# och en i VB, som visar hur det går till.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}
## **Använda variabla arrayer**
Följande exempelkod visar hur man använder variabla arrayer i Smart Markers. Vi placerar en variabel arraymarkör dynamiskt i A1-cellen i det första kalkylbladet i arbetsboken som innehåller en sträng med värden som vi ställer in för markören, bearbetar markörerna för att fylla data i cellerna mot markören. Slutligen sparar vi Excel-filen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **Gruppera data**
I vissa Excel-rapporter kan du behöva dela upp data i grupper för att göra det lättare att läsa och analysera. Ett av de primära syftena med att dela upp data i grupper är att köra beräkningar (utföra sammanfattningar) på varje grupp av poster.

Aspose.Cells smarta markörer låter dig gruppera data efter fält och placera sammanfattningsrader mellan datamängder eller datagrupper. Om du till exempel grupperar data efter Customers.CustomerID, kan du lägga till en sammanfattningspost varje gång gruppen ändras.
### **Parametrar**
Nedan följer några av de smarta markörparametrarna som används för att gruppera data.
#### **grupp:normal/sammanfoga/upprepa**
Vi stödjer tre typer av grupper som du kan välja mellan.

- **vanligt** - Värdet för grupp efter fält upprepas inte för motsvarande poster i kolumnen; istället skrivs de ut en gång per datagrupp.
- **sammanfoga** - Samma beteende som för den normala parametern, förutom att den slår samman cellerna i gruppen efter fält för varje gruppuppsättning.
- **upprepa** - Värdet för grupp efter fält upprepas för motsvarande poster.

Till exempel: &=Kunder.Kund-ID(grupp:sammanfoga)
#### **hoppa**
Hoppa över ett angivet antal rader efter varje grupp.

Till exempel &=Anställda.Anställd-ID(grupp:normal,hoppa över:1)
#### **delsummaN**
Utför en sammanfattningsåtgärd för en specificerad fältdata relaterad till en grupp för fält. N representerar siffror mellan 1 och 11 som anger funktionen som används vid beräkning av delsummor i en lista med data. (1=GENOMsnitt, 2=ANTAL, 3=ANTAL, 4=MAX, 5=MIN,...9=SUMMA etc.) Se Deltotalreferensen i Microsoft Excels hjälp för ytterligare detaljer.

Formatet säger faktiskt som:
subtotalN:Ref där Ref refererar till gruppen för kolumn.

Till exempel,

-  &=Products.Units(subtotal9:Products.ProductID) specificerar sammanfattningsfunktion på**Enheter** fält med avseende på**Serienummer** fältet i**Produkter** tabell.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) anger sammanfattningsfunktionen på**Kol3** fältgrupp efter**Kol 1** i bordet**Tabx**.
-  &=Tabell1.KolumnD(delsumma9:Tabell1.KolumnA&Tabell1.KolumnB) anger sammanfattningsfunktion på**KolumnD** fältgrupp efter**Kolumn A** och**KolumnB** i bordet**Bord 1**.

Det här exemplet visar några av grupperingsparametrarna i funktion. Den använder Northwind.mdb Microsoft Access-databasen och extraherar data från tabellen med namnet "Order Details". Vi skapar en designerfil som heter SmartMarker_Designer.xls i Microsoft Excel och lägger in smarta markörer i olika celler i kalkylblad. Markörerna bearbetas för att fylla kalkylbladen. Data placeras och organiseras av ett gruppfält.

Designerfilen har två kalkylblad. I den första lägger vi smarta markörer med grupperingsparametrar som visas i skärmdumpen nedan. Tre smarta markörer (med grupperingsparametrar) placeras:
&=[Beställningsinformation].OrderID(grupp:sammanfoga,hoppa över:1),
&=[Beställningsinformation].Quantity(subtotal9:Order Details.OrderID), och
&=[Beställningsinformation].UnitPrice(delsumma9:Beställningsdetaljer.OrderID) går in i A5, B5 respektive C5.

|**Det första kalkylbladet i filen SmartMarker_Designer.xls, komplett med smarta markörer**|
|:- |
|![todo:image_alt_text](using-smart-markers_5.png)|
det andra kalkylbladet i designerfilen lägger vi några fler smarta markörer som visas i figuren nedan. Vi placerar följande smarta markörer:
&=[Beställningsinformation].OrderID(grupp:normal),
&=[Beställningsinformation].Antal,
&=[Beställningsinformation].UnitPrice,
&=&=B(r)*C(r), och
&=subtotal9:Beställningsdetaljer.OrderID till A5, B5, C5, D5 respektive C6.

|**Det andra kalkylbladet i filen SmartMarker_Designer.xls, som visar blandade smarta markörer.**|
|:- |
|![todo:image_alt_text](using-smart-markers_6.png)|
Här är källkoden som används i exemplet.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Om du behöver lägga till dina egna anpassade etiketter till sammanfattningsraderna eller om du vill sammanfoga fältets namn med en etikett, t.ex. "Subtotal of Orders", ger Aspose.Cells dig Label- och LabelPosition-attribut, så att du kan placera dina anpassade etiketter i Smart Markörer vid sammanlänkning med Subtotal-raderna i grupperingsdata. Se dokumentet om hur du lägger till anpassade etiketter för att sammanfoga med subtotalraderna i smarta markörer som referens.

{{% /alert %}} 
## **Använda anonyma typer eller anpassade objekt**
Aspose.Cells stöder även anonyma typer eller anpassade objekt i smarta markörer. Exemplet som följer visar hur detta fungerar. För att importera data från dynamiska objekt med smarta markörer, besök följande artikel:

[Importerar från dynamiskt objekt som datakälla](/cells/sv/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **Bildmarkörer**
Aspose.Cells smarta markörer stöder också bildmarkörer. Det här avsnittet visar hur du infogar bilder med smarta markörer.
### **Bildparametrar**
Smarta markörparametrar för att hantera bilder.

- **Bild: FitToCell** - Anpassa bilden automatiskt till cellens radhöjd och kolumnbredd.
- **Bild: ScaleN** - Skala höjd och bredd till N procent.
- **Bild:Bredd:Nin&Höjd:Nin** - Gör bilden N tum hög och N tum bred. Du kan också ange vänster- och topppositioner (i poäng).

Här är källkoden som används i exemplet.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **Använda kapslade objekt**
Aspose.Cells stöder kapslade objekt i smarta markörer, de kapslade objekten ska vara enkla. Vi använder en enkel mallfil. Se designerkalkylarket som innehåller några kapslade smarta markörer.

|**Det första kalkylbladet i filen SM_NestedObjects.xlsx som visar kapslade smarta markörer.**|
|:- |
|![todo:image_alt_text](using-smart-markers_7.png)|
Exemplet som följer visar hur detta fungerar.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}
## **Använder generisk lista som kapslade objekt**
Aspose.Cells stöder nu även användning av generisk lista som ett kapslat objekt. Kontrollera skärmdumpen av den utgående excel-filen som genereras med följande kod. Som du kan se på skärmdumpen innehåller ett Lärarobjekt flera kapslade Studentobjekt.

|![todo:image_alt_text](using-smart-markers_8.png)|
|:- |




{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **Använder HTML egendom för Smart Markers**
 Följande exempelkod förklarar användningen av egenskapen HTML för Smart Markers. När det kommer att bearbetas kommer det att visa "World" i "Hello World" som fetstil på grund av HTML<b> märka.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **Inte rad för rad**
 Den nuvarande standardbehandlingsmetoden är att bearbeta smartmaker rad för rad. Men ibland måste de smarta markörerna i samma datatabell bearbetas tillsammans, oavsett
om de är i samma rad eller inte, måste du ange ett namngivet intervall "_CellsSmartMarkers" och ange WorkbookDesigner.LineByLine som falskt innan du anropar bearbetningen.

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **Få aviseringar när du slår samman data med smarta markörer**
Ibland kan det krävas att du får meddelanden om cellreferensen eller den specifika smarta markören som bearbetas innan slutförandet. Detta kan uppnås med hjälp av egenskapen WorkbookDesigner.CallBack och ISmartMarkerCallBack

## **Förhandsämnen**
- [Lägga till anonymt eller anpassat objekt i SmartMarkers](/cells/sv/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Fyll i smartmarkördata automatiskt till andra kalkylblad om data är för stor](/cells/sv/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formatera smarta markörer](/cells/sv/net/formatting-smart-markers/)
- [Få aviseringar när du slår samman data med smarta markörer](/cells/sv/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Ställ in anpassad DataSource för WorkbookDesigner](/cells/sv/net/set-custom-datasource-for-workbookdesigner/)
- [Visa ledande apostrof i celler](/cells/sv/net/show-leading-apostrophe-in-cells/)
- [Använder formelparametern i Smart Marker-fältet](/cells/sv/net/using-formula-parameter-in-smart-marker-field/)
- [Använda bildmarkörer samtidigt som data grupperas i smarta markörer](/cells/sv/net/using-image-markers-while-grouping-data-in-smart-markers/)


