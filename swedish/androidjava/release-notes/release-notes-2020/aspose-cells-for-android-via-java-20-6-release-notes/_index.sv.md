---
title: Aspose.Cells for Android via Java 20.6 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-android-via-java-20-6-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Android via Java 20.6.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43153|Visa vattenfallsdiagramförklaring på turkiska liknande MS Excel|Förbättring|
|CELLSJAVA-43173|När gruppfältet har ett nollvärde förlorar resultatet av delsummanN delsumman för nollgruppen|Förbättring|
|CELLSJAVA-43186|Beräkna totalsumman för varje rad med utökad kolumn|Förbättring|
|CELLSJAVA-43191|Tillhandahåll ett sätt att hantera scenarier när du anger felaktiga teckensnittstyper|Förbättring|
|CELLSJAVA-43187|Undantag vid laddning av en XLS "Microsoft Excel 5.0 / 95 Workbook"-filer|Förbättring|
|CELLSJAVA-43142|Excel till HTML-rendering - vissa celler är inte justerade efter konvertering|Insekt|
|CELLSJAVA-43155|Roterad text placeras utanför cellen när den renderas som HTML|Insekt|
|CELLSJAVA-43161|Felaktig återgivning av ekvationen|Insekt|
|CELLSJAVA-43130|Problem med transparens för vattenfallsdiagram|Insekt|
|CELLSJAVA-43131|Excel till PDF - Former med text som inte konverterats korrekt|Insekt|
|CELLSJAVA-43133|Chart.toImage inkluderar inte dataetiketter i utdatabilden|Insekt|
|CELLSJAVA-43138|Bild genererad med renderingsproblem.|Insekt|
|CELLSJAVA-43151|Stiländringar efter konvertering av XLS-fil|Insekt|
|CELLSJAVA-43162|Excel till HTML-rendering - konverteringsprocessen tar lång tid|Insekt|
|CELLSJAVA-43164|HTML till Excel-konvertering som inte behåller de rika textformaten i utdata|Insekt|
|CELLSJAVA-43166|Roterad text renderas inte korrekt i XLSX till HTML-konvertering|Insekt|
|CELLSJAVA-43178|RichText-formatering går förlorad när filen exporteras till HTML|Insekt|
|CELLSJAVA-43165|Strängen "20TT1" ersattes med nummer 43850 under konvertering av CSV till XLSB|Insekt|
|CELLSJAVA-43026|Efter att ha renderat diagram till en bild ändrar dataetiketter stilen och värdena är inte desamma|Insekt|
|CELLSJAVA-43154|Vissa diagrampunkter överlappar varandra efter etikett|Insekt|
|CELLSJAVA-43089|Radardiagrammet vänds och axelvärdena är inte identiska med originaldiagrammet i XLS till PDF-konvertering|Insekt|
|CELLSJAVA-43171|Dokumentet är trasigt efter kopiering av arken|Insekt|
|CELLSJAVA-43172|Ett problem med smarta markörer i sammanslagna celler|Insekt|
|CELLSJAVA-43180|HTML till Excel-konvertering skapar svart kalkylblad|Insekt|
|CELLSJAVA-43181|Det finns en skillnad i radhöjd vid konvertering av Excel till HTML|Insekt|
|CELLSJAVA-43188|Bakgrundsfärgstilen behålls inte under konvertering av HTML till Excel|Insekt|
|CELLSJAVA-43196|Det finns ett annat antal VBA-moduler som detekteras genom att använda Aspose.Cells for Java 20.4 och 20.5|Insekt|
|CELLSJAVA-43202|Resurserna släpps inte när arbetsboken har skapats|Insekt|
|CELLSJAVA-43203|Det går inte att bearbeta vissa Excel-valideringslistor baserat på de namngivna intervallen med Unicode-namn|Insekt|
|CELLSJAVA-43185|JPEG-kvalitet är alltid 75 på setImageResample på Linux|Insekt|
|CELLSJAVA-43192|Ladda teckensnittsmapp /System/Bibliotek/Teckensnitt på macOS som standard|Insekt|
|CELLSJAVA-43157|Anpassad dataseriefärg bevaras inte när du skapar ett vattenfallsdiagram|Insekt|
|CELLSJAVA-43175|Ett problem med diagramseriens namn när arbetsboken hänvisas till andra arbetsböcker|Insekt|
|CELLSJAVA-43158|IllegalArgumentException: Kartstorlek(0) måste vara >= 1|Undantag|
|CELLSJAVA-43149|Undantag uppstod när XLSM sparades efter att kalkylbladet tagits bort|Undantag|
|CELLSJAVA-43150|Undantag "java.lang.NumberFormatException" vid filladdning|Undantag|
|CELLSJAVA-43183|Undantag "ClassCastException: ...." vid beräkning av pivottabell|Undantag|
|CELLSJAVA-43177|Ny arbetsbok med CSV-fil resulterar i "java.lang.IndexOutOfBoundsException: millisecond"|Undantag|
|CELLSJAVA-43168|Undantag "IllegalStateException: Detta är inte en strukturerad lagringsfil" vid sammanslagning av Excel-filer|Undantag|
|CELLSJAVA-43179|Undantag NumberFormatException: För inmatningssträng: "bevara"|Undantag|
|CELLSJAVA-43182|Undantag 'lang.IllegalStateException: Ogiltig kodning: null' vid laddning av XLS-fil|Undantag|
|CELLSJAVA-43201|Undantag "java.util.EmptyStackException" för att spara till HTML|Undantag|
|CELLSJAVA-43204|NegativeArraySizeException uppstår när Cell.getDisplayStringValue() används|Undantag|
|CELLSJAVA-43189|Undantag uppstod när XLS-filen laddades|Undantag|
|CELLSJAVA-43193|NullPointerException inträffade när några XLSX-filer laddades|Undantag|
|CELLSJAVA-43200|Undantag "java.lang.ArrayIndexOutOfBoundsException" vid inläsning av filen|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts för allmänheten API, t.ex. tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Android via Java. Om du har frågor om någon ändring i listan, vänligen ta upp det på supportforumet Aspose.Cells.
### **Lägger till egenskapen ChartTextFrame.DirectionType.**
Hämtar och ställer in textens riktning i diagrammet.
### **Lägger till ChartTextFrame.ReadingOrder och föråldrar egenskapen ChartTextFrame.TextDirection.**
Använd egenskapen ChartTextFrame.ReadingOrder istället.
### **Lägger till klasser för de förbättrade funktionerna i Revisions.**
Får information om revisionen.
### **Ändrar standardvärdet för egenskapen TxtSaveOptions.TrimLeadingBlankRowAndColumn.**
För att göra standardbeteendet för att spara CSV på samma sätt med ms excel, ändrade vi standardvärdet och beteendet för den här egenskapen. För gamla versioner var dess standardvärde "**falsk**". Från 20.4 blir dess standardvärde "**Sann**".
### **Ändrar beteendet för att upptäcka tomma rader/kolumner för att spara CSV.**
För gamla versioner tog vi de rader/kolumner som inte har några data men har anpassade inställningar (synlighet, formatering, ... etc.) som tomma. Från 20.4 tar vi dem inte längre som tomma, det nya beteendet är detsamma med ms excel.
### **Lägger till egenskapen TxtSaveOptions.ExportArea.**
Anger intervallet av celldata som ska exporteras. Användare kan använda detta alternativ för att få samma resultat med gamla versioner för det ändrade beteendet för TxtSaveOptions.TrimLeadingBlankRowAndColumn och tomma rader/kolumner.
### **Lägger till UnionRange-klass.**
Representerar fackligt utbud.
### **Tar bort föråldrad DrawObject.Image-egenskap.**
Använd egenskapen DrawObject.ImageBytes istället.
### **Lägger till egenskapen Bullet.FontName**
Hämtar och ställer in teckensnittsnamnet på kulan.
### **Lägger till metoden WorksheetCollection.CreateUnionRange().**
Skapar ett fackligt sortiment.
### **Tar bort föråldrad SaveType-enum.**
Den är oanvänd.
### **Tar bort föråldrade egenskaper för OleObject.ImageFormat och Pictuer.ImageFormat.**
Använd egenskaperna OleObject.ImageType och Picture.ImageType istället.
### **Lägger till WorkbookSettings.GetThemeFont()-metoden.**
Får tematypsnitt.
### **Lägger till egenskapen DataLabels.LinkedSource.**
Hämtar och ställer in den länkade källan.
### **Lägger till DefaultEditLanguage enum.**
Representerar standardspråket för redigering.
### **Lägger till egenskapen ImageOrPrintOptions.DefaultEditLanguage.**
Hämtar eller ställer in standardspråk för redigering.
Det kan visa/rendera olika layouter för textstycken när olika redigeringsspråk är inställda.
### **Lägger till egenskapen PdfSaveOptions.DefaultEditLanguage.**
Hämtar eller ställer in standardspråk för redigering.
Det kan visa/rendera olika layouter för textstycken när olika redigeringsspråk är inställda.
### **Lägger till metoden ReferredArea.GetValues(bool calculateFormulas)/GetValue(int rowOffset, int colOffset, bool calculateFormulas).**
Det ger användaren möjlighet att styra om formler ska beräknas rekursivt i implementeringen av AbstractCalculationEngine.
### **Lägger till WarningType.InvalidFontName och WarningType.InvalidTextOfDefinedName enum.**
Representerar varningstypen.
### **Lägger till egenskaperna WarningInfo.CorrectedObject och WarningInfo.ErrorObject.**
Representerar fel data och uppdaterad data när en varning skickas.
### **Lägger till WorkbookDesigner.RepeatFormulasWithSubtotal-egenskaper.**
Anger om repeterande formler med delsumma rader.
### **Lägger till egenskapen PlotArea.IsAutomaticSize.**
Den indikerar om storleken på tomtytan är automatisk.
### **Tar bort föråldrad Style.Rotation-egenskap.**
Använd Style.RotationAngle-egenskapen istället.
### **Lägger till metoden Gridweb.SetFontFolder(string fontFolder, bool rekursiv)/SetFontFolders(string[] fontFolders, bool rekursiv).**
Ställer in typsnittsmapp/mappar
