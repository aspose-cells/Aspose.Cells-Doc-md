---
title: Få räckvidd med externa länkar
type: docs
weight: 120
url: /sv/net/get-range-with-external-links/
---
## **Få räckvidd med externa länkar**

Många gånger får Excel-filer tillgång till data från andra Excel-filer med hjälp av externa länkar. Aspose.Cells ger möjlighet att hämta dessa externa länkar genom att använda[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)metod. De[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)metod returnerar en array av typ[**Refererat område**](https://reference.aspose.com/cells/net/aspose.cells/referredarea). De[**Refererat område**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) klass ger en[**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)egenskap som returnerar namnet på den externa filen. De[**Refererat område**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)klass avslöjar följande medlemmar.

- [**Slutkolumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): Slutkolumnen för området
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): Områdets sista rad
- [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): Hämta det externa filnamnet om detta är en extern referens
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Indikerar om detta är ett område
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Indikerar om detta är en extern länk
- [**SheetName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Indikerar i vilket blad denna referens finns
- [**Startkolumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): Startkolumnen för området
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): Områdets startrad

 Exempelkoden nedan visar användningen av[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)metod för att få Ranges med externa länkar.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
