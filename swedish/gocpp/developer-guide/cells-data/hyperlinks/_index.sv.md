---
title: Infoga hyperlänkar i Excel eller OpenOffice med Golang via C++
linktitle: Hantera hyperlänkar
type: docs
weight: 45
url: /sv/go-cpp/insert-hyperlinks-to-excel/
description: Hur man infogar hyperlänkar i Excel fil med Aspose.Cells bibliotek utan MS Excel med C++.
keywords: Infoga hyperlänkar i Excel, Lägg till eller infoga hyperlänkar, Lägg till eller infoga länk till en URL, Lägg till eller infoga en länk till en cell, Lägg till en länk till en extern fil
---

{{% alert color="primary" %}} 

En hyperlänk används för att skapa en länk mellan två enheter. Alla är bekanta med användningen av hyperlänkar, särskilt på webbplatser.
Med Aspose.Cells kan utvecklare skapa olika typer av hyperlänkar i Microsoft Excel-filer. I det här ämnet diskuteras vilka typer av hyperlänkar som stöds av Aspose.Cells och hur de kan användas i våra Excel-filer.

{{% /alert %}} 

## **Lägga till hyperlänkar**
 Aspose.Cells tillåter utvecklare att lägga till hyperlänkar i Excel-filer antingen med API:et eller diagramblad (blad där hyperlänkar skapas manuellt och Aspose.Cells används för att importera dem till andra blad).

Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) klassen innehåller en [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) som ger tillgång till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen tillhandahåller olika metoder för att lägga till olika hyperlänkar till Excel-filer.

## **Lägga till länk till en URL**
[Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) klassen innehåller en [GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/) samling. Varje objekt i [GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/) samlingen representerar en [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/). Lägg till hyperlänkar till URL:er genom att anropa [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) samlingens [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) metod. [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) metoden tar följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, URL-adressen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks.go" >}}
{{% alert color="primary" %}} 

I det ovanstående exemplet läggs en hyperlänk till en URL i en tom cell, **A1**. I sådana fall, om en cell är tom, läggs URL-adressen också till den tomma cellen som dess värde. Om cellen inte är tom och en hyperlänk läggs till, ser cellens värde ut som vanlig text. För att få det att se ut som en hyperlänk, använd lämpliga formateringsinställningar på den cellen.

{{% /alert %}} 

## **Lägga till en länk till en cell i samma fil**
Det är möjligt att lägga till hyperlänkar till celler i samma Excel-fil genom att anropa [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/) samlingens [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) metod. [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) metoden fungerar för både interna och externa hyperlänkar. En version av den överbelastade metoden tar följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målcellen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-1.go" >}}
## **Lägga till en länk till en extern fil**
Det är möjligt att lägga till hyperlänkar till externa Excel-filer genom att anropa [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/) samlingens [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) metod. [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) metoden tar följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målet, extern Excel-fil.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-2.go" >}}
## **Fortsatta ämnen**
- [Lägg till bildhyperlänkar](/cells/sv/cpp/add-image-hyperlinks/)
- [Identifiera hyperlänkstyp](/cells/sv/cpp/detect-hyperlink-type/)
- [Redigera hyperlänkar på arbetsbladet](/cells/sv/cpp/editing-hyperlinks-of-worksheet/)
- [Hämta hyperlänkar i omfånget](/cells/sv/cpp/get-hyperlinks-in-range/)
