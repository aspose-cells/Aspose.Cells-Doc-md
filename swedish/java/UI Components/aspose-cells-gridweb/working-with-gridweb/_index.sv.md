---
title: Jobbar med GridWeb
type: docs
weight: 20
url: /sv/java/working-with-gridweb/
---
## **Öppna en Microsoft Excel-fil**

Aspose.Cells.GridWeb-kontroll kan öppna och ladda Microsoft Excel-filer - komplett med data, formatering, diagram, bilder etc. Detta ämne förklarar hur.

Så här öppnar du en Excel-fil med GridWeb-kontroll:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ett webbformulär eller en sida.
1. Importera Excel-filen genom att ange sökvägen.
1. Kör programmet eller öppna sidan.

För att ladda innehållet från en Excel-fil till Aspose.Cells. GridWeb-kontroll måste du anropa importExcelFile-metoden för att ange sökvägen till Excel-filen. Därefter kommer GridWeb control automatiskt att hitta filen från den angivna sökvägen och visa dess innehåll i den. Ett kodavsnitt som laddar innehållet i en Excel-fil finns nedan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

Ovanstående kodavsnitt kan användas hur du vill. Till exempel, för att ladda en Excel-fil automatiskt när ett webbformulär laddas, lägg till den här koden i formulärets Page_Load-händelse som du själv har angett.

**En Excel-fil laddas in i GridWeb**

![todo:image_alt_text](working-with-gridweb_1.png)

## **Sparar en Microsoft Excel-fil**

Det är möjligt att skapa nya eller manipulera befintliga Microsoft Excel-filer på webbplatser i GUI-läge med Aspose.Cells.GridWeb-kontroll. Filerna kan sedan sparas i Excel-filer. Aspose.Cells.GridWeb fungerar effektivt som kalkylarksredigerare online. Det här avsnittet beskriver hur du sparar rutnätsinnehåll i Excel-filer.

### **Sparar som en fil**

Så här sparar du innehållet i Aspose.Cells.GridWeb-kontrollen som en Excel-fil:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ett webbformulär eller en sida.
1. Spara ditt arbete som en Excel-fil på en angiven sökväg.
1. Kör programmet eller öppna sidan.

Kodexemplet nedan illustrerar hur man sparar rutnätsinnehåll till en Excel-fil.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

 Ovanstående kodavsnitt kan användas på flera sätt. Ett vanligt sätt är att lägga till en knapp som sparar rutnätsinnehållet i en Excel-fil när du klickar på den. Aspose.Cells.GridWeb erbjuder ett enklare tillvägagångssätt för uppgiften. Aspose.Cells.GridWeb har en händelse som heter SaveCommand. Ovanstående kodavsnitt kan läggas till i SaveCommand-händelsens händelsehanterare, vilket tillåter användare att spara sitt arbete genom att klicka på Aspose.Cells.GridWebs inbyggda**Spara** knapp.

## **Ändra storlek på Aspose.Cells.GridWeb och dess huvudfält**

Den här artikeln förklarar hur man ändrar storlek på GridWeb under körning med hjälp av Aspose.Cells.GridWeb API. Den förklarar också hur man ändrar storlek på rubrikfälten för Aspose.Cells.GridWeb-kontrollen för att göra deras data lättare att läsa.

### **Ändra bredd och höjd på Aspose.Cells.GridWeb**

Ändra bredd och höjd på Aspose.Cells. GridWeb-kontroll är en enkel men viktig funktion. Aspose.Cells.GridWeb-kontrollen representeras av GridWeb-klassen i API. För att ändra storlek på bredden och höjden på GridWeb-kontrollen, använd helt enkelt dess egenskaper för bredd och höjd.

{{% alert color="primary" %}}

Kontrollens bredd och höjd kan definieras i pixlar eller punkter.

{{% /alert %}}

Utdata från kodavsnittet som följer visas nedan.

**Ändrad bredd och höjd på GridWeb-kontrollen**

