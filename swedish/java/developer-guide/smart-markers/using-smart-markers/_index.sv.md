---
title: Använda smarta markörer
type: docs
weight: 40
url: /sv/java/using-smart-markers/
---
## **Introduktion**

{{% alert color="primary" %}}

**Smarta markörer** används för att låta Aspose.Cells veta vilken information som ska placeras i en Microsoft Excel[designerkalkylblad](/cells/sv/java/what-is-a-designer-spreadsheet/). Smarta markörer låter dig skapa mallar som endast innehåller relevant information och formatering.

{{% /alert %}}

## **Designerkalkylblad och smarta markörer**

Designer-kalkylblad är vanliga Excel-filer som innehåller visuell formatering, formler och smarta markörer. De kan innehålla smarta markörer som refererar till en eller flera datakällor, till exempel information från ett projekt och information för relaterade kontakter. Smarta markörer skrivs in i cellerna där du vill ha information.

 Alla smarta markörer börjar med &=. Ett exempel på en datamarkör är &=Party.FullName. Om datamarkören resulterar i mer än ett objekt, till exempel en hel rad, flyttas följande rader ned automatiskt för att ge plats åt den nya informationen. Således kan delsummor och totaler placeras på raden omedelbart efter datamarkören för att göra beräkningar baserade på infogade data. För att göra beräkningar på de infogade raderna, använd[dynamiska formler](/cells/sv/java/using-smart-markers/#dynamic-formulas).

 Smarta markörer består av**datakälla** och**fält namn**delar för mest information. Särskild information kan också skickas med variabler och variabla arrayer. Variabler fyller alltid bara en cell medan variabla arrayer kan fylla flera. Använd endast en datamarkör per cell. Oanvända smarta markörer tas bort.

En smart markör kan också innehålla parametrar. Parametrar låter dig ändra hur informationen är upplagd. De läggs till i slutet av den smarta markören inom parentes som en kommaseparerad lista.

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
- *stigande:n eller fallande:n - Sortera data i smarta markörer. Om n är 1, är kolumnen den första nyckeln i sorteraren. Data sorteras efter bearbetning av datakällan. Till exempel: &=Tabell1.Fält3(stigande:1).
- **horisontell** - Skriv data från vänster till höger, istället för från topp till botten.
- **numerisk** - Konvertera text till nummer om möjligt.
- **flytta** - Växla nedåt eller höger, skapa extra rader eller kolumner för att passa data. Skiftparametern fungerar på samma sätt som i Microsoft Excel. Till exempel i Microsoft Excel, när du markerar ett cellintervall, högerklickar du och väljer**Föra in** och specificera**flytta ner cellerna**, **flytta celler åt höger** och andra alternativ. Kort sagt, skiftparametern fyller samma funktion för vertikala/normala (uppifrån och ned) eller horisontella (vänster till höger) smarta markörer.
- **böna** - Indikerar att datakällan är en enkel POJO. Stöds endast i Java API.

Parametrarna noadd och skip kan kombineras för att infoga data på alternerande rader. Eftersom mallen bearbetas från botten till toppen bör du lägga till noadd på den första raden för att undvika att extra rader infogas före den alternativa raden.

Om du har flera parametrar, separera dem med ett kommatecken, men inget mellanslag: parameterA,parameterB,parameterC

Följande skärmdumpar visar hur man infogar data på varannan rad.

![todo:image_alt_text](using-smart-markers_1.png)

**blir...**

![todo:image_alt_text](using-smart-markers_2.png)

### **Dynamiska formler**

Dynamiska formler låter dig infoga Excel-formler i celler även när formeln refererar till rader som kommer att infogas under exportprocessen. Dynamiska formler kan upprepas för varje infogat rad eller bara använda cellen där datamarkören är placerad.

Dynamiska formler tillåter följande ytterligare alternativ:

- r - Aktuellt radnummer.
- 2, -1 - Offset till aktuellt radnummer.

Följande illustrerar en återkommande dynamisk formel och det resulterande Excel-kalkylbladet.

![todo:image_alt_text](using-smart-markers_3.png)

**blir...**

![todo:image_alt_text](using-smart-markers_4.png)

Cell C1 innehåller formeln =A1*B1, C2 innehåller = A2*B2 och C3 = A3*B3.

Det är väldigt enkelt att bearbeta de smarta markörerna. Följande kodavsnitt visar hur det går till.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **Använda variabla arrayer**

Följande exempelkod visar hur man använder variabla arrayer i Smart Markers. Vi placerar en variabel arraymarkör dynamiskt i A1-cellen i det första kalkylbladet i arbetsboken som innehåller en sträng med värden som vi ställer in för markören, bearbetar markörerna för att fylla data i cellerna mot markören. Slutligen sparar vi Excel-filen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **Gruppera data**

I vissa Excel-rapporter kan du behöva dela upp data i grupper för att göra det lättare att läsa och analysera. Ett av de primära syftena med att dela upp data i grupper är att köra beräkningar (utföra sammanfattningar) på varje grupp av poster.

Aspose.Cells smarta markörer låter dig gruppera data efter fältuppsättningar och placera sammanfattningsrader mellan datamängder eller datagrupper. Om du till exempel grupperar data efter Customers.CustomerID, kan du lägga till en sammanfattningspost varje gång gruppen ändras.

### **Parametrar**

Nedan följer några smarta markörparametrar som används för att gruppera data.

#### **grupp:normal/sammanfoga/upprepa**

Vi stödjer tre typer av grupper som du kan välja mellan.

- **vanligt** - Värdet för grupp efter fält upprepas inte för motsvarande poster i kolumnen; istället skrivs de ut en gång per datagrupp.
- **sammanfoga** - Samma beteende som för den normala parametern, förutom att den slår samman cellerna i gruppen efter fält för varje gruppuppsättning.
- **upprepa** - Värdet för grupp efter fält upprepas för motsvarande poster.

Till exempel: &=Kunder.Kund-ID(grupp:sammanfoga)

#### **hoppa**

Hoppa över ett visst antal rader efter varje grupp.

Till exempel &=Anställda.Anställd-ID(grupp:normal,hoppa över:1)

#### **delsummaN**

Utför en sammanfattningsåtgärd för en specificerad fältdata relaterad till en grupp för fält. N representerar siffror mellan 1 och 11 som anger funktionen som används vid beräkning av delsummor i en lista med data. (1=GENOMsnitt, 2=ANTAL, 3=ANTAL, 4=MAX, 5=MIN,...9=SUMMA etc.) Se Deltotalreferensen i Microsoft Excels hjälp för ytterligare detaljer.

Formatet säger faktiskt som:
subtotalN:Ref där Ref refererar till gruppen för kolumn.

Till exempel,

-  &=Products.Units(subtotal9:Products.ProductID) specificerar sammanfattningsfunktion på**Enheter** fält med avseende på**Serienummer** fältet i**Produkter** tabell.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) anger sammanfattningsfunktionen på**Kol3** fältgrupp efter**Kol 1** i bordet**Tabx**.
-  &=Tabell1.KolumnD(delsumma9:Tabell1.KolumnA&Tabell1.KolumnB) anger sammanfattningsfunktion på**KolumnD** fältgrupp efter**Kolumn A** och**KolumnB** i tabellen**Bord 1**.

