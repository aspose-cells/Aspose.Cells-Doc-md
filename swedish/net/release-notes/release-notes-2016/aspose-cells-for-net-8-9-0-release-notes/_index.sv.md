---
title: Aspose.Cells för .NET 8.9.0 Release Notes
type: docs
weight: 70
url: /sv/net/aspose-cells-for-net-8-9-0-release-notes/
---
### **1) Aspose.Cells**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSNET-44574 | Stöd för att expandera text från höger till vänster vid export av fil till HTML| Ny funktion|
|CELLSNET-44561 | Möjlighet att ställa in standardteckensnitt samtidigt som kalkylblad renderas till HTML| Ny funktion|
|CELLSNET-44562 | Möjlighet att ställa in standardteckensnitt samtidigt som kalkylblad renderas till bilder| Ny funktion|
|CELLSNET-44552 |Uppfriskande av pivottabellen ger undantag| Insekt|
|CELLSNET-44542 | Excel-filen renderas inte korrekt till HTML-filformat| Insekt|
|CELLSNET-44541 | Innehållet överlappar varandra vid konvertering av kalkylblad till HTML| Insekt|
|CELLSNET-44520 | Pivotfältets rullgardinsmeny saknas efter att XLSX har sparats igen som XLSB| Insekt|
|CELLSNET-44518 | Kalkylarket blir skadat efter att XLSX har sparats igen som XLSB| Insekt|
|CELLSNET-44501 | Uppdatering och beräkning av data på befintlig pivottabell genererar korrupta Excel-filer| Insekt|
|CELLSNET-44447 | Chart.ToImage genererar en felaktig bild| Insekt|
|CELLSNET-43656 | Vissa textobjekt är något trunkerade i HTML-utdata| Insekt|
|CELLSNET-44590 | Problem med att exportera Excel till PDF med specialtecken i sidhuvudet och sidfoten| Insekt|
|CELLSNET-44517 | Vertikal justering fel vid generering av intervall till bild med SheetRender.ToImage| Insekt|
|CELLSNET-44589 | Aspose.Cells genererad EMF visar felaktiga axeletiketter när de infogas i Word-dokument och konverteras till PDF| Insekt|
|CELLSNET-44586 | Mindre än enstaka mellanrum exporterar inte till PDF korrekt| Insekt|
|CELLSNET-44564 | Diagrammets EMF som genereras under Session 0 visar inte allt innehåll| Insekt|
|CELLSNET-44559 | Chart.HasAxis visar fel värde| Insekt|
|CELLSNET-44538 |Tom PNG 0KB-fil som genererades vid konvertering av XLSX till HTML| Insekt|
|CELLSNET-44591 | Cells.ClearContents tar bort formeln för cellerna under det angivna intervallet| Insekt|
|CELLSNET-44577 | Problem med Worksheet.Copy() - Alla kommentarer efter IV-kolumnen saknas i det kopierade bladet| Insekt|
|CELLSNET-44573 | Bilder i kalkylblad som kopierats från en extern XLSX har inte samma storlek som original| Insekt|
|CELLSNET-44571 | Kopiering av arbetsbok till ny arbetsbok gav ett oläsbart innehållsfel| Insekt|
|CELLSNET-44568 | TextBox i diagrammet försvinner när du kopierar arbetsböcker| Insekt|
|CELLSNET-44567 | Diagramfärger går förlorade när arbetsboken kopieras| Insekt|
|CELLSNET-44545 | Formel resulterar i "#NAMN" fel efter kopiering av rader och beräkning av formler| Insekt|
|CELLSNET-44544 | Formel ersätts med 0 efter kopiering av rader och beräkningsformler| Insekt|
|CELLSNET-44543 | Formens fyllnadsformat går förlorat när filen konverteras till HTML| Insekt|
|CELLSNET-41153 | Utskriftszonen flyttas lite med de senaste versionerna av produkten| Insekt|
|CELLSNET-44599 | Att visa totalt för listobjekt med endast 1 post förstör arbetsboken| Insekt|
|CELLSNET-44598 | Felaktig ListObject-storlek efter ShowTotals inställd på false| Insekt|
|CELLSNET-44563 | Undantag: "Inmatningssträngen var inte i ett korrekt format." när du laddar ett HTML-filformat| Undantag|
|CELLSNET-44560 |Problem med att spara en arbetsbok| Undantag|
|CELLSNET-44558 | ArgumentNullException vid metoden WorksheetCollection.GetNamedRanges| Undantag|
|CELLSNET-44588 | ArgumentOutOfRangeException när AutoFitColumns() anropas på ett kalkylblad| Undantag|
|CELLSNET-44556 | Undantag inträffade när ett Excel-dokument sparades| Undantag|
|CELLSNET-44554 | CellsException: fel i Cell: C2-Length får inte vara mindre än noll, vid Workbook ctor| Undantag|
|CELLSNET-44546 | Undantag: "Ogiltigt lösenord" när en krypterad Excel XLS-fil öppnas med Aspose.Cells API:er| Undantag|
### **2) Aspose.Cells Grid Suite**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSNET-44515 | Lägg till/ta bort kontextmenyobjekt i Aspose.Cells.GridWeb| Ny funktion|
|CELLSNET-44565 | Stöd för CellsHelper.GetVersion() API för GridWeb| Förbättring|
|CELLSNET-44583 | GridWeb-kontrollens höjd växer när du rullar nedåt i posten bakåt| Insekt|
|CELLSNET-44580 | Rullningslisten flyttas ner på IE11 och ibland tappar GridWeb rutformateringen| Insekt|
|CELLSNET-44550 | Personsökning fungerar inte efter att ha angett sessionslagringssökvägen - Aspose.Cells.GridWeb| Insekt|
|CELLSNET-44547 | Gridweb ändrar layout när sidindex ändras| Insekt|
|CELLSNET-44539 | Gridweb uppdateras inte efter rullning eller sidbyte på grund av registrering av Telerik RadAjaxManager-kontroll| Insekt|
|CELLSNET-44537 | Layoutproblem av Dropdown i GridWeb| Insekt|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Lägger till egenskapen HtmlSaveOptions.DefaultFontName**
Anger standardteckensnittsnamnet vid export av HTML, standardteckensnittet kommer att användas när stiltypsnittet inte finns. Om den här egenskapen är null kommer Aspose.Cells att använda universellt teckensnitt som har samma familj som det ursprungliga teckensnittet, standardvärdet är null.
#### **Lägger till egenskapen PivotTable.IsExcel2003Compatible**
Anger om pivottabellen är kompatibel med Excel2003 vid uppdatering av pivottabell. Om sant måste en sträng vara mindre än eller lika med 255 tecken, så om strängen är större än 255 tecken kommer den att trunkeras. Om det är falskt kommer en sträng inte att ha den ovannämnda begränsningen. Standardvärdet är sant.
#### **Lägger till egenskapen ImageOrPrintOptions.DefaultFont**
När tecken i Excel är unicode och inte ska ställas in med korrekt typsnitt i cellstil, kan de visas som block i PDF och bild.
Ställ in standardteckensnittet som MingLiu eller MS Gothic för att visa dessa tecken. Om den här egenskapen inte är inställd kommer Aspose.Cells att använda systemets standardteckensnitt för att visa dessa unicode-tecken.
#### **Lägger till GetVersion-metoden i GridWeb.**
Hämta releaseversionen.
