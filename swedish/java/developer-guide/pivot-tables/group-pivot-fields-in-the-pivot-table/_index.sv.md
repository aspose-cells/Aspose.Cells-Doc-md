---
title: Gruppera Pivot Fields i PivotTable
type: docs
weight: 90
url: /sv/java/group-pivot-fields-in-the-pivot-table/
---

## **Möjliga användningsscenario**

Microsoft Excel gör det möjligt att gruppera pivotfält i pivot-tabellen. När det finns en stor mängd data relaterad till ett pivotfält, är det ofta användbart att gruppera dem i sektioner. Aspose.Cells tillhandahåller också denna funktion med hjälp av metoden [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)).

## **Gruppera Pivot Fields i PivotTable**

Följande kodexempel laddar in den [exempelvisk filen](64716838.xlsx) och grupperar sedan det första pivotfältet med hjälp av metoden [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)). Sedan uppdateras och beräknas data i pivot-tabellen och arbetsboken sparas som den [utdataexempelviska filen](64716837.xlsx). Skärmbilden visar effekten av kodexemplet på exempelvisk filen. Som du kan se i skärmbilden är det första pivotfältet nu grupperat efter månader och kvartal.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
