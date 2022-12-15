---
title: Aspose.Cells for Java 20.2 Release Notes
type: docs
weight: 50
url: /sv/java/aspose-cells-for-java-20-2-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 20.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.2/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43076|Ställ in bildtyp EMF i den renderade HTML-filen|Förbättring|
|CELLSJAVA-43113|Konvertering till PDF - java.lang.NumberFormatException: För inmatningssträng|Förbättring|
|CELLSJAVA-43114|Konvertering till PDF - Ogiltig formel:"'APRIL''12'.A1:'APRIL''12'.I23"|Förbättring|
|CELLSJAVA-43117|Konvertering till PDF - hex är inte ett giltigt hexnummer!|Förbättring|
|CELLSJAVA-43118|Konvertering till PDF - java.lang.NumberFormatException: För inmatningssträng: "341,403,811.74"|Förbättring|
|CELLSJAVA-43077|Undantaget "Oväntad bildtyp" uppstod när kalkylbladet renderades till HTML|Insekt|
|CELLSJAVA-43096|Programmet hänger sig vid konvertering av Excel-fil till HTML|Insekt|
|CELLSJAVA-43107|Konvertering till PDF - com.aspose.cells.CellsException: Form till bild Fel!|Insekt|
|CELLSJAVA-43108|Konvertering till PDF - com.aspose.cells.CellsException|Insekt|
|CELLSJAVA-43088|Radardiagram renderas inte i utdatafilen i XLSX till PDF-konvertering|Insekt|
|CELLSJAVA-43091|Dataetiketter på Donuts-diagrammet överlappas i PDF-filen|Insekt|
|CELLSJAVA-43099|Kalkylbladsbilden återges inte korrekt|Insekt|
|CELLSJAVA-43093|ActiveX-kontrollen upptäcks inte i XLS-filformat|Insekt|
|CELLSJAVA-43104|Problem med getShowTabs och setShowTabs|Insekt|
|CELLSJAVA-43121|OOM försöker få antal sidor i XLS|Insekt|
|CELLSJAVA-43125|Form- och ActiveX-objekt dupliceras|Insekt|
|CELLSJAVA-43094|Undantag vid laddning av ett XLSX-filformat|Undantag|
|CELLSJAVA-43100|Undantag "java.lang.ArrayIndexOutOfBoundsException" när Workbook.calculateFormula() anropas i en Excel-fil|Undantag|
|CELLSJAVA-43123|ArrayIndexOutOfBoundsException när du använder MEMORY_PREFERENCE|Undantag|
|CELLSJAVA-43105|Konvertering till PDF - java.lang.ArrayIndexOutOfBoundsException: 60|Undantag|
|CELLSJAVA-43106|Konvertering till PDF - java.lang.IllegalArgumentException|Undantag|
|CELLSJAVA-43109|Konvertering till PDF - java.lang.NullPointerException|Undantag|
|CELLSJAVA-43111|Konvertering till PDF - com.aspose.cells.CellsException: Ogiltig data!|Undantag|
|CELLSJAVA-43112|Konvertering till PDF - java.lang.NullPointerException|Undantag|
|CELLSJAVA-43115|Konvertering till PDF - java.lang.NegativeArraySizeException|Undantag|
|CELLSJAVA-43116|Konvertering till PDF - java.lang.IllegalStateException: Den strukturerade lagringen verkar vara korrupt.|Undantag|
|CELLSJAVA-43120|java.lang.NumberFormatException vid konvertering av arbetsbok till PDF|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till egenskapen FormulaParseOptions.Parse.**
 Anger om formeln tolkas när ett formeluttryck ställs in i cellen. Standard är**Sann** . Om**falsk**då kommer det inmatade formeluttrycket att behållas som det är för cellen tills användaren anropar andra metoder för att analysera dem eller tills tolkad formeldata krävs av andra operationer, såsom beräkning av formler.
### **Lägger till metoden Workbook.ParseFormulas(bool ignoreError).**
Analyserar alla formler som inte har analyserats när de laddades eller sattes till en cell.
### **Lägger till egenskapen PivotTable.ExternalConnectionDataSource.**
Hämtar den externa anslutningsdatakällan.
### **Lägger till FileFormatType.Numbers35 enum.**
Representerar nummer 3.5-filer sedan office 2014. Endast för att kasta filformatet vid läsning.
### **Lägger till egenskapen LoadOptions.CheckDataValid.**
Indikerar om de ogiltiga uppgifterna ska kontrolleras när filerna laddas.
