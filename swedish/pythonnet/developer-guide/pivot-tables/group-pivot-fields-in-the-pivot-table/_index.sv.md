---
title: Gruppera Pivot Fields i PivotTable
type: docs
weight: 80
url: /sv/python-net/group-pivot-fields-in-the-pivot-table/
description: Hur man grupperar Pivot fält i pivottabellen med Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python bibliotek, Hur man grupperar Pivot fält i pivottabellen med Aspose.Cells for Python Excel Library.
---

## **Möjliga användningsscenario**

Microsoft Excel tillåter dig att gruppera pivottabellens fält. När det finns en stor mängd data relaterad till ett pivottabellfält är det ofta användbart att gruppera dem i avsnitt. Aspose.Cells for Python via .NET ger också denna funktion med hjälp av metoden [**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float).

## **Hur man grupperar Pivot-fält i pivottabellen**

Följande exempelkod laddar den [provpå Excel-filen](64716818.xlsx) och utför gruppering på det första pivotfältet med [**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float)-metoden. Sedan uppdaterar och beräknar det pivotabellens data och sparar arbetsboken som [utdata Excel-fil](64716817.xlsx). Skärmbilden visar effekten av exempelkoden på den provpå Excel-filen. Som du kan se på skärmbilden är det första pivotfältet nu grupperat efter månader och kvartal.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.py" >}}
{{< app/cells/assistant language="python-net" >}}
