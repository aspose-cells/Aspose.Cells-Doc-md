---
title: Visual Studio Export GridView Till Excel kontroll
type: docs
weight: 10
url: /sv/net/visual-studio-export-gridview-to-excel-control/
---

## **Introduktion**
Exportera GridView Till Excel-kontroll är en ASP.NET-serverkontroll som möjliggör export av innehåll från GridView till Microsoft Excel eller OpenOffice-kalkylblad med hjälp av [Aspose.Cells](https://products.aspose.com/cells/net/). Den lägger till knappen **Exportera till Excel** ovanpå GridView-kontrollen. Genom att klicka på knappen exporteras innehållet i GridView-kontrollen dynamiskt till en Microsoft Excel- eller OpenOffice-kalkylblad och sedan laddas den exporterade filen automatiskt ner till den av användaren valda diskplatsen på några sekunder.
### **Modulfunktioner**
Denna första version av kontrollen har följande funktioner:

- Få en offlinekopia av ditt favorit online-GridView-innehåll för redigering, delning och utskrift.
- Ärvd från standard ASP.NET GridView-kontroll och har därför alla dess funktioner och egenskaper.
- Exportera GridView till Xlsx, Xlsb, Xls, Txt, Csv, Ods.
- Fungerar med alla .NET-versioner från och med .NET 2.0.
- Möjlighet att anpassa/lokalisera exportknappstexten.
- Applicera utseendet på din egen tema på exportknappen med hjälp av css.
- Möjlighet att lägga till anpassad rubrik ovanpå den exporterade dokument
- Möjlighet att spara varje exporterad dokument på servern på konfigurerbar diskbana
- Möjlighet att exportera nuvarande sida eller alla sidor när sidvisning är aktiverad

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_1.png)

Det här kontrollen gör det möjligt att exportera GridView i olika filformat.

1. Exportera GridView till Excel
1. Exportera GridView till Xlsx
1. Exportera GridView till Xlsb
1. Exportera GridView till Xls
1. Exportera GridView till Txt
1. Exportera GridView till Csv
1. Exportera GridView till Ods
## **Systemkrav och stödda plattformar**
### **Systemkrav**
Exportera GridView Till Excel-kontroll för Visual Studio kan användas på vilket system som har IIS och .NET Framework 2.0 eller senare installerat.
### **Stödda plattformar**
Exportera GridView Till Excel-kontroll för Visual Studio stöds av alla versioner av ASP.NET som körs på .NET Framework 2.0 eller senare. Du kan använda någon av följande versioner av Visual Studio för att använda denna kontroll i dina ASP.NET-applikationer

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013
## **Nedladdning**
Du kan ladda ner Exportera GridView Till Excel-kontroll från en av de följande platserna

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Export_GridView_Excel)
## **Installation**
Det är mycket enkelt och lätt att installera Exportera GridView Till Excel-kontroll, följ dessa enkla steg
### **För Visual Studio 2010, 2012 och 2013**
1. Extrahera den nedladdade zip-filen
1. Dubbelklicka på VSIX-filen Aspose.Excel.GridViewExport.vsix
1. En dialogruta visas som visar de tillgängliga och stödda Visual Studio-versionerna installerade på din dator
1. Välj de du vill lägga till Exportera GridView Till Excel-kontrollen till.
1. Klicka på Installera

Du får en framgångsrik dialogruta när installationen är slutförd.

**Observera:** Se till att starta om Visual Studio så att ändringarna träder i kraft.
### **För Visual Studio 2005, 2008 och Express utgåvor**
Följ dessa steg för att integrera Exportera GridView Till Excel-kontroll i Visual Studio för enkel dra och släpp precis som andra ASP.NET-kontroller

1. Extrahera den nedladdade zip-filen
1. Se till att köra Visual Studio som administratör

På Verktygsmenyn, klicka på Välj verktygslådans komponenter.

1. Klicka på Bläddra. 
   Dialögfönstret Öppna visas.
1. Bläddra till den extraherade mappen och välj Aspose.Excel.GridViewExport.dll
1. Klicka på OK.

När du öppnar en aspx eller ascx-kontroll i verktygsfältet till vänster ser du ExportGridViewToWord under fliken Allmänt

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_2.png)
## **Användning**
När det är installerat är det mycket enkelt att börja använda denna kontroll i dina ASP.NET-applikationer

