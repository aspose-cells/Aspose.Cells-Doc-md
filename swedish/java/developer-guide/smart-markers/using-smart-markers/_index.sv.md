---
title: Användning av Smart Markers
type: docs
weight: 40
url: /sv/java/using-smart-markers/
---

## **Introduktion**

{{% alert color="primary" %}}

**Smart markörer** används för att låta Aspose.Cells veta vilken information som ska placeras i en Microsoft Excel [designer spreadsheet](/cells/sv/java/what-is-a-designer-spreadsheet/). Smart markers gör dig möjligt att skapa mallar som endast innehåller relevant information och formatering.

{{% /alert %}}

## **Designer Spreadsheet & Smart Markers**

Designer spreadsheets är standard Excel-filer som innehåller visuell formatering, formler och smart markers. De kan innehålla smart markers som refererar till en eller flera datakällor, såsom information från ett projekt och information för relaterade kontakter. Smart markers är skrivna i cellerna där du vill ha information.

Alla smart markers börjar med &=. Ett exempel på en datamarkör är &=Party.FullName. Om datamarkören resulterar i mer än en post, till exempel en komplett rad, flyttas de följande raderna ned automatiskt för att göra plats för den nya informationen. Därmed kan delsummer och totaler placeras på raden omedelbart efter datamarkören för att göra beräkningar baserade på infogad data. För att göra beräkningar på de infogade raderna, använd [dynamiska formler](/cells/sv/java/using-smart-markers/#dynamic-formulas).

Smart markers består av **datakälla** och **fältnamn** för de flesta uppgifter. Speciell information kan också skickas med variabler och variabelmatriser. Variabler fyller alltid bara en cell medan variabelmatriser kan fylla flera. Använd endast en datamarkör per cell. Oanvända smart markers tas bort.

En smart marker kan också innehålla parametrar. Parametrar gör att du kan ändra hur informationen är utformad. De läggs till i slutet av smart markern inom parentes som en kommaseparerad lista.

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
- *ascending:n eller descending:n - Sortera data i smarta markörer. Om n är 1, är kolumnen den första nyckeln för sorteraren. Data sorteras efter bearbetning av datakällan. Till exempel: &=Tabell1.Fält3(ascending:1).
- **horisontell** - Skriv data från vänster till höger i stället för uppifrån och ner.
- **numerisk** - Konvertera text till nummer om möjligt.
- **shift** - Flytta nedåt eller åt höger, skapa extra rader eller kolumner för att passa data. Shift-parametern fungerar på samma sätt som i Microsoft Excel. Till exempel, när du väljer ett cellintervall, högerklickar och väljer **Infoga** och specificerar **flytta celler nedåt**, **flytta celler åt höger** och andra alternativ. Kort sagt, fyller shift-parametern samma funktion för vertikala/normala (uppifrån och ner) eller horisontella (från vänster till höger) smarta markörer.
- **bean** - Indikerar att datakällan är en enkel POJO. Endast stöds i Java API.

Parametrarna noadd och skip kan kombineras för att infoga data på växelvis rader. Eftersom mallen bearbetas nerifrån och upp bör du lägga till noadd på första raden för att undvika att extra rader infogas före den alternativa raden.

Om du har flera parametrar, separera dem med ett kommatecken, men inget utrymme: parameterA, parameterB, parameterC

Följande skärmbilder visar hur du infogar data på varannan rad.

![todo:image_alt_text](using-smart-markers_1.png)

**blir...**

![todo:image_alt_text](using-smart-markers_2.png)

### **Dynamiska formler**

Dynamiska formler gör det möjligt att infoga Excel-formler i celler även när formeln refererar till rader som kommer att infogas under exportprocessen. Dynamiska formler kan upprepas för varje infogad rad eller använda endast den cell där datamarkören placeras.

Dynamiska formler möjliggör följande ytterligare alternativ:

- r - Nuvarande radnummer.
- 2, -1 - Förskjutning till aktuellt radnummer.

Följande illustrerar en upprepande dynamisk formel och den resulterande Excel-arket.

![todo:image_alt_text](using-smart-markers_3.png)

**blir...**

![todo:image_alt_text](using-smart-markers_4.png)

Cell C1 innehåller formeln =A1*B1, C2 innehåller = A2*B2 och C3 = A3*B3.

Det är mycket enkelt att bearbeta smarta markörer. Följande exempelkod visar hur du använder dynamiska formler i Smart Markers. Vi laddar [mallfilen](templateDynamicFormulas.xlsx) och skapar testdata, bearbetar markörerna för att fylla i data i cellerna mot markören. 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **Användning av variabla Arrayer**

Följande exempelkod visar hur du använder variabla arrayer i Smart Markers. Vi placerar en variabel arraymarkör i cell A1 i den första kalkylbladet i arbetsboken dynamiskt som innehåller en sträng med värden som vi ställer in för markören, bearbetar markörerna för att fylla i data i cellerna mot markören. Slutligen sparar vi Excel-filen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **Gruppering av data**

I vissa Excel-rapporter kan du behöva bryta upp datan i grupper för att göra det lättare att läsa och analysera. Ett av de primära syftena med att bryta upp data i grupper är att köra beräkningar (utföra sammanfattande operationer) på varje grupp av poster.

Aspose.Cells smarta markörer gör det möjligt för dig att gruppera data efter inställda fält och placera sammanfattande rader mellan datasatser eller datagrupper. Till exempel, om du grupperar data efter Customers.CustomerID, kan du lägga till en sammanfattande post varje gång gruppen ändras.

### **Parametrar**

Följande är några smarta markörsparametrar som används för att gruppera data.

#### **group:normal/merge/repeat**

Vi stödjer tre typer av grupper som du kan välja mellan.

- **normal** - Gruppera efter fält(s) värde upprepas inte för de motsvarande posterna i kolumnen; istället skrivs de ut en gång per datagrupp.
- **merge** - Samma beteende som för normalparametern, förutom att den slår samman cellerna i grupperingsfält(en) för varje gruppsats.
- **repeat** - Gruppera efter fält(s) värde upprepas för de motsvarande posterna.

Till exempel: &=Customers.CustomerID(group:merge)

#### **skip**

Hoppa över ett specifikt antal rader efter varje grupp.

Till exempel &=Employees.EmployeeID(group:normal,skip:1)

#### **subtotalN**

Utför en sammanfattande operation för ett specificerat fältdata relaterat till ett grupperingsfält. N står för nummer mellan 1 och 11 som anger den funktion som används vid beräkning av delsummor inom en lista över data. (1=MEDDELVÄRDE, 2=RÄKNA, 3=RÄKNAA, 4=MAX, 5=MIN,...9=SUMMA osv.) Se delsummareferensen i Microsoft Excels hjälp för ytterligare detaljer.

Formatet anges faktiskt som:
delsummaN:Ref där Ref avser grupperingskolumnen.

Till exempel,

- &=Products.Units(delsumma9:Products.ProductID) anger sammanfattningsfunktion för fältet **Units** med avseende på fältet **ProductID** i tabellen **Products**.
- &=Tabx.Col3(delsumma9:Tabx.Col1) anger sammanfattningsfunktion för fältet **Col3** grupperat efter **Col1** i tabellen **Tabx**.
- &=Table1.ColumnD(delsumma9:Table1.ColumnA&Table1.ColumnB) anger sammanfattningsfunktion för fältet **ColumnD** grupperat efter **ColumnA** och **ColumnB** i tabellen **Table1**.

## **Användning av inbäddade objekt**

Aspose.Cells stöder inbäddade objekt i smarta markörer, de inbäddade objekten bör vara enkla.

Vi använder en enkel mallfil. Se kalkylbladet som innehåller några inbäddade smarta markörer.

**Första kalkylbladet i designmallen visar inbäddade smarta markörer.**

![todo:image_alt_text](using-smart-markers_5.png)

Exemplet nedan visar hur detta fungerar. Att köra koden nedan resulterar i utdata nedan.

**Första kalkylbladet i utdatafilen visar den resulterande datan.**

![todo:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **Användning av generisk lista som inbäddat objekt**

Aspose.Cells stödjer nu även användning av en generisk lista som ett inbäddat objekt. Var vänlig kontrollera skärmbilden av den genererade excel-filen med följande kod. Som du kan se i skärmbilden innehåller en Lärar-objekt flera inbäddade elevobjekt.

![todo:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **Användning av HTML-egenskapen hos Smart Markers**

The following sample code explains the use of the HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML \<b> tag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **Få meddelanden när data sammanfogas med smarta markörer**

Ibland kan det vara nödvändigt att få meddelanden om cellreferensen eller den specifika Smart Markern som behandlas före slutförandet. Detta kan uppnås med hjälp av [**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)-egenskapen och [**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

För exempelkod och detaljerad förklaring, se denna artikel.

- [Få meddelanden när data sammanfogas med smarta markörer](/cells/sv/java/getting-notifications-while-merging-data-with-smart-markers/)
{{< app/cells/assistant language="java" >}}
