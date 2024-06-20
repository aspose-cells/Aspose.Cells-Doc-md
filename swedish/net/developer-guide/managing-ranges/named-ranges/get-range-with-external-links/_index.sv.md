---
title: Hämta intervall med externa länkar
type: docs
weight: 120
url: /sv/net/get-range-with-external-links/
---

## **Hämta intervall med externa länkar**

Många gånger får Excel-filer åtkomst till data från andra Excelfiler via externa länkar. Aspose.Cells ger möjlighet att hämta dessa externa länkar genom användning av metoden [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas). Metoden [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) returnerar en matris av typen [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea). Klassen [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) tillhandahåller en [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)-egenskap som returnerar namnet på den externa filen. Klassen [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) exponerar följande medlemmar.

- [**EndColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): Slutkolumnen för området
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): Slutraden för området
- [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): Hämta det externa filnamnet om det är en extern referens
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Anger om det här är ett område
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Anger om det här är en extern länk
- [**SheetName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Anger vilket blad denna referens är i
- [**StartColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): Startkolumnen för området
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): Startraden för området

Det givna kodexemplet nedan demonstrerar användningen av [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) metod för att hämta intervall med externa länkar.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
