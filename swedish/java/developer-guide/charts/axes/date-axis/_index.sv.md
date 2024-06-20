---
title: Datumsaxel
description: Lär dig hur man hanterar datumaxeln i Aspose.Cells for Java. Vår guide hjälper dig att förstå hur man arbetar med olika datumformat, tidskalor och tickmärkesfrekvenser.
keywords: Aspose.Cells for Java, datumaxel, hantera, datumformat, tidskalor, tickmärkesfrekvenser.
type: docs
weight: 200
url: /sv/java/date-axis/
---

## **Möjliga användningsscenario**
När du skapar ett diagram från arbetsboksdatabaser som använder datum och datumen ritas längsmed den horisontella (kategori)axeln i diagrammet, ändrar Aspose.cells automatiskt kategori-axeln till en datum (tidskal)axel.
En datumsaxel visar datum i kronologisk ordning vid specifika intervall eller basenheter, såsom antalet dagar, månader eller år, även om datumen i arbetsboken inte är i sekventiell ordning eller i samma basenheter.
Som standard bestämmer Aspose.cells basenheterna för dataraden baserat på den minsta skillnaden mellan vilka två datum som helst i kalkylbladsdatan. Till exempel, om du har data för aktiepriser där den minsta skillnaden mellan datum är sju dagar, ställer Excel basenheten till dagar, men du kan ändra basenheten till månader eller år om du vill se aktiens prestanda under en längre tidsperiod.
## **Hantera datumaxeln som Microsoft Excel**
Se följande exempelkod som skapar en ny Excelfil och sätter in värdena för diagrammet på det första kalkylarket. 
Sedan lägger vi till ett diagram och ställer in typen för [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/) 
till [**TimeScale**](https://reference.aspose.com/cells/java/com.aspose.cells/categorytype/#TIME-SCALE) och ställer sedan in basenheterna till Dagar.

![todo:image_alt_text](excel.png)

Följande exempelkod genererar [utdata Excel-filen](DateAxis.xlsx).

## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DateAxis.java" >}}
