---
title: Konvertera Text till Kolumner med Aspose.Cells
type: docs
weight: 70
url: /sv/java/convert-text-to-columns-using-aspose-cells/
---

## **Möjliga användningsscenario**
Du kan konvertera din Text till Kolumner med Microsoft Excel. Denna funktion finns under *Data Tools* på *Data*-fliken. För att dela innehållet i en kolumn till flera kolumner, bör data innehålla en specifik skiljetecken som ett komma (eller annat tecken) som Microsoft Excel använder för att dela innehållet i en cell till flera celler. Aspose.Cells erbjuder också denna funktion via [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) metod.
## **Konvertera Text till Kolumner med Aspose.Cells**
Följande exempelkod förklarar användningen av [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-). Koden lägger först till några personnamn i kolumn A i det första arbetsbladet. Förnamn och efternamn separeras med ett mellanslag. Sedan tillämpar den [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) på kolumn A och sparar det som en utdataexcel fil. Om du öppnar [utdataexcel-filen](25395230.xlsx), kommer du att se att förnamnen är i kolumn A medan efternamnen är i kolumn B som visas i denna skärmdump.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
{{< app/cells/assistant language="java" >}}
