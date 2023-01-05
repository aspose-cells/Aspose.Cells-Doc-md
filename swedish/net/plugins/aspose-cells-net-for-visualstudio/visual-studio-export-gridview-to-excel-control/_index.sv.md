---
title: Visual Studio Exportera GridView till Excel-kontroll
type: docs
weight: 10
url: /sv/net/visual-studio-export-gridview-to-excel-control/
---
## **Introduktion**
 Exportera GridView till Excel Control är en ASP.NET-serverkontroll som tillåter export av innehåll från GridView till Microsoft Excel- eller OpenOffice-kalkylblad med[Aspose.Cells](https://products.aspose.com/cells/net/) . Det tillägger**exportera till Excel** knappen ovanpå GridView-kontrollen. Genom att klicka på knappen exporteras innehållet i GridView-kontrollen dynamiskt till ett Microsoft Excel- eller OpenOffice-kalkylblad och laddar sedan automatiskt ned den exporterade filen till den diskplats som användaren valt på bara några sekunder.
### **Modulfunktioner**
Denna första version av kontrollen har följande funktioner:

- Få en offlinekopia av ditt favoritinnehåll i GridView online för redigering, delning och utskrift.
- Ärvt från standard ASP.NET GridView-kontroll och har därför alla dess funktioner och egenskaper.
- Exportera GridView till Xlsx, Xlsb, Xls, Txt, Csv, Ods.
- Fungerar med alla .NET-versioner från .NET 2.0.
- Möjlighet att anpassa/lokalisera Exportknapptext.
- Tillämpa utseendet och känslan av ditt eget tema på knappen Exportera med css.
- Möjlighet att lägga till anpassad rubrik ovanpå det exporterade dokumentet
- Möjlighet att spara varje exporterat dokument på servern på konfigurerbar diskväg
- Möjlighet att exportera aktuell sida eller alla sidor när personsökning är aktiverad

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_1.png)

Denna kontroll låter dig exportera GridView i följande olika filformat.

1. Exportera GridView till Excel
1. Exportera GridView till Xlsx
1. Exportera GridView till Xlsb
1. Exportera GridView till Xls
1. Exportera GridView till Txt
1. Exportera GridView till Csv
1. Exportera GridView till Ods
## **Systemkrav och plattformar som stöds**
### **Systemkrav**
Export GridView till Excel Control för Visual Studio kan användas på alla system som har IIS och .NET framework 2.0 eller senare installerat.
### **Plattformar som stöds**
Export GridView till Excel Control för Visual Studio stöds av alla versioner av ASP.NET som körs på .NET framework 2.0 eller senare. Du kan använda någon av följande Visual Studio-versioner för att använda denna kontroll i dina ASP.NET-applikationer

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013
## **Laddar ner**
Du kan ladda ner Export GridView To Excel Control från en av följande platser

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Export_GridView_Excel)
## **Installerar**
Det är väldigt enkelt och lätt att installera Export GridView To Excel Control, följ dessa enkla steg
### **För Visual Studio 2010, 2012 och 2013**
1. Extrahera den nedladdade zip-filen
1. Dubbelklicka på VSIX-filen Aspose.Excel.GridViewExport.vsix
1. En dialogruta visas som visar de tillgängliga och stödda Visual Studio-versionerna installerade på din maskin
1. Välj de du vill lägga till Export GridView To Excel Control till.
1. Klicka på Installera

Du kommer att få en framgångsdialog när installationen är klar.

**Notera:** Se till att starta om Visual Studio för att ändringarna ska träda i kraft.
### **För Visual Studio 2005, 2008 och Express-utgåvor**
Följ dessa steg för att integrera Export GridView till Excel Control i Visual studio för enkel dra och släpp precis som andra ASP.NET kontroller

1. Extrahera den nedladdade zip-filen
1. Se till att köra Visual Studio som administratör

På Verktyg-menyn klickar du på Välj Verktygslåda.

1.  Klicka på Bläddra.
 Dialogrutan Öppna visas.
1. Bläddra till den extraherade mappen och välj Aspose.Excel.GridViewExport.dll
1. Klicka på OK.

När du öppnar en aspx- eller ascx-kontroll i verktygslådan till vänster ser du ExportGridViewToWord under fliken Allmänt

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_2.png)
## **Använder sig av**
När den väl har installerats är det mycket enkelt att börja använda den här kontrollen i dina ASP.NET-applikationer

