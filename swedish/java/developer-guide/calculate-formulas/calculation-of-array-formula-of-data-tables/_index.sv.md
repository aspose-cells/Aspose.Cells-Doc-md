---
title: Beräkning av matrisformel för datatabeller
type: docs
weight: 550
url: /sv/java/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}} 

Du kan skapa datatabell i Microsoft Excel med Data > Vad-om-analys > Datatabell.... Aspose.Cells låter dig nu beräkna matrisformeln för datatabellen. Snälla använd[Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) som normalt för att beräkna alla typer av formler.

{{% /alert %}} 
## **Beräkning av matrisformel för datatabeller**
 I följande exempelkod använde vi detta[källkod excel-fil](5472579.xlsx) som också visas i följande bild.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

 Om du ändrar värdet på cell B1 till 100 kommer värdena i Data Table som är fyllda med gul färg att bli 120. Exempelkoden genererar[mata ut PDF](5472577.pdf) som visar 120 som värden i datatabellen som visas i den här bilden.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

 Här är exempelkoden som används för att generera[mata ut PDF](5472577.pdf) från[källkod excel-fil](5472579.xlsx). Läs kommentarerna för mer information.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
