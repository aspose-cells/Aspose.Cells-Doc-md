---
title: Aspose.Cells för PHP via Java 22.10 Release Notes
type: docs
weight: 3
url: /sv/php-java/aspose-cells-for-php-via-java-22-10-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för PHP via Java 22.10](https://releases.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-22.10/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44890|stöd importfil med openpassword för GridWeb|
|CELLSJAVA-44884| Listnummer är felaktiga efter konvertering av XLSX till HTML eller PDF|
|CELLSJAVA-44883|Arbetsboken som innehåller pivottabellen skadas efter bearbetning av pivottabellen i den|
|CELLSJAVA-44879|Det formaterade resultatet för GridWeb skilde sig från Cell.DisplayStringValue|
|CELLSJAVA-44327|Kanter och färre linjer visas i svartvita pajskivor i diagram till bildrendering|
|CELLSJAVA-44853|Data om x-axelns vinkel är inte samma som Excel i diagram till bild-rendering|
|CELLSJAVA-44854|Data på y-axelsteget är inte samma som Excel i diagram-till-bild-rendering|
|CELLSJAVA-44904|Problem vid rendering av Excel-diagram till JPG-konvertering|
|CELLSJAVA-44850|När du importerar en XLT-fil, visas inte texten helt med de senaste demos med senaste Aspose.Cells.GridWeb-versionen med senaste resursfiler|
|CELLSJAVA-44857|När du använder versionen Aspose.Cells.GridWeb för Java v22.8 med de senaste resursfilerna för att öppna ett Excel-dokument, skiljer sig effekten av cellerna från originaldokumentet|
|CELLSJAVA-44903|SVG-återgivningen fungerar inte som förväntat|
|CELLSJAVA-44909| När flera rader är fetstilade verkar det svämma över till de andra raderna i onödan|
|CELLSJAVA-44898|Att läsa från GZIPInputStream ger ibland falskt "Filen är skadad" fel i 22.7 och nyare versioner|
|CELLSJAVA-44881|Undantag "java.lang.ArrayIndexOutOfBoundsException: 15070" vid inläsning av en XLS-fil|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Ändrade gränsen för att flytta celler ut från arket för att infoga rader**

I gamla versioner, om det finns celler som har formateringsinställningar men som inte har något värde? och som kommer att flyttas ut från arket, är infogning inte tillåten. Från 22.10 är infogning tillåten för en sådan typ av situation och sådant beteende är samma sak med ms excel nu.

### **Lägger till klassen DataModelConnection**

Anger en datamodellanslutning.

### **Lägger till metoder för Chart.ChangeTemplate(byte[]).**

Ändra diagramtyp med förinställd mallfil.

### **Lägger till ChartCollection.Add(byte[] data, sträng dataRange, bool isVertical, int topRow, int leftColumn,int rightRow, int bottomColumn).**

Lägger till diagram med förinställd mallfil.