|**För .NET ram 4.0 och högre** |**För .NET ramverk 2.0 och högre** |** |
|:- |:- |:- |
| För applikationer som körs i .NET ramverk 4.0 och senare i Visual Studio 2010 och senare, bör du se**ExportGridViewToExcel**styra in**Aspose** Fliken i verktygsfältet som visas nedan. Du kan helt enkelt dra och släppa den här kontrollen till din ASP.NET-sida, kontroll eller mastersida precis som alla andra .NET-kontroller och börja.|För att du ska kunna använda den här kontrollen i applikationer som körs i .NET 2.0 i valfri Visual Studio-version, se till att du har lagt till ExportGridViewToExcel i din verktygslåda enligt instruktionerna på ﻿[8.1.2.1 Ladda ner och installera]() under rubriken**För Visual Studio 2005, 2008 och Express-utgåvor** <br> Du borde se**ExportGridViewToExcel**styra in**Allmän** Fliken i verktygsfältet som visas nedan. Du kan helt enkelt dra och släppa den här kontrollen till din ASP.NET-sida, kontroll eller mastersida precis som alla andra .NET-kontroller och börja.||
|<p>![todo:image_alt_text](picture2.png)</p><p></p>|<p>![todo:image_alt_text](picture3.png)</p><p></p>||
### **Manuell lägga till ExportGridViewToExcel-kontroll**
Om du har några problem med att använda ovanstående metoder som använder Visual Studio Toolbox, kan du manuellt lägga till den här kontrollen till din ASP.NET-applikation som körs på valfritt .NET-ramverk större än 2.0

1. Om du använder Visual Studio se till att köra det som administratör
1.  Lägg till referens till**Aspose.Excel.GridViewExport.dll**tillgängligt i ett extraherat nedladdningspaket i ditt ASP.NET-projekt eller webbapplikation. Se till att din webbapplikation/Visual Studio har full åtkomst till den här mappen annars kan du få Access is denied undantag.
1.  Lägg till den här raden överst på sidan, kontroll eller MasterPage

{{< highlight "java" >}}

 <%@ Register assembly="Aspose.Excel.GridViewExport" namespace="Aspose.Excel.GridViewExport" tagprefix="aspose" %>

{{< /highlight >}}

1.  Lägg till följande till en plats på din ASP.NET-sida, kontroll eller mastersida där du vill att kontrollen ska läggas till

{{< highlight "java" >}}

 <aspose:ExportGridViewToExcel ID="ExportGridViewToExcel1" runat="server"></aspose:ExportGridViewToExcel>

{{< /highlight >}}
### **Vanliga frågor**
Vanliga frågor och problem du kan möta när du använder denna kontroll

|**#** |**Fråga** |**Svar** |
|:- |:- |:- |
|1 | Jag kan inte se ExportGridViewToExcel-kontrollen i Toolbox|<p>**Visual Studio 2010 och senare** </p><p>1. Se till att du har installerat den här kontrollen med VSIX-tilläggsfilen som finns i det nedladdade paketet. För att verifiera gå till Verktyg -> Tillägg och uppdateringar. Under Installerat bör du se 'Aspose Export Export GridView to Excel Control'. Om du inte ser den, försök att installera om den</p><p>2. Se till att din webbapplikation körs i .NET framework 4.0 eller högre, för lägre versioner av .NET framework, kontrollera ovanstående alternativa metod.<br>   **Äldre versioner av Visual Studio**</p><p>3. Se till att du har lagt till den här kontrollen manuellt i din verktygslåda enligt instruktionerna ovan.</p>|
|2 | Jag får felmeddelandet "Åtkomst nekas" när jag kör programmet|<p>1. Om du upplever det här problemet i produktionen, se till att du kopierar både Aspose.Excel.dll och Aspose.Excel.GridViewExport.dll till din bin-mapp.</p><p>2. Om du använder Visual Studio se till att köra det som administratör även om du redan är inloggad som administratör.</p>|
### **Aspose .NET Exportera GridView till Excel-kontrollegenskaper**
Följande egenskaper är exponerade för att konfigurera och använda coola funktioner som tillhandahålls av denna kontroll

