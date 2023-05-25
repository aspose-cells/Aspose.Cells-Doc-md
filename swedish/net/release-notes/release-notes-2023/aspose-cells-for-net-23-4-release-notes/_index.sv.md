---
title: Aspose.Cells for .NET 23.4 Release Notes
type: docs
weight: 9
url: /sv/net/aspose-cells-for-net-23-4-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 23.4](https://www.nuget.org/packages/Aspose.Cells/23.4.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
| :- | :- | :- |
|CELLSNET-52860|Stöd för beräkning av ENCODEURL-funktion|
|CELLSNET-53092|Stöd för att spara xlsb-fil i LightCells-läge|
|CELLSNET-53098|CalculateFormula() multiplicera array|
|CELLSNET-53136|Stöd render ActiveX-kontroll och formulärkontroll för kryssruta i GridWeb|
|CELLSNET-53151|Stöd render ActiveX-kontroll för textbox i GridWeb|
|CELLSNET-53152|Stöd render ActiveX-kontroll och formulärkontroll för alternativknapp i GridWeb|
|CELLSNET-53059|Lägg till API för att kontrollera om teckensnittet är installerat eller tillgängligt|
|CELLSNET-53064|Stöd för att ställa in formel till angiven cell i ListObject|
|CELLSNET-52903|KOD-funktionen returnerar olika värden i Excel och Aspose.Cells|
|CELLSNET-53128|Förbättra den mittjusterade texten när du exporterar till html|
|CELLSNET-53135|Spara namnet på arket som namnet på noden när du konverterar excel till xml|
|CELLSNET-53079|Formkorruption när du sparar fil till pdf|
|CELLSNET-52982|Ett fel uppstår vid inställning av LET-formel för cell|
|CELLSNET-53009|1.36 blir 1.3599999999999999 efter att ha läst från xlsx mallfil|
|CELLSNET-53132|Worksheet.CalculateFormula-metoden beräknar ogiltig formel felaktigt|
|CELLSNET-53139|Problem med att läsa decimaler med mer än 15 tecken|
|CELLSNET-53049|Gridline överensstämmer inte med Excel i utdata PDF|
|CELLSNET-53078|GetPrintingPageBreaks returnerar felaktiga värden|
|CELLSNET-53123| Bilden täckte text i konverterad pdf|
|CELLSNET-53103|Tabeller slås samman och skärs av under konvertering till HTML|
|CELLSNET-52661|Konvertering av viss Xlsx till Pptx ger trasiga resultat|
|CELLSNET-52953| Cell-justeringen i Excel HTML är fel|
|CELLSNET-52968|De automatiskt anpassade kolumnerna kan inte innehålla allt innehåll|
|CELLSNET-52993|Aspose.Cells känner inte av filformatet korrekt|
|CELLSNET-53035|AutoFitRows fungerar inte i kombination med sammanslagna celler och kanter|
|CELLSNET-53048| Den genererade filen är skadad om Module.Name innehåller japanska|
|CELLSNET-53063|Cells.InsertRows kopierar inte formeluppsättningen för en tabellkolumn|
|CELLSNET-53065|Teckensnittsunderstrykning gäller inte för WordArt|
|CELLSNET-53082|Problem med popup-fönster för innehåll visas efter att du har sparat .xlsb-filen|
|CELLSNET-53089|Visa meddelandet Beräkningsinställningar när du öppnar genererad ods-fil i MS Excel|
|CELLSNET-53104|Att kopiera kalkylblad eller arbetsböcker bevarar inte tabellsortering|
|CELLSNET-53111|Justera att distribuerad justering saknas när du sparar filen till xls|
|CELLSNET-53115|Sparkline-diagram saknas vid konvertering av fil till ODS|
|CELLSNET-53117|Resultatfilen kraschar när filen med pivottabell konverteras till ODS|
|CELLSNET-53118|Återge diagram vid konvertering av fil till ODS|
|CELLSNET-53119|Flera diagramförluster vid konvertering av fil till ODS|
|CELLSNET-53120|Aktiediagram saknas i utdatafilen ODS från en XLSX-fil|
|CELLSNET-53125|Namngivna intervall försvinner från makroaktiverad arbetsbok när de öppnas igen efter lagring|
|CELLSNET-53138|Pivottabellen visas inte längre i rapportanslutningar|
|CELLSNET-53157|En intern länk mellan ark i en arbetsbok fungerar inte när man konverterar mht till excel|
|CELLSNET-53108|Ett undantag inträffade när html laddades|

##  **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

###  **Lägger till egenskapen XlsbSaveOptions.LightCellsDataProvider**

Tillåter användaren att spara xlsb-fil i LightCell-läge.

###  **Lägger till metoder för Worksheet.CalculateArrayFormula(...).**

Tillåter användaren att beräkna en formel som matrisformel dynamiskt utan att först ställa in den i en cell.

###  **Lägger till egenskapen CalculationOptions.CharacterEncoding**

Tillåter användaren att specificera kodningen som används för kodning/avkodning av tecken vid beräkning av formler som CHAR och CODE-funktion.

###  **Lägger till Aspose.Cells.Drawing.Equations namnutrymme**

Tillåter användare att slutföra konstruktionen av en ekvationsform genom att infoga relevanta noder steg för steg.

###  **Lägger till FileFormatType.XHtml och FileFormat.OneNote enums**

Representerar filformattypen xhtml och One Note.

###  **Lägger till metoden FontConfigs.IsFontAvailable().**

Returnerar om teckensnittet är tillgängligt.

###  **Lägger till egenskapen LoadOptions.IgnoreUselessShapes**

Anger om onödiga former ignoreras i xlsx-filerna.

###  **Lägger till egenskaperna PivotArea.OnlyData och OnlyLabel.**

Representerar om man endast väljer data eller etikett för pivotområde.

###  **Lägger till SaveFormat.XHtml enum.**

Representerar sparformatet.

###  **Lägger till metoden ListObject.PutCellFormula().**

Lägger formel till cellerna i tabellen.

###  **Lägger till egenskapen VbaProject.Encoding**

Hämtar och ställer in kodningen av VBA-projektet i Excel-filerna.

###  **Lägger till egenskapen XmlSaveOptions.SheetNameAsElementName.**

Anger om arknamnet sparas som elementnamn vid konvertering av excel- till xml-data.

###  **Lägger till egenskapen XmlSaveOptions.DataAsAttribute.**

Anger om data sparas som nodens attribut vid konvertering av excel- till xml-data.

