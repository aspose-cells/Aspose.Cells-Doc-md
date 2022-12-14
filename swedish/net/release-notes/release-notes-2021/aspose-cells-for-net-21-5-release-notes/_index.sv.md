---
title: Aspose.Cells för .NET 21.5 Release Notes
type: docs
weight: 8
url: /sv/net/aspose-cells-for-net-21-5-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 21.5](https://www.nuget.org/packages/Aspose.Cells/21.5.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47964| Stöd bindande Slicer-rapport med pivottabell och pivotdiagram|Ny funktion|
|CELLSNET-48003|Stöd importera gratis html med svg-bild|Ny funktion|
|CELLSNET-47988|Refererar till spillområde med #|Ny funktion|
|CELLSNET-47996|Stöd flytta befintlig kolumn i GridWeb|Ny funktion|
|CELLSNET-48002|Stöd export av alla kalkylblad till .csv-fil.|Ny funktion|
|CELLSNET-47975|ArgumentException på CalculateFormula-metoden|Förbättring|
|CELLSNET-47984|Stöd ELSE-funktionen när du konverterar xls till xlsx|Förbättring|
|CELLSNET-47989| Stöd för inställning av global PageOrientationType|Förbättring|
|CELLSNET-48051|PasteType.Values fungerar endast när den klistras in på annat än källintervallet|Förbättring|
|CELLSNET-47956|Vänta på beräkningsformeln|Prestanda|
|CELLSNET-47982|Ny arbetsbok hänger på ogiltig fil|Prestanda|
|CELLSNET-48012|Förbättra prestanda för läsning av .ods-filer med ett stort antal valideringar.|Prestanda|
|CELLSNET-48039|Oändlig slinga när kopierad arbetsbok sparas|Prestanda|
|CELLSNET-44224|WordArt vattenstämpel återges inte i PDF-filformatet|Insekt|
|CELLSNET-47887|Text inuti formen är felplacerad|Insekt|
|CELLSNET-47920|En del innehåll saknas i HTML till Excel-konvertering|Insekt|
|CELLSNET-47981|Resultatet av att exportera intervall med sammanslagna celler till html är felaktigt|Insekt|
|CELLSNET-47985|Mindre antal rader vid konvertering till html|Insekt|
|CELLSNET-47987|Flytta pivotfältet till sidavsnittet eller pivotfilter|Insekt|
|CELLSNET-47997|Ytterligare kolumner skapas efter att filen har sparats till html|Insekt|
|CELLSNET-48009|Filen är skadad efter att ha sparat arbetsboken med Slicers|Insekt|
|CELLSNET-48036|Utsnittskontroll läggs inte till baserat på sidfilterfältet i pivottabellen|Insekt|
|CELLSNET-48044| Undantag ökar vid läsning av en specifik mhtml-fil|Insekt|
|CELLSNET-47118|Felaktigt värde 'TRUE' hämtat från Cell istället för värdet 'FALSE'|Insekt|
|CELLSNET-48042|Hämtade formaterade cellvärden är felaktiga i Excel-kalkylbladet|Insekt|
|CELLSNET-48031|"Shape to image Error" ökar när xlsx-fil konverteras till html|Insekt|
|CELLSNET-48037|Bilden förvrängs när du sparar till PDF|Insekt|
|CELLSNET-47714|Text i vertikal axel överlappar horisontell axel på diagrammet vid konvertering till EMF|Insekt|
|CELLSNET-47856|XLSX till PDF-konverteringsproblem med pivottabeller|Insekt|
|CELLSNET-47986|Diagram till bild/PDF - fel utdata med vattenfallsdiagramtyp|Insekt|
|CELLSNET-48010|Undantag vid laddning av en Excel 2010 XLSX-filer|Insekt|
|CELLSNET-48020|Formulärkontroller raderas efter Ladda och spara Excel 95 via Aspose.Cells|Insekt|
|CELLSNET-48033|Excel-fil skadad efter att ha laddats och sparats|Insekt|
|CELLSNET-47957| "Shape to image Error" ökar när en Excel-fil konverteras till PDF-filformat|Undantag|
|CELLSNET-48027|Ogiltigt parameterundantag vid konvertering av form till bild|Undantag|
|CELLSNET-48029|"Shape to image Error" höjs|Undantag|
|CELLSNET-48017|Undantaget "Inmatningssträngen var inte i korrekt format" vid import av html-fil|Undantag|
|CELLSNET-48034|Ogiltig teckenstorlek i Mht-fil.|Undantag|
|CELLSNET-47977|Undantag vid analys av formeln '[96]Kostnadsark'!$D$6|Undantag|
|CELLSNET-47979|Objektreferensundantag på Spara-metoden|Undantag|
|CELLSNET-48040|Undantagshöjningar vid konvertering av XLSB till XLSX|Undantag|
|CELLSNET-47980|Ett fel uppstod när en Excel-fil sparades med Aspose.Cells|Undantag|
|CELLSNET-48001|Ogiltigt radindexundantag vid anrop av GetPrintingPageBreaks()|Undantag|
|CELLSNET-48022|Oväntad Border.LineTyp av en cell|Undantag|
|CELLSNET-48032|Undantag när dokument ODS-fil är öppen|Undantag|
|


## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Lägger till Slicer.AddPivotConnection(PivotTable pivot) metod.**

 Lägger till PivotTable-anslutning för slicer.

### **Lägger till Slicer.RemovePivotConnection(PivotTable pivot) metod.**

 
Tar bort PivotTable-anslutning av slicer.

### **Lägger till egenskapen TxtSaveOptions.ExportAllSheets.**

 
 Anger om alla kalkylblad exporteras till filen. Dafaut-värdet är falskt som MS Excel.

### **Lägger till FileFormatType.Numbers09 enum.**

  
Representerar filformatet .numbers 09. Och FileFormatType.Number kommer att representera den senaste.numbers filformattypen senare.

### **Lägger till metoden WorkbookSettings.SetPageOrientationType().**

 
Ställer in utskriftssidans orienteringstyp för hela filen.

### **Tar bort föråldrad DataBarAxisPosition.DataBarAxisAutomatic enum.**

 
Använd DataBarAxisPosition.Automatic enum istället.

### **Tar bort föråldrad DataBarAxisPosition.DataBarAxisMidpointe num.**

 
Använd DataBarAxisPosition.Midpoint enum istället.

### **Tar bort föråldrad DataBarAxisPosition.DataBarAxisNone enum.**

 
 Använd DataBarAxisPosition.None enum istället.

### **Tar bort föråldrade DataBarBorderType.DataBarBorderNone enum.**

 
Använd DataBarBorderType.None enum istället.

### **Tar bort föråldrade DataBarBorderType.DataBarBorderSolid enum.**

 
Använd DataBarBorderType.Solid enum istället.

### **Tar bort föråldrad DataBarFillType.DataBarFillGradient enum.**

 
 Använd DataBarFillType.Gradient enum istället.

### **Tar bort föråldrade DataBarFillType.DataBarFillSolid enum.**

 
Använd DataBarFillType.Solid enum istället.

### **Tar bort föråldrad DataBarNegativeColorType.DataBarColor enum.**

 
Använd DataBarNegativeColorTypeColor enum istället.

### **Tar bort föråldrad DataBarNegativeColorType.DataBarSameAsPositive enum.**

 
 Använd DataBarNegativeColorType.SameAsPositive enum istället.

### **Tar bort föråldrad OleObject.FileFormatType enum.**

 
 Använd OleObject.FileFormatType enum istället.

### **Tar bort föråldrad DynamicFilterType.Februray enum.**

 
Använd DynamicFilterType.Feburay enum istället.

### **Föråldrar FileFormatType.BMP enum och lägger till FileFormatType.Bmp enum.**

 
Använd FileFormatType.Bmp enum istället.

### **Föråldrar FileFormatType.CSV enum och lägger till FileFormatType.Csv enum.**

 
 Använd FileFormatType.Csv enum istället.

### **Föråldrar FileFormatType.TSV enum och lägger till FileFormatType.Tsv enum.**

 
 Använd FileFormatType.Tsv enum istället.

### **Föråldrar FileFormatType.FODS enum och lägger till FileFormatType.Fods enum.**

 Använd FileFormatType.Fods enum istället.

### **Föråldrar FileFormatType.MSEquation enum och lägger till FileFormatType.MsEquation enum.**

 
Använd FileFormatType.MsEquation enum istället.

### **Föråldrar FileFormatType.ODF enum och lägger till FileFormatType.Odf enum.**

 
Använd FileFormatType.Odf enum istället.

### **Föråldrar FileFormatType.ODG enum och lägger till FileFormatType.Odg enum.**

 
 Använd FileFormatType.Odg enum istället.

### **Föråldrar FileFormatType.ODP enum och lägger till FileFormatType.Odp enum.**

 
 Använd FileFormatType.Odp enum istället.

### **Föråldrar FileFormatType.ODS enum och lägger till FileFormatType.Ods enum.**

 
 Använd FileFormatType.Ods enum istället.

### **Föråldrar FileFormatType.ODT enum och lägger till FileFormatType.Odt enum.**

 
 Använd FileFormatType.Odt enum istället.

### **Föråldrar FileFormatType.OTP enum och lägger till FileFormatType.Otp enum.**

 
 Använd FileFormatType.Otp enum istället.

### **Föråldrar FileFormatType.OTS enum och lägger till FileFormatType.Ots enum.**

 
 Använd FileFormatType.Ots enum istället.

### **Föråldrar FileFormatType.OTT enum och lägger till FileFormatType.Ott enum.**

 
 Använd FileFormatType.Ott enum istället.


### **Föråldrar FileFormatType.SVG enum och lägger till FileFormatType.Svg enum.**

 
 Använd FileFormatType.Svg enum istället.

### **Föråldrar FileFormatType.Sxc enum och lägger till FileFormatType.Sxc enum.**

 
 Använd FileFormatType.Sxc enum istället.

### **Föråldrar FileFormatType.TIFF enum och lägger till FileFormatType.Tiff enum.**

 
 Använd FileFormatType.Tiff enum istället.

### **Föråldrar FileFormatType.VSD enum och lägger till FileFormatType.Vsd enum.**

 
 Använd FileFormatType.Vsd enum istället.

### **Föråldrar FileFormatType.VSDX enum och lägger till FileFormatType.Vsdx enum.**

 
 Använd FileFormatType.Vsdx enum istället.


### **Föråldrar FileFormatType.XML enum och lägger till FileFormatType.Xml enum.**

 
 Använd FileFormatType.Xml enum istället.

### **Föråldrar FileFormatType.XPS enum och lägger till FileFormatType.Xps enum.**

 
 Använd FileFormatType.Xps enum istället.

### **Föråldrar FileFormatType.Excel2003XML enum och lägger till FileFormatType.SpreadsheetML enum.**

 
 Använd FileFormatType.SpreadsheetML enum istället.

### **Föråldrar SaveFormat.XPS enum och lägger till SaveFormat.Xps enum.**

 
 Använd SaveFormat.Xps enum istället.

### **Föråldrar SaveFormat.TSV enum och lägger till SaveFormat.Tsv enum.**

 Använd SaveFormat.Tsv enum istället.

### **Föråldrar SaveFormat.TIFF enum och lägger till SaveFormat.Tiff enum.**

 
Använd SaveFormat.Tiff enum istället.

### **Föråldrar SaveFormat.SXC enum och lägger till SaveFormat.Sxc enum.**

Använd SaveFormat.Sxc enum istället.

### **Föråldrar SaveFormat.SVG enum och lägger till SaveFormat.Svg enum.**

 
Använd SaveFormat.Svg enum istället.

### **Föråldrar SaveFormat.ODS enum och lägger till SaveFormat.Ods enum.**

 
 Använd SaveFormat.Ods enum istället.

### **Föråldrar SaveFormat.Fods enum och lägger till SaveFormat.Fods enum.**

 
 Använd SaveFormat.Fods enum istället.

### **Föråldrar SaveFormat.CSV enum och lägger till SaveFormat.Csv enum.**

 
 Använd SaveFormat.Csv enum istället.

### **Föråldrar LoadFormat.CSV enum och lägger till LoadFormat.Csv enum.**

 
 Använd LoadFormat.Csv enum istället.

### **Föråldrar LoadFormat.TSV enum och lägger till LoadFormat.Tsv enum.**

 
 Använd LoadFormat.Tsv enum istället.

### **Föråldrar LoadFormat.ODS enum och lägger till LoadFormat.Ods enum.**

Använd LoadFormat.Ods enum istället.

### **Föråldrar LoadFormat.SXC enum och lägger till LoadFormat.Sxc enum.**

 
 Använd LoadFormat.Sxc enum istället.

### **Föråldrar LoadFormat.FODS enum och lägger till LoadFormat.Fods enum.**

 
 Använd LoadFormat.Fods enum istället.

### **Lägger till metoden GridCells.MoveRange().**

 Flyttar intervallet.

### **Lägger till metoden GridCells.InsertRange().**

 
Infogar ett område med växlingsalternativ.

### **Lägger till metoden GridCells.DeleteRange().**

 
Tar bort ett område med skiftalternativ.