## **Använda kapslade objekt**

Aspose.Cells stöder kapslade objekt i smarta markörer, de kapslade objekten ska vara enkla.

Vi använder en enkel mallfil. Se designerkalkylarket som innehåller några kapslade smarta markörer.

**Det första kalkylbladet i designerfilen som visar kapslade smarta markörer.**

![todo:image_alt_text](using-smart-markers_5.png)

Exemplet som följer visar hur detta fungerar. Att köra koden nedan resulterar i utgången nedan.

**Det första kalkylbladet i utdatafilen som visar de resulterande data.**

![todo:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **Använder generisk lista som kapslade objekt**

Aspose.Cells stöder nu även användning av en generisk lista som ett kapslat objekt. Kontrollera skärmdumpen av den utgående excel-filen som genereras med följande kod. Som du kan se på skärmdumpen innehåller ett Lärarobjekt flera kapslade elevobjekt.

![todo:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **Använder HTML egendom för Smart Markers**

Följande exempelkod förklarar användningen av egenskapen HTML för Smart Markers. När det kommer att bearbetas kommer det att visa "World" i "Hello World" som fetstil på grund av HTML \<b> märka.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **Få aviseringar när du slår samman data med smarta markörer**

 Ibland kan det krävas att du får meddelanden om cellreferensen eller den specifika smarta markören som bearbetas innan slutförandet. Detta kan uppnås med hjälp av[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)egendom och[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

För exempelkod och detaljerad förklaring, se den här artikeln.

- [Få aviseringar när du slår samman data med smarta markörer](/cells/sv/java/getting-notifications-while-merging-data-with-smart-markers/)
