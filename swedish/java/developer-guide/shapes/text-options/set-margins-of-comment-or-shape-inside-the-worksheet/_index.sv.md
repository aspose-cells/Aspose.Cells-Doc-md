---
title: Ställ in marginaler för kommentar eller shape i kalkylbladet
type: docs
weight: 90
url: /sv/java/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **Möjliga användningsscenario**

Aspose.Cells tillåter dig att ställa in marginalerna för valfri shape eller kommentar med hjälp av egenskapen [**Shape.TextBody.TextAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/fontsettingcollection#TextAlignment). Denna egenskap returnerar objektet för klassen [**ShapeTextAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeTextAlignment) som har olika egenskaper som t.ex. [**TopMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#TopMarginPt), [**LeftMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#LeftMarginPt), [**BottomMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#BottomMarginPt), [**RightMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RightMarginPt), osv. som kan användas för att ställa in de övre, vänstra, nedre och högra marginalerna.

## **Ställ in marginaler för kommentar eller shape i kalkylbladet**

Var god se följande exempelkod. Den laddar in [exempel Excel-filen](61767867.xlsx) som innehåller två shapes. Koden får åtkomst till shaperna en efter en och ställer in deras övre, vänstra, nedre och högra marginaler. Var god se [utdata Excel-filen](61767866.xlsx) genererad av koden och skärmbild som visar effekten av koden på utdata Excel-filen.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-SetMarginsOfCommentOrShapeInsideTheWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
