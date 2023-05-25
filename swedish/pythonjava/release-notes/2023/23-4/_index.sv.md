---
title: Aspose.Cells for Python via Java 23.4 Release Notes
type: docs
weight: 9
url: /sv/python-java/aspose-cells-for-python-via-java-23-4-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Python via Java 23.4](https://downloads.aspose.com/cells/python-java/new-releases/aspose.cells-for-python-via-java-23.4/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
| :- | :- | :- |
|CELLSJAVA-45255|Visa text från topp till botten med CSS "writing-mode"|
|CELLSJAVA-45227|Aspose.Cells fastnar när filen sparas som XLSB|
|CELLSJAVA-45241|Det beräknade resultatet av MIRR är inte korrekt|
|CELLSJAVA-45296|Aspose Cells räknar inte om formeln för vissa värden|
|CELLSJAVA-45223|Diagram till bild - tecken och förklaringshöjd renderade inte korrekt|
|CELLSJAVA-45257| Skalor av diagrammet saknas i Excel till PDF-rendering|
|CELLSJAVA-45054|kan inte byta kalkylblad för den angivna filen från kunden|
|CELLSJAVA-45229|kan inte ladda filen i GridWeb för filen test.xlsx|
|CELLSJAVA-45231|setRowHeightForCSV träder inte i kraft efter byte av kalkylblad, csv-filens radhöjd är fortfarande liten|
|CELLSJAVA-45251|Efter justering av kolumnbredden bör även filterknappens position justeras på plats|
|CELLSJAVA-45082|Våglinjefyllning är annorlunda efter att ha sparat filen till pdf|
|CELLSJAVA-45237|Formelvisningsfel när filen sparas till SVG|
|CELLSJAVA-45236|Linjepositionsfel när filen sparas till SVG|
|CELLSJAVA-45252|Felaktig borttagning av sidor under konvertering av Excel till PDF när du använder alternativet PrintingPageType.IGNORE_BLANK|
|CELLSJAVA-45273|Vissa texter syns inte vid konvertering till svg|
|CELLSJAVA-45266|Cell innehållsplatsfel vid konvertering till html|
|CELLSJAVA-45279|Extra blanksteg visas när filen exporteras till HTML|
|CELLSJAVA-45248| HTML till Excel: Kan inte hålla flera format samtidigt|
|CELLSJAVA-45304|Plot saknas i stapeldiagram vid konvertering av xlsx till ods|
|CELLSJAVA-45305|Solform konverteras till en rektangelform när ods konverteras till xlsx|
|CELLSJAVA-45308|Cell-värden är inte synliga för celler som har korsark vid konvertering av xlsx till ods|
|CELLSJAVA-45259|Dataförlust vid konvertering av HTML med listor till XLSX|
|CELLSJAVA-45260|HTML till XLSX: Inriktningen bibehålls inte|
|CELLSJAVA-45271| Resultatfilen har en annan uid när du sparar en arbetsbok två gånger|
|CELLSJAVA-45283|PivotArea-val stöder andra pivotfältstyper än PivotFieldType.Data|
|CELLSJAVA-45298|Färger på cirkeldiagram bör bevaras när du konverterar xlsx till ods|
|CELLSJAVA-45309|Den första skivans vinkel i cirkeldiagrammet är inte korrekt när du konverterar excel till ods|
|CELLSJAVA-45310|Lägg till OneNote-format till FileFormatUtil API för att upptäcka FileFormatType|

##  **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

###  **Lägger till egenskapen XlsbSaveOptions.LightCellsDataProvider**

Tillåter användaren att spara xlsb-fil i LightCell-läge.

###  **Lägger till metoder för Worksheet.CalculateArrayFormula(...).**

Tillåter användaren att beräkna en formel som matrisformel dynamiskt utan att först ställa in den i en cell.

###  **Lägger till egenskapen CalculationOptions.CharacterEncoding**

Tillåter användaren att specificera kodningen som används för kodning/avkodning av tecken vid beräkning av formler som CHAR och CODE-funktion.

###  **Lägger till EquationNode-klassen och det är härledda klasser**

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
