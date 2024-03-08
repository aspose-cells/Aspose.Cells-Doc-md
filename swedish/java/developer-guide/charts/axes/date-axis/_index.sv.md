---
title: Datumaxel
description: Lär dig hur du hanterar datumaxeln i Aspose.Cells for Java. Vår guide hjälper dig att förstå hur du arbetar med olika datumformat, tidsskalor och ticketikettsfrekvenser.
keywords: Aspose.Cells for Java, date axis, manage, date formats, time scales, tick label frequencies.
type: docs
weight: 200
url: /sv/java/date-axis/
---
##  **Möjliga användningsscenarier**
När du skapar ett diagram från kalkylbladsdata som använder datum, och datumen plottas längs den horisontella (kategori) axeln i diagrammet, ändrar Aspose.cells automatiskt kategoriaxeln till en datumaxel (tidsskala).
En datumaxel visar datum i kronologisk ordning med specifika intervall eller basenheter, som antalet dagar, månader eller år, även om datumen på kalkylbladet inte är i sekventiell ordning eller i samma basenheter.
Som standard bestämmer Aspose.cells basenheterna för datumaxeln baserat på den minsta skillnaden mellan två valfria datum i kalkylbladets data. Om du till exempel har data för aktiekurser där den minsta skillnaden mellan datum är sju dagar, ställer Excel basenheten till dagar, men du kan ändra basenheten till månader eller år om du vill se aktiens prestanda över en längre tid.
##  **Hantera datumaxeln som Microsoft Excel**
 Se följande exempelkod som skapar en ny Excel-fil och anger värden för diagrammet i det första kalkylbladet.
 Sedan lägger vi till ett diagram och ställer in typen av[**Axel**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/) 
 till[**Tidsskala**](https://reference.aspose.com/cells/java/com.aspose.cells/categorytype/#TIME-SCALE) och ställ sedan in basenheterna på Dagar.

![todo:image_alt_text](excel.png)

 Följande exempelkod genererar[utdata Excel-fil](DateAxis.xlsx).

##  **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DateAxis.java" >}}
