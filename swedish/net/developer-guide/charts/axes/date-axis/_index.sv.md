---
title: Datumaxel
type: docs
weight: 200
url: /sv/net/date-axis/
---
## **Möjliga användningsscenarier**
När du skapar ett diagram från kalkylbladsdata som använder datum, och datumen plottas längs den horisontella (kategori) axeln i diagrammet, ändrar Aspose.cells automatiskt kategoriaxeln till en datumaxel (tidsskala).
En datumaxel visar datum i kronologisk ordning med specifika intervall eller basenheter, som antalet dagar, månader eller år, även om datumen på kalkylbladet inte är i sekventiell ordning eller i samma basenheter.
Som standard bestämmer Aspose.cells basenheterna för datumaxeln baserat på den minsta skillnaden mellan två valfria datum i kalkylbladets data. Om du till exempel har data för aktiekurser där den minsta skillnaden mellan datum är sju dagar, ställer Excel basenheten till dagar, men du kan ändra basenheten till månader eller år om du vill se aktiens prestanda över en längre tid.
## **Hantera Date Axis som Microsoft Excel**
 Se följande exempelkod som skapar en ny Excel-fil och anger värden för diagrammet i det första kalkylbladet.
 Sedan lägger vi till ett diagram och ställer in typen av[**Axel**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
 till[**Tidsskala**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/) och ställ sedan in basenheterna på Dagar.

![todo:image_alt_text](excel.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
