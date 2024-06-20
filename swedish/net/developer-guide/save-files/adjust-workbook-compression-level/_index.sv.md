---
title: Justera arbetsbokens kompressionsnivå
type: docs
weight: 180
url: /sv/net/adjust-workbook-compression-level/
---

## **Justera arbetsbokens kompressionsnivå**

Utvecklare kan justera arbetsbokens kompressionsnivå när de arbetar med större arbetsböcker. Utvecklare kan prioritera mindre filstorlekar framför bearbetningstid eller vice versa. Aspose.Cells tillhandahåller [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) uppräkningen som du kan använda för att ställa in arbetsbokens kompressionsnivå. Uppräkningen [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) tillhandahåller följande medlemmar.

- Nivå1: Den snabbaste men minst effektiva kompressionen.
- Nivå2: Lite långsammare, men bättre än nivå 1.
- Nivå3: Lite långsammare, men bättre än nivå 2.
- Nivå4: Lite långsammare, men bättre än nivå 3.
- Nivå5: Lite långsammare än nivå 4, men med bättre kompression.
- Nivå6: En bra balans mellan hastighet och kompressionseffektivitet.
- Nivå7: Ganska bra kompression!
- Nivå8: Bättre kompression än nivå 7!
- Nivå9: "Bästa" kompressionen, där bäst innebär största minskningen av indataströmmens storlek. Detta är även den långsammaste kompressionen.

Följande kodsnutt demonstrerar användningen av [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) uppräkningen och jämför konverteringstiden för Nivå1, Nivå6 och Nivå9. Du kan också jämföra storlekarna på de genererade filerna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
