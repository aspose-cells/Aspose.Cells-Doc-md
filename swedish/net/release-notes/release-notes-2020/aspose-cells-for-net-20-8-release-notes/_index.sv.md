---
title: Aspose.Cells för .NET 20.8 Release Notes
type: docs
weight: 9
url: /sv/net/aspose-cells-for-net-20-8-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 20.8](https://www.nuget.org/packages/Aspose.Cells/20.8.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47524|Stöd slicers i Excel-tabeller|Ny funktion|
|CELLSNET-47512|Klient-API för direkt teckensnittsinställning för GridWeb|Ny funktion|
|CELLSNET-47513|Client API för att lägga till/ta bort hyperlänkar för GridWeb|Ny funktion|
|CELLSNET-47514|Lägg till egenskapen ShowAddButton för att stödja lägg till/ta bort kalkylblad för GridWeb|Ny funktion|
|CELLSNET-43975|Stöd för OTF-teckensnittstyper med Aspose.Cells API:er för renderingsändamål|Ny funktion|
|CELLSNET-47445|Pivottabellen visas inte när den sparas som ODS-fil|Ny funktion|
|CELLSNET-47495|Stöd för att konvertera arbetsbok till PPTX vilka bilder är bild.|Ny funktion|
|CELLSNET-47499|Sipport konverterar arbetsbok till DOCX vilka sidor är bilder.|Ny funktion|
|CELLSNET-47538|Stödtabell för .ods-fil.|Ny funktion|
|CELLSNET-47515|XLSX till HTML-konvertering tar ett antal minuter när du använder Aspose.Cells|Förbättring|
|CELLSNET-47483|Undantag "Maximal längd på teckensnittsnamnet är 31" när en XLS laddas|Förbättring|
|CELLSNET-47489|Bestämmelse för att redigera PowerQueryFormulaParameters|Förbättring|
|CELLSNET-47387|Beräkna formel på stora Excel-data med fler 140K rader som inte fungerar|Prestanda|
|CELLSNET-47474|Sidan är inte samma som webbläsare|Insekt|
|CELLSNET-47480|Stilar och innehåll saknas vid konvertering av kalkylblad till HTML/bilder|Insekt|
|CELLSNET-47493|Problem med att konvertera XLSX till HTML|Insekt|
|CELLSNET-47501|Vissa positiva talformateringsutrymme till höger saknas i utdata|Insekt|
|CELLSNET-47503|Fält saknas vid konvertering av XLSX till HTML|Insekt|
|CELLSNET-47516|Stöd linjär gradientbakgrund vid export av fil till HTML eller MHT|Insekt|
|CELLSNET-47521|Felmeddelande vid öppning av utdatafil efter att ha sparat om en XLSX|Insekt|
|CELLSNET-47475|CalculateFormula() beräknar annorlunda än MS Excel|Insekt|
|CELLSNET-47504|Fel formatkonvertering i Excel till HTML-rendering|Insekt|
|CELLSNET-47464|En rad bildas överst i dokumentet i Excel till PDF-konvertering|Insekt|
|CELLSNET-47481|Etikett saknas vid konvertering av kalkylblad till bilder|Insekt|
|CELLSNET-47497|Excel till EMF-textjustering är inte konsekvent|Insekt|
|CELLSNET-47522|Aspose renderade bilder har större mellanrum mellan kolumner jämfört med manuellt kopiera och klistra in|Insekt|
|CELLSNET-47533|Bilder i Excel-filen renderas inte till PDF|Insekt|
|CELLSNET-47484|XLSX till HTML-konverteringsproblem med diagram och unicode-tecken med noll bredd|Insekt|
|CELLSNET-47509|XLS till PDF: Diagram X-Axis har felaktig skalning|Insekt|
|CELLSNET-47520|Cells.InsertRange gör att diagramtiteln försvinner|Insekt|
|CELLSNET-47485|RelativeToOriginalPictureSize = false fungerar inte|Insekt|
|CELLSNET-47507|Smart Marker sammanslagningsgruppering från json-data|Insekt|
|CELLSNET-47511|Externa länkar finns fortfarande kvar efter att ha anropat RemoveExternalLinks|Insekt|
|CELLSNETCORE-74|Formens position ändrades när XLS-filen laddades och sparades|Insekt|
|CELLSNETCORE-75|Textramen blir mindre efter att XLS-filen laddats och sparats|Insekt|
|CELLSNETCORE-76|Teckensnittet ändras när XLS-filen laddas och sparas|Insekt|
|CELLSNET-47487|Form till bild Fel vid konvertering av XLSB till PDF|Undantag|
|CELLSNET-47490|Konvertering av XLSX-filer med dolda element till HTML ger undantag|Undantag|
|CELLSNET-47526|Ett undantag skapas om pivotfältet är datafält.|Undantag|
|CELLSNET-47529|Undantag vid fullständig HTML-konvertering tur och retur med specifik fil|Undantag|
|CELLSNET-47496|Undantag vid konvertering av diagram till bild|Undantag|
|CELLSNET-47488|Undantag "Zoomvärdet ska vara mellan 10 och 400" när ODS-fil öppnas|Undantag|
|CELLSNET-47491|FormatException kastas vid konvertering av vissa strikta XLSX-filer till HTML|Undantag|
|CELLSNET-47494|Undantag "Ogiltig definition av pPower-frågeformel" vid hämtning av mashup-data från arbetsboken|Undantag|
|CELLSNET-47500|StackOverflowException under konvertering av Excel till HTML|Undantag|
|CELLSNET-47506|ArgumentException-fel med SaveFormat.Xlsx|Undantag|
|CELLSNET-47510|Undantag har kastats på Spara-metoden efter RemoveExternalLinks|Undantag|
|CELLSNET-47525|Att spara en arbetsbok ger undantag efter att kommentarerna har rensats|Undantag|
|CELLSNET-47528|FormatException när en XLSX-fil laddas|Undantag|
|CELLSNET-47530|Undantag "Indragsnivån måste vara mellan 0 och 250" när en Excel-fil renderas till PDF|Undantag|
|CELLSNET-47541|Undantag "Ogiltigt cellnamn" när en XLSX-fil laddas|Undantag|

### **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

#### **Markerar gränssnittet ICustomFunction som föråldrat.**

 Detta gränssnitt orsakar ibland oklarheter och missförstånd för användarna. Användaren ska använda**AbstractCalculation Engine** istället som ger mer bekväma och flexibla API:er för att manipulera anpassade funktioner.

#### **Markerar egenskapen CalculationOptions.CustomFunction som föråldrad.**

Snälla använd**AbstractCalculation Engine** istället för**ICustomFunction** av egenskapen CalculationOptions.CustomEngine.

#### **Markerar Workbook.CalculateFormula(bool, ICustomFunction)-metoden som föråldrad.**

Snälla använd**Workbook.CalculateFormula(CalculationOptions)** metod istället.

#### **Markerar Worksheet.CalculateFormula(bool, bool, ICustomFunction)-metoden som föråldrad.**

Snälla använd**Worksheet.CalculateFormula(CalculationOptions, bool)** metod istället.

#### **Markerar Cell. Beräkna (bool, ICustomFunction)-metoden som föråldrad.**

Snälla använd**Cell. Beräkna (Beräkningsalternativ)** metod istället.

#### **Lägger till DocxSaveOptions-klassen och SaveFormat.Docx enum**

Representerar alternativen och uppräkningen för att spara arbetsboken som .docx-filer.

#### **Lägger till klass PptxSaveOptions och SaveFormat.Pptx enum**

Representerar alternativen och uppräkningen för att spara arbetsboken som .pptx-filer.

#### **Lägger till egenskapen OdsLoadOptions.RefresPivotTables**

Indikerar om pivottabeller ska uppdateras när filen laddas.

#### **Lägger till klassen PowerQueryFormulaFunction**

Representerar power query formel funktion.

#### **Lägger till SaveOptions.UpdateSmartArt och tar bort OoxmlSaveOptions.UpdateSmartArt-egenskapen**

Indikerar om texten i smarta konstformer ska uppdateras när filer sparas.

#### **Lägger till metoden SlicerCollection.Add(ListObject table, int index, string destCellName)**

Lägg till en ny Slicer med ListObject som datakälla.

#### **Lägger till metoden SlicerCollection.Add(ListObject table, ListColumn listColumn, string destCellName)**

Lägg till en ny Slicer med ListObject som datakälla.

#### **Lägger till metoden SlicerCollection.Add(ListObject table, ListColumn listColumn, int rad, int kolumn)**

Lägg till en ny Slicer med ListObject som datakälla.
