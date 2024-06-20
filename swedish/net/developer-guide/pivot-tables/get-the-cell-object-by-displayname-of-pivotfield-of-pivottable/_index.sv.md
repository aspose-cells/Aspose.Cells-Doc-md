---
title: Hämta Cell objektet genom visningsnamn för PivotField i PivotTable
type: docs
weight: 70
url: /sv/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**PivotTable.GetCellByDisplayName()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getcellbydisplayname)-metoden som du kan använda för att komma åt cellobjektet genom visningsnamnet för pivotfält. Denna metod är användbar när du vill markera eller formatera din pivotfältrubrik. Denna artikel förklarar hur man hämtar cellobjektet genom visningsnamnet för datafält och sedan tillämpar formatering på det.

{{% /alert %}}

## **Hämta Cell-objektet genom visningsnamn för PivotField i PivotTable**

Följande kod får åtkomst till den första pivottabellen i kalkylarket och sedan får cellen genom visningsnamn för det andra datafältet i pivottabellen. Det ändrar sedan fyllningsfärgen och teckensnittsfärgen på cellen till ljusblått och svart, respektive. Nedan visas skärmbilderna hur pivottabellen ser ut före och efter att koden har utförts.

|**Pivot-tabel - Före**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-GetCellByDisplayName-GetCellObjectByDisplayName.cs" >}}

|**Pivot-tabel - Efter**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
