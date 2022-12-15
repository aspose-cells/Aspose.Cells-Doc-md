---
title: Aspose.Cells for .NET 17.11 Release Notes
type: docs
weight: 20
url: /sv/net/aspose-cells-for-net-17-11-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for .NET 17.11.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-45748|XmlMapQuery-liknande funktionalitet behövs som tillgänglig i MS Excel|Ny funktion|
|CELLSNET-45747|Associerad egenskap behövs för XMLMaps för att få RootElementName för kartan|Ny funktion|
|CELLSNET-45709|Skalan blir mindre - Problem med teckensnitt|Ny funktion|
|CELLSNET-45743|Skydda delad arbetsbok - Ange eller ändra lösenord|Ny funktion|
|CELLSNET-45737|Stöd PasteType för Aspose.Cells.GridDesktop under kopiera/klistra in åtgärder|Ny funktion|
|CELLSNET-45755|Det går inte att få text med smarta konstformer|Förbättring|
|CELLSNET-45720|Pivottabellen tar för lång tid att uppdatera data|Prestanda|
|CELLSNET-45680|Formriktningen är fel när den konverteras till bildformat|Insekt|
|CELLSNET-45679|Stjärnformer visas inte korrekt i PDF-filen|Insekt|
|CELLSNET-45669|Tecken överlappar varandra vid konvertering till bild|Insekt|
|CELLSNET-45665|Vissa ritelement är inverterade medan andra flyttas åt höger|Insekt|
|CELLSNET-43912|Positionen för linjeobjekten ändrades under renderingen av kalkylarket till PDF|Insekt|
|CELLSNET-45715|Pivottabellalternativ - Visa värderaden - aktiveras när du sparar om|Insekt|
|CELLSNET-45671|Saknar totala värden för de beräknade fälten vid uppdatering/beräkning av pivottabelldata|Insekt|
|CELLSNET-45650|Fel vid expansion av data till rätt kolumner när ett MHTML-filformat sparades till Excel-fil|Insekt|
|CELLSNET-45721|LightCellsDataProvider tar bort ledande och efterföljande utrymmen|Insekt|
|CELLSNET-45719|Formelberäkning löser formeln oväntat till fel|Insekt|
|CELLSNET-45724|Att spara Excel som PDF minskar kolumnbredden|Insekt|
|CELLSNET-45712|Förklaring av diagrammet saknas i utdata-PDF-filen|Insekt|
|CELLSNET-45710|Nummerformatering i diagram går förlorad efter att en Excel-fil sparats som PDF|Insekt|
|CELLSNET-45708|PDF-fil skapad av Aspose.Cells orsakar fel i Adobe Acrobat Reader|Insekt|
|CELLSNET-45684|Diagram till bild eller PDF - 3D-linjediagram är inte korrekt eller roterat|Insekt|
|CELLSNET-45760|Validering är inte korrekt kopierad från ett kalkylblad till ett annat|Insekt|
|CELLSNET-45758|Style.QuotePrefix-egenskapen fungerar inte för XLSB-filformat|Insekt|
|CELLSNET-45757|Specifik Excel-arbetsbok blir dold efter att ha öppnats och sparats|Insekt|
|CELLSNET-45754|Kolumner utökades oväntat i den sammanslagna arbetsboken|Insekt|
|CELLSNET-45749|HTML-sträng med flera teckensnitt korrumperar utdatafilen i Excel|Insekt|
|CELLSNET-45739|SpreadsheetML-fil när den sparas på nytt via Aspose.Cells innehåller ytterligare skyddsinställningar som tillämpas|Insekt|
|CELLSNET-45738|AutoFitColumns bryter HTML-formatering i utdata Excel-fil|Insekt|
|CELLSNET-45734|MS Excel visar ett felmeddelande när utdatafilen öppnas|Insekt|
|CELLSNET-45733|Textbox-teckensnittet ändras efter att form(er) delas upp|Insekt|
|CELLSNET-45714|Radhöjden blir för stor efter autopassning av rader|Insekt|
|CELLSNET-45735|Problem med CellColor när du använder snabbmenyn för att ändra|Insekt|
|CELLSNET-45707|Undantag vid användning av PivotTable.RefreshData|Undantag|
|CELLSNET-45728|Index var utanför intervallet undantag när du sparade som PDF-sida|Undantag|
|CELLSNET-45704|Workbook.Save() misslyckas med ett undantag när Aspose.Cells används som ett Azure-webbjobb|Undantag|
|CELLSNET-45753|När XLSB konverteras till PDF uppstår System.ArgumentOutOfRangeException|Undantag|
|CELLSNET-45751|ExportTableOptions.Index-egenskapen som används i metoden ExportDataTable() orsakar undantag|Undantag|
|CELLSNET-45726|Undantag vid laddning av utdata-XLS-filen (med OLE-objekt, bilder etc. uteslutna)|Undantag|
|CELLSNET-45723|R1C1Formula ger undantag om formeln innehåller tecknet "[" ]|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till metoden Shape.GetResultOfSmartArt().**
Konvertera den smarta konsten till en gruppform.
#### **Lägger till egenskapen Shape.IsSmartArt**
Indikerar om formen är smart konst.
#### **Metoden Workbook.ProtectSharedWorkbook() och Workbook.UnprotectSharedWorkbook()**
Skyddar och tar bort skyddet för den delade arbetsboken.
#### **Lägger till enum StyleModifyFlag.Spacing**
Anger avståndet mellan tecken i en textkörning.
#### **Lägger till egenskapen PdfSaveOptions.IgnoreError**
Indikerar om du behöver dölja felet under renderingen.
#### **Lägger till egenskapen ImageOrPrintOptions.PageIndex**
Hämtar eller ställer in det 0-baserade indexet för den första sidan som ska sparas.
#### **Lägger till egenskapen ImageOrPrintOptions.PageCount**
Hämtar eller ställer in antalet sidor som ska sparas.
#### **Lägger till egenskapen XmlMap.RootElementName**
Hämtar namnet på rotelementet.
#### **Lägger till metoden Worksheet.XmlMapQuery(strängsökväg, XmlMap xmlMap).**
Fråga cellområden som mappade/länkade till den specifika sökvägen för xml-kartan.
#### **Lägger till egenskapen GridDesktop.PasteType**
Hämtar eller ställer in vilken inklistringstyp som gäller för inklistringsåtgärd, endast tillgängligt när EnableClipboardCopyPaste är falskt.
#### **Lägger till egenskapen LoadOptions.AutoFitterOptions**
Hämtar och ställer in alternativen för automatisk montering.
#### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Konvertera den smarta konsten till gruppform](/cells/sv/net/convert-the-smart-art-to-group-shape/)
- [Skapa delad arbetsbok med Aspose.Cells](/cells/sv/net/create-shared-workbook-with-aspose-cells/)
- [Bestäm om Shape är Smart Art Shape](/cells/sv/net/determine-if-shape-is-smart-art-shape/)
- [Hitta rotelementets namn på XML-karta](/cells/sv/net/find-the-root-element-name-of-xml-map/)
- [Ignorera fel när du renderar Excel till Pdf](/cells/sv/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Lösenordsskydda eller avskydda den delade arbetsboken](/cells/sv/net/password-protect-or-unprotect-the-shared-workbook/)
- [Fråga Cell Områden mappade till Xml Map Path med metoden Worksheet.XmlMapQuery](/cells/sv/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/)
- [Rendera sekvens av sidor med hjälp av PageIndex och PageCount Properties för ImageOrPrintOptions](/cells/sv/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Copy Paste Beteende för EnableClipboardCopyPaste och PasteType GridDesktop Properties](/cells/sv/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/)


