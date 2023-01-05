---
title: Infoga hyperlänkar i Excel eller OpenOffice
linktitle: Hantera hyperlänkar
type: docs
weight: 160
url: /sv/java/insert-hyperlinks-to-excel/
---
## **Lägga till hyperlänkar till länkdata**
{{% alert color="primary" %}} 

En hyperlänk används för att skapa en länk mellan två enheter. Alla är bekanta med användningen av hyperlänkar, särskilt på webbplatser.

Med hjälp av Aspose.Cells kan utvecklare skapa olika typer av hyperlänkar i Microsoft Excel-filer. Det här ämnet diskuterar vilka typer av hyperlänkar som stöds av Aspose.Cells och hur de kan användas i våra Excel-filer.

{{% /alert %}} 
## **Lägga till hyperlänkar**
Tre typer av hyperlänkar kan läggas till i en cell med Aspose.Cells:

- [Lägga till en länk till en URL](/cells/sv/java/working-with-hyperlinks-to-link-data/).
- [Lägga till en länk till en annan cell i samma fil](/cells/sv/java/working-with-hyperlinks-to-link-data/).
- [Lägga till en länk till en extern fil](/cells/sv/java/working-with-hyperlinks-to-link-data/).

 Aspose.Cells tillåter utvecklare att lägga till hyperlänkar till Excel-filer antingen genom att använda API eller[designerkalkylblad](/cells/sv/java/what-is-a-designer-spreadsheet/)(kalkylblad där hyperlänkar skapas manuellt och Aspose.Cells används för att importera dem till andra kalkylblad).

Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)class tillhandahåller olika metoder för att lägga till olika hyperlänkar till Excel-filer.
## **Lägger till länk till en URL**
 De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass innehåller en[Hyperlänkar](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) samling. Varje objekt i[Hyperlänkar](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) samlingen representerar en[Hyperlänk](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) . Lägg till hyperlänkar till webbadresser genom att anropa[Hyperlänkar](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks) samlingens[Lägg till](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )metod. De[Lägg till](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))-metoden tar följande parametrar:

- Cell namn, namnet på cellen som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperlänksområde.
- Antal kolumner, antalet kolumner i detta hyperlänksintervall
- URL, URL-adressen.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


 I exemplet ovan läggs en hyperlänk till en URL i en tom cell,**A1**I sådana fall, om en cell är tom, läggs URL-adressen också till den tomma cellen som dess värde. Om cellen inte är tom och en hyperlänk läggs till ser cellens värde ut som vanlig text. För att få det att se ut som en hyperlänk, tillämpa lämpliga formateringsinställningar på den cellen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Lägga till en länk till en Cell i samma fil**
 Det är möjligt att lägga till hyperlänkar till celler i samma Excel-fil genom att anropa[Hyperlänkar](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) samlingens[Lägg till](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )metod. De[Lägg till](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))-metoden fungerar för både interna och externa hyperlänkar. En version av den överbelastade metoden tar följande parametrar:

- Cell namn, namnet på cellen som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperlänksområde.
- Antal kolumner, antalet kolumner i detta hyperlänkintervall.
- URL, adressen till målcellen.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Lägga till en länk till en extern fil**
 Det är möjligt att lägga till hyperlänkar till externa Excel-filer genom att anropa[Hyperlänkar](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) samlingens[Lägg till](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )metod. De[Lägg till](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))-metoden tar följande parametrar:

- Cell namn, namnet på cellen som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperlänksområde.
- Antal kolumner, antalet kolumner i detta hyperlänkintervall.
- URL, adressen till målet, extern Excel-fil.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **Förhandsämnen**
- [Lägg till bildhyperlänkar](/cells/sv/java/add-image-hyperlinks/)
- [Upptäck hyperlänkstyp](/cells/sv/java/detect-hyperlink-type/)
- [Redigera hyperlänkar till arbetsblad](/cells/sv/java/editing-hyperlinks-of-worksheet/)
- [Få hyperlänkar inom räckvidd](/cells/sv/java/get-hyperlinks-in-range/)


