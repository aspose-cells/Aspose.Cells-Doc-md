---
title: Hämta intervall med externa länkar
type: docs
weight: 140
url: /sv/java/get-range-with-external-links/
---

## **Hämta intervall med externa länkar**

Många gånger får Excel-filer åtkomst till data från andra Excel-filer med hjälp av externa länkar. Aspose.Cells erbjuder möjligheten att hämta dessa externa länkar genom att använda metoden [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)). Metoden [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) returnerar en array av typen [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea). Klassen [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) tillhandahåller en [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)-egenskap som returnerar namnet på den externa filen. Klassen [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) exponerar följande medlemmar.

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): Slutkolumnen för området
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): Slutraden för området
- [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): Hämta det externa filnamnet om det är en extern referens
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Anger om det här är ett område
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): Anger om det här är en extern länk
- [**SheetName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Anger vilket blad denna referens är i
- [**StartColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): Startkolumnen för området
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): Startraden för området

Den angivna exempelkoden nedan visar användningen av [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean))-metoden för att få överensstämmelser med externa länkar.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
