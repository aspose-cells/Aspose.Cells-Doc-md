---
title: Ange hur strängen ska korsas i utdata-HTML med HtmlCrossType
type: docs
weight: 140
url: /sv/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Möjliga användningsscenarier**

När cellen innehåller text eller sträng men den är större än cellens bredd, svämmar strängen över om nästa cell i nästa kolumn är null eller tom. När du sparar din Excel-fil i HTML kan du kontrollera detta överflöde genom att ange korstypen med hjälp av[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)uppräkning. Den har följande värden

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): Visa som MS Excel vilket beror på nästa cell. Om nästa cell är null kommer strängen att korsas eller trunkeras.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): Visa strängen som MS Excel exporterar HTML.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS) : Visa HTML-korssträng, prestandan för att skapa stora HTML-filer blir mer än tio gånger snabbare än att ställa in värdet till[**STANDARD**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) eller[**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): Visa HTML-korssträng och dölj den högra strängen när texterna överlappar varandra.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL): Visar endast strängen inom cellens bredd.

## **Ange hur strängen ska korsas i utdata-HTML med HtmlCrossType**

Följande exempelkod laddar[exempel på Excel-fil](51740747.xlsx)och sparar den i HTML-format genom att ange olika[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)Vänligen ladda ner[mata ut HTML](51740745.zip) filer genererade med denna kod. Exemplet i Excel-filen innehåller bilden kantad med röd färg som visas i den här skärmdumpen som visar effekten av[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)värden på utdata HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