![todo:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **Ändra bredd och höjd på sidhuvudet**

Aspose.Cells.GridWeb-kontrollen innehåller två huvudfält enligt följande:

- Översta rubrikfältet, detta rubrikfält representerar kolumner som A, B, C, D, etc.
- Vänster rubrikfält, denna rubrikstapel representerar rader som 1, 2, 3, 4, etc.

Båda dessa rubrikfält visas nedan.

**Rubriker**

![todo:image_alt_text](working-with-gridweb_3.png)

Ändra höjden på den översta rubriken och bredden på den vänstra rubriken med hjälp av GridWeb-kontrollens HeaderBarHeight respektive HeaderBarWidth egenskaper. Bilden nedan visar resultatet av kodexemplet som följer.

**Ändrad rubrikstavs bredd och höjd**

![todo:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Arbetar med Aspose.Cells.GridWeb Events**

Alla utvecklare måste vara bekanta med händelser och deras syfte. Händelser används för att skicka meddelanden om ändringar som kan inträffa i en kontroll eller klass. Aspose.Cells.GridWeb har flera händelser som kan användas för att utföra specifika uppgifter när vissa förändringar sker i kontrollen.

Det här avsnittet ger en introduktion till alla händelser som stöds av Aspose.Cells.GridWeb-kontrollen tillsammans med några detaljer om hur man hanterar dessa händelser.

### **Introduktion till Grid Events**

Aspose.Cells.GridWeb-kontroll stöder flera händelser som ger mer kontroll för att utföra operationer när specifika händelser utlöses i kontrollen. En komplett lista över händelser som stöds av Aspose.Cells.GridWeb-kontroll finns nedan.

|**evenemang**|**Beskrivning**|
|:- |:- |
|CellCommand|Uppstår när kommandohyperlänken för en cell klickas. När den här händelsen avfyras ger dess parameter e.Argument kommandots namn.|
|CellDoubleClick|Uppstår när cellen dubbelklickas.|
|Kolumn Raderad|Uppstår när en användare tar bort en kolumn från ett kalkylblad med hjälp av menyn på klientsidan.|
|Kolumn Raderar|Uppstår när en användare försöker ta bort en kolumn från ett kalkylblad med hjälp av klientsidans meny.|
|KolumnDubbelklicka|Uppstår när kolumnrubriken dubbelklickas.|
|KolumnInfogad|Uppstår när en användare infogar en kolumn i ett kalkylblad med hjälp av klientsidans meny.|
|CustomCommand|Uppstår när en användare klickar på en anpassad kommandoknapp.|
|Ladda CustomData|Uppstår när kontrollens EnableSession-egenskap är inställd på false och behöver ladda kalkylbladsdata. Du kan hantera denna händelse i sessionslöst läge för att ladda kalkylbladsdata från en fil eller databas.|
|SidindexÄndrad|Uppstår när kontrollens arksideindex ändras.|
|Radraderad|Uppstår när en användare tar bort en rad från kalkylbladet med hjälp av klientsidans meny.|
|Radrader|Uppstår när en användare försöker ta bort en rad från ett kalkylblad med hjälp av klientsidans meny.|
|RowDoubleClick|Uppstår när radhuvudet dubbelklickas.|
|RowInserted|Uppstår när en användare infogar en rad i kalkylbladet med hjälp av klientsidans meny.|
|SaveCommand| Uppstår när**Spara** knappen klickas.|
|SheetTabClick|Uppstår när en arkflik klickas.|
|SubmitCommand| Uppstår när**Skicka in** knappen klickas.|
|Ångra kommando| Uppstår när**Ångra** knappen klickas.|
|AjaxCallFinished|Avfyras när AJAX-uppdateringen av kontrollen är klar. (EnableAJAX ska ställas in på sant).|
|CellModifiedOnAjax|Avfyras när cellen modifieras i AJAX-anrop.|
|AfterColumnFilter|Avfyras när filtret appliceras på en kolumn.|

### **Hantering av Grid Events**

För att utföra en specifik operation för att utlösa en specifik händelse, måste vi skapa en händelsehanterare. En händelsehanterare utför den önskade uppgiften när en viss händelse utlöses. Exemplet som följer visar hur man hanterar en enkel grid-händelse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **Arbeta med Double Click Events**

Aspose.Cells.GridWeb innehåller tre typer av dubbelklickshändelser:

- CellDoubleClick, aktiveras när en cell dubbelklickas.
- ColumnDoubleClick, aktiveras när en kolumnrubrik dubbelklickas.
- RowDoubleClick, aktiveras när en radrubrik dubbelklickas.

Det här ämnet diskuterar hur du aktiverar dubbelklickshändelser i Aspose.Cells.GridWeb. Den diskuterar också att skapa händelsehanterare för dessa händelser.

### **Aktiverar dubbelklickshändelser**

Alla typer av dubbelklickshändelser kan aktiveras på klientsidan genom att ställa in GridWeb-kontrollens EnableDoubleClickEvent-egenskap till true.

{{% alert color="primary" %}}

Som standard är egenskapen EnableDoubleClickEvent inställd på false. Detta betyder att dubbelklickshändelser inte är aktiverade som standard. För att implementera sådana händelser, aktivera först funktionen.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

När dubbelklickshändelser är aktiverade är det möjligt att skapa händelsehanterare för alla dubbelklickshändelser. Dessa händelsehanterare utför specifika uppgifter när en given dubbelklickshändelse utlöses.

### **Hantera dubbelklickshändelser**

#### **Dubbelklicka Cell**

Händelsehanteraren för händelsen CellDoubleClick tillhandahåller ett argument av typen CellEventArgs, som tillhandahåller fullständig information om cellen som dubbelklickas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **Dubbelklicka på kolumnrubrik**

Händelsehanteraren för ColumnDoubleClick-händelsen tillhandahåller ett argument av typen RowColumnEventArgs som ger indexnumret för kolumnen för rubriken som dubbelklickades och annan information.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **Dubbelklicka på radrubrik**

Händelsehanteraren för händelsen RowDoubleClick tillhandahåller ett argument av typen RowColumnEventArgs som ger indexnumret för raden för rubriken som dubbelklickades och annan relaterad information.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Inställning av stil eller utseende för Aspose.Cells.GridWeb**

Aspose.Cells.GridWeb har sitt eget standardutseende och känsla men det är möjligt att ändra dess utseende. Aspose.Cells.GridWeb tillhandahåller flera egenskaper för att låta utvecklare helt kontrollera dess utseende. Det här ämnet diskuterar några av dessa egenskaper.

### **Inställning av stil eller utseende för Aspose.Cells.GridWeb**

#### **Förinställda stilar**

För att spara på utvecklarnas ansträngningar erbjuder Aspose.Cells.GridWeb några förinställda stilar. Välj helt enkelt en stil från listan för att tillämpa stilen.

|**Stilar**|**Färgschema**|
|:- |:- |
|Standard|Silver|
|Färgglad 1|Reste sig|
|Färgglada 2|Blå|
|Professionell 1|Cyan|
|Professionell 2|Cyan igen|
|Traditionell 1|Mörk|
|Traditionell 2|grå|
|Beställnings|Anpassat|
När en viss stil väljs ändrar den hela utseendet på GridWeb-kontrollen. Utvecklare kan välja en förinställd stil som ska tillämpas under körning med den flexibla API eller Aspose.Cells.GridWeb.

GridWeb-kontrollen tillhandahåller PresetStyle-egenskapen som utvecklare kan tilldela vilken förinställd stil som helst.

Utdata från nedanstående kodavsnitt visas nedan.

**GridWeb-kontroll med Colorful1-stilen applicerad på den**

![todo:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Header Bar Style**

Om du tittar på GridWeb-kontrollen kommer du att märka två rubrikfält. En för kolumner (det vill säga A, B, C, D, etc.) och en annan för rader (det vill säga 1, 2, 3, 4, etc.). Aspose.Cells.GridWeb tillåter utvecklare att kontrollera utseendet på dessa sidhuvuden. Utvecklare kan ställa in stilen på sidhuvuden under körning.

{{% alert color="primary" %}}

GridWeb-kontrollen tillhandahåller egenskapen HeaderBarStyle som tillämpar en stil på kontrollens båda rubrikfält.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Tabbar stil**

Det är möjligt att ställa in stilen på flikfältet också. Se följande kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **Laddar stilfil**

För att tillämpa stilinställningar från en befintlig stilfil på GridWeb-kontroll kan utvecklare ställa in sökvägen för stilfilen till CustomStyleFileName-egenskapen för kontrollen. Men innan du gör det måste du ställa in PresetStyle-egenskapen för kontrollen till Custom. Det beror på att stilfilen innehåller anpassad stilinformation som redan är definierad av en utvecklare.

Se följande bild som visar GridWeb med den anpassade stilen tillämpad på den.

![todo:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

VIKTIGT: Att ladda stilfilen till GridWeb-kontrollen påverkar inte formateringsinställningarna för kontrollens celler.

{{% /alert %}}

#### **Exempel på anpassad stilmall**

Här är ett exempel på mallen för anpassad stil. Du kan ändra det enligt dina krav.

{{< highlight "java" >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Skapa kontroll på ett webbformulär**

Den här artikeln kommer att guida dig om hur du skapar ett enkelt webbformulär JSP (Java Server Page) med GridWeb-kontroll på den.

**Steg 1 - Skapa katalogstruktur**

 Du måste skapa följande katalogstruktur i**webbappar**katalog för Tomcat Server

![todo:image_alt_text](working-with-gridweb_7.png)

 Det här är katalogerna och filerna du behöver skapa. Läs kommentarerna och följ dem. Du kan hämta de senaste Aspose.Cells.GridWeb for Java utgivningsarkiven från[den här länken](https://downloads.aspose.com/cells/java).

{{< highlight "java" >}}

 SamplePageGridWebJava

SamplePageGridWebJava\grid

//Get acwclient directory from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\acwclient

SamplePageGridWebJava\WEB-INF

SamplePageGridWebJava\WEB-INF\lib

//Get aspose-gridweb-x.x.x.jar file from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\WEB-INF\aspose-gridweb-x.x.x.jar

SamplePageGridWebJava\WEB-INF\web.xml

SamplePageGridWebJava\head.jsp

//Create this excel file using Microsoft Excel or you can use any excel file and rename it SampleExcel.xlsx

SamplePageGridWebJava\SampleExcel.xlsx

SamplePageGridWebJava\SamplePage.jsp

{{< /highlight >}}

**Steg 2 - Lägga till koder i skapade filer**

Det här avsnittet visar koden för olika filer som skapats i ovanstående katalogstruktur. Vänligen skaffa dessa koder och lägg till dem i dina filer genom att öppna dem i Anteckningar och kopiera/klistra in det.

**Web.xml**

{{< highlight "java" >}}

 <?xml version="1.0" encoding="UTF-8"?>

<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" id="WebApp_ID" version="2.5">

  <display-name>testGridWeb</display-name>

  <welcome-file-list>

    <welcome-file>SamplePage.jsp</welcome-file>

  </welcome-file-list>

  <servlet>

    <display-name>GridWebServlet</display-name>

    <servlet-name>GridWebServlet</servlet-name>

    <servlet-class>com.aspose.gridweb.GridWebServlet</servlet-class>

  </servlet>

  <servlet-mapping>

    <servlet-name>GridWebServlet</servlet-name>

    <url-pattern>/GridWebServlet</url-pattern>

  </servlet-mapping>

</web-app>

{{< /highlight >}}

**head.jsp**

{{< highlight "java" >}}

 <%

String path = request.getContextPath();

String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

%>

<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9"/>

<base href="<%=basePath%>">

<script type="text/javascript" language="javascript"

	src="grid/acw_client/acwmain.js"></script>

<script type="text/javascript" language="javascript"

	src="grid/acw_client/lang_en.js"></script>

<link href="grid/acw_client/menu.css" rel="stylesheet" type="text/css" />

<style>

span.acwxc {

	overflow: hidden;

	border: none;

	display: block;

	white-space: pre;

}

</style>

<style>

span.rotation90 {

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(-90deg);

	-moz-transform: rotate(-90deg);

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3 );

	display: block

}

</style>

<style>

span.rotation-90 {

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1 );

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(90deg);

	-moz-transform: rotate(90deg);

	display: block

}

</style>

<style>

span.wrap {

	white-space: pre-wrap;

	white-space: -moz-pre-wrap;

	white-space: -pre-wrap;

	white-space: -o-pre-wrap;

	word-wrap: break-word;

	-ms-word-break: break-all;

}

</style>

{{< /highlight >}}

**SamplePage.jsp**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-SamplePage-SamplePage.jsp" >}}

**Steg 3 - Köra din exempel-JSP-webbsida**

Nu har du gjort allt. Det är dags att köra webbsidan. Starta din Tomcat-server och klistra sedan in följande URL i webbläsaren.

{{< highlight "java" >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Du kommer att se något i stil med följande skärmdump. Grattis, du har framgångsrikt använt GridWeb-kontrollen på din JSP-sida.

![todo:image_alt_text](working-with-gridweb_8.png)

## **Utskrift GridWeb**

Det finns tillfällen då utvecklare behöver skriva ut GridWeb-innehållet från en webbsida utan att spara en Microsoft Excel-fil. Aspose.Cells.GridWeb-kontrollen stöder denna funktion.

### **Utskrift GridWeb**

För att skriva ut utan att spara en separat fil, anropa GridWeb-klassens print()-metod på klientsidan för att skriva ut rutnätet. Du kan också välja något lämpligt evenemang.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Eftersom du anropar det från klientsidan, så måste du först skaffa gridweb klient-id. Du kan få klient-id:t med gridweb.getClientID()-metoden.

### **Exempelkod på klientsidan**

Se följande länk som anropar gridweb.print()-metoden från klientsidan.

**HTML**

{{< highlight "java" >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **Introduktion till olika rutnätslägen**

Den här artikeln beskriver Aspose.Cells.GridWebs olika lägen. Dessa lägen är logiskt differentierade på grund av deras olika egenskaper och beteenden. Vi har identifierat olika typer av lägen som:

- Redigeringsläge
- Visningsläge

Alla dessa lägen har sina egna egenskaper. Utvecklare kan arbeta med Aspose.Cells.GridWeb i alla lägen enligt deras krav. Vi kommer att titta på varje läge nedan.

### **Redigeringsläge**

Som standard är Aspose.Cells.GridWeb-kontrollen i redigeringsläge. I redigeringsläge kan du helt redigera eller modifiera rutnätets innehåll med alla funktioner som erbjuds av Aspose.Cells.GridWeb-kontrollen. Dessa funktioner inkluderar:

- Spara rutnätsinnehållet till Microsoft Excel-filer.
- Skicka data till en server.
- Beräkna formler.
- Ångra eller kassera tidigare åtgärder.
- Hantera rader och kolumner.
- Klipp ut, kopiera eller klistra in data.
- Formatera celler etc.

**GridWeb-kontroll i redigeringsläge**

![todo:image_alt_text](working-with-gridweb_9.png)

Utvecklare kan också byta till redigeringsläge programmatiskt genom att ställa in egenskapen EditMode för GridWeb-kontrollen till true.

### **Kodexempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **Visningsläge**

När GridWeb-kontrollen är i visningsläge kan användare inte redigera eller ändra rutnätsinnehåll, vilket innebär att användare bara kan se rutnätsinnehåll. Det är därför detta läge kallas View mode. I visningsläge, några knappar (**Skicka in**, **Spara** och**Ångra** ) är dolda och menyn som visas när du högerklickar innehåller bara**Kopiera** och**Hitta** alternativ.

**GridWeb-kontroll i View Mode** 

![todo:image_alt_text](working-with-gridweb_10.png)

 Om utvecklare vill att deras användare endast ska se data kan de byta till visningsläge programmatiskt genom att ställa in GridWeb-kontrollens EditMode-egenskap till**falsk**.

### **Kodexempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Även i vyläget kan användare ändra höjden och bredden på rader och kolumner.

{{% /alert %}}
