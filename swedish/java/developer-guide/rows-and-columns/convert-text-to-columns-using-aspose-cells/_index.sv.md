---
title: Konvertera text till kolumner med Aspose.Cells
type: docs
weight: 70
url: /sv/java/convert-text-to-columns-using-aspose-cells/
---
## **Möjliga användningsscenarier**
Du kan konvertera din text till kolumner med Microsoft Excel. Denna funktion är tillgänglig från*Dataverktyg* under*Data* flik. För att dela upp innehållet i en kolumn till flera kolumner bör data innehålla en specifik avgränsare som ett kommatecken (eller något annat tecken) baserat på vilket Microsoft Excel delar upp innehållet i en cell till flera celler. Aspose.Cells tillhandahåller också denna funktion via[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) metod.
## **Konvertera text till kolumner med Aspose.Cells**
Följande exempelkod förklarar användningen av[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) metod. Koden lägger först till några personers namn i kolumn A i det första kalkylbladet. För- och efternamn separeras med mellanslag. Då gäller det[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\) ) metoden i kolumn A och sparar den som utdata excel-fil. Om du öppnar[output excel-fil](25395230.xlsx), kommer du att se, förnamn finns i kolumn A medan efternamn finns i kolumn B som visas i den här skärmdumpen.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
