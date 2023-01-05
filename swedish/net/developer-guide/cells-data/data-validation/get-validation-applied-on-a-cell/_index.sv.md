---
title: Få validering tillämpad på en Cell
type: docs
weight: 200
url: /sv/net/get-validation-applied-on-a-cell/
description: Den här artikeln visar hur du tillämpar validering på en Cell med C#
keywords: apply cell validation in excel with c#, apply validation on a cell in excel with c#, apply validation in excel with c#, cell validation in excel with c#, c# apply cell validation in excel, c# apply validation on a cell in excel, c# cell validation in excel, c# cell validation
---
{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att få valideringen tillämpad på en cell. Aspose.Cells tillhandahåller[**Cell.GetValidation()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidation) metod för detta ändamål. Om ingen validering tillämpas på cellen, returnerar den null.

 På samma sätt kan du använda[**Worksheet.Validations.GetValidationInCell**](https://reference.aspose.com/cells/net/aspose.cells/validationcollection/methods/getvalidationincell) metod för att erhålla valideringen som tillämpas på en cell genom att tillhandahålla dess rad- och kolumnindex.

{{% /alert %}}

## C# kod för att få valideringen tillämpad på en Cell

Nedan kodexempel visar hur du får validering tillämpad på en cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetValidationAppliedOnCell-GetValidationAppliedOnCell.cs" >}}

## relaterade artiklar

- [Datavalidering](/cells/sv/net/data-validation/)
