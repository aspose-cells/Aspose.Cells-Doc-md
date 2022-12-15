---
title: Infoga hyperlänkar i Excel eller OpenOffice
linktitle: Hantera hyperlänkar
type: docs
weight: 45
url: /sv/net/insert-hyperlinks-to-excel/
description: Hur man infogar hyperlänkar i Excel-fil med Aspose.Cells-bibliotek utan MS Excel.
---
{{% alert color="primary" %}} 

En hyperlänk används för att skapa en länk mellan två enheter. Alla är bekanta med användningen av hyperlänkar, särskilt på webbplatser.
Med hjälp av Aspose.Cells kan utvecklare skapa olika typer av hyperlänkar i Microsoft Excel-filer. Det här ämnet diskuterar vilka typer av hyperlänkar som stöds av Aspose.Cells och hur de kan användas i våra Excel-filer.

{{% /alert %}} 
## **Lägga till hyperlänkar**
Aspose.Cells tillåter utvecklare att lägga till hyperlänkar till Excel-filer antingen med API eller designerkalkylblad (kalkylblad där hyperlänkar skapas manuellt och Aspose.Cells används för att importera dem till andra kalkylblad).

 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/net/aspose.cells/worksheet)class tillhandahåller olika metoder för att lägga till olika hyperlänkar till Excel-filer.
## **Lägger till länk till en URL**
 De[Arbetsblad](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass innehåller en[Hyperlänkar](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) samling. Varje objekt i[Hyperlänkar](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) samlingen representerar en[Hyperlänk](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) . Lägg till hyperlänkar till webbadresser genom att anropa[Hyperlänkar](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) samlingens[Lägg till](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) metod. De[Lägg till](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)metoden tar följande parametrar:

- Cell namn, namnet på cellen som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperlänksområde.
- Antal kolumner, antalet kolumner i detta hyperlänkintervall
- URL, URL-adressen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

 I exemplet ovan läggs en hyperlänk till en URL i en tom cell,**A1**. I sådana fall, om en cell är tom, läggs URL-adressen också till den tomma cellen som dess värde. Om cellen inte är tom och en hyperlänk läggs till ser cellens värde ut som vanlig text. För att få det att se ut som en hyperlänk, tillämpa lämpliga formateringsinställningar på den cellen.

{{% /alert %}} 
## **Lägga till en länk till en Cell i samma fil**
 Det är möjligt att lägga till hyperlänkar till celler i samma Excel-fil genom att anropa[Hyperlänkar](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) samlingens[Lägg till](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) metod. De[Lägg till](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)Metoden fungerar för både interna och externa hyperlänkar. En version av den överbelastade metoden tar följande parametrar:

- Cell namn, namnet på cellen som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperlänksområde.
- Antal kolumner, antalet kolumner i detta hyperlänkintervall.
- URL, adressen till målcellen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Lägga till en länk till en extern fil**
 Det är möjligt att lägga till hyperlänkar till externa Excel-filer genom att anropa[Hyperlänkar](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) samlingens[Lägg till](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) metod. De[Lägg till](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)metoden tar följande parametrar:

- Cell namn, namnet på cellen som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperlänksområde.
- Antal kolumner, antalet kolumner i detta hyperlänkintervall.
- URL, adressen till målet, extern Excel-fil.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **Förhandsämnen**
- [Lägg till bildhyperlänkar](/cells/sv/net/add-image-hyperlinks/)
- [Upptäck hyperlänkstyp](/cells/sv/net/detect-hyperlink-type/)
- [Redigera hyperlänkar till arbetsblad](/cells/sv/net/editing-hyperlinks-of-worksheet/)
- [Få hyperlänkar inom räckvidd](/cells/sv/net/get-hyperlinks-in-range/)