|**Egendomsnamn** |**Typ** |**Exempel/Möjliga värden** |**Beskrivning** |
|:- |:- |:- |:- |
| ExportButtonText| sträng| exportera till Excel| Du kan använda den här egenskapen för att åsidosätta befintlig standardtext|
|ExportButtonCssClass| sträng| btn btn-primär| Css-klass som appliceras på exportknappens yttre div. För att tillämpa css på knappen kan du använda .yourClass-inmatningen|
| ExportFileHeading| sträng|<h4>Exempelrapport för GridView-export</h4> | Du kan använda html-taggar för att lägga till stil till din rubrik|
| ExportOutputFormat| uppräkning| Xlsx, Xlsb, Xls, Txt, Csv, Ods| Utdataformat för det exporterade dokumentet. Format som stöds är Xlsx, Xlsb, Xls, Txt, Csv, Ods|
| ExportOutputPathOnServer| sträng| c:<br> temp| Lokal utdata Disksökväg på server där en kopia av exporten automatiskt sparas. Applikationen måste ha skrivbehörighet till denna sökväg.|
| ExportDataSource| objekt| allRowsDataTable|Ställer in objektet från vilket denna databindningskontroll hämtar sin lista över dataobjekt. Objektet måste ha all data som behöver exporteras. Den här egenskapen används utöver den normala DataSource-egenskapen och är användbar när anpassad sökning är aktiverad och den aktuella sidan bara hämtar rader som ska visas på skärmen.|
| LicenseFilePath| sträng|| Lokal sökväg på servern till licensfilen. Till exempel c:<br> inetpub<br> Aspose.Cells.lic|
Ett exempel på Export GridView till Excel-kontroll med alla använda egenskaper visas nedan

{{< highlight "java" >}}

 <aspose:ExportGridViewToExcel Width="800px" ID="ExportGridViewToExcel1" ExportButtonText="Export to Excel"

    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExcelOutputFormat="xlsx"

    ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h1>Example Report</h1>"

    OnPageIndexChanging="ExportGridViewToExcel1_PageIndexChanging" PageSize="5" AllowPaging="True"

    LicenseFilePath="c:\inetpub\Aspose.Cells.lic" runat="server" CellPadding="4"

    ForeColor="#333333" GridLines="Both">

</aspose:ExportGridViewToExcel>


{{< /highlight >}}
## **Videodemo**
 Vänligen kontrollera[videon](https://www.youtube.com/watch?v=_fSq_3TP1oM) nedan för att se modulen i aktion.
## **Stödja, utöka och bidra**
### **Stöd**
Från de allra första dagarna av Aspose visste vi att det inte skulle räcka att bara ge våra kunder bra produkter. Vi behövde också leverera bra service. Vi är själva utvecklare och förstår hur frustrerande det är när ett tekniskt problem eller en egenhet i programvaran hindrar dig från att göra det du behöver göra. Vi är här för att lösa problem, inte skapa dem.

Det är därför vi erbjuder gratis support. Alla som använder vår produkt, oavsett om de har köpt dem eller använder en utvärdering, förtjänar vår fulla uppmärksamhet och respekt.

Du kan logga eventuella problem eller förslag relaterade till denna kontroll med någon av följande plattformar

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **Utöka och bidra**
Aspose .NET Exportera GridView till Excel Control för Visual Studio är öppen källkod och dess källkod är tillgänglig på de stora sociala kodningswebbplatserna nedan. Utvecklare uppmanas att ladda ner källkoden och utöka funktionaliteten enligt sina egna krav.
#### **Källkod**
Du kan få den senaste källkoden från en av följande platser

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins)
#### **Hur man konfigurerar källkoden**
Du måste ha följande installerat för att kunna öppna och utöka källkoden

- Visual Studio 2010

Följ dessa enkla steg för att komma igång

1. Ladda ner/klona källkoden.
1.  Öppna Visual Studio 2010 och välj**Fil** > **Öppet projekt**
1.  Bläddra till den senaste källkoden som du har laddat ner och öppna**Aspose.Excel.GridViewExport.sln**
#### **Källkodsöversikt**
Det finns tre projekt i lösningen

- Aspose.Excel.GridViewExport - Innehåller VSIX-paket och serverkontroll for .NET 4.0.
- Aspose.Excel.GridViewExport_DotNet_2.0 - Utökad GridView-kontroll for .NET 2.0
- Aspose.Excel.GridViewExport.Website - Webbprojekt för att testa Excel Exportable GridView-kontrollen
