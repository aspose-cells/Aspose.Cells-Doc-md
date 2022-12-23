---
title: Aspose.Cells for .NET 8.5.1 Release Notes
type: docs
weight: 60
url: /sv/net/aspose-cells-for-net-8-5-1-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 8.5.1](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.5.1/)

{{% /alert %}}

Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells

## 1) Aspose.Cells

### **Andra förbättringar och förändringar**

### **Nya egenskaper**

(CELLSNET-43703) - ICustomFunction - returnerar ett intervall istället för en enda cell

(CELLSNET-43777) - Cell.GetHeightOfValue() liknande Cell.GetWidthOfValue() behövs

### **Buggar**

(CELLSNET-43744) - Pivottabell uppdateras inte när du sparar till PDF

(CELLSNET-43735) - Pivottabellens alternativ för bandade rader har förlorats

(CELLSNET-43759) - Pivotbordet fortsätter inte att sortera när man kombinerar

(CELLSNET-43721) - Felmeddelande dyker upp efter att arbetsboken har sparats

(CELLSNET-43724) - Värden är inte korrekta när data ändras

(CELLSNET-43719) - Annat värde efter CalculateFormula

(CELLSNET-43713) - Workbook.CalculateFormula beräknar inte korrekta värden

(CELLSNET-43708) - Att anropa arbetsbladet.GetPrintingPageBreaks ändrar textrutans bredd

(CELLSNET-43695) - Cell.RemoveArrayFormula tar inte bort arrayformeln

(CELLSNET-41874) - Excel-syntax stöds inte för formlerna

(CELLSNET-43753) - Aspose.Cells återger 2 sidor

(CELLSNET-43731) - Texten klipps av när kalkylbladet renderas till EMF bild

(CELLSNET-43756) - Diagrambilden innehåller inte samma värden som x-axeln från exceldiagrammet

(CELLSNET-43728) - Uppdatering av pivottabellen med ny data ändrar diagrammets färgstil

(CELLSNET-43726) - Att kombinera arbetsböcker ändrar diagramstilen

(CELLSNET-43700) - Färgen på bilden ser annorlunda ut efter konvertering till PDF

(CELLSNET-43199) - Innehåll och former ändras när Excel sparas till PDF

(CELLSNET-43767) - Excel visar skyddad vy på Aspose.Cells sparat kalkylblad

(CELLSNET-43762) - Cell.GetPrecedents() returnerar inte korrekt kalkylbladsnamn

(CELLSNET-43761) - Bakgrundsfärgen för de villkorligt formaterade cellerna ändras

(CELLSNET-43760) - Regler för villkorligt format är skadade

(CELLSNET-43742) - Inkonsekvent arbetsbokskyddsbeteende

(CELLSNET-43734) - Excel kan inte öppna filen efter konvertering från XLSM till XLS

(CELLSNET-43727) - Att kombinera arbetsböcker orsakar varningen "Kan inte redigera en pivottabell i gruppredigeringsläge" i Excel

### **Undantag**

(CELLSNET-43768) - Okänt områdesfel vid kopiering av kalkylblad från annan arbetsbok

(CELLSNET-43716) - Form till bild Fel vid konvertering till PDF

(CELLSNET-43764) - NullReferenceException i Workbook ctor med kalkylblad sparat som Strict OpenXML

(CELLSNET-43740) - System.IndexOutOfRangeException vid Workbook.Save

## 2) Aspose.Cells Grid Suite

### **Andra förbättringar och förändringar**

### **Nya egenskaper**

(CELLSNET-42783) - Länk till extern arbetsbok skapar #REF! i GridDesktop

(CELLSNET-41744) - Höger till vänster display

### **Buggar**

(CELLSNET-43730) - Skillnaden mellan GridWeb.ActiveCell och GridWeb.WorkSheets[0].ActiveCell

(CELLSNET-43175) - GridDesktop Random Red X Error

(CELLSNET-42321) - Anpassad nummerformatering matchade inte med Excel i Aspose.Cells.GridDesktop

(CELLSNET-43763) - Saknade metoder i Aspose.Cells.GridDesktop

(CELLSNET-43774) - GridDesktop nytt läge: ramar återges inte korrekt i sammanslagna celler

### **Undantag**

(CELLSNET-43670) - System.ArgumentException på GridDesktop.ImportExcelFile

### **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

Lägger till enum TableDataSourceType och ListObject.DataSourceType

Den används för att få datakällans typ av tabellen.

Lägger till metoden Workbook.Dispose().

Det används för att frigöra ohanterade resurser.

Lägger till metoden Cell.GetHeightOfValue().

Det används för att få höjden på värdet i pixelenhet.
