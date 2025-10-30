---
title: Justera arbetsbokens komprimeringsnivå med Golang via C++
linktitle: Justera arbetsbokens komprimeringsnivå
type: docs
weight: 180
url: /sv/go-cpp/adjust-workbook-compression-level/
description: Lär dig hur du justerar kompressionsnivån för en arbetsbok med Aspose.Cells for C++ för att optimera filstorlek och bearbetningstid.
---

## **Justera arbetsbokens kompressionsnivå**

Utvecklare kan justera arbetsbokens kompressionsnivå när de arbetar med större arbetsböcker. Utvecklare kan prioritera mindre filstorlekar framför bearbetningstid eller vice versa. Aspose.Cells tillhandahåller [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) uppräkningen som du kan använda för att ställa in arbetsbokens kompressionsnivå. Uppräkningen [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) tillhandahåller följande medlemmar.

- Nivå1: Den snabbaste men minst effektiva kompressionen.
- Nivå2: Lite långsammare, men bättre än nivå 1.
- Nivå3: Lite långsammare, men bättre än nivå 2.
- Nivå4: Lite långsammare, men bättre än nivå 3.
- Nivå5: Lite långsammare än nivå 4, men med bättre kompression.
- Nivå6: En bra balans mellan hastighet och kompressionseffektivitet.
- Nivå7: Ganska bra kompression!
- Nivå8: Bättre kompression än nivå 7!
- Nivå9: "Bästa" kompressionen, där bäst innebär största minskningen av indataströmmens storlek. Detta är även den långsammaste kompressionen.

Följande kodsnutt demonstrerar användningen av [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) uppräkningen och jämför konverteringstiden för Nivå1, Nivå6 och Nivå9. Du kan också jämföra storlekarna på de genererade filerna.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AdjustWorkbookCompressionLevel.go" >}}
