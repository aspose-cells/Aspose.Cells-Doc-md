---
title: Aspose.Cells för Java 20.6 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-java-20-6-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 20.6](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.6/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43186|Beräkna totalsumman för varje rad med utökad kolumn|Förbättring|
|CELLSJAVA-43191|Tillhandahåll sätt att hantera scenarier när du anger felaktiga teckensnittstyper|Förbättring|
|CELLSJAVA-43187|Undantag när en XLS "Microsoft Excel 5.0 / 95 Workbook"-filer laddas|Förbättring|
|CELLSJAVA-43180|HTML till Excel-konvertering skapar svart kalkylblad|Insekt|
|CELLSJAVA-43181|Skillnaden i radhöjd vid konvertering av Excel till HTML|Insekt|
|CELLSJAVA-43188|Bakgrundsfärgstilen behålls inte under HTML till Excel-konvertering|Insekt|
|CELLSJAVA-43196|Ett annat antal VBA-moduler upptäcktes med Aspose.Cells för Java 20.4 och 20.5|Insekt|
|CELLSJAVA-43202|Resurser som inte släpps när arbetsboken har skapats|Insekt|
|CELLSJAVA-43203|Det går inte att bearbeta vissa Excel-valideringslistor baserat på de namngivna intervallen med Unicode-namn|Insekt|
|CELLSJAVA-43185|JPEG-kvalitet är alltid 75 på setImageResample på Linux|Insekt|
|CELLSJAVA-43192|Ladda teckensnittsmapp /System/Bibliotek/Teckensnitt på macOS som standard|Insekt|
|CELLSJAVA-43157|Anpassad dataseriefärg bevaras inte när du skapar ett vattenfallsdiagram|Insekt|
|CELLSJAVA-43175|Ett problem med diagramseriens namn när arbetsboken hänvisas till andra arbetsböcker|Insekt|
|CELLSJAVA-43201|Undantag "java.util.EmptyStackException" för att spara till HTML|Undantag|
|CELLSJAVA-43204|NegativeArraySizeException uppstår när Cell.getDisplayStringValue() används|Undantag|
|CELLSJAVA-43189|Undantag uppstod när XLS-filen laddades|Undantag|
|CELLSJAVA-43193|NullPointerException inträffade när några XLSX-filer laddades|Undantag|
|CELLSJAVA-43200|Undantag "java.lang.ArrayIndexOutOfBoundsException" vid inläsning av filen|Undantag|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
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
