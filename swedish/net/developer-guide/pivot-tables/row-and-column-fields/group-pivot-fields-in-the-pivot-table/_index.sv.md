---
title: Gruppera Pivot Fields i PivotTable
type: docs
weight: 80
url: /sv/net/group-pivot-fields-in-the-pivot-table/
---

## **Möjliga användningsscenario**

Microsoft Excel tillåter dig att gruppera pivottabellens pivotfält. När det finns en stor mängd data relaterad till ett pivotfält är det ofta användbart att gruppera dem i avsnitt. Aspose.Cells tillhandahåller också denna funktion med hjälp av [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/)-metoden.

## **Gruppera Pivot Fields i PivotTable**

Följande exempelkod laddar den [provpå Excel-filen](64716818.xlsx) och utför gruppering på det första pivotfältet med [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/)-metoden. Sedan uppdaterar och beräknar det pivotabellens data och sparar arbetsboken som [utdata Excel-fil](64716817.xlsx). Skärmbilden visar effekten av exempelkoden på den provpå Excel-filen. Som du kan se på skärmbilden är det första pivotfältet nu grupperat efter månader och kvartal.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
{{< app/cells/assistant language="csharp" >}}
