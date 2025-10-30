---
title: Hämta område med externa länkar med Golang via C++
linktitle: Hämta intervall med externa länkar
type: docs
weight: 120
url: /sv/go-cpp/get-range-with-external-links/
description: Lär dig att hämta områden med externa länkar i Excel filer med Aspose.Cells med Golang via C++
---

## **Hämta intervall med externa länkar**

Ofta använder Excel-filer externa länkar för att få åtkomst till data i andra Excel-filer. Aspose.Cells ger möjlighet att hämta dessa externa länkar med hjälp av [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) metoden. [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) metoden returnerar en array av typen [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/). [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) klassen tillhandahåller en [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) egenskap som returnerar namnet på den externa filen. [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) klassen exponeras av följande medlemmar.

- [**GetEndColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendcolumn/): ändens kolumn för området
- [**GetEndRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendrow/): ändens rad för området
- [**GetExternalFileName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getexternalfilename/): Hämta det externa filnamnet om detta är en extern referens
- [**IsArea**](https://reference.aspose.com/cells/go-cpp/referredarea/isarea/): Indikerar om detta är ett område
- [**IsExternalLink**](https://reference.aspose.com/cells/go-cpp/referredarea/isexternallink/): Indikerar om detta är en extern länk
- [**GetSheetName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getsheetname/): Indikerar vilken bladreferens detta är i
- [**GetStartColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartcolumn/): Startkolumn för området
- [**GetStartRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartrow/): Startrad för området

Kodexemplet nedan visar hur man använder [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) metoden för att hämta områden med externa länkar.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRangeWithExternalLinks.go" >}}
