---
title: Arbete med GridWeb
type: docs
weight: 20
url: /sv/java/working-with-gridweb/
---

## **Öppna en Microsoft Excel-fil**

Aspose.Cells.GridWeb-kontrollen kan öppna och ladda Microsoft Excel-filer - komplett med data, formatering, diagram, bilder etc. Detta ämne förklarar hur.

För att öppna en Excel-fil med hjälp av GridWeb-kontrollen:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på en webbformulär eller sida.
1. Importera Excel-filen genom att ange filens sökväg.
1. Kör programmet eller öppna sidan.

För att ladda innehållet från en Excel-fil till Aspose.Cells.GridWeb-kontrollen måste du anropa metoden importExcelFile för att ange sökvägen till Excel-filen. Därefter kommer GridWeb-kontrollen automatiskt hitta filen från den angivna sökvägen och visa dess innehåll i den. Ett kodutklipp som laddar innehållet från en Excel-fil ges nedan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

Det ovannämnda kodutklippet kan användas på vilket sätt du vill. Till exempel kan du lägga till denna kod för att automatiskt ladda in en Excel-fil när ett webbformulär laddas. 

**En Excel-fil är inladdad i GridWeb**

![todo:image_alt_text](working-with-gridweb_1.png)

## **Spara en Microsoft Excel-fil**

Det är möjligt att skapa nya eller manipulera befintliga Microsoft Excel-filer på webbplatser i GUI-läge med hjälp av Aspose.Cells.GridWeb-kontrollen. Filer kan sedan sparas som Excel-filer. Aspose.Cells.GridWeb fungerar effektivt som en online kalkylbladsredigerare. Detta ämne beskriver hur man sparar ruts innehåll som Excel-filer.

### **Spara som en fil**

För att spara innehållet i Aspose.Cells.GridWeb-kontrollen som en Excel-fil:

1. Lägg till Aspose.Cells.GridWeb-kontrollen på en webbformulär eller sida.
1. Spara ditt arbete som en Excel-fil på en angiven sökväg.
1. Kör programmet eller öppna sidan.

Exemplet nedan illustrerar hur du sparar innehållet i GridWeb som en Excel-fil.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

Det ovannämnda kodutklippet kan användas på flera sätt. Ett vanligt sätt är att lägga till en knapp som sparar ruts innehåll som en Excel-fil när den klickas. Aspose.Cells.GridWeb erbjuder en enklare metod för uppgiften. Aspose.Cells.GridWeb har en händelse som kallas SaveCommand. Det ovannämnda kodutklippet kan läggas till i händelseshanteraren för SaveCommand-händelsen, vilket gör att användare kan spara sitt arbete genom att klicka på Aspose.Cells.GridWebs inbyggda **Spara**-knapp.

## **Storleksjustering av Aspose.Cells.GridWeb och dess huvudmeny**

Denna artikel förklarar hur man ändrar storleken på GridWeb under körning med hjälp av Aspose.Cells.GridWeb API. Den förklarar också hur man ändrar storleken på huvudmenyerna för Aspose.Cells.GridWeb-kontrollen för att göra deras data lättare att läsa.

### **Ändra bredd och höjd på Aspose.Cells.GridWeb**

Ändra bredden och höjden på Aspose.Cells.GridWeb-kontrollen är en enkel men viktig funktion. Aspose.Cells.GridWeb-kontrollen representeras av GridWeb-klassen i API:et. För att ändra bredd och höjd på GridWeb-kontrollen, använd dess bredd- och höjdegenskaper.

{{% alert color="primary" %}}

Kontrollens bredd och höjd kan definieras i pixlar eller punkter.

{{% /alert %}}

Utmatningen av kodsnutten som följer visas nedan.

Ändrad bredd och höjd på GridWeb-kontrollen