|**För .NET Framework 4.0 och högre** |**För .NET Framework 2.0 och högre** |** |
| :- | :- | :- |
|För program som körs i .NET Framework 4.0 och högre i Visual Studio 2010 och högre, borde du se **ExportGridViewToExcel**-kontroll i **Aspose**-fliken i verktygsfältet som visas nedan. Du kan enkelt dra och släppa den här kontrollen på din ASP.NET-sida, kontroll eller master-sida precis som vilken annan .NET-kontroll och komma igång. |För att använda denna kontroll i applikationer som körs i .NET 2.0 i valfri version av Visual Studio se till att du har lagt till ExportGridViewToExcel i ditt verktygsfält enligt instruktionerna på ﻿[8.1.2.1 Hämtning och Installation]() under rubriken **För Visual Studio 2005, 2008 och Express-utgåvor** <br>Du borde se **ExportGridViewToExcel**-kontrollen under fliken **Allmänt** i verktygsfältet som visas nedan. Du kan enkelt dra och släppa denna kontroll på din ASP.NET-sida, kontroll eller master-sida precis som vilken annan .NET-kontroll och komma igång. | |
|<p>![todo:image_alt_text](picture2.png)</p><p></p>|<p>![todo:image_alt_text](picture3.png)</p><p></p>| |
### **Manuellt tillägg av ExportGridViewToExcel-kontrollen**
Om du har några problem med att använda ovanstående metoder som använder Visual Studio Toolkit, kan du manuellt lägga till denna kontroll i din ASP.NET-applikation som körs på vilken .NET Framework som helst som är större än 2.0

1. Om du använder Visual Studio, se till att köra den som administratör
1. Lägg till referens till **Aspose.Excel.GridViewExport.dll** som finns i den extraherade nedladdningspaketet i ditt ASP.NET-projekt eller webbapplikation. Se till att din webbapplikation/Visual Studio har full tillgång till denna mapp, annars kan du få ett undantag om åtkomst nekas.
1. Lägg till den här raden högst upp på sidan, kontrollen eller MasterPage 

{{< highlight java >}}

 <%@ Register assembly="Aspose.Excel.GridViewExport" namespace="Aspose.Excel.GridViewExport" tagprefix="aspose" %>

{{< /highlight >}}

1. Lägg till följande på en plats på din ASP.NET-sida, kontroll eller master-sida där du vill lägga till kontrollen 

{{< highlight java >}}

 <aspose:ExportGridViewToExcel ID="ExportGridViewToExcel1" runat="server"></aspose:ExportGridViewToExcel>

{{< /highlight >}}
### **Vanliga frågor och problem du kan stöta på när du använder denna kontroll**
Vanliga frågor och problem du kan stöta på när du använder denna kontroll

|**#** |**Fråga** |**Svar** |
| :- | :- | :- |
|1 |Jag kan inte se ExportGridViewToExcel-kontrollen i verktygsfältet |<p>**Visual Studio 2010 och högre** </p><p>1. Se till att du har installerat denna kontroll med hjälp av VSIX-fil som finns i det nedladdade paketet. För att verifiera gå till Verktyg -> Tillägg och uppdateringar. Under installerat borde du se 'Aspose Export Export GridView Till Excel Control'. Om du inte ser det försök med att installera om det</p><p>2. Se till att din webbapplikation körs i .NET Framework 4.0 eller högre, för lägre versioner av .NET Framework, vänligen kontrollera ovanstående alternativa metod. <br>   **Äldre versioner av Visual Studio**</p><p>3. Se till att du manuellt har lagt till denna kontroll i ditt verktygsfält enligt ovanstående instruktioner.</p>|
|2 |Jag får 'Åtkomst nekas' fel när jag kör applikationen |<p>1. Om du upplever detta problem i produktion se till att du kopierar både Aspose.Excel.dll och Aspose.Excel.GridViewExport.dll till din bin-mapp.</p><p>2. Om du använder Visual Studio, se till att köra den som administratör även om du redan är inloggad som administratör.</p>|
### **Aspose .NET Export GridView Till Excel Kontroll Egenskaper**
Följande egenskaper exponeras för att konfigurera och använda de coola funktionerna som tillhandahålls av denna kontroll

