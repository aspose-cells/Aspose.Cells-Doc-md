---
title: Skicka form framåt eller bakåt inne i Arbetsbladet
type: docs
weight: 600
url: /sv/java/send-shape-front-or-back-inside-the-worksheet/
---

## **Möjliga användningsscenario**

När det finns flera former på samma plats bestäms deras synlighet av deras z-ordningspositioner. Aspose.Cells tillhandahåller metoden [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) som ändrar z-positionspositionen för formen. Om du vill skicka en form bakåt kommer du att använda ett negativt nummer som -1, -2, -3 osv. och om du vill skicka en form framåt kommer du att använda ett positivt nummer som 1, 2, 3 osv.

## **Skicka form framåt eller bakåt inne i Arbetsbladet**

Följande exempelkod förklarar användningen av [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) -metoden. Var god se den [exempel-Excel-filen](50528362.xlsx) som används i koden och den [utdata-Excel-filen](50528361.xlsx) som genereras av den. Skärmbilden visar effekten av koden på exempel-Excel-filen vid körning.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
