---
title: Hämta Cell objektet genom visningsnamn för PivotField i PivotTable
type: docs
weight: 70
url: /sv/python-net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Hur man får cellobjektet genom visningsnamn för PivotField av PivotTable med Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python bibliotek, Hämta cellobjektet genom visningsnamn för PivotField av PivotTable med Aspose.Cells for Python Excel Library.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET tillhandahåller [**PivotTable.get_cell_by_display_name(display_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_cell_by_display_name/#str)-metoden som du kan använda för att komma åt cellobjektet genom visningsnamnet för pivottabellfält. Denna metod är användbar när du vill markera eller formatera rubriken för ditt pivottabellfält. Denna artikel förklarar hur du hämtar cellobjektet genom visningsnamnet för datafältet och sedan tillämpar formatering på det.

{{% /alert %}}

## **Hur man får cellobjektet genom visningsnamn för PivotField av PivotTable**

Följande kod får åtkomst till den första pivottabellen i kalkylarket och sedan får cellen genom visningsnamn för det andra datafältet i pivottabellen. Det ändrar sedan fyllningsfärgen och teckensnittsfärgen på cellen till ljusblått och svart, respektive. Nedan visas skärmbilderna hur pivottabellen ser ut före och efter att koden har utförts.

|**Pivot-tabel - Före**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-GetCellByDisplayName-GetCellObjectByDisplayName.py" >}}

|**Pivot-tabel - Efter**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="python-net" >}}
