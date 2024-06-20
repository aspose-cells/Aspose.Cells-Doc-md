---
title: Ange om PivotTable är kompatibel med Excel 2003 vid uppdatering av PivotTable
type: docs
weight: 80
url: /sv/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Denna artikel visar hur man anger om PivotTable är kompatibel för Excel2003 vid uppdatering av PivotTable med Aspose.Cells för Python via .NET.
keywords: Aspose.Cells för Python Excel, Excel Python bibliotek, Ange om PivotTable är kompatibel för Excel2003 vid uppdatering av PivotTable
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET tillhandahåller egenskapen [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) som du kan använda för att ange om PivotTable är kompatibel för Excel2003 vid uppdatering av PivotTable. Om true, bör en sträng vara mindre än eller lika med 255 tecken, så om strängen är längre än 255 tecken kommer den att bli avskuren. Om false, kommer en sträng inte ha den nämnda begränsningen. Standardvärdet är true.

{{% /alert %}}

## **Hur man anger om PivotTable är kompatibel för Excel2003 vid uppdatering av PivotTable**

Följande provkod förklarar användningen av egenskapen [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/). Den ursprungliga strängen är 383 tecken lång. Men när egenskapen [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) är inställd som **true** och pivottabellen uppdateras, avkortas datan i cell B5 i pivottabellen och blir 255 tecken lång. Men när egenskapen [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) är inställd som **false** och pivottabellen återigen uppdateras, avkortas inte datan i cell B5 i pivottabellen utan förblir 383 tecken lång. Vänligen läs kommentarerna inuti koden för att bättre förstå denna egenskap.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
