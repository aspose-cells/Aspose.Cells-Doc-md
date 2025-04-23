---
title: Ange hur texten ska korsas i utdata HTML med HtmlCrossType
type: docs
weight: 140
url: /sv/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Möjliga användningsscenario**

När cellen innehåller text eller sträng men den är större än cellens bredd, då överlappar strängen om nästa cell i nästa kolumn är null eller tom. När du sparar din Excel-fil till HTML kan du kontrollera detta överlapp genom att ange korsnings-typen med [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)-uppräkningen. Den har följande värden

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): Visa som i MS Excel som beror på nästa cell. Om nästa cell är null, kommer strängen att korsas eller den kommer att avkortas.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS-EXPORT): Visa strängen som vid MS Excel vid export av HTML.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS): Visa HTML-korsningssträngen, prestandan för att skapa stora HTML-filer kommer att vara mer än tio gånger snabbare än att ställa in värdet till [**DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) eller [**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT-TO-CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT): Visa HTML-korsningssträng och dölj den högra strängen när texterna överlappar.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT-TO-CELL): Visar endast strängen inom cellens bredd.

## **Ange hur man korsar sträng i utmatnings-HTML med HtmlCrossType**

Följande exempelkod laddar [inledande Excel-fil](51740747.xlsx) och sparar den i HTML-format genom att specificera olika [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType). Vänligen ladda ner [utdata-HTML](51740745.zip) filerna genererade med denna kod. Den inledande Excel-filen innehåller bilden med röd ram som visas i detta skärmbild som visar effekten av [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType) värden på utdata-HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
{{< app/cells/assistant language="java" >}}
