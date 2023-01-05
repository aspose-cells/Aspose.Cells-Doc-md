---
title: Aspose.Cells for Java 20.11 Release Notes
type: docs
weight: 2
url: /sv/java/aspose-cells-for-java-20-11-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 20.11](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.11/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43322|Egenskapen Shape.getWorksheet() krävs|Ny funktion|
|CELLSJAVA-43191| Tillhandahålla medel för att hantera scenarier när du anger felaktiga teckensnittstyper?|Förbättring|
|CELLSJAVA-43319|Problem med att få cellvärde med formel|Insekt|
|CELLSJAVA-43330|Problem efter återlagring av XLSB-fil - skadad fil|Insekt|
|CELLSJAVA-43333|Bilder och textpositionering är felaktig när Excel renderas som HTML|Insekt|
|CELLSJAVA-43321|Problem med autofilter - tomma rader visas|Insekt|
|CELLSJAVA-43335|Dödläge inträffade vid beräkning av formler på arbetsbok|Insekt|
|CELLSJAVA-43313|Sjökortetiketten ändrar sin position när den skrivs ut|Insekt|
|CELLSJAVA-43314|0/100 % rad skrivs inte ut för 100 % cirkeldiagram|Insekt|
|CELLSJAVA-43316| Olika problem vid utskrift av diagram|Insekt|
|CELLSJAVA-40582|Smart art-text renderas inte korrekt till PDF/bild|Insekt|
|CELLSJAVA-41639|Kolumnbredder bevaras inte vid konvertering från formatet "XML Spreadsheet 2003" till formatet XLSX|Insekt|
|CELLSJAVA-43315|Konvertering av XLS till XLSX gör filen korrupt och ger "Shape to Image" fel vid konvertering av utdata XLSX till PDF|Insekt|
|CELLSJAVA-43334|Problem med autofilter på tabell|Insekt|
|


## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Tar bort föråldrad CellsHelper.IsProtectedByRMS()-metod**

Använd egenskapen FileFormatUtil.DetectFileFormat().IsProtectedByRMS istället.

### **Tar bort föråldrade metoderna CellsHelper.DetectLoadFormat() och CellsHelper.DetectFileFormat()**

Använd FileFormatUtil.DetectFileFormat() istället.

### **Tar bort föråldrad CellsHelper.FontDir-egenskap.**

Använd FontConfigs.SetFontsFolder(sträng, bool) istället.

### **Tar bort föråldrad CellsHelper.FontDirs-egenskap.**

Använd FontConfigs.SetFontFolders(string[], bool) istället.

### **Tar bort föråldrad CellsHelper.FontFiles-egenskap.**

Använd FontConfigs.SetFontSources(FontSourceBase[]) istället.

### **Lägger till egenskapen CellsHelper.IsCloudPlatform.**

Indikerar om den körs på kundeplattformen.

### **Lägger till egenskapen Shape.Worksheet.**

Hämtar kalkylbladet som innehåller denna form.

### **Lägger till egenskapen SaveOptions.SortExternalNames.**

Anger om externa namn sorteras när .xlsx-filer sparas.

### **Lägger till metoden ListObject.Filter().**

Filtrerar tabellen.

### **Lägger till åsidosättande XmlMapCollection.Clear()-metoden.**

Rensar alla xml-kartor.

### **Lägger till SaveFormat.Docx enum.**

Representerar att spara som .docx-filer.

### **Lägger till ImageType.OfficeCompatibleEmf enum.**

Windows Förbättrad metafil som är mer kompatibel med Office.

