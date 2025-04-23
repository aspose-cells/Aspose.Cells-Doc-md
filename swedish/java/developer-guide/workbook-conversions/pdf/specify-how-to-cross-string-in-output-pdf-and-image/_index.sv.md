---
title: Ange hur du ska korsa strängen i utdata PDF och bild
type: docs
weight: 110
url: /sv/java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Möjliga användningsscenario**

När en cell innehåller text eller sträng men den är större än cellens bredd, då överlappar strängen om nästa cell i nästa kolumn är tom eller tom. När du sparar din Excel-fil i PDF/Bildformat kan du kontrollera detta överskott genom att specificera korsa-typen med hjälp av [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)-enumerationen. Den har följande värden

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Visa som MS Excel, beroende på nästa cell. Om nästa cell är tom kommer strängen att korsa eller bli avhuggen.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-KEEP): Visa strängen som MS Excel exporterar till PDF/Bild

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-OVERRIDE): Visa all text genom att korsa andra celler och åsidosätta texten från de korsade cellerna

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT-IN-CELL): Endast visa strängen inom cellens bredd.

## **Ange hur du ska korsa strängen i utdata PDF/Bild med hjälp av TextCrossType**

Följande exempelkod laddar den prov Excel-filen och sparar den i PDF/Bildformat genom att specificera olika [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). Provfilen och utdatafilerna kan laddas ner från följande länkar:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
{{< app/cells/assistant language="java" >}}
