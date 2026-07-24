---
title: Hämta Cell objektet genom visningsnamn för PivotField i PivotTable
type: docs
weight: 70
url: /sv/nodejs-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Hur man får Cell objektet genom DisplayName för PivotField i PivotTable med Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js Bibliotek, Hämta Cell objektet genom DisplayName för PivotField i PivotTable med Aspose.Cells for Node.js via C++ Excel bibliotek.
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ tillhandahåller [**PivotTable.getCellByDisplayName(string)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getCellByDisplayName-string-) metoden som du kan använda för att komma åt cell-objektet via displaynamnet för pivottabelfältet. Denna metod är användbar när du vill markera eller formatera rubriken för pivottabelfältet. Denna artikel förklarar hur man hämtar cell-objektet via displaynamnet för dataramen och sedan tillämpar formatering på den.

{{% /alert %}}

## **Hur man får cellobjektet genom visningsnamn för PivotField av PivotTable**

Följande kod får åtkomst till den första pivottabellen i kalkylarket och sedan får cellen genom visningsnamn för det andra datafältet i pivottabellen. Det ändrar sedan fyllningsfärgen och teckensnittsfärgen på cellen till ljusblått och svart, respektive. Nedan visas skärmbilderna hur pivottabellen ser ut före och efter att koden har utförts.

|**Pivot-tabel - Före**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GetCellByDisplayName-GetCellObjectByDisplayName.js" >}}

|**Pivot-tabel - Efter**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="nodejs-cpp" >}}
