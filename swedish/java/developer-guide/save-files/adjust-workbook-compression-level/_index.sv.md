---
title: Justera arbetsbokens komprimeringsnivå
type: docs
weight: 130
url: /sv/java/adjust-workbook-compression-level/
---
## **Justera arbetsbokens komprimeringsnivå**

Utvecklare kan justera komprimeringsnivån för arbetsboken när de arbetar med större arbetsböcker. Utvecklare kan prioritera mindre filstorlekar framför bearbetningstid eller vice versa. Aspose.Cells tillhandahåller**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)**uppräkning som du kan använda för att ställa in komprimeringsnivån för arbetsboken. De**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** uppräkning ger följande medlemmar.

- **[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**: Den snabbaste men minst effektiva kompressionen.
- **[LEVEL_2](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_2)**: Lite långsammare, men bättre, än nivå 1.
- **[LEVEL_3](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_3)**Lite långsammare, men bättre, än nivå 2.
- **[LEVEL_4](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_4)**: Lite långsammare, men bättre, än nivå 3.
- **[LEVEL_5](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_5)**: Lite långsammare än nivå 4, men med bättre kompression.
- **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)**: En bra balans mellan hastighet och kompressionseffektivitet.
- **[LEVEL_7](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_7)**: Ganska bra kompression!
- **[LEVEL_8](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_8)**: Bättre komprimering än Level7!
- **[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**Den "bästa" komprimeringen, där bäst betyder största minskningen av storleken på indataströmmen. Detta är också den långsammaste kompressionen.

Följande kodavsnitt visar användningen av**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** uppräkning och jämför omvandlingstiden för**[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**, **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)** , och**[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**. Du kan också jämföra storleken på de genererade filerna.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