![todo:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **Ändra bredd och höjd på sidhuvuden**

Aspose.Cells.GridWeb-kontrollen innehåller två sidhuvuden enligt följande:

- Övre sidhuvud, detta sidhuvud representerar kolumnerna som A, B, C, D osv.
- Vänster sidhuvud, detta sidhuvud representerar raderna som 1, 2, 3, 4 osv.

Båda dessa sidhuvuden visas nedan.

Sidhuvuden

![todo:image_alt_text](working-with-gridweb_3.png)

Ändra höjden på det övre sidhuvudet och bredden på det vänstra sidhuvudet med hjälp av GridWeb-kontrollens HeaderBarHeight- respektive HeaderBarWidth-egenskaper. Figuren nedan visar utmatningen av kodexemplet som följer.

Ändrad sidhuvudsbredd och höjd

![todo:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Arbeta med Aspose.Cells.GridWeb-händelser**

Alla utvecklare måste vara förtrogna med händelser och deras syfte. Händelser används för att skicka meddelanden om förändringar som kan inträffa i en kontroll eller klass. Aspose.Cells.GridWeb har flera händelser som kan användas för att utföra specifika uppgifter när vissa förändringar inträffar i kontrollen.

Det här ämnet ger en introduktion till alla händelser som stöds av Aspose.Cells.GridWeb-kontrollen tillsammans med några detaljer om hur man hanterar dessa händelser.

### **Introduktion till rutnätshändelser**

Aspose.Cells.GridWeb-kontrollen stöder flera händelser som ger mer kontroll för att utföra operationer när specifika händelser utlöses i kontrollen. En komplett lista över de händelser som stöds av Aspose.Cells.GridWeb-kontrollen finns nedan.

|**Händelser**|**Beskrivning**|
| :- | :- |
|CellCommand|Uppstår när kommandolänken för en cell klickas på. När detta händelse utlöses, tillhandahåller dess parameter e.Argument kommandots namn.
|CellDoubleClick|Uppstår när cellen dubbelklickas på.
|ColumnDeleted|Uppstår när en användare tar bort en kolumn från ett arbetsblad med hjälp av den klientbaserade menyn.
|ColumnDeleting|Uppstår när en användare försöker ta bort en kolumn från ett arbetsblad med hjälp av den klientbaserade menyn.
|ColumnDoubleClick|Uppstår när kolumnrubriken dubbelklickas på.
|ColumnInserted|Uppstår när en användare lägger till en kolumn i ett arbetsblad med hjälp av den klientbaserade menyn.
|CustomCommand|Uppstår när en användare klickar på en anpassad kommandoknapp.
|LoadCustomData|Uppstår när kontrollens EnableSession-egenskap är inställd på falskt och behöver ladda arbetsbladsdata. Du kan hantera denna händelse i sessionlöst läge för att ladda arbetsbladsdata från en fil eller en databas.
|PageIndexChanged|Uppstår när kontrollens sidindex ändras.
|RowDeleted|Uppstår när en användare tar bort en rad från arbetsbladet med hjälp av den klientbaserade menyn.
|RowDeleting|Uppstår när en användare försöker ta bort en rad från ett arbetsblad med hjälp av den klientbaserade menyn.
|RowDoubleClick|Inträffar när radrubriken dubbelklickas.|
|RowInserted|Inträffar när en användare lägger till en rad i arbetsbladet med hjälp av klientens meny.|
|SaveCommand|Inträffar när knappen **Spara** klickas på.|
|SheetTabClick|Inträffar när en flik i kalkylarket klickas på.|
|SubmitCommand|Inträffar när knappen **Skicka** klickas på.|
|UndoCommand|Inträffar när knappen **Ångra** klickas på.|
|AjaxCallFinished|Triggers när AJAX-uppdateringen av kontrollen är klar. (EnableAJAX ska vara inställt på true).|
|CellModifiedOnAjax|Triggers när cellen ändras i AJAX-anropet.|
|AfterColumnFilter|Triggers när filtret tillämpas på en kolumn.|

### **Hantering av rutnätshändelser**

För att utföra en specifik operation vid utlösning av en specifik händelse måste vi skapa en händelsehanterare. En händelsehanterare utför uppgiften när en viss händelse inträffar. Exemplet nedan visar hur man hanterar en enkel rutnäthändelse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **Arbeta med dubbelklickshändelser**

Aspose.Cells.GridWeb innehåller tre typer av dubbelklickshändelser:

- CellDoubleClick, aktiveras när en cell dubbelklickas.
- ColumnDoubleClick, aktiveras när en kolumnrubrik dubbelklickas.
- RowDoubleClick, aktiveras när en radrubrik dubbelklickas.

Detta ämne diskuterar hur man aktiverar dubbelklickshändelser i Aspose.Cells.GridWeb. Det diskuterar också skapandet av händelsehanterare för dessa händelser.

### **Aktivera dubbelklickshändelser**

Alla typer av dubbelklickshändelser kan aktiveras på klientens sida genom att ställa in Egenskapen EnableDoubleClickEvent för GridWeb-kontrollen till true.

{{% alert color="primary" %}}

Som standard är Egenskapen EnableDoubleClickEvent inställd på false. Detta innebär att dubbelklickshändelser inte är aktiverade som standard. För att implementera sådana händelser, aktivera funktionen först.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

När dubbelklickshändelser är aktiverade, är det möjligt att skapa händelsehanterare för vilka dubbelklickshändelser som helst. Dessa händelsehanterare utför specifika uppgifter när en given dubbelklickshändelse inträffar.

### **Hantering av dubbelklickshändelser**

#### **Dubbelklick på cell**

Händelsehanteraren för CellDoubleClick-händelsen tillhandahåller en argument av typen CellEventArgs, som ger all information om cellen som dubbelklickades på.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **Dubbelklick på kolumnrubrik**

Händelsehanteraren för ColumnDoubleClick-händelsen tillhandahåller ett argument av typen RowColumnEventArgs som ger indexnumret för kolumnen för rubriken som dubbelklickades på och annan information.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **Dubbelklick på radrubrik**

Händelsehanteraren för RowDoubleClick-händelsen tillhandahåller ett argument av typen RowColumnEventArgs som ger indexnumret för raden för rubriken som dubbelklickades på och annan relaterad information.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Inställning av stil eller utseende på Aspose.Cells.GridWeb**

Aspose.Cells.GridWeb har sin egen standardstil men det är möjligt att ändra dess utseende. Aspose.Cells.GridWeb tillhandahåller flera egenskaper för att låta utvecklare ha full kontroll över dess utseende. Detta ämne diskuterar några av dessa egenskaper.

### **Inställning av stil eller utseende på Aspose.Cells.GridWeb**

#### **Förinställda stilar**

För att spara utvecklares ansträngningar erbjuder Aspose.Cells.GridWeb några förinställda stilar. Välj helt enkelt en stil från listan för att tillämpa stilen.

|**Stilar**|**Färgschema**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
När en särskild stil väljs ändrar den hela utseendet av GridWeb-kontrollen. Utvecklare kan välja en förinställd stil att tillämpas vid runtime med hjälp av den flexibla API: en för Aspose.Cells.GridWeb.

GridWeb-kontrollen tillhandahåller egenskapen PresetStyle till vilken utvecklare kan tilldela en önskad förinställd stil.

Resultatet av kodsnutten nedan visas nedan.

**GridWeb-kontroll med stil applicerad på Colorful1**

![todo:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Header Bar Style**

Om du tittar på GridWeb-kontrollen kommer du att märka två headerfält. Ett för kolumner (det vill säga A, B, C, D osv.) och det andra för rader (det vill säga 1, 2, 3, 4 osv.). Aspose.Cells.GridWeb tillåter utvecklare att kontrollera utseendet på dessa headerfält. Utvecklare kan ange stilen på headerfälten vid runtime.

{{% alert color="primary" %}}

GridWeb-kontrollen tillhandahåller egenskapen HeaderBarStyle som tillämpar en stil på båda headerfälten i kontrollen.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Tab Bar Style**

Det är möjligt att ställa in stilen på flikfältet också. Se följande kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **Laddningsstilfil**

För att tillämpa stilkonfigurationer från en befintlig stilfil till GridWeb-kontrollen kan utvecklare ange sökvägen till stilfilen till egenskapen CustomStyleFileName för kontrollen. Men innan detta är det ett måste att ställa in egenskapen PresetStyle för kontrollen till Anpassad. Detta beror på att stilfilen innehåller anpassad stilinformation som redan definierats av en utvecklare.

Se följande bild som visar GridWeb med den anpassade stilen applicerad på den.

![todo:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

VIKTIGT: Att ladda stilfilen i GridWeb-kontrollen påverkar inte cellens formateringsinställningar för kontrollen.

{{% /alert %}}

#### **Exempel på anpassad stilmall**

Här är den anpassade stilmallen följt. Du kan ändra den enligt dina krav.

{{< highlight java >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Skapa kontroll på ett webbformulär**

Den här artikeln kommer att guida dig om hur du skapar ett enkelt webbformulär JSP (Java Server Page) med GridWeb-kontroll på den.

**Steg 1 - Skapa mappstruktur**

Du måste skapa följande mappstruktur i katalogen **webapps** i Tomcat Server

![todo:image_alt_text](working-with-gridweb_7.png)

Detta är mappar och filer du behöver skapa. Vänligen läs kommentarerna och följ dem. Du kan få de senaste arkiven för utgåvor av Aspose.Cells.GridWeb för Java från [den här länken](https://downloads.aspose.com/cells/java).

{{< highlight java >}}

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

Denna avsnitt visar koden för olika filer skapade i ovanstående katalogstruktur. Hämta dessa koder och lägg till dem i dina filer genom att öppna dem i Anteckningar och kopiera/klistra in dem.

**Web.xml**

{{< highlight java >}}

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

{{< highlight java >}}

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

**Steg 3 - Köra din prov JSP-webbsida**

Nu har du gjort allt. Det är dags att köra webbsidan. Starta din Tomcat-server och klistra sedan in följande URL i webbläsaren.

{{< highlight java >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Du kommer att se något liknande följande skärmbild. Grattis, du har lyckats använda GridWeb-kontrollen på din JSP-sida.

![todo:image_alt_text](working-with-gridweb_8.png)

## **Utskrift av GridWeb**

Det finns tillfällen då utvecklare behöver skriva ut innehållet i GridWeb från en webbsida utan att spara en Microsoft Excel-fil. Aspose.Cells.GridWeb-kontrollen stödjer den här funktionen.

### **Utskrift av GridWeb**

För att skriva ut utan att spara en separat fil, anropa GridWeb-klassens print()-metod på klientsidan för att skriva ut rutan. Du kan också välja något lämpligt evenemang.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Eftersom du anropar det från klientsidan måste du först hämta gridwebb-klient-ID. Du kan få klient-ID med hjälp av gridwebb.getClientID()-metoden.

### **Klientsida provkod**

Vänligen se följande länk som anropar gridwebb.print()-metoden från klientsidan.

**HTML**

{{< highlight java >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **Introduktion till olika rutlägeslägen**

Den här artikeln beskriver olika lägen för Aspose.Cells.GridWeb. Dessa lägen är logiskt differentierade på grund av deras olika funktioner och beteenden. Vi har identifierat olika typer av lägen som:

- Redigeringsläge
- Visa läge

Alla dessa lägen har sina egna egenskaper. Utvecklare kan arbeta med Aspose.Cells.GridWeb i vilket läge de än vill enligt sina behov. Vi kommer att titta på varje läge nedan.

### **Redigeringsläge**

Som standard är Aspose.Cells.GridWeb-kontrollen i redigeringsläge. I redigeringsläge kan du fullständigt redigera eller modifiera rutinnehållet med alla funktioner som erbjuds av Aspose.Cells.GridWeb-kontrollen. Dessa funktioner inkluderar:

- Spara rutinnehållet i Microsoft Excel-filer.
- Skicka data till en server.
- Beräkna formler.
- Ångra eller kassera tidigare åtgärder.
- Hantera rader och kolumner.
- Klippa, kopiera eller klistra in data.
- Formatera celler etc.

**GridWeb-kontroll i redigeringsläge**

![todo:image_alt_text](working-with-gridweb_9.png)

Utvecklare kan också växla till redigeringsläge programmässigt genom att ställa in Egenskapen EditMode för GridWeb-kontrollen till true.

### **Kodexempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **Visningsläge**

När GridWeb-kontrollen är i visningsläge kan användare inte redigera eller modifiera rutinnehåll, vilket innebär att användare endast kan se rutinnehåll. Därför kallas detta läge för visningsläge. I visningsläge är några knappar (Skicka, Spara och Ångra) dolda och menyn som visas vid högerklick innehåller endast alternativen Kopiera och Hitta.

**GridWeb-kontroll i visningsläge** 

![todo:image_alt_text](working-with-gridweb_10.png)

Om utvecklare vill att deras användare endast ska kunna se data kan de växla till visningsläge programmässigt genom att ställa in EditMode-egenskapen för GridWeb-kontrollen till falskt

### **Kodexempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Även i visningsläge kan användare ändra höjd och bredd på rader och kolumner.

{{% /alert %}}
