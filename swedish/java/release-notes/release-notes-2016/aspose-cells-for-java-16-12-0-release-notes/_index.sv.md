---
title: Aspose.Cells for Java 16.12.0 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-java-16-12-0-release-notes/
---
|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSJAVA-42043 | Ange kartpunkters positioner| Ny funktion|
|CELLSJAVA-42073 |XLSM blir skadad efter att ha sparat på nytt| Insekt|
|CELLSJAVA-42060 | DataBar-bredden är inte korrekt vid konvertering av kalkylblad till HTML| Insekt|
|CELLSJAVA-42016 | Orange Row ingår inte i SUM of Pivot Table| Insekt|
|CELLSJAVA-42006 | Bilden är avskuren i utdata-HTML| Insekt|
|CELLSJAVA-42067 | Diagram saknas vid konvertering av kalkylark till HTML| Insekt|
|CELLSJAVA-41983 | Radhöjden är inte korrekt vid konvertering av XLSX till HTML| Insekt|
|CELLSJAVA-42089 | DCOUNTA Excel-formel utvärderas inte bra av Aspose.Cells formelberäkningsmotor| Insekt|
|CELLSJAVA-42081 | Problem med DataBar villkorlig formatering när du sparar en XLSM-fil som PDF| Insekt|
|CELLSJAVA-42100 | Mellanrummet mellan vissa tecken tas bort på några ställen i utdata-PDF-filen| Insekt|
|CELLSJAVA-42078 | Diagrametiketter visas/renderas inte på samma sätt (som i den ursprungliga Excel-filen) i den utgående PDF-filen| Insekt|
|CELLSJAVA-42077 | Problem med teckensnittsattribut för TextBox i utdata-PDF| Insekt|
|CELLSJAVA-42064 | TextBox innehållsfärg och storlek ändras när kalkylbladet konverteras till EMF| Insekt|
|CELLSJAVA-42063 | TextBox innehålls färg och storlek ändras när kalkylblad konverteras till PDF| Insekt|
|CELLSJAVA-42059 |Hebreiska ord återges inte korrekt när en Excel-fil konverteras till PDF-filformat| Insekt|
|CELLSJAVA-42053 | Innehåll i TextBox klipps bort medan kalkylblad renderas till PDF| Insekt|
|CELLSJAVA-42052 | Pillinjer är felplacerade när kalkylblad renderas till PDF| Insekt|
|CELLSJAVA-42049 | Problem med SVG-bilden av diagrammet i den renderade HTML-filen| Insekt|
|CELLSJAVA-42036 | Teckensnittsersättning verkar inte träda i kraft för diagramförklaring när du använder Chart.toPdf()| Insekt|
|CELLSJAVA-42024 | Förklaring som överlappar med text i diagrammets PDF| Insekt|
|CELLSJAVA-42070 | Felaktiga ChartPoints ShapeXPx- och ShapeYPx-värden| Insekt|
|CELLSJAVA-42083 | Ofullständig rendering av rektangelformen vid konvertering av XLS till HTML| Insekt|
|CELLSJAVA-42104 | Texten trunkeras när kalkylark konverteras till PDF-filformat| Insekt|
|CELLSJAVA-42098 | Extra sidor läggs till på grund av att vissa sidor inte renderas helt på en PDF-sida| Insekt|
|CELLSJAVA-42097 | SheetRender - Ogiltigt kolumnindex| Insekt|
|CELLSJAVA-42093 | Om du utökar Excel-tabellen ändras data| Insekt|
|CELLSJAVA-42092 | Om du öppnar och sparar filen medan du använder SheetRender förstörs den utgående Excel-filen| Insekt|
|CELLSJAVA-42085 | Om du ställer in formtexten ändras textstilen| Insekt|
|CELLSJAVA-42074 |Texten i vissa celler som C2 och C3 får inte fetstil| Insekt|
|CELLSJAVA-42058 | Metoden Worksheet.autoFitColumns verkar inte träda i kraft när det önskade teckensnittet inte finns i Linux| Insekt|
|CELLSJAVA-42054 | Oväntad bakgrundsfärg applicerades på TextBoxes när kalkylblad renderades till PDF| Insekt|
|CELLSJAVA-42072 | java.lang.ArrayIndexOutOfBoundsException vid Workbook.calculateFormula(false)| Undantag|
|CELLSJAVA-42066 | CellsException på Workbook.save när du konverterar en XLS till PDF| Undantag|
|CELLSJAVA-42101 | Ogiltigt formelundantag när Excel-filen öppnades| Undantag|
|CELLSJAVA-42080 | Undantag för att spara arbetsboken| Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till egenskaperna BuiltInDocumentPropertyCollection.ScaleCrop och BuiltInDocumentPropertyCollection.LinksUpToDate**
Hämtar och ställer in några inbyggda dokumentegenskaper.
### **Tar bort föråldrad DataLabels.Rotation-egenskap**
Använd egenskapen DataLabels.RotationAngle istället.
### **Tar bort föråldrad Title.Rotation-egenskap**
Använd egenskapen Title.RotationAngle istället.
### **Tar bort föråldrad DataLabels.Background-egenskap**
Använd egenskapen DataLabels.BackgroundMode istället.
### **Tar bort föråldrad DisplayUnitLabel.Rotation-egenskap**
Använd egenskapen DisplayUnitLabel.RotationAngle istället.
### **Tar bort föråldrad Title.getCharacters()-metod**
Använd metoden Title.characters() istället.
### **Lägger till LoadFilter-klassen och LoadOptions.LoadFilter-egenskapen**
Tillåter användaren att styra vilken data som ska laddas när en arbetsbok laddas från mallfilen.
### **Föråldrade egenskapen LoadOptions.LoadDataFilterOptions**
Använd egenskapen LoadOptions.LoadFilter istället. Exempel: LoadOptions.LoadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.Chart);
### **Föråldrade egenskapen LoadOptions.OnlyLoadDocumentProperties**
Använd egenskapen LoadOptions.LoadFilter istället. Användning: LoadOptions.LoadFilter = new LoadFilter(LoadDataFilterOptions.DocumentProperties);
### **Föråldrade LoadOptions.LoadDataAndFormatting-egenskapen**
Använd egenskapen LoadOptions.LoadFilter istället. Användning: LoadOptions.LoadFilter = new LoadFilter(LoadDataFilterOptions.CellData);
### **Föråldrade egenskapen LoadOptions.LoadDataOptions**
Använd LoadFilter-egenskapen istället, användaren kan utöka LoadFilter för att filtrera kalkylbladet och data.
### **Lägger till Workbook.ExportXml-metoden (sträng mapName, string path).**
Exportera XML-data.
### **Lägger till enum FileFormatType.OTS**
Representerar OTS-filformatet.
### **Lägger till metoden WorksheetCollection.CreateRange().**
Skapar ett intervall.
### **Lägger till egenskapen FontConfigs.PreferSystemFontSubstitutes**
Ange om du ska använda systemteckensnittsersättning först eller inte när ett teckensnitt inte visas och ersättningen för detta teckensnitt inte är inställd.
