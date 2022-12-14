---
title: Aspose.Cells för .NET 20.5 Release Notes
type: docs
weight: 30
url: /sv/net/aspose-cells-for-net-20-5-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 20.5](https://www.nuget.org/packages/Aspose.Cells/20.5.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-42948|Stöd GridWeb på MVC|Ny funktion|
|CELLSNET-46946|Stöd för Aspose.Cells.GridWeb i ASP.NET Core|Ny funktion|
|CELLSNET-47251|Ny Excel "Implicit Intersection Operators"@-symbol har infogats|Förbättring|
|CELLSNET-47303|Möjlighet att komma åt aktiv cell eller valda celler utanför GridWeb|Förbättring|
|CELLSNET-47243|Vänta på getdisplaystyle för ett kalkylblad med rader 65536|Prestanda|
|CELLSNET-47044|Datumformateringsproblem i de första kolumncellerna i pivottabellen|Insekt|
|CELLSNET-47301|Rader/kolumner döljs genom att exportera pivottabellen till en bild efter beräkning|Insekt|
|CELLSNET-47308|Få egenskaper saknas i utdata-HTML efter inställning av Cell.HtmlString|Insekt|
|CELLSNET-47343|Rubriker saknas vid konvertering av utskriftsområdet till HTML|Insekt|
|CELLSNET-47344|Hela kalkylbladet exporteras när endast utskriftsområdet förväntas|Insekt|
|CELLSNET-47322|Fel värde beräknat av Aspose.Cells vid användning av OFFSET-funktionen|Insekt|
|CELLSNET-47333|När du använder CalculateFormula API på ett kalkylblad är värdet på två celler felaktigt|Insekt|
|CELLSNET-46960|Formaterings- och beteendeproblem vid laddning av Excel-fil till GridWeb|Insekt|
|CELLSNET-47096|Ett problem med GridDesktops formelfält med SplitterPane|Insekt|
|CELLSNET-47200|Problem med överlappning av navigeringsknappar när du ställer in dolt ark som aktivt ark|Insekt|
|CELLSNET-47221|Visa radnumret korrekt i GridDesktop|Insekt|
|CELLSNET-47228|Problem med att öppna filen i GirdDesktop|Insekt|
|CELLSNET-47240|FormulaBar.VerticalScroll i GridDesktop fungerar inte|Insekt|
|CELLSNET-47294|Vertikal justering inte effektiv i GridWeb|Insekt|
|CELLSNET-47302|GridWeb visar partiella kommentarer i cellerna|Insekt|
|CELLSNET-47311|Kommentarer har beskurits på grund av att rutan fryser|Insekt|
|CELLSNET-47323|Gridweb clear cells bakre bild orsakar sidladdning med IsPostBack false|Insekt|
|CELLSNET-47346|GridDesktop visar vanliga tecken istället för '*' medan du anger lösenordet för att ändra|Insekt|
|CELLSNET-47349|JS fel|Insekt|
|CELLSNET-47281|Oavsiktliga radbrytningar i celler vid konvertering av Excel-fil till PDF|Insekt|
|CELLSNET-47298|Befintligt teckensnitt ersatt av Aspose.Cells|Insekt|
|CELLSNET-47299|CellsException under konvertering av Excel till PDF|Insekt|
|CELLSNET-47320|Importera XML till cell får fel värde|Insekt|
|CELLSNET-47321|Import av XML skadar utdatafilen|Insekt|
|CELLSNET-47324|Ikonfel i Excel till PDF-konvertering|Insekt|
|CELLSNET-46149|Problem med textjustering i diagrambilden|Insekt|
|CELLSNET-47231|En etikett saknas på diagrambilden vid rendering med den nyare versionen|Insekt|
|CELLSNET-47116|Data går förlorad när sample.xlsx konverteras till .xls|Insekt|
|CELLSNET-47325|Att anropa TextBox.Characters() orsakar ytterligare taggar i HtmlText|Insekt|
|CELLSNET-47326|Style of HyperLinks går förlorad när du sparar ODS-arbetsbok som PDF eller HTML|Insekt|
|CELLSNET-47327|Text från hyperlänkar går förlorad när en ODS-fil åter sparas eller renderas|Insekt|
|CELLSNET-47332|Att ställa in egenskaper för TextParagraph resulterar i flera överlappande textrader|Insekt|
|CELLSNET-47339|Cell format försvinner/innehåll saknas efter att ha sparats|Insekt|
|CELLSNET-47348|Datumformatet har ändrats i ODS-filen efter att den laddats och sparats|Insekt|
|CELLSNET-47290|Undantag när man försöker öppna en viss HTML-fil|Undantag|
|CELLSNET-47305|RANDBETWEEN() väcker undantag ArgumentOutOfRangeException|Undantag|
|CELLSNET-47351|Villkorlig formatering som orsakar StackOverflowException när du sparar till PDF|Undantag|
|CELLSNET-47319|NullReferenceException på Excel-fil med länkad SVG-bild|Undantag|
|CELLSNET-47359|Undantag vid laddning av en XLSX-fil|Undantag|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Lägger till WorkbookSettings.GetThemeFont()-metoden.**
Får tematypsnitt.
#### **Lägger till egenskapen DataLabels.LinkedSource.**
Hämtar och ställer in den länkade källan.
#### **Lägger till DefaultEditLanguage enum.**
Representerar standardspråket för redigering.
#### **Lägger till egenskapen ImageOrPrintOptions.DefaultEditLanguage.**
Hämtar eller ställer in standardspråk för redigering.
Det kan visa/rendera olika layouter för textstycken när olika redigeringsspråk är inställda.
#### **Lägger till egenskapen PdfSaveOptions.DefaultEditLanguage.**
Hämtar eller ställer in standardspråk för redigering.
Det kan visa/rendera olika layouter för textstycken när olika redigeringsspråk är inställda.
