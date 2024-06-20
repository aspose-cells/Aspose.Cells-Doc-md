---
title: Upptäck sammanfogade celler i ett arbetsblad
type: docs
weight: 3000
url: /sv/java/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

I Microsoft Excel kan flera celler slås samman till en. Detta används ofta för att skapa komplexa tabeller eller skapa en cell som håller en rubrik som spänner över flera kolumner.

Aspose.Cells tillåter dig att identifiera sammanslagna cellområden i en arbetsbok. Du kan också dela upp dem. Den här artikeln ger de enklaste kodraderna för att utföra uppgiften med Aspose.Cells.

Den här artikeln ger kompakta instruktioner om hur du hittar och sedan dela upp sammanslagna celler i en arbetsbok.

{{% /alert %}}

## **Demonstration**

Detta exempel använder en mall för Microsoft Excel-filen kallad **MergeTrial**. Den har några sammanslagna cellområden på ett blad som också kallas Merge Trial.

**Mallfilen**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_1.png)

Aspose.Cells tillhandahåller [**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells)-metoden som används för att få en ArrayList med sammanslagna cellområden.

När koden nedan körs rensar den innehållet i arket och delar upp alla cellområden innan filen sparas igen.

**Utgångsfilen**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_2.png)

## **Kodexempel**

Se följande kodexempel för att se hur du identifierar sammanslagna cellområden i en arbetsbok och delar upp dem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **Relaterade artiklar**

- [Sammanslagning och delning av celler](/cells/sv/java/sammanslagning-och-delsning-av-celler/).
