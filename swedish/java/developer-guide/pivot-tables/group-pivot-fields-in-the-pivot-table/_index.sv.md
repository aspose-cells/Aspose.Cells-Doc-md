---
title: Gruppera pivotfält i pivottabellen
type: docs
weight: 90
url: /sv/java/group-pivot-fields-in-the-pivot-table/
---
## **Möjliga användningsscenarier**

Microsoft Excel låter dig gruppera pivotfält i pivottabellen. När det finns en stor mängd data relaterad till ett pivotfält är det ofta användbart att gruppera dem i sektioner. Aspose.Cells tillhandahåller också denna funktion med hjälp av[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) metod.

## **Gruppera pivotfält i pivottabellen**

Följande exempelkod laddar[exempel på Excel-fil](64716838.xlsx)och utför gruppering på det första pivotfältet med hjälp av[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) metod. Den uppdaterar sedan och beräknar data från pivottabellen och sparar arbetsboken som[utdata Excel-fil](64716837.xlsx). Skärmdumpen visar effekten av exempelkoden på exemplet i Excel-filen. Som du kan se på skärmdumpen är det första pivotfältet nu grupperat efter månader och kvartal.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
