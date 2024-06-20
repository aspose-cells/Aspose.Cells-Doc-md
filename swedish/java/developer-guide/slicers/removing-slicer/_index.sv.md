---
title: Ta bort slicer
type: docs
weight: 30
url: /sv/java/removing-slicer/
---

## **Möjliga användningsscenario**
Om du vill ta bort slicern i Microsoft Excel, välj den och tryck på *Delete*-knappen. På liknande sätt om du vill ta bort den programmatiskt med Aspose.Cells API, använd [Worksheet.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove\(com.aspose.cells.Slicer\)). Den kommer att ta bort slicern från arbetsbladet. 
## **Ta bort slicer**
Följande provkod laddar in [provmappen](67338504.xlsx) som innehåller en befintlig slicer. Den går igenom slicerna och tar sedan bort den. Slutligen sparar den arbetsboken som [output Excel-fil](67338502.xlsx). Skärmbilden visar slicern som kommer att tas bort efter körningen av provkoden.

![todo:image_alt_text](removing-slicer_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
