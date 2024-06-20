---
title: Konvertera Text till Kolumner med Aspose.Cells
type: docs
weight: 70
url: /sv/java/convert-text-to-columns-using-aspose-cells/
---

## **Möjliga användningsscenario**
Du kan konvertera din text till kolumner med hjälp av Microsoft Excel. Denna funktion finns under *Data Tools* under fliken *Data*. För att dela upp innehållet i en kolumn till flera kolumner, bör datan innehålla en specifik avgränsare, som ett kommatecken (eller något annat tecken) baserat på vilket Microsoft Excel delar upp innehållet i en cell till flera celler. Aspose.Cells tillhandahåller också denna funktion via [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) metoden.
## **Konvertera Text till Kolumner med Aspose.Cells**
Följande exempelkod förklarar användningen av [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) metoden. Koden lägger först till några namn på personer i kolumn A i den första arbetsboken. För- och efternamn är separerade med ett mellanslagstecken. Sedan tillämpas [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) metoden på kolumn A och sparar den som en utdata Excel-fil. Om du öppnar [utdata Excel-filen](25395230.xlsx) kommer du att se att förnamnen är i kolumn A medan efternamnen är i kolumn B som visas på denna skärmbild.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
