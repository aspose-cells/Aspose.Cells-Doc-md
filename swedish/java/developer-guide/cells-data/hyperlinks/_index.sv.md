---
title: Infoga hyperlänkar i Excel eller OpenOffice
linktitle: Hantera hyperlänkar
type: docs
weight: 160
url: /sv/java/insert-hyperlinks-to-excel/
---

## **Lägga till hyperlänkar för att länka data**
{{% alert color="primary" %}} 

En hyperlänk används för att skapa en länk mellan två enheter. Alla är bekanta med användningen av hyperlänkar, särskilt på webbplatser.

Med Aspose.Cells kan utvecklare skapa olika typer av hyperlänkar i Microsoft Excel-filer. I det här ämnet diskuteras vilka typer av hyperlänkar som stöds av Aspose.Cells och hur de kan användas i våra Excel-filer.

{{% /alert %}} 
## **Lägga till hyperlänkar**
Tre typer av hyperlänkar kan läggas till i en cell med hjälp av Aspose.Cells:

- [Lägga till en länk till en URL](/cells/sv/java/working-with-hyperlinks-to-link-data/).
- [Lägga till en länk till en annan cell i samma fil](/cells/sv/java/working-with-hyperlinks-to-link-data/).
- [Lägga till en länk till en extern fil](/cells/sv/java/working-with-hyperlinks-to-link-data/).

Aspose.Cells tillåter utvecklare att lägga till hyperlänkar till Excel-filer antingen genom att använda API:et eller [designer kalkylblad](/cells/sv/java/what-is-a-designer-spreadsheet/) (kalkylblad där hyperlänkar skapas manuellt och Aspose.Cells används för att importera dem till andra kalkylblad).

Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) tillhandahåller olika metoder för att lägga till olika hyperlänkar till Excel-filer.
## **Lägga till länk till en URL**
Klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) innehåller en [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) samling. Varje objekt i [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) samlingen representerar en [Hyperlink](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink). Lägg till hyperlänkar till URL:er genom att ringa [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks) samlingens [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-) metod. [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-) metoden tar emot följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner av detta hyperlänksområde
- URL, URL-adressen.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


I det ovanstående exemplet läggs en hyperlänk till en URL till en tom cell, **A1**. I sådana fall, om en cell är tom läggs också URL-adressen till den tomma cellen som dess värde. Om cellen inte är tom och en hyperlänk läggs till ser cellens värde ut som vanlig text. För att få det att se ut som en hyperlänk, applicera lämpliga formatteringsinställningar på den cellen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Lägga till en länk till en cell i samma fil**
Det är möjligt att lägga till hyperlänkar till celler i samma Excel-fil genom att ringa [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) samlingens [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-) metod. [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-) fungerar för både interna och externa hyperlänkar. En överlagrad version av metoden tar emot följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målcellen.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Lägga till en länk till en extern fil**
Det är möjligt att lägga till hyperlänkar till externa Excel-filer genom att ringa [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) samlingens [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-) metod. [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add-int-int-int-int-java.lang.String-) tar emot följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målet, extern Excel-fil.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **Fortsatta ämnen**
- [Lägg till bildhyperlänkar](/cells/sv/java/add-image-hyperlinks/)
- [Identifiera hyperlänkstyp](/cells/sv/java/detect-hyperlink-type/)
- [Redigera hyperlänkar på arbetsbladet](/cells/sv/java/editing-hyperlinks-of-worksheet/)
- [Hämta hyperlänkar i omfånget](/cells/sv/java/get-hyperlinks-in-range/)


{{< app/cells/assistant language="java" >}}
