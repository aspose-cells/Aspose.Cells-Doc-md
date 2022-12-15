---
title: Aspose.Cells for .NET 8.8.1 Release Notes
type: docs
weight: 100
url: /sv/net/aspose-cells-for-net-8-8-1-release-notes/
---
### **1) Aspose.Cells**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSNET-41817 | Ställer in texteffekt på Offset i rektangelform| Ny funktion|
|CELLSNET-44407 | Kanttjockleken minskas under renderingen när utskriftsområdet passerar genom cellerna som delar ram| Förbättring|
|CELLSNET-44413 | Gör standardvärdet för WorkbookSettings.IsDefaultEncrypted som falskt| Förbättring|
|CELLSNET-44392 | Aspose.Cells.xml saknas i mappen ".\Bin\net4.0"| Förbättring|
|CELLSNET-44291 | Optimera koden för att göra dolda tomma kolumner och rader mer effektiva| Förbättring|
|CELLSNET-44417 | API hänger sig när ett skadat och infekterat kalkylark konverteras till PDF| Prestanda|
|CELLSNET-44088 | Ikoner för reglerna för villkorlig formatering återges inte till HTML| Insekt|
|CELLSNET-44263 | Formatering går förlorad när HTML importeras som XLSX| Insekt|
|CELLSNET-44427 | Datum i ISO 8601-format behandlas som strängar istället för datum| Insekt|
|CELLSNET-44414 | Problem med stora bilder vid konvertering från Excel till PDF| Insekt|
|CELLSNET-44341 | Fel radhöjder med AutoFitRows med alternativet AutoFitMergedCells på för kinesiska och engelska ord i cellerna| Insekt|
|CELLSNET-44309 |Parentes visas inte roterad i utdata-PDF (Excel till PDF-konvertering)| Insekt|
|CELLSNET-44302 | SheetRender.ToImage återger inte cellkanten| Insekt|
|CELLSNET-43237 | Vertikala symboler återges inte korrekt när kalkylblad konverteras till PDF| Insekt|
|CELLSNET-41907 | En del vertikal text kan fortfarande inte visas korrekt i den konverterade PDF-filen| Insekt|
|CELLSNET-44405 | Diagrambilden har serien "Din organisation" på 0 % även om den är inställd på 50 %| Insekt|
|CELLSNET-44404 | Metoden Worksheet.Copy kopierar inte diagram korrekt| Insekt|
|CELLSNET-44398 | EMF-rendering av diagram fungerar inte korrekt i nyare version| Insekt|
|CELLSNET-44397 | Återgivning av diagram till bild - Text (dataetiketter) är mer fet än i det ursprungliga diagrammet| Insekt|
|CELLSNET-44387 | Bild genererad med Chart.ToImage är felaktig| Insekt|
|CELLSNET-44365 | En del av dataseriens etikett saknas för specifikt diagram genererat som bild med aspose.cells| Insekt|
|CELLSNET-44426 |Inställning av ImportOptions.ConvertNumericData = true resulterar i värden med '<' or '> siffran visas inte| Insekt|
|CELLSNET-44408 | Problem med rullgardins-/listposter för datavalidering som innehåller ett kommatecken| Insekt|
|CELLSNET-44403 |Bakgrundsvattenstämpel tas bort medan XLS sparas till XLSX| Insekt|
|CELLSNET-44402 | ExternalLink returnerade fel DataSource med utökad sökväg| Insekt|
|CELLSNET-44394 | Smart Marker-gruppering är bruten i nyare version| Insekt|
|CELLSNET-44390 | Problem med gruppattributet för smarta markörer - All data bearbetas inte| Insekt|
|CELLSNET-44388 | Namngivna celler på olika kalkylblad skadar arbetsboken| Insekt|
|CELLSNET-44379 | Diagrametiketter försvinner efter att kalkylarket har sparats på nytt| Insekt|
|CELLSNET-44329 | Olika sparade pdf-filstorlekar för valda eller ej valda celler i Excel-filen| Insekt|
|CELLSNET-44400 | Text beskärs när diagrammarkeringen är lång medan kalkylbladet renderas till bild| Insekt|
|CELLSNET-44401 | Roterad textruta är felplacerad när kalkylblad renderas till bild| Insekt|
|CELLSNET-44420 | Det gick inte att öppna Excel2003XML-filen i Aspose.Cells| Undantag|
|CELLSNET-44393 | System.ArgumentOutOfRangeException med sammanfogad Aspose.Cells Assembly med ILMerge| Undantag|
|CELLSNET-44389 | System.FormatException: Inmatningssträngen var inte i korrekt format, på WorkbookDesigner.Process| Undantag|
### **2) Aspose.Cells Grid Suite**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSNET-42313 | Stöd för läsning av datavalidering i Excel-fil - Aspose.Cells.GridDesktop| Ny funktion|
|CELLSNET-44267 |Problem med lat laddning när du ställer in EnableAsync-attributet när du rullar i GridWeb-kontrollen| Förbättring|
|CELLSNET-41793 | Nedåtpilen fungerar inte korrekt efter cellsammanslagning| Förbättring|
|CELLSNET-44424 | Välj markering är inte korrekt i GridWeb| Insekt|
|CELLSNET-44364 | Formateringen av cellen ändras efter att ha klickat på cellen på GridWeb| Insekt|
|CELLSNET-44343 | GridDesktop visar inte rullgardinsmenyn när kalkylbladet laddas| Insekt|
|CELLSNET-44409 | Undantag vid import av en Excel-fil till GridWeb| Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till egenskapen WorkbookSettings.PaperSize.**
Den används för att ställa in pappersstorleken för standardskrivaren som standardpappersstorlek för arbetsboken.
#### **Lägger till klassen LoadDataFilterOptions och egenskapen LoadOptions.LoadDataFilterOptions.**
Den används för att specificera vilken typ av data som ska laddas när man bygger arbetsboken från mallfilen. Filtrering av laddad data kan förbättra prestandan för användarens speciella syfte, särskilt när du använder LightCells API:er.
#### **Lägger till Worksheet.CalculateFormula(strängformel, CalculationOptions opts) metod.**
Den används för att beräkna given formel direkt med användaranpassade alternativ.
#### **Lägger till klasser av namnutrymme Aspose.Cells.Drawing.Texts.**
Den används för att ställa in egenskaperna för formens textteckensnitt.
#### **Föråldrad Shape.TextFrame-egenskap.**
Använd egenskapen Shape.TextBody.TextAlignment istället.
#### **Lägger till egenskapen Shape.TextBody.**
Presenterar inställningen av formens text.
#### **Lägger till metoden GridCell.CreateValidation(GridValidationType validationType, bool isRequired).**
Skapar ett valideringsobjekt för en rutnätscell.
#### **Lägger till metoden GridCell.RemoveValidation().**
Tar bort valideringsobjektet från en rutnätscell.
#### **Lägger till metoden Chart.ToPdf (System.IO.Stream stream).**
Lägger till spardiagram till PDF som en ström.
