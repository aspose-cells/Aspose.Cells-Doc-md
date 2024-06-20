---
title: Slå samman eller dela upp cellintervall
type: docs
weight: 70
url: /sv/java/merge-or-unmerge-range-of-cells/
description: Slå samman och avsloga celler i ett område i Excel med Java kod.
keywords: java slå samman och avsloga celler i ett område, java slå samman och avsloga celler i område, slå samma och avsloga celler i område med java, slå samma och avsloga celler i område med hjälp av java, slå samma och avsloga celler i excel med java, slå samma och avsloga celler i excel med java, java slå samman och avsloga celler i excel, java slå samman celler i excel, java avsloga celler i excel, slå samman celler i område med java
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att slå samman eller dela upp ett cellintervall. Aspose.Cells tillhandahåller [**Range.merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#merge--) och [**Range.unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#unMerge--) metoder för detta ändamål. Denna artikel förklarar hur man slår samman ett cellintervall till en enda cell.

{{% /alert %}}

Den följande exempelkoden skapar först ett område - A1:D4 - och sedan slår samman cellerna i området till en enda cell med hjälp av [**Range.merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#merge--)-metoden.
På samma sätt är det möjligt att dela celler genom att skapa ett intervall och anropa metoden [**Range.unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#unMerge--).

Följande bild visar den genererade Excel-filen med det exempelkod genererat utdata. Som du kan se har området A1:D4 sammanslagits till en enda cell.

![todo:image_alt_text](merge-or-unmerge-range-of-cells_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-MergeUnmergeRangeofCells-MergeUnmergeRangeofCells.java" >}}

{{% alert color="primary" %}}

## **Relaterade artiklar**

- [Sammanslagning och delning av celler](/cells/sv/java/sammanslagning-och-delsning-av-celler/).

{{% /alert %}}
