---
title: Sammanfoga eller ta bort sammanslagningsintervall för Cells
type: docs
weight: 70
url: /sv/java/merge-or-unmerge-range-of-cells/
description: Sammanfoga och ta bort Cells i ett intervall i Excel med Java-kod.
keywords: java merge and unmerge cells in a range, java merge and unmerge cells in range, merge and unmerge cells in range with java, merge and unmerge cells in range using java, merge and unmerge cells in excel using java, merge and unmerge cells in excel with java, java merge and unmerge cells in excel, java merge cells in excel, java unmerge cells in excel, merge cells in range with java
---
{{% alert color="primary" %}}

 Du kan använda Aspose.Cells för att slå samman eller dela ett cellintervall. Aspose.Cells tillhandahåller[**Range.merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#merge() ) och[**Range.unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#unMerge()) metoder för detta ändamål. Den här artikeln förklarar hur du slår samman ett cellintervall till en enda cell.

{{% /alert %}}

 Följande exempelkod skapar först ett intervall - A1:D4 - och slår sedan samman cellerna i intervallet till en enda cell med hjälp av[**Range.merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#merge()) metod.
 På samma sätt är det möjligt att dela celler genom att skapa ett intervall och anropa[**Range.unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#unMerge()) metod.

Följande bild visar utdata Excel-filen genererad med exempelkoden. Som du kan se har området A1:D4 slagits samman till en enda cell.

![todo:image_alt_text](merge-or-unmerge-range-of-cells_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-MergeUnmergeRangeofCells-MergeUnmergeRangeofCells.java" >}}

{{% alert color="primary" %}}

## **relaterade artiklar**

- [Sammanfoga och dela celler](/cells/sv/java/merging-and-unmerging-cells/).

{{% /alert %}}