|**Egenskapsnamn** |**Typ** |**Exempel/Möjliga värden** |**Beskrivning** |
| :- | :- | :- | :- |
|ExportKnappText |sträng |Exportera till Excel |Du kan använda den här egenskapen för att ersätta befintlig standardtext |
|ExportKnappCssKlass |sträng |btn btn-primary |Css-klass som används på yttre div av exportknappen. För att använda css på knappen kan du använda .dinKlass input |
|ExportFilRubrik |sträng |<h4>GridView Export Exempelrapport</h4> |Du kan använda html-taggar för att lägga till stil i din rubrik |
|ExportUtdataFormat |enum |Xlsx, Xlsb, Xls, Txt, Csv, Ods |Utdataformat för det exporterade dokumentet. Stödda format är Xlsx, Xlsb, Xls, Txt, Csv, Ods |
|ExportUtdataSökvägPåServer |sträng |c: <br>temp |Lokal utdata Disk-sökväg på server där en kopia av exporten automatiskt sparas. Applikationen måste ha skrivbehörighet till denna sökväg. |
|ExportDatasamling |objekt |allRowsDataTable |Använder objektet från vilket denna data-bindningskontroll hämtar sin lista med dataenheter. Objektet måste ha all data som behöver exporteras. Denna egenskap används utöver normal DataSource-egenskap och är användbar när anpassad sidning är aktiverad och aktuell sida bara hämtar rader som ska visas på skärmen. |
|LicensFilSökväg |sträng | |Lokal sökväg på servern till licensfilen. Till exempel c: <br>inetpub <br>Aspose.Cells.lic |
Ett exempel på Export GridView till Excel-kontroll med alla använda egenskaper visas nedan

{{< highlight java >}}

 <aspose:ExportGridViewToExcel Width="800px" ID="ExportGridViewToExcel1" ExportButtonText="Export to Excel"

    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExcelOutputFormat="xlsx"

    ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h1>Example Report</h1>"

    OnPageIndexChanging="ExportGridViewToExcel1_PageIndexChanging" PageSize="5" AllowPaging="True"

    LicenseFilePath="c:\inetpub\Aspose.Cells.lic" runat="server" CellPadding="4"

    ForeColor="#333333" GridLines="Both">

</aspose:ExportGridViewToExcel>


{{< /highlight >}}
## **Video Demonstration**
Vänligen kolla [videon](https://www.youtube.com/watch?v=_fSq_3TP1oM) nedan för att se modulen i aktion.
## **Support, Utvidga och Bidra**
### **Support**
Från allra första början av Aspose visste vi att det inte bara skulle räcka med att ge våra kunder bra produkter. Vi behövde också leverera en bra service. Vi är själva utvecklare och förstår hur frustrerande det är när en teknisk fråga eller en egenhet i programvaran hindrar dig från att göra det du behöver göra. Vi är här för att lösa problem, inte skapa dem. 

Detta är anledningen till att vi erbjuder kostnadsfri support. Alla som använder våra produkter, vare sig de har köpt dem eller använder en utvärdering, förtjänar vår fulla uppmärksamhet och respekt.

Du kan logga eventuella problem eller förslag relaterade till denna kontroll genom någon av följande plattformar

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **Utvidga och Bidra**
Aspose .NET Export GridView To Excel Control for Visual Studio är öppen källkod och dess källkod är tillgänglig på de största sociala kodningswebbplatserna som listas nedan. Utvecklare uppmanas att ladda ner källkoden och utöka funktionaliteten enligt sina egna krav.
#### **Källkod**
Du kan få den senaste källkoden från någon av följande platser

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins)
#### **Hur man konfigurerar källkoden**
Du måste ha följande installerat för att öppna och utöka källkoden

- Visual Studio 2010

Följ dessa enkla steg för att komma igång

1. Ladda ner/Klona källkoden.
1. Öppna Visual Studio 2010 och välj **Fil** > **Öppna projekt**
1. Bläddra till den senaste källkoden som du har laddat ner och öppna **Aspose.Excel.GridViewExport.sln**
#### **Översikt över källkoden**
Det finns tre projekt i lösningen

- Aspose.Excel.GridViewExport - Innehåller VSIX-paket och serverkontroll för .NET 4.0.
- Aspose.Excel.GridViewExport_DotNet_2.0 - Utökad GridView-kontroll för .NET 2.0
- Aspose.Excel.GridViewExport.Website - Webbprojekt för att testa Excel Exportable GridView-kontroll
