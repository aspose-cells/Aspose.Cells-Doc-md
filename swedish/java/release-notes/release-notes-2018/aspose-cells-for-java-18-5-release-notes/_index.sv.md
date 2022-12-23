---
title: Aspose.Cells for Java 18.5 Release Notes
type: docs
weight: 80
url: /sv/java/aspose-cells-for-java-18-5-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Java 18.5.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42550|Den samtidiga konverteringen till PDF medan varje arbetsbok har sin egen privata (exklusiva) uppsättning teckensnitt|Ny funktion|
|CELLSJAVA-42594|Upptäck LoadFormat och FileFormatType av XLAM|Förbättring|
|CELLSJAVA-42604|Pivottabellens formatering och beteende ändrades efter att ha öppnat/sparat mallfilen|Insekt|
|CELLSJAVA-41918|Kalkylark (XLS) blir skadat efter enkel inläsning och lagring|Insekt|
|CELLSJAVA-42616|Aspose.Cells bryter iteratorgränssnittet när Iterator.hasnext() anropas två gånger|Insekt|
|CELLSJAVA-42607|Egenskapsvärden förvanskade vid extrahering av dokumentegenskaper|Insekt|
|CELLSJAVA-42601|Arbetsboken är skadad efter att ha lagt till en vattenstämpel|Insekt|
|CELLSJAVA-42600|Samma kod körs långsammare i nya utgåvor|Insekt|
|CELLSJAVA-42598|Egenskaper extraheras inte i mallfilen|Insekt|
|CELLSJAVA-42589|NullPointerException när HTML läggs till i en cell|Insekt|
|CELLSJAVA-41414|Linjer försvann från diagrammet när XLSX-filen sparas på nytt|Insekt|
|CELLSJAVA-42602|Undantag "IndexOutOfBoundsException" när celler slås samman i lättviktsläge|Undantag|
|CELLSJAVA-42610|Undantag "java.lang.IllegalStateException: Ogiltig kodning: null" när en XLS-fil laddas|Undantag|
|CELLSJAVA-42608|ArrayIndexOutOfBoundsException inträffar när en Excel-fil öppnas|Undantag|
|CELLSJAVA-42596|"java.lang.ArrayIndexOutOfBoundsException" inträffar när en Excel-fil öppnas|Undantag|
|CELLSJAVA-42595|"java.io.IOException: Filen är skadad" inträffar när en Excel-fil öppnas|Undantag|
|CELLSJAVA-42591|"com.aspose.cells.CellsException: Ogiltig formel" när en Excel-fil laddas|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till nya egenskaper Cell.IsTableFormula/IsArrayFormula för att ersätta Cell.IsInTable/IsInArray**
Anger om en cell är en del av tabellformeln eller matrisformeln. Gamla namn gör otydlighet, så vi gjorde dem föråldrade och tillhandahåller nya.
### **Lägger till klass IndividualFontConfigs**
Representerar teckensnittskonfigurationer för varje arbetsboksobjekt.
### **Lägger till egenskapen LoadOptions.FontConfigs**
Hämtar och ställer in individuella teckensnittskonfigurationer.
### **Tar bort föråldrad FontSetting.ShapeFont-egenskap**
Använd egenskapen FontSetting.TextOptions istället.
### **Lägger till OoxmlCompliance enum och WorkbookSettings.Compliance-egenskapen**
Stöder Strict Open XML-kalkylblad.
### **Lägger till metoden GroupShape.Ungroup().**
Delar upp former.
### **Lägger till MsoFormatPicture.Gamma-egenskapen**
Får och ställer in bildens gamma.
### **Lägger till egenskaperna TextOptions.FarEastName och TextOptions.LatinName**
Hämta och ställer in Fjärran Östern och det latinska namnet på teckensnittet.
