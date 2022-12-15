---
title: Aspose.Cells for .NET 17.7 Release Notes
type: docs
weight: 60
url: /sv/net/aspose-cells-for-net-17-7-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 17.7](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-17.7/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-45437|Stöd för fel och booleskt värde i ryska språket i Excel till PDF-rendering|Ny funktion|
|CELLSNET-45456|Läsa cellers data, formel och stil från nummerfil|Ny funktion|
|CELLSNET-45483|Stöd för att ändra startvärdet för radindex till 0 (istället för 1) i Aspose.Cells.GridDesktop|Ny funktion|
|CELLSNET-45434|GridWeb ViewPanel är inte alltid synligt|Ny funktion|
|CELLSNET-45224|Rendera pivottabell i GridDesktop|Ny funktion|
|CELLSNET-45490|Kasta fel eller undantag när fel namn tilldelas till egenskapen ListObject.DisplayName|Förbättring|
|CELLSNET-45470|Länkkälla DataSource vs. OriginalDataSource vs. Excel=>Data => Redigera länkar|Förbättring|
|CELLSNET-45439|Metoden GridDesktop.GetVersion() behövs för att kontrollera versionsnumret för GridDesktop under körning|Förbättring|
|CELLSNET-45457|Applikationen fastnar när man försöker få tag i bildens egendom|Prestanda|
|CELLSNET-45388|Pilformen återges inte bra i renderingar av ark till bild (.jpg).|Insekt|
|CELLSNET-45426|Diagramdata kan inte uppdatera data från pivottabellen|Insekt|
|CELLSNET-45447|Excel-fil skadad när pivottabell lades till efter import av källdata|Insekt|
|CELLSNET-45396|Formateringsfel när Excel-fil konverteras till HTML|Insekt|
|CELLSNET-45402|Cell.DisplayStringValue matchar inte de ursprungliga värdena|Insekt|
|CELLSNET-45479|Aspose.Cells 17.5 - Felaktig digital signering med DSA-certifikat|Insekt|
|CELLSNET-45420|Standardfontinställningen fungerar inte|Insekt|
|CELLSNET-45364|Vissa former/objekt klipps ut i PDF-filen|Insekt|
|CELLSNET-45491|Något svart oskärpa som fästs på dataetiketterna dök upp i utdatabilden av diagrammet|Insekt|
|CELLSNET-45476|Datumformatet för X-axeletiketterna ändras och åsidosätts i teckenförklaringsposter|Insekt|
|CELLSNET-45471|Texten "III.LowerQualityAboveSML" på andra sidan av PDF-filen är trasig|Insekt|
|CELLSNET-45454|Bubblans färger ändras lite för olika diagram även med samma kodrader|Insekt|
|CELLSNET-45452|Sparklines renderas inte korrekt i utdata-PDF-filen|Insekt|
|CELLSNET-45493|Ändra storlek på ListObject får inte anpassad formatering överförd|Insekt|
|CELLSNET-45482|Vissa former går förlorade i XLS-filen när bilder extraheras och infogas igen|Insekt|
|CELLSNET-45466|Vissa ytterligare ramar läggs till automatiskt|Insekt|
|CELLSNET-45464|Diagrammets axeltyp ändras efter Workbook.Combine()|Insekt|
|CELLSNET-45463|Radhöjder och diagramstorlekar blir mindre när du använder metoden Workbook.Combine().|Insekt|
|CELLSNET-45462|Fel pappersstorleksvärde returneras när kalkylbladet inte har inställningar för sidinställningar|Buggar|
|CELLSNET-45453|Formateringen av kalkylbladet ändrades efter Workbook.Combine()|Insekt|
|CELLSNET-45428|Cells.DeleteBlankRows/DeleteBlankColumns tar bort diagrammen i kalkylbladet|Insekt|
|CELLSNET-45488|GridWeb visar inte alla rader och stöter på ett fel|Insekt|
|CELLSNET-45438|Att rotera texten i cellen till 90 grader förstör cellens textjustering|Insekt|
|CELLSNET-45425|GridWeb lägger till utrymme i rullgardinsmenyn i Excel|Insekt|
|CELLSNET-42363|Problem med pivotfältens bildtexter i pivottabell (GridWeb)|Insekt|
|CELLSNET-45486|NullReferenceException inträffade när Excel-arbetsboken (med sammanslagna celler) sparades till HTML-filformat|Undantag|
|CELLSNET-45478|Undantag för att öppna en skadad MHTML-fil via Aspose.Cells API:er|Undantag|
|CELLSNET-45467|System.ArgumentOutOfRangeException' inträffade när en MHTML-fil laddades|Undantag|
|CELLSNET-45485|Undantag inträffade vid beräkning av en giltig formel|Undantag|
|CELLSNET-45433|Undantag förekommer vid öppning av fd1507a97b7f40fb85f9725535ecd215.xlsb|Undantag|
|CELLSNET-45432|Undantag förekommer vid öppning av 0c29bc12429844fe983c2a152fa9b744.xlsb|Undantag|
|CELLSNET-45431|Undantag förekommer vid öppning av 000bc1ec5fda4528a18f267f4dfe4a98.xlsb|Undantag|
|CELLSNET-45430|Undantag inträffar vid öppning misslyckades_till_sparat_i_xlsb_type.xlsx|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till metoderna GlobalizationSettings.GetBooleanValueString()/GetErrorValueString()**
Hämtar anpassat visningssträngvärde för cellens booleska värde och felvärde vid formatering/rendering.
#### **Tar bort föråldrad ValidationCollection.Add() metod**
Använd metoden ValidationCollection.Add(CellArea) istället.
#### **Lägger till egenskapen PdfSaveOptions.CheckWorkbookDefaultFont**
Indikerar om man ska försöka använda arbetsbokens standardteckensnitt först för att visa tecknen vilket teckensnitt som inte är korrekt inställt.
#### **Lägger till egenskapen ImageOrPrintOptions.CheckWorkbookDefaultFont**
Indikerar om man ska försöka använda arbetsbokens standardteckensnitt först för att visa tecknen vilket teckensnitt som inte är korrekt inställt.
#### **Lägger till FileFormatType.Numbers, LoadFormat.Numbers och SaveFormat.Numbers enum**
Representerar Numbers-kalkylarksfilformatet av Apple Inc/.
#### **Lägger till metoden Worksheet.AdvancedFilter().**
Filtrerar data med hjälp av komplexa kriterier.
#### **Lägger till egenskapen WorkbookSettings.SignificantDigits**
Hämtar och ställer in antalet signifikanta siffror.
#### **Föråldrar egenskapen Validation.AreaList och lägger till egenskapen Validation.Areas**
Hämtar allt område som innehåller datavalideringsinställningarna.
#### **Lägger till egenskapen PageSetup.IsAutomaticPaperSize**
Indikerar om pappersstorleken är automatisk.
#### **Lägger till metoden FontSettingCollection.Replace().**
Ersätter formens text.
#### **Lägger till Cells.importResultSet(ResultSet rs, int rowIndex, int columnIndex, ImportTableOptions options)/Cells.importResultSet(ResultSet rs, String startCell, ImportTableOptions options) (endast for Java)**
Stöder import av ResultSet med fler alternativ.
#### **Lägger till egenskapen GridWorksheet.CustomColumnCaption**
Hämtar eller ställer in den anpassade kolumntexten för kalkylbladet - Aspose.Cells.GridDesktop.
#### **Lägger till egenskapen GridWorksheet.CustomRowCaption**
Hämtar eller ställer in den anpassade radtexten för kalkylbladet - Aspose.Cells.GridDesktop.
#### **Lägger till metoden GridDesktop.GetVersion().**
Hämta releaseversionen.
#### **Lägger till funktionen GridWebInstance.resize() i GridWeb-klienten js, (GridWebInstance är kontrollobjektet GridWeb)**
Gör att GridWeb-kontrollen är kompatibel med aktuell webbläsarfönsterstorlek.


#### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Läs Numbers-kalkylblad Utvecklat av Apple Inc. med Aspose.Cells](/cells/sv/net/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Ställ in egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions att ha prioritet](/cells/sv/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Använd avancerat filter av Microsoft Excel för att visa poster som uppfyller komplexa kriterier](/cells/sv/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Implementera fel och booleskt värde på ryska eller något annat språk](/cells/sv/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/)
- [Bestäm om arbetsbladets pappersstorlek är Automatisk](/cells/sv/net/determine-if-paper-size-of-worksheet-is-automatic/)
- [Rendera pivottabell i GridDesktop](/cells/sv/net/render-pivottable-in-griddesktop/)
- [Anpassad rad och anpassad kolumntext av GridDesktop-arbetsblad](/cells/sv/net/custom-row-and-custom-column-caption-of-griddesktop-worksheet/)
- [Hitta GridDesktop-versionen vid RunTime](/cells/sv/net/find-griddesktop-version-at-runtime/)
- [Ändra storlek på GridWeb i webbläsarfönstret](/cells/sv/net/resize-gridweb-in-the-browser-window/)
