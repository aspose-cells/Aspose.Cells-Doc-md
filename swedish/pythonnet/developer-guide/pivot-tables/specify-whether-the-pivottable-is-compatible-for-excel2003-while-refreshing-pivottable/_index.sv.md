---
title: Ange om pivottabellen är kompatibel för Excel2003 medan du uppdaterar pivottabellen
type: docs
weight: 80
url: /sv/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Den här artikeln visar hur du anger om pivottabellen är kompatibel med Excel2003 medan pivottabellen uppdateras med Aspose.Cells for Python via .NET.
keywords: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET tillhandahåller[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) egenskap som du kan använda för att ange om pivottabellen är kompatibel med Excel2003 medan du uppdaterar pivottabellen. Om sant måste en sträng vara mindre än eller lika med 255 tecken, så om strängen är större än 255 tecken kommer den att trunkeras. Om *false** kommer en sträng inte att ha den ovannämnda begränsningen. Standardvärdet är *true**.

{{% /alert %}}

##  **Ange om pivottabellen är kompatibel för Excel2003 medan du uppdaterar pivottabellen**

 Följande exempelkod förklarar användningen av[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) fast egendom. Den ursprungliga strängen är 383 tecken lång. Men när[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) egenskapen är inställd**Sann** och pivottabellen uppdateras, trunkeras data i cell B5 i pivottabellen och den blir 255 tecken lång. Men när[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) egenskapen är inställd**falsk**och pivottabellen uppdateras igen, trunkeras inte data i cell B5 i pivottabellen och förblir 383 tecken långa. Vänligen läs kommentarerna i koden för bättre förståelse av den här egenskapen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
