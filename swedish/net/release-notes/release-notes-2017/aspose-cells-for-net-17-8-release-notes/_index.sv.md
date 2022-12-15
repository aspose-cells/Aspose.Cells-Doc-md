---
title: Aspose.Cells for .NET 17.8 Release Notes
type: docs
weight: 50
url: /sv/net/aspose-cells-for-net-17-8-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 17.8](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-17.8/).

{{% /alert %}} 

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSNET-45357 |Möjlighet att inaktivera nednivåavslöjad typ av villkorliga kommentarer under export till HTML|Ny funktion|
|CELLSNET-45330 |Återge kommentarer när du sparar som bild, HTML eller PDF|Ny funktion|
|CELLSNET-45014 |Stöd style.xml i diagrammet sedan office 2013|Ny funktion|
|CELLSNET-45501 |Ställ in standardstil för GridDesktop liknande Aspose.Cells.Workbook.DefaultStyle både på Design Time och Run Time|Ny funktion|
|CELLSNET-44243 |Hoppa över låsta celler när du navigerar med Tab on GridDesktop-komponenten|Ny funktion|
|CELLSNET-45517 |Lägg till stöd för Share xlsx-fil|Förbättring|
|CELLSNET-45554 |Synkronisera eller uppdatera kommentaren på klientsidan efter Cell Kommentaren har uppdaterats på serversidan|Förbättring|
|CELLSNET-45530 |MS Excel förbrukar mer minne (ca 2 GB) för att öppna utdatafilen|Prestanda|
|CELLSNET-45531 |Positionen för formtexten är fel i utdata-PDF - Excel till PDF-konvertering|Insekt|
|CELLSNET-45507 |Diagram inte korrekt återgivna i Output Pdf|Insekt|
|CELLSNET-45477 |Problem med att rendera former i omvandling av ark till bild|Insekt|
|CELLSNET-45473 |Problem med textjustering när du sparar en XLS-fil som HTML av Aspose.Cells API:er|Insekt|
|CELLSNET-45536 |Text klipps ut när Excel-ark renderas till bild|Insekt|
|CELLSNET-45524 |Redundant linje uppträdde vid rendering av former i omvandling av ark till bild|Insekt|
|CELLSNET-45522 |Cells till PDF - sidfoten radbryts inte när sidfoten innehåller|Insekt|
|CELLSNET-45512 |Aspose.Cells skapar en massiv EMF-fil vid rendering av ark till bildfil|Insekt|
|CELLSNET-45508 |Data trunkeras även efter autopassningsrader|Insekt|
|CELLSNET-45495 |Lägg till digitala signaturer till redan signerade dokument|Insekt|
|CELLSNET-45553 |Diagram i resulterande PDF har oväntade värden|Insekt|
|CELLSNET-45551 |Bilden blir svart när den renderas till PDF-filformat|Insekt|
|CELLSNET-45547 |Sparklines är inte jämnare i den utgående EMF-bilden|Insekt|
|CELLSNET-45514 |ErrorBar caps renderas inte korrekt|Insekt|
|CELLSNET-45398 |Sekundäraxeltitel i diagram renderades felaktigt|Insekt|
|CELLSNET-45570 |Excel-filen är korrupt på grund av datavalideringsintervall efter att ha öppnats och åter sparats via Aspose.Cells API:er|Insekt|
|CELLSNET-45560 |Felmeddelande visas i Microsoft Excel efter anrop av metoden RemoveMacro().|Insekt|
|CELLSNET-45555 |Cells.GroupRows isHidden-attributet visas felaktigt med kapslade grupper|Insekt|
|CELLSNET-45552 |Länkade bilder dupliceras i diagrammet när du öppnar och sparar en XLSX-fil|Insekt|
|CELLSNET-45549 |Utdata XLS-fil är korrupt när du öppnar och sparar Source Xls-filen|Insekt|
|CELLSNET-45548 |SpreadsheetML AllowFilter-elementet fungerar inte i utdata XLSX|Insekt|
|CELLSNET-45546 |Saknade celldata när ODS-fil öppnas och sparas|Insekt|
|CELLSNET-45544 |När intervallet flyttas hänvisar formeln bara till den första cellen i intervallet|Insekt|
|CELLSNET-45543 |Om du flyttar villkorligt formaterade celler tas formateringen bort|Insekt|
|CELLSNET-45541 |H7 i space.xlsx - mellanslag visas inte|Insekt|
|CELLSNET-45540 |H9-värde i ref.xlsx ändras vid sparande|Insekt|
|CELLSNET-45534 |Workbook.Unprotect-metoden fungerar även med fel lösenord|Insekt|
|CELLSNET-45532 |Tillåt heltalsdatavalidering med formeln som inte fungerar|Insekt|
|CELLSNET-45529 |ListObject.Resize ändrar format och ställer in filter|Insekt|
|CELLSNET-45520 |Kommentarsfält är inte korrekt öppnade från SpreadsheetML|Insekt|
|CELLSNET-45518 |Datavalidering i den utgående Excel-filen fungerar inte|Insekt|
|CELLSNET-45509 |Inbäddade objekt/bilder renderas inte i Excel till PDF-konvertering|Insekt|
|CELLSNET-45505 |Vissa former förskjuts i XLS-filen när bilder extraheras och infogas igen|Insekt|
|CELLSNET-45504 |Ledande citattecken saknas i xlsx-filen|Insekt|
|CELLSNET-45502 |Duplicering av arbetsbok genererar skadad fil för Excel 2016/2007|Insekt|
|CELLSNET-45527 |Genom att tillämpa grupprader på dolda rader (i fryst fönster) blir GridWeb oredigerbar|Insekt|
|CELLSNET-45523 |Vissa dolda rader visas felaktigt i GridDesktop|Insekt|
|CELLSNET-45472 |Undantag: "Shape to image Error" vid rendering av en XLSX-fil till PDF-filformat|Undantag|
|CELLSNET-45550 |System.NullReferenceException när du öppnar källfilen i Excel|Undantag|
|CELLSNET-45526 |Undantag när du sparar XLSX-filer till XLSB-filformat|Undantag|
|CELLSNET-45519 |Undantag för att öppna mallen XLSB-fil (Office 365 (1707-uppdatering))|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
## **Lägger till egenskapen HtmlSaveOptions.IsExportComments**
Indikerar om du exporterar kommentarer när du sparar fil till html, standardvärdet är falskt.
## **Lägger till egenskapen HtmlSaveOptions.DisableDownlevelRevealedComments**
Indikerar om inaktivera Downlevel-avslöjade villkorliga kommentarer vid export av fil till html, standardvärdet är false.
## **Lägger till klassen CustomImplementationFactory**
Ger API för användaren att utöka/förbättra komponentens förmåga med några speciella implementeringar för vissa speciella situationer. Till exempel, när det finns tillräckligt med minne på systemet men förmodligen inte tillräckligt med angränsande minne för att bearbeta stora filer, kan användaren använda RecyclableMemoryStream istället för MemoryStream för att undvika System.OutOfMemoryException.
## **Lägger till egenskapen CellsHelper.CustomImplementationFactory**
Hämtar/ställer in CustomImplementationFactory-instansen som används av cells-komponenten.
## **Lägger till metoden Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**
Lägger till digital signatur till en redan signerad OOXML-kalkylbladsfil (Excel2007 och senare).
## **Lägger till egenskapen ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**
Indikerar om en tom sida ska matas ut när det inte finns något att skriva ut.
## **Lägger till metoden GridCell.CreateComment**
Skapar ett kommentarsobjekt för en cell.
## **Lägger till metoden GridCell.RemoveComment**
Tar bort kommentarobjektet från cellen.
## **Lägger till GridCell.GetComment-metoden**
Hämtar kommentarobjekt på denna cell.
## **Lägger till egenskapen GridDesktop.DefaultCellFont**
Hämtar eller ställer in standardteckensnittet för cellen.
## **Lägger till egenskapen GridDesktop.DefaultCellFontColor**
Hämtar eller ställer in standardteckensnittsfärgen för cellen.
## **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Lägg till digital signatur i en redan signerad Excel-fil](/cells/sv/net/add-digital-signature-to-an-already-signed-excel-file/)
- [Inaktivera Downlevel Revealed Comments medan du sparar till HTML](/cells/sv/net/disable-downlevel-revealed-comments-while-saving-to/)
- [Exportera kommentarer medan du sparar Excel-fil till HTML](/cells/sv/net/export-comments-while-saving-excel-file-to/)
- [Skriv ut tom sida när det inte finns något att skriva ut](/cells/sv/net/output-blank-page-when-there-is-nothing-to-print/)
- [Använder CustomImplementationFactory för att skapa anpassad implementering av Memory Stream](/cells/sv/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/)
- [Skapa Ta bort och få GridCell-kommentarer](/cells/sv/net/create-remove-and-get-gridcell-comments/)
- [Standardteckensnitt och teckensnittsfärg för GridDesktop](/cells/sv/net/default-font-and-font-color-of-the-griddesktop/)
