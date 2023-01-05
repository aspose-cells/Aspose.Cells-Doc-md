---
title: Gruppera pivotfält i pivottabellen
type: docs
weight: 80
url: /sv/net/group-pivot-fields-in-the-pivot-table/
---
## **Möjliga användningsscenarier**

Microsoft Excel låter dig gruppera pivotfält i pivottabellen. När det finns en stor mängd data relaterad till ett pivotfält är det ofta användbart att gruppera dem i sektioner. Aspose.Cells tillhandahåller också denna funktion med hjälp av[**PivotTable.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)metod.

## **Gruppera pivotfält i pivottabellen**

 Följande exempelkod laddar[exempel på Excel-fil](64716818.xlsx) och utför gruppering på det första pivotfältet med hjälp av[**PivotTable.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)metod. Den uppdaterar sedan och beräknar data från pivottabellen och sparar arbetsboken som[utdata Excel-fil](64716817.xlsx). Skärmdumpen visar effekten av exempelkoden på exemplet i Excel-filen. Som du kan se på skärmdumpen är det första pivotfältet nu grupperat efter månader och kvartal.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
