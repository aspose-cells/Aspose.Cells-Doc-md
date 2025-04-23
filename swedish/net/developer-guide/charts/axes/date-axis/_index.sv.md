---
title: Datumsaxel
description: Lär dig hur man hanterar datumsaxeln i Aspose.Cells for .NET. Vår guide hjälper dig att förstå hur man arbetar med olika datumformat, tidskalor och ticketikettfrekvenser.
keywords: Aspose.Cells for .NET, datumsaxel, hantera, datumformat, tidskalor, ticketikettfrekvenser.
type: docs
weight: 200
url: /sv/net/date-axis/
---

## **Möjliga användningsscenario**
När du skapar ett diagram från arbetsboksdatabaser som använder datum och datumen ritas längsmed den horisontella (kategori)axeln i diagrammet, ändrar Aspose.cells automatiskt kategori-axeln till en datum (tidskal)axel.
En datumsaxel visar datum i kronologisk ordning vid specifika intervall eller basenheter, såsom antalet dagar, månader eller år, även om datumen i arbetsboken inte är i sekventiell ordning eller i samma basenheter.
Som standard bestämmer Aspose.cells basenheterna för dataraden baserat på den minsta skillnaden mellan vilka två datum som helst i kalkylbladsdatan. Till exempel, om du har data för aktiepriser där den minsta skillnaden mellan datum är sju dagar, ställer Excel basenheten till dagar, men du kan ändra basenheten till månader eller år om du vill se aktiens prestanda under en längre tidsperiod.
## **Hantera datumaxeln som Microsoft Excel**
Se följande exempelkod som skapar en ny Excelfil och sätter in värdena för diagrammet på det första kalkylarket. 
Sedan lägger vi till ett diagram och ställer in typen för [**Axis**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
till [**TimeScale**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/) och ställer sedan in basenheterna till Dagar.

![todo:image_alt_text](excel.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
{{< app/cells/assistant language="csharp" >}}
