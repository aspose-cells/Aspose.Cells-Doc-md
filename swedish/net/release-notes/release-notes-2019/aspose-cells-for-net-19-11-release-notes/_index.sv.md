---
title: Aspose.Cells for .NET 19.11 Release Notes
type: docs
weight: 20
url: /sv/net/aspose-cells-for-net-19-11-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 19.11](https://www.nuget.org/packages/Aspose.Cells/19.11.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-44956|Stöd för att dölja valda intervall och sortera de visade resultaten av pivottabellen|Ny funktion|
|CELLSNET-46852|Stöd läs- och skrivtabell vars datakälla är en frågetabell i filen XLS.|Ny funktion|
|CELLSNET-46967|Stöd för att få indragsstorlek i pixelenhet|Ny funktion|
|CELLSNET-46973|Excel-formeln fungerar inte i den genererade XLS-filen|Förbättring|
|CELLSNET-46981|Stöd för att läsa/skriva med minnesström för Workbook.ImportXml och Workbook.ExportXml|Förbättring|
|CELLSNET-46905|Inga ändringar för länkkälla sparade i filen XLS|Förbättring|
|CELLSNET-46898|Bakgrunden för 3D-modellen blir blå|Insekt|
|CELLSNET-46314|Problem vid uppdatering av pivottabell med "Visa värde som % av totalsumman"|Insekt|
|CELLSNET-46789|CalculateData-metoden fungerar inte korrekt med formatet PDF|Insekt|
|CELLSNET-46955|HTML till Excel-fil väcker undantag "Artikel har redan lagts till"|Insekt|
|CELLSNET-46987|Det går inte att beräkna formeln när man refererar till celler|Insekt|
|CELLSNET-46968|Den indirekta formeln fungerar inte korrekt i MS Excel|Insekt|
|CELLSNET-46991|XLSX-filen är skadad.|Insekt|
|CELLSNET-46994|# Värde! i Excel-utdatafilen (öppnad i Excel 365) efter att ha anropat Calculate Formula
|Insekt|
|CELLSNET-47001|CalculateFormula() orsakar NullReferenceException|Insekt|
|CELLSNET-46953|Innehållet skärs vid utskrift|Insekt|
|CELLSNET-46966|Höger kant saknas när Horizontal Alignment är inställt på Fyll|Insekt|
|CELLSNET-45362|Alternativ för kakelbilder fungerar inte för diagrambakgrunder i XLS-filer|Insekt|
|CELLSNET-46949|OLE-objekt blir bilder vid kopiering av arbetsblad|Insekt|
|CELLSNET-46963|Diagrametiketter förlorar formatering efter att ha sparat Excel-fil|Insekt|
|CELLSNET-46965|Att anropa Chart.Calculate() på ett tomt diagram som har en tom autotexttitel ger ett fel|Insekt|
|CELLSNET-46971|Det nyligen kopierade arket döljer alla dolda kolumner och återställer även kolumnbredden|Insekt|
|CELLSNET-46972|Komma tas bort från diagramtitlar när Excel-filen är dekrypterad|Insekt|
|CELLSNET-46912|StackOverflowException kastades vid konvertering av XLSX till HTML|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till metoder: Validation.AddArea(CellArea,bool,bool),AddAreas(CellArea[], bool, bool),RemoveAreas(CellArea[])**
Lägger till/tar bort valideringsinställningar från givna områden med hänsyn till prestanda.
#### **Lägger till metoden Workbook.ImportXml (Stream stream, string sheetName, int row, int col).**
Importerar en XML-filström till arbetsboken.
#### **Lägger till metoden Workbook.ExportXml (sträng mapName, Stream stream).**
Exportera XML-data till en ström.
#### **Lägger till egenskapen HtmlSaveOptions.ExportArea**
Hämtar eller ställer in den exporterande CellArea för det aktuella aktiva arbetsbladet. Om du ställer in det här attributet kommer utskriftsområdet för det aktuella aktiva arbetsbladet att utelämnas. Endast det angivna området kommer att exporteras när filen sparas till HTML.
#### **Lägger till klasser: DataMashup,PowerQueryFormula,PowerQueryFormulaCollection,PowerQueryFormulaItem och PowerQueryFormulaItemCollection**
Får information i DataMashup.
#### **Lägger till egenskapen DBConnection.SeverCommand.**
Hämtar och ställer in en andra kommandotextsträng som kvarstår när PivotTable-serverbaserade sidfält används.
#### **Lägger till metoden CellsHelper.GetTextWidth().**
Hämtar textens bredd i punktenheten.
