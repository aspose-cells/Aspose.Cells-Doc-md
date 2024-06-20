---
title: Infoga hyperlänkar i Excel eller OpenOffice
linktitle: Hantera hyperlänkar
type: docs
weight: 45
url: /sv/net/insert-hyperlinks-to-excel/
description: Hur man infogar hyperlänkar i Excel fil med Aspose.Cells biblioteket utan MS Excel.
keywords: Infoga hyperlänkar i Excel, Lägg till eller infoga hyperlänkar, Lägg till eller infoga länk till en URL, Lägg till eller infoga en länk till en cell, Lägg till en länk till en extern fil
---

{{% alert color="primary" %}} 

En hyperlänk används för att skapa en länk mellan två enheter. Alla är bekanta med användningen av hyperlänkar, särskilt på webbplatser.
Med Aspose.Cells kan utvecklare skapa olika typer av hyperlänkar i Microsoft Excel-filer. I det här ämnet diskuteras vilka typer av hyperlänkar som stöds av Aspose.Cells och hur de kan användas i våra Excel-filer.

{{% /alert %}} 
## **Lägga till hyperlänkar**
Aspose.Cells tillåter utvecklare att lägga till hyperlänkar i Excel-filer antingen med hjälp av API:et eller designer- kalkylblad (kalkylblad där hyperlänkar skapas manuellt och Aspose.Cells används för att importera dem till andra kalkylblad).

Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen innehåller en [WorksheetCollection](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen. [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen tillhandahåller olika metoder för att lägga till olika hyperlänkar i Excel-filer.
## **Lägga till länk till en URL**
Klassen [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) innehåller en samling [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks). Varje objekt i samlingen [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) representerar en [Hyperlink](https://reference.aspose.com/cells/net/aspose.cells/hyperlink). Lägg till hyperlänkar till URL:er genom att anropa samlingens [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)-metod. Metoden [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) tar följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i denna hyperlänkomfång
- URL, URL-adressen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

I det ovanstående exemplet läggs en hyperlänk till en URL i en tom cell, **A1**. I sådana fall, om en cell är tom, läggs URL-adressen också till den tomma cellen som dess värde. Om cellen inte är tom och en hyperlänk läggs till, ser cellens värde ut som vanlig text. För att få det att se ut som en hyperlänk, använd lämpliga formateringsinställningar på den cellen.

{{% /alert %}} 
## **Lägga till en länk till en cell i samma fil**
Det är möjligt att lägga till hyperlänkar till celler i samma Excel-fil genom att anropa samlingens [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)-metod. Metoden [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) fungerar för både interna och externa hyperlänkar. En version av den överbelastade metoden tar följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målcellen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Lägga till en länk till en extern fil**
Det är möjligt att lägga till hyperlänkar till externa Excel-filer genom att anropa samlingens [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)-metod. Metoden [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) tar följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målet, extern Excel-fil.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **Fortsatta ämnen**
- [Lägg till bildhyperlänkar](/cells/sv/net/add-image-hyperlinks/)
- [Identifiera hyperlänkstyp](/cells/sv/net/detect-hyperlink-type/)
- [Redigera hyperlänkar på arbetsbladet](/cells/sv/net/editing-hyperlinks-of-worksheet/)
- [Hämta hyperlänkar i omfånget](/cells/sv/net/get-hyperlinks-in-range/)

