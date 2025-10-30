---
title: Datumsaxel
description: Lär dig hur du hanterar datumaxeln i Aspose.Cells för Python via .NET. Vår guide hjälper dig att förstå hur du arbetar med olika datumformat, tidsskala och frekvens av ticketiketter.
keywords: Aspose.Cells för Python via .NET, datumaxel, hantera, datumformat, tidskalor, tick etikettfrekvenser.
type: docs
weight: 200
url: /sv/python-net/date-axis/
---

## **Möjliga användningsscenario**
När du skapar ett diagram från arbetsboksdatabaser som använder datum och datumen ritas längsmed den horisontella (kategori)axeln i diagrammet, ändrar Aspose.cells automatiskt kategori-axeln till en datum (tidskal)axel.
En datumsaxel visar datum i kronologisk ordning vid specifika intervall eller basenheter, såsom antalet dagar, månader eller år, även om datumen i arbetsboken inte är i sekventiell ordning eller i samma basenheter.
Som standard bestämmer Aspose.cells basenheterna för dataraden baserat på den minsta skillnaden mellan vilka två datum som helst i kalkylbladsdatan. Till exempel, om du har data för aktiepriser där den minsta skillnaden mellan datum är sju dagar, ställer Excel basenheten till dagar, men du kan ändra basenheten till månader eller år om du vill se aktiens prestanda under en längre tidsperiod.

## **Hantera datumaxeln som Microsoft Excel**
Se följande exempelkod som skapar en ny Excelfil och sätter in värdena för diagrammet på det första kalkylarket. 
Sedan lägger vi till ett diagram och ställer in typen för [**Axis**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis) 
till [**TIME_SCALE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/categorytype/) och ställer sedan in basenheterna till Dagar.

![todo:image_alt_text](excel.png)

## **Exempelkod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DateAxis.py" >}}
{{< app/cells/assistant language="python-net" >}}
