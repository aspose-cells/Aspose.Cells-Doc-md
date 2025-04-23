---
title: Beräkning av Data Table Arrayformel
type: docs
weight: 550
url: /sv/java/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}} 

Du kan skapa en datatabell i Microsoft Excel med Data > Vad-om-analys > Datablad.... Aspose.Cells tillåter nu att beräkna arrayformeln för databladet. Använd [Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) precis som vanligt för att beräkna vilken formeltyp som helst.

{{% /alert %}} 
## **Beräkning av Array Formula av Data Tables**
I det följande provkoden använde vi denna [källa excel-fil](5472579.xlsx) som också visas i följande bild.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

Om du ändrar värdet av cell B1 till 100 kommer värdena i Data Table som är fyllda med gul färg att bli 120. Provkoden genererar [utmatnings PDF](5472577.pdf) som visar 120 som värden i Data Table enligt denna bild.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Här är provkoden som användes för att generera [utmatnings PDF](5472577.pdf) från [källa excel-filen](5472579.xlsx). Läs kommentarerna för mer information.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
{{< app/cells/assistant language="java" >}}
