---
title: Aspose.Cells for .NET 21.10 Release Notes
type: docs
weight: 3
url: /sv/net/aspose-cells-for-net-21-10-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 21.10](https://www.nuget.org/packages/Aspose.Cells/21.10.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-49192| Problem med att hämta intervall (RefersTo) med en offsetfunktion|Ny funktion|
|CELLSNET-49132|Öppna filer med HTML-tabell inuti som XLS-filer|Ny funktion|
|CELLSNET-49173|Stöd Range.CurrentRegion Property|Ny funktion|
|CELLSNET-49015|Uppdatera hyperlänk (Sheet1!A1) när du ändrar namnet på kalkylbladet.|Förbättring|
|CELLSNET-49021|Villkorlig formatering av ods går förlorad i MS Excel om typen är "Innehåller text"|Förbättring|
|CELLSNET-49280|Stöd autofyllintervall med fyllningstyp|Förbättring|
|CELLSNET-49413|Ta bort osynliga former när du renderar HTML|Förbättring|
|CELLSNETCORE-135|Applikationen stannar när stora filer och UDF:er beräknas|Prestanda|
|CELLSNET-49124|Suddiga radioknappar vid konvertering av XLSM till HTML|Insekt|
|CELLSNET-49115|Felaktig beräkning av operatorer i formel när operander är intervall|Insekt|
|CELLSNETCORE-132|Förvrängt diagram skapat i konverterad HTML|Insekt|
|CELLSNETCORE-141|Saknas text, fel textjustering och saknade procentsatser i diagrammet|Insekt|
|CELLSNET-49067|Problem med få och ställ in flikfärg i GridDesktop|Insekt|
|CELLSNET-49069|Aspose.Cells.GridWeb SessionMode fungerar inte|Insekt|
|CELLSNET-49118|Problem med XML-import|Insekt|
|CELLSNET-49195|XLSX till HTML-konvertering behåller inte sekvensen av osynliga tecken|Insekt|
|CELLSNET-49245|Bild skiftar i specifika XLS-filer när de renderas till HTML|Insekt|
|CELLSNET-49246|Bilden är inte synlig när du konverterar specifik XLSX-fil till HTML|Insekt|
|CELLSNET-49334| Problem med teckensnittstext i sidfotsfältet för Excel-rendering|Insekt|
|CELLSNET-49393|Det gick inte att importera XML-filen till mallfilen|Insekt|
|CELLSNETCORE-226|Onödigt blanksteg som återges under konvertering av Excel till EMF|Insekt|
|CELLSNET-49091|"strCache"-noden saknas i en XML|Insekt|
|CELLSNET-49161|Det går inte längre att kopiera korrekt värdeaxelmarkeringsetiketts teckensnittsnamn|Insekt|
|CELLSNET-49191|Kan inte visa procentvärden i dataetikett|Insekt|
|CELLSNET-49305|Vissa dataetiketter i diagrammet saknas|Insekt|
|CELLSNET-49374|Diagramlinjen är annorlunda med funktionen Chart.ToImage än i Excel|Insekt|
|CELLSNET-48613|En resurs som ligger utanför det valda intervallet ska inte exporteras till HTML|Insekt|
|CELLSNET-49027|Förvrängning av dokumentsidans färg och layout|Insekt|
|CELLSNET-49145|DataMashup-information har inte hämtats från Excel-fil|Insekt|
|CELLSNET-49146|Vattenstämpel i Excel-fil kan inte genereras och visas korrekt|Insekt|
|CELLSNET-49239|Skuggeffekt tillämpas på bild(er) vid konvertering från XLSM till XLS|Insekt|
|CELLSNET-49244|Ikonens villkorliga formatering går förlorade när du sparar som html|Insekt|
|CELLSNET-49328|Fel vid kopiering av arbetsblad|Insekt|
|CELLSNET-49365|Text klipps i skrivarutdata efter anrop till AutoFitRows|Insekt|
|CELLSNET-49366|Problem med Cell indatafält för datavalidering i XLSB-format|Insekt|
|CELLSNETCORE-269|Fel rad med stor höjd läggs till i HTML-tabellen|Insekt|
|CELLSNETCORE-270|Problem med HTMLString Font när Excel sparats som HTML en gång|Insekt|
|CELLSNET-49375|Problem vid uppdatering av pivottabell efter att ha lagt till data|Insekt|
|CELLSNET-49194|Undantag vid laddning av excel-filen|Undantag|
|CELLSNET-49363|CalculateData-metoden på pivottabellen ger undantag|Undantag|
|CELLSNET-49373|"Inmatningssträngen var inte i rätt format." undantag när XLSX-filen öppnas|Undantag|
|CELLSNET-49394|Null undantag när filen NUMBERS är öppen|Undantag|
|


## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till överbelastad metod Name.GetRefersTo().**

Hämtar formeluttrycket baserat på den angivna cellen.

### **Lägger till överbelastad metod Range.AutoFill().**

Fyll automatiskt målområdet med fyllningstyp.

### **Lägger till egenskapen Comment.IsThreadedComment.**

Anger om denna kommentar är trådad kommentar.

### **Lägger till egenskapen HtmlSaveOptions.IgnoreInvisibleShapes.**

Anger om osynliga former används när du sparar html.

### **Lägger till egenskapen Range.CurrentRegion.**

Returnerar ett intervall avgränsat av valfri kombination av tomma rader och tomma kolumner.

### **Lägger till AxisBins klass.**

 Representerar axelfack för histogramdiagram.

### **Föråldrad metod SheetRender.GetPageSize(int pageIndex)**

Använd SheetRender.GetPageSizeInch(int pageIndex) istället.

### **Lägger till metod SheetRender.GetPageSizeInch(int pageIndex)**

Få sidstorlek på utdatabilden? i enhet av tum.

### **Föråldrad metod WorkbookRender.GetPageSize(int pageIndex)**

Använd WorkbookRender.GetPageSizeInch(int pageIndex) istället.

### **Lägger till metod WorkbookRender.GetPageSizeInch(int pageIndex)**

Få sidstorlek utdatabild? i enhet av tum.

