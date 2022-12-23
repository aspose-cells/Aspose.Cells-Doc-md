---
title: Aspose.Cells for Java 21.11 Release Notes
type: docs
weight: 2
url: /sv/java/aspose-cells-for-java-21-11-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 21.11](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.11/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43844| En förbättring som behövs för bokföringsnummerformat|
|CELLSJAVA-43953|Återge specifik text/del "Cell" och "Kommentar" för att översättas till japanska i Excel till PDF konvertering|
|CELLSJAVA-43935|Forma text teckensnittsstorlek när du sparar och laddar XLS-filen|
|CELLSJAVA-43952|Tillfällig licens Utgångsfråga|
|CELLSJAVA-43954|XLSX till PDF: Bilden orsakar ett undantag "java.lang.OutOfMemoryError: Java heap space"|
|CELLSJAVA-43902|Vissa gränser i Excel konverterade till HTML är överflödiga|
|CELLSJAVA-43933|När du exporterar till HTML med endast en data skiljer sig det villkorliga formatet från Excel|
|CELLSJAVA-43878| Felaktig placering av Excel-klusterstapeldiagramdataetiketter|
|CELLSJAVA-43895|Linjeform och andra diagramformer renderas inte korrekt vid konvertering av XLS till XLSX|
|CELLSJAVA-43932|Problem med att ställa in dataetiketternas position för exploderade munkdiagram i utdatabilden|
|CELLSJAVA-43934|Cirkeldiagrametiketterna matchade inte med Excel efter manipulering eller uppdatering av diagram|
|CELLSJAVA-43519|Sammanslagna celler som ingår i dolda rader eller kolumner ger en ojämn HTML tabell|
|CELLSJAVA-43962|Effekten är inkonsekvent efter att det villkorliga formatet i excel har konverterats till HTML|
|CELLSJAVA-43969|Ett namn med COUNTIF-funktionen och extern referens ger ett NullPointerException|
|CELLSJAVA-43903|java.lang.NumberFormatException: För inmatningssträng vid rendering av Excel-fil till HTML|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till enum CellValueFormatStrategy.DisplayString.**

Med denna strategi kommer Cell.GetStringValue(CellValueFormatStrategy) att ta hänsyn till gränsen för kolumnbredden vid formatering av cellvärden med visningsstilen. Om det formaterade resultatet överskrider den tillgängliga bredden, kan en eller flera "#" returneras, precis som vad ms excel visar för sådana typer av celler.

### **Lägger till egenskapen WorksheetCollection.ActiveSheetName.**

Hämtar och ställer in det aktiva arknamnet för arbetsboken.

### **Lägger till klasserna JsonLoadOptions och JsonSaveOptions.**

Representerar alternativen för att ladda eller spara filerna.

### **Lägger till egenskapen ImageSaveOptions.StreamProvider.**

Ange strömmarna om det finns två eller fler sidor.

### **Lägger till LoadFormat.Image och LoadFormat.Json enum.**

Representerar bilden och json-typen.

### **Lägger till SaveFormat.Bmp, SaveFormat.Emf,SaveFormat.Gif,SaveFormat.Jpg,SaveFormat.Json och SaveFormat.Png enum**

Nya sparade format som stöds.

### **Lägger till FileFormatType.Emf,FileFormatType.Gif,FileFormatType.Jpg,FileFormatType.Json,FileFormatType.Png,FileFormatType.Wmf enum**

Nya filformatstyper som stöds.

