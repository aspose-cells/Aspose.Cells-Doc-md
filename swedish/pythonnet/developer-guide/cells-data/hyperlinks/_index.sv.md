---
title: Infoga hyperlänkar i Excel eller OpenOffice
linktitle: Hantera hyperlänkar
type: docs
weight: 45
url: /sv/python-net/insert-hyperlinks-to-excel/
description: Hur man sätter in hyperlänkar i Excel fil med Aspose.Cells för Python via .NET bibliotek utan MS Excel.
keywords: Python Excel Library, Python Infoga hyperlänkar i Excel, Python Lägg till eller Infoga hyperlänkar, Python Lägg till eller Infoga en länk till en URL, Python Lägg till en eller Infoga en länk till en cell, Python Lägg till en länk till en extern fil
---

{{% alert color="primary" %}} 

En hyperlänk används för att skapa en länk mellan två enheter. Alla är bekanta med användningen av hyperlänkar, särskilt på webbplatser.
Med Aspose.Cells för Python via .NET kan utvecklare skapa olika typer av hyperlänkar i Microsoft Excel-filer. Detta ämne diskuterar vilka typer av hyperlänkar som stöds av Aspose.Cells för Python via .NET och hur de kan användas i våra Excel-filer.

{{% /alert %}} 
## **Hur man lägger till hyperlänkar**
Aspose.Cells för Python via .NET tillåter utvecklare att lägga till hyperlänkar i Excel-filer antingen genom att använda API:et eller designkalkylblad (kalkylblad där hyperlänkar skapas manuellt och Aspose.Cells för Python via .NET används för att importera dem till andra kalkylblad).

Aspose.Cells för Python via .NET tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [WorksheetCollection](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller olika metoder för att lägga till olika hyperlänkar till Excel-filer.

## **Hur man lägger till en länk till en URL**
Klassen [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) innehåller en [hyperlänkar](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) samling. Varje objekt i [hyperlänkar](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) samlingen representerar en [Hyperlänk](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink). Lägg till hyperlänkar till URL:er genom att anropa [hyperlänkar](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) samlingens [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) metod. Metoden [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) tar följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i denna hyperlänkomfång
- URL, URL-adressen.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToURL-1.py" >}}

{{% alert color="primary" %}} 

I det ovanstående exemplet läggs en hyperlänk till en URL i en tom cell, **A1**. I sådana fall, om en cell är tom, läggs URL-adressen också till den tomma cellen som dess värde. Om cellen inte är tom och en hyperlänk läggs till, ser cellens värde ut som vanlig text. För att få det att se ut som en hyperlänk, använd lämpliga formateringsinställningar på den cellen.

{{% /alert %}} 

## **Hur man lägger till en länk till en cell i samma fil**
Det är möjligt att lägga till hyperlänkar till celler i samma Excel-fil genom att anropa [hyperlänkar](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) samlingens [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) metod. Metoden [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) metoden fungerar både för interna och externa hyperlänkar. En version av den överlagrade metoden tar följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målcellen.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToAnotherCell-1.py" >}}

## **Hur man lägger till en länk till en extern fil**
Det är möjligt att lägga till hyperlänkar till externa Excel-filer genom att anropa [hyperlänkar](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) samlingens [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) metod. Metoden [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) tar följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målet, extern Excel-fil.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToExternalFile-1.py" >}}

## **Fortsatta ämnen**
- [Lägg till bildhyperlänkar](/cells/sv/python-net/add-image-hyperlinks/)
- [Identifiera hyperlänkstyp](/cells/sv/python-net/detect-hyperlink-type/)
- [Redigera hyperlänkar på arbetsbladet](/cells/sv/python-net/editing-hyperlinks-of-worksheet/)
- [Hämta hyperlänkar i omfånget](/cells/sv/python-net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="python-net" >}}
