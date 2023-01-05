---
title: Få räckvidd med externa länkar
type: docs
weight: 140
url: /sv/java/get-range-with-external-links/
---
## **Få räckvidd med externa länkar**

Många gånger får Excel-filer tillgång till data från andra Excel-filer med hjälp av externa länkar. Aspose.Cells ger möjlighet att hämta dessa externa länkar genom att använda[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) metod. De[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) metod returnerar en array av typen[**Refererat område**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea). De[**Refererat område**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)klass ger en[**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)egenskap som returnerar namnet på den externa filen. De[**Refererat område**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)klass avslöjar följande medlemmar.

- [**Slutkolumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): Slutkolumnen för området
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): Områdets sista rad
- [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): Hämta det externa filnamnet om detta är en extern referens
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Indikerar om detta är ett område
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): Indikerar om detta är en extern länk
- [**SheetName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Indikerar i vilket blad denna referens finns
- [**Startkolumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): Startkolumnen för området
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): Områdets startrad

Exempelkoden nedan visar användningen av[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) metod för att få Ranges med externa länkar.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
