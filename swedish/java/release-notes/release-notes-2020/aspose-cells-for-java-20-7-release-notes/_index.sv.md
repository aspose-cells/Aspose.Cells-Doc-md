---
title: Aspose.Cells för Java 20.7 Release Notes
type: docs
weight: 9
url: /sv/java/aspose-cells-for-java-20-7-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för Java 20.7](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.7/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43221|Undantag "java.lang.NullPointerException" vid laddning av XLT-fil|Förbättring|
|CELLSJAVA-43222|Undantag "com.aspose.cells.CellsException: formeldata borde ha skadats..." när en XLS-fil laddas|Förbättring|
|CELLSJAVA-43223|Undantag "java.lang.IllegalStateException: Ogiltig kodning: null" när en XLS-fil laddas|Förbättring|
|CELLSJAVA-43226|Undantag "java.lang.ArrayIndexOutOfBoundsException" när bildens data hämtas|Förbättring|
|CELLSJAVA-43234|Data före 2014 läses inte från pivottabellen|Insekt|
|CELLSJAVA-43210|Fel värde #Värde läst av Aspose.Cells|Insekt|
|CELLSJAVA-43215|Det går inte att omvandla XLSM-fil till PDF|Insekt|
|CELLSJAVA-43219|Att lägga till formelreferens till olika ark resulterar i en skadad Excel-arbetsbok|Insekt|
|CELLSJAVA-43232|ROUNDUP-funktionsproblem|Insekt|
|CELLSJAVA-43243|Formeln kunde inte hämtas när formeln för den intilliggande cellen ändrades|Insekt|
|CELLSJAVA-43217|Utskrift av XLSX till XPS förlorar bakgrundsformateringen|Insekt|
|CELLSJAVA-43224|Problem vid utskrift till en fysisk skrivare|Insekt|
|CELLSJAVA-43241|Problem med linjehöjd och kant när du skapar en bild från Excel-området|Insekt|
|CELLSJAVA-43209|setRepeatFormulaWithSubtotal(true) genererar inte förväntade resultat när du använder SmartMarkers|Insekt|
|CELLSJAVA-43213|Aspose.Cells 20.6 fungerar inte bra med formulärkontroller på Office 365 (version 2005 Build 12827.20268)|Insekt|
|CELLSJAVA-43214|När du översätter XLS till XLSX producerar den en trasig XLSX-fil|Insekt|
|CELLSJAVA-43216|XLS till XLSX-konvertering - teckensnittets fethet och placering ändras för formen|Insekt|
|CELLSJAVA-43228|Genererad XLS är i skyddad vy|Insekt|
|CELLSJAVA-43231|Fel i utdatafilen efter ersättningar|Insekt|
|CELLSJAVA-43225|Undantag "java.lang.NullPointerException" när strängvärde hämtas från cellen|Undantag|
|CELLSJAVA-43229|Undantag vid laddning av XLSM-fil med alternativet setKeepUnparsedData(false)|Undantag|
|CELLSJAVA-43238|Beräkningen misslyckas med NPE (java.lang.NullPointerException)|Undantag|
|CELLSJAVA-43199|Undantag "java.lang.NegativeArraySizeException" för att spara till HTML|Undantag|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Lägger till metoden Cells.RemoveDuplicates().**

Överbelastad metod för Cells.RemoveDuplicates(...) för användarens bekvämlighet för att ta bort dubblerade rader i hela arket.

### **Lägger till egenskapen TickLabels.DisplayNumberFormat.**

Hämtar och ställer in visningsnummerformatet för bocketiketter.

### **Lägger till metoden Cells.GetViewRowHeight() och Cells.GetViewRowHeightInch().**

Får utsiktsradens höjd.

### **Lägger till enum SheetType.InternationalMacro.**

Lägger till ny arktyp: internationellt makro.

### **Lägger till metoden PivotFieldCollection.iterator().**

Får en uppräkning över elementen i denna samling i rätt ordning.

### **Lägger till metoden PivotItemCollection.iterator().**

Får en uppräkning över elementen i denna samling i rätt ordning.

### **Lägger till egenskapen Workbook.IsWorkbookProtectedWithPassword.**

Indikerar om strukturen och fönstret är skyddade med ett lösenord.

### **Lägg till klasser PowerQueryFormulaParameters och PowerQueryFormulaParameter**

Representerar parametrarna för powerfrågeformeln.
