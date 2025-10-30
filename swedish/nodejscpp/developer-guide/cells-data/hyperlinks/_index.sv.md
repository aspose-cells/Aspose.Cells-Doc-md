---
title: Infoga hyperlänkar i Excel eller OpenOffice
linktitle: Hantera hyperlänkar
type: docs
weight: 45
url: /sv/nodejs-cpp/insert-hyperlinks-to-excel/
description: Hur man infogar hyperlänkar i Excel fil med Aspose.Cells biblioteket utan MS Excel via Node.js via C++.
keywords: Infoga hyperlänkar i Excel Node.js via C++, Lägg till eller infoga hyperlänkar Node.js via C++, Lägg till eller infoga länk till en URL Node.js via C++, Lägg till eller infoga en länk till en cell Node.js via C++, Lägg till en länk till en extern fil Node.js via C++
---

{{% alert color="primary" %}} 

En hyperlänk används för att skapa en länk mellan två enheter. Alla är bekanta med användningen av hyperlänkar, särskilt på webbplatser.
Med Aspose.Cells kan utvecklare skapa olika typer av hyperlänkar i Microsoft Excel-filer. I det här ämnet diskuteras vilka typer av hyperlänkar som stöds av Aspose.Cells och hur de kan användas i våra Excel-filer.

{{% /alert %}} 

## **Lägga till hyperlänkar**
 Aspose.Cells tillåter utvecklare att lägga till hyperlänkar i Excel-filer antingen med API:et eller diagramblad (blad där hyperlänkar skapas manuellt och Aspose.Cells används för att importera dem till andra blad).

Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) innehåller en [WorksheetCollection](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) som ger tillgång till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Klassen [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) tillhandahåller olika metoder för att lägga till olika hyperlänkar till Excel-filer.
## **Lägga till länk till en URL**
Klassen [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) innehåller en [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--) collection. Varje objekt i [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--) collection representerar en [Hyperlink](https://reference.aspose.com/cells/nodejs-cpp/hyperlink). Lägg till hyperlänkar till URL:er genom att ringa metoden [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-). Metoden [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) tar emot följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, URL-adressen.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToURL.js" >}}


{{% alert color="primary" %}} 

I det ovanstående exemplet läggs en hyperlänk till en URL i en tom cell, **A1**. I sådana fall, om en cell är tom, läggs URL-adressen också till den tomma cellen som dess värde. Om cellen inte är tom och en hyperlänk läggs till, ser cellens värde ut som vanlig text. För att få det att se ut som en hyperlänk, använd lämpliga formateringsinställningar på den cellen.

{{% /alert %}} 
## **Lägga till en länk till en cell i samma fil**
Det är möjligt att lägga till hyperlänkar till celler i samma Excel-fil genom att ringa [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection) samlingens [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-). [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) fungerar för både interna och externa hyperlänkar. En version av den överlagrade metoden tar emot följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målcellen.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToCell.js" >}}


## **Lägga till en länk till en extern fil**
Det är möjligt att lägga till hyperlänkar till externa Excel-filer genom att ringa [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection) samlingens [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-). Metoden [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) tar emot följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målet, extern Excel-fil.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToExternalFile.js" >}}



## **Fortsatta ämnen**
- [Lägg till bildhyperlänkar](/cells/sv/nodejs-cpp/add-image-hyperlinks/)
- [Identifiera hyperlänkstyp](/cells/sv/nodejs-cpp/detect-hyperlink-type/)
- [Redigera hyperlänkar på arbetsbladet](/cells/sv/nodejs-cpp/editing-hyperlinks-of-worksheet/)
- [Hämta hyperlänkar i omfånget](/cells/sv/nodejs-cpp/get-hyperlinks-in-range/)

{{< app/cells/assistant language="nodejs-cpp" >}}
