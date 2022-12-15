---
title: Justera arbetsbokens komprimeringsnivå
type: docs
weight: 180
url: /sv/net/adjust-workbook-compression-level/
---
## **Justera arbetsbokens komprimeringsnivå**

Utvecklare kan justera komprimeringsnivån för arbetsboken när de arbetar med större arbetsböcker. Utvecklare kan prioritera mindre filstorlekar framför bearbetningstid eller vice versa. Aspose.Cells tillhandahåller**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** uppräkning som du kan använda för att ställa in komprimeringsnivån för arbetsboken. De**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** uppräkning ger följande medlemmar.

- Nivå 1: Den snabbaste men minst effektiva kompressionen.
- Nivå 2: Lite långsammare, men bättre, än nivå 1.
- Nivå 3: Lite långsammare, men bättre, än nivå 2.
- Nivå 4: Lite långsammare, men bättre, än nivå 3.
- Nivå 5: Lite långsammare än nivå 4, men med bättre kompression.
- Nivå 6: En bra balans mellan hastighet och kompressionseffektivitet.
- Nivå 7: Ganska bra kompression!
- Level8: Bättre komprimering än Level7!
- Nivå9: Den "bästa" komprimeringen, där bäst betyder största minskningen av storleken på indataströmmen. Detta är också den långsammaste kompressionen.

 Följande kodavsnitt visar användningen av**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**uppräkning och jämför omvandlingstiden för Level1, Level6 och Level9. Du kan också jämföra storleken på de genererade filerna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
