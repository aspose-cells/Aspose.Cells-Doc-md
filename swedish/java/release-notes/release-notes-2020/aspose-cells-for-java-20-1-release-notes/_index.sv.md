---
title: Aspose.Cells för Java 20.1 Release Notes
type: docs
weight: 60
url: /sv/java/aspose-cells-for-java-20-1-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för Java 20.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.1/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-41325|Cell.getValidation-metoden returnerar null för ODS|Ny funktion|
|CELLSJAVA-43074|XLSX till PDF, skillnad i PDF-utdata när du använder Oracle JDK vs Open JDK|Förbättring|
|CELLSJAVA-43083|Opacitet tillämpas inte på kolumndiagram|Insekt|
|CELLSJAVA-41879|%of, %of Row, %of ParentRowTotal, %ParentTotal, etc. fungerar inte i pivot excel-utdata|Insekt|
|CELLSJAVA-43062|Cells standardbakgrundsfärg är fel i utdata-HTML|Insekt|
|CELLSJAVA-43063|Utdata från SheetRender.toImage() är felaktig|Insekt|
|CELLSJAVA-43070|calculateFormula() beräknar inte värde|Insekt|
|CELLSJAVA-43086|Formatformat för procent har tillämpats felaktigt under norsk språk|Insekt|
|CELLSJAVA-43082|Mindre teckensnitt återges i varje första rad i tabellen|Insekt|
|CELLSJAVA-41360|Cells med formler visas i PDF-filen medan de inte visas i ODS|Insekt|
|CELLSJAVA-42786|ODS till XLSX - linjediagram förlorar linjer och teckenförklaringar|Insekt|
|CELLSJAVA-42788|ODS till XLSX - cirkel blir kvadratisk|Insekt|
|CELLSJAVA-43073|DataMashup-information är inte tillgänglig i arbetsboken|Insekt|
|CELLSJAVA-43092|Kan inte bearbeta Excel-fil|Insekt|

## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till egenskapen ReplaceOptions.RegexKey.**
 Indikerar om den sökta nyckeln är regex. Om**Sann** då kommer den sökta nyckeln (som ska ersättas del) att tas som ett användarspecificerat regex.
### **Tar bort föråldrad ValidationCollection.Add(Aspose.Cells.Validation) metod.**
Använd metoden ValidationCollection.Add(CellArea) istället.
### **Lägger till egenskapen PowerQueryFormula.FormulaDefinition.**
Hämtar definitionen av power-frågeformeln.
### **Lägger till egenskapen DBConnection.PowerQueryFormula.**
Hämtar definitionen av kraftfrågeformel.
### **Lägger till egenskapen HtmlSaveOptions.ExportHeadings.**
Anger om rubriker exporteras när filen sparas till HTML. Standardvärdet är falskt. Om du vill importera HTML-filen till Excel, behåll standardvärdet.
### **Lägger till XAdESType-klass**
Typ av XML Advanced Electronic Signature (XAdES).
### **Lägger till egenskapen DigitalSignature.XAdESType**
Hämtar och ställer in typen av XML Advanced Electronic Signature (XAdES). Standardvärdet är None (XAdES är avstängt).
