---
title: Identifiera sammanslagna Cells i ett kalkylblad
type: docs
weight: 3000
url: /sv/java/detect-merged-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

I Microsoft Excel kan flera celler slås samman till en. Detta används ofta för att skapa komplexa tabeller eller för att skapa en cell som innehåller en rubrik som sträcker sig över flera kolumner.

Aspose.Cells låter dig identifiera sammanslagna cellområden i ett kalkylblad. Du kan också ta bort dem. Den här artikeln ger de enklaste kodraderna för att utföra uppgiften med Aspose.Cells.

Den här artikeln innehåller kompakta instruktioner om hur du hittar och sedan tar bort sammanslagna celler i ett kalkylblad.

{{% /alert %}}

## **Demonstration**

 Det här exemplet använder en mall Microsoft Excel-fil som heter**MergeTrial**. Den har några sammanslagna cellområden i ett ark som även kallas Merge Trial.

**Mallfilen**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_1.png)

 Aspose.Cells tillhandahåller[**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells)metod som används för att få en ArrayList av sammanslagna cellområden.

När koden nedan exekveras rensar den innehållet i arket och sammanfogar alla cellområden innan filen sparas igen.

**Utdatafilen**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_2.png)

## **Kodexempel**

Se följande exempelkod för att ta reda på hur du identifierar sammanslagna cellområden i ett kalkylblad och tar bort sammanslagningen av dem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **relaterade artiklar**

- [Sammanfoga och dela celler](/cells/sv/java/merging-and-unmerging-cells/).
