---
title: Ange hur strängen ska korsas i utgång PDF och bild
type: docs
weight: 110
url: /sv/java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Möjliga användningsscenarier**

När en cell innehåller text eller sträng men den är större än cellens bredd, svämmar strängen över om nästa cell i nästa kolumn är null eller tom. När du sparar din Excel-fil i PDF/Image kan du kontrollera detta överflöde genom att ange korstypen med hjälp av[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)uppräkning. Den har följande värden

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Visa som MS Excel, beror på nästa cell. Om nästa cell är null kommer strängen att korsas eller trunkeras.

- [**TextCrossType. CROSS_BEHÅLL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP): Visa strängen som MS Excel som exporterar PDF/bild

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE): Visa all text genom att korsa andra celler och åsidosätta text i korsade celler

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL): Visar endast strängen inom cellens bredd.

## **Ange hur strängen ska korsas i utdata PDF/Bild med TextCrossType**

Följande exempelkod laddar exemplet i Excel-filen och sparar den i PDF/bildformat genom att ange olika[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). Exemplet på Excel-filen och utdatafilerna kan laddas ner från följande länkar:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
