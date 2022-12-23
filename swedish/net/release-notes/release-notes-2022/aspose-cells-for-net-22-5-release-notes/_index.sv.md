---
title: Aspose.Cells for .NET 22.5 Release Notes
type: docs
weight: 8
url: /sv/net/aspose-cells-for-net-22-5-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 22.5](https://www.nuget.org/packages/Aspose.Cells/22.5.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-50663|Förbättra prestandan för att ta bort tomma kolumner|
|CELLSNET-50877|Initiera cellens beräknade värde när du ställer in dynamisk matrisformel|
|CELLSNET-51006|Ta bort metoden SetDataSource(strängvariabel, objekt[]dataArray) metod.|
|CELLSNET-50685|Problem med att hämta länkade OLE-bilagor i filen ODS|
|CELLSNET-50920|Excel till Tiff-konverteringsproblem|
|CELLSNET-50820| Problem med att exportera JSON-strängen till Excel|
|CELLSNET-50853|Slicers-filtret försvinner efter att ha sparats om av Aspose.Cells API:er|
|CELLSNET-50960|Arbetsboken skadad när en XLSM-fil (som innehåller en pivottabell) sparades på nytt med Aspose.Cells|
|CELLSNET-50648|DIV/0-felet förvandlas till NUM-fel vid beräkning av NPER-funktionen|
|CELLSNET-50694|Problem med DeleteBlankColumns(alternativ) när kommentarer finns i Excel-ark|
|CELLSNET-50730|INDEX funktion array form beräkningsfel|
|CELLSNET-50781|Formel inte beräknad som i MS Excel|
|CELLSNET-50861| Innehåller för Cells.Find() fungerar inte med Tilde-tecken|
|CELLSNET-50879|Cell:s beräknade värde uppdaterades inte vid uppdatering av dynamiska matrisformler med sant värde för parametern "beräkna"|
|CELLSNET-50992|Värdet för datum och tid ändrades för anpassade dokumentegenskaper efter att ha sparats till ODS|
|CELLSNET-50953|Inaktivera kopiera/klistra in tangentbord i GridDesktop|
|CELLSNET-50771| Teckensnittet blir fetstilt under konvertering av Excel till PDF|
|CELLSNET-50924|Cell bakgrund förlorad efter konvertering till html|
|CELLSNET-50951|Konvertering av Excel till HTML resulterar i problem|
|CELLSNET-50962|Problem med att avbryta Spara-processen med PdfSaveOptions.OnePagePerSheet-alternativet för stor arbetsbok|
|CELLSNET-50997|Prickade cellboxkonturer bryts på höger sida av rutan höjdmässigt|
|CELLSNET-50865|Diagram till bild - inte renderat korrekt|
|CELLSNET-50952|XLS till XLSX konvertering ändrar tvåfärgsgradienten för villkorliga format|
|CELLSNET-50989|Bredden på automatiskt anpassade kolumner är inte korrekt om celler slås samman.|
|CELLSNET-50987|Justering av trapetsform resulterar i "System.ArgumentOutOfRangeException"|
|CELLSNET-50930| Processen kan inte komma åt filundantaget sedan Aspose.Cells 22.1|
|CELLSNET-50946|En konvertering av Excel-kalkylblad misslyckas med felet "Kan inte casta .."|
|CELLSNET-51009|TextToColumns orsakar "System.NullReferenceException" vid Spara|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Ändringar för att spara arbetsbok med LightCells**

För att göra formelrelaterade funktioner tillgängliga för LightCells, i gamla versioner behåller vi all formeldata i cellmodell i minnet när vi sparar arbetsbok med LightCells. Detta orsakade missförstånd och missbruk av LightCells för vissa användare. Användaren trodde att cellens formeldata har släppts utanför räckvidden för StartCell(Cell) men faktiskt inte. För de flesta användare som använder LightCells är deras primära oro prestanda (minneskostnad). Få människor kommer att använda formelrelaterade funktioner förutom att ställa in enkel formel till cellen i processen att spara arbetsboken. Så från den här versionen lägger vi till några begränsningar för att ändra cellobjektet inom ramen för metoden StartCell(Cell). Nu är det inte tillåtet att ställa in delade formler, matrisformler för det givna cellobjektet i metoden StartCell(Cell). Om sådan typ av formler behövs, bör användaren ställa in dem innan arbetsboken sparas. Med denna ändring förbättrade vi prestandan för de flesta användare som behöver spara enkla formel för celler till den resulterande kalkylarksfilen med LightCells.

### **Tar bort föråldrad metod Cell.SetAddInFormula()**

Använd WorksheetCollection.RegisterAddInFunction() och Cell.Formula/Cell.SetFormula() istället.

### **Lägger till ExceptionType.FileCorrupted enum**

Representerar typen av undantag där filen är skadad.

### **Lägger till WarningType.Limitation enum**

Representerar varningstypen är begränsningen av Excel.

### **Lägger till metoden ShapeGuideCollection.Add(strängnamn, dubbelvärde).**

Lägger till en formguide.
