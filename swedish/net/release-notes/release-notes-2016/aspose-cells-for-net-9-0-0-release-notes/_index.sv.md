---
title: Aspose.Cells for .NET 9.0.0 Release Notes
type: docs
weight: 40
url: /sv/net/aspose-cells-for-net-9-0-0-release-notes/
---
### **1) Aspose.Cells**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSNET-40617 | Läs/skriv värden från/till ActiveX ComboBox-kontroll| Ny funktion|
|CELLSNET-41264 | Använder Aspose.Cells.GridDesktop i WPF-applikation| Ny funktion|
|CELLSNET-44681 | Import av HTML misslyckas när skripttaggen använder CDATA| Förbättring|
|CELLSNET-44693 | Innehåll saknas vid konvertering av HTML till XLSX| Insekt|
|CELLSNET-44650 | Det går inte att konvertera bakgrunds- eller förgrundsfärger från HTML| Insekt|
|CELLSNET-44645 | Felmeddelande visas när du dubbelklickar på valfritt värde i pivottabellen i utdatafilen| Insekt|
|CELLSNET-44644 |Den resulterande filen blir skadad när filen XLS öppnas och sparas| Insekt|
|CELLSNET-44622 | Slutlig XLSX-fil saknar bildtextstilar medan dessa finns i indata XLSX och mellanliggande HTML| Insekt|
|CELLSNET-44581 | Problem med konvertering av kalkylark till HTML: STYLE-tagg mellan BODY- och HTML-taggar| Insekt|
|CELLSNET-44718 |ICustomFunction fungerar inte med [@columnName]| Insekt|
|CELLSNET-44705 | Fel SUMMA visas vid beräkning av formler| Insekt|
|CELLSNET-44692 | API beräknar felaktigt formelvärdet jämfört med MS Excel| Insekt|
|CELLSNET-44688 | Fel beräkning av cellvärdet| Insekt|
|CELLSNET-44684 | Fel värde från cell vid beräkning av formler| Insekt|
|CELLSNET-44716 | Resultatet PDF matchar inte Excel för utskrift av rubrikrader| Insekt|
|CELLSNET-44713 | Data är gömd i konverteringsresultatet för PDF| Insekt|
|CELLSNET-44675 | Återgivning till bildfil misslyckas för ett kalkylblad| Insekt|
|CELLSNET-44717 | Kalkylblad till XPS: Processen slutförs aldrig och tar för mycket minne| Insekt|
|CELLSNET-44678 | Sparklines renderas inte rätt när kalkylarket renderas till PDF/bild| Insekt|
|CELLSNET-44654 | Metoden Chart.Calculate() förstör diagrambilden| Insekt|
|CELLSNET-44714 |När du sparar till minnesström (SpreadsheetML), hängs processen och tar mycket tid| Insekt|
|CELLSNET-44711 | Att visa raden dold av Aspose.Cells fungerar inte korrekt i Microsoft Excel| Insekt|
|CELLSNET-44709 | Bildformeln är borta efter att bilden tagits bort och satts in igen| Insekt|
|CELLSNET-44708 | Om du bäddar in presentationsbilden på nytt i XLS får du presentationsvy när du dubbelklickar| Insekt|
|CELLSNET-44696 | Linje med pilhuvud renderas inte helt i formaten XLSX och PDF| Insekt|
|CELLSNET-44689 | Skrivarinställningarna ändras när källfilen XLS öppnas och sparas på nytt| Insekt|
|CELLSNET-44683 | "panel" xml inom "customSheetView" xml replikeras inte från designerkalkylark| Insekt|
|CELLSNET-44660 | Y- och X-axeln i grafen blir fet efter att ha laddat och sparat en XLS-fil| Insekt|
|CELLSNET-44658 | Textstorleken på diagrammets vertikala axeletiketter ändras efter att XLS-filen laddats och sparats| Insekt|
|CELLSNET-44691 | NullReferenceException på Workbook ctor på grund av display:none i källan HTML| Undantag|
|CELLSNET-44685 | Metoden Workbook.CalculateFormula() kastar undantag på källfilen i Excel| Undantag|
|CELLSNET-44712 | Undantag: "Ogiltig text för det definierade namnet." när du öppnar en Excel-fil| Undantag|
### **2) Aspose.Cells Grid Suite**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSNET-44667 |Cell skuggning på grund av villkorlig formatering visas inte på GridWeb-gränssnittet| Insekt|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till egenskapen Shape.TextOptions**
Representerar formens textalternativ.
#### **Obsoletes Worksheet.SetBackground-metod**
Använd egenskapen Worksheet.BackgroundImage istället.
#### **Föråldrade LineShape.BeginArrowheadStyle och ArcShape.BeginArrowheadStyle**
Använd egenskapen Shape.Line.BeginArrowheadStyle istället.
#### **Föråldrade LineShape.BeginArrowheadWidth och ArcShape.BeginArrowheadWidth**
Använd egenskapen Shape.Line.BeginArrowheadWidth istället.
#### **Föråldrade LineShape.BeginArrowheadLength och ArcShape.BeginArrowheadLength**
Använd egenskapen Shape.Line.BeginArrowheadLength istället.
#### **Föråldrade LineShape.EndArrowheadStyle och ArcShape.EndArrowheadStyle**
Använd egenskapen Shape.Line.EndArrowheadStyle istället.
#### **Föråldrade LineShape.EndArrowheadWidth och ArcShape.EndArrowheadWidth**
Använd egenskapen Shape.Line.EndArrowheadWidth istället.
#### **Föråldrade LineShape.EndArrowheadLength och ArcShape.EndArrowheadLength**
Använd egenskapen Shape.Line.EndArrowheadLength istället.
#### **Tar bort föråldrad Worksheet.CopyConditionalFormatting()-metod**
#### **Tar bort föråldrad Workbook.CheckWriteProtectedPassword()-metod**
Använd metoden WorkbookSettings.WriteProtection.ValidatePassword istället.
#### **Byter namn på Workbook.RemoveDigitalSign som Workbook.RemoveDigitalSignature-metod**
Metoden Workbook.RemoveDigitalSign har bytt namn till Workbook.RemoveDigitalSignature.
#### **Lägger till egenskapen ChartSplitType.Auto**
Representerar att datapunkterna ska delas med standardmekanismen för denna diagramtyp.
#### **Lägger till egenskapen ChartPoint.IsInSecondaryPlot**
Hämtar eller ställer in ett värde indikerar om dessa datapunkter finns i den andra cirkeln eller stapeln på en cirkel- eller stapeldiagram.
#### **Lägger till egenskapen OleObject.ClassIdentifier**
Hämtar eller ställer in klassidentifieraren för det inbäddade objektet.
#### **Lägger till egenskapen LoadOptions.CultureInfo**
Hämtar eller ställer in systemkulturinformationen vid den tidpunkt då filen laddades.
