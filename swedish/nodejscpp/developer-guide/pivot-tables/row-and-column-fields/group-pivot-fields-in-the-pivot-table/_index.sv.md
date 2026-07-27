---
title: Gruppera Pivot Fields i PivotTable
type: docs
weight: 80
url: /sv/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
description: Hur man grupperar pivottabelfält i pivottabellen med Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js bibliotek, Hur man grupperar pivottabelfält i pivottabellen med Aspose.Cells for Node.js via C++ Excel bibliotek.
---

## **Möjliga användningsscenario**

Microsoft Excel tillåter att du grupperar pivottabelfält i pivottabellen. När det finns mycket data relaterad till ett pivottabelfält kan det vara användbart att gruppera dem i sektioner. Aspose.Cells for Node.js via C++ tillhandahåller också denna funktion med hjälp av [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-) metoden.

## **Hur man grupperar Pivot-fält i pivottabellen**

Följande exempelkod laddar den [provpå Excel-filen](64716818.xlsx) och utför gruppering på det första pivotfältet med [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-)-metoden. Sedan uppdaterar och beräknar det pivotabellens data och sparar arbetsboken som [utdata Excel-fil](64716817.xlsx). Skärmbilden visar effekten av exempelkoden på den provpå Excel-filen. Som du kan se på skärmbilden är det första pivotfältet nu grupperat efter månader och kvartal.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GroupPivotFieldsInPivotTable.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
