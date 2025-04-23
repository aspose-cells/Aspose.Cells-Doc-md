---
title: Få validering som tillämpats på en cell
type: docs
weight: 200
url: /sv/net/get-validation-applied-on-a-cell/
description: Den här artikeln visar hur man tillämpar validering på en cell med C#
keywords: tillämpa cellvalidering i excel med c#, tillämpa validering på en cell i excel med c#, tillämpa validering i excel med c#, cellvalidering i excel med c#, c# tillämpa cellvalidering i excel, c# tillämpa validering på en cell i excel, c# cellvalidering i excel, c# cellvalidering
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att få valideringen som tillämpas på en cell. Aspose.Cells tillhandahåller [**Cell.GetValidation()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidation) metoden för detta ändamål. Om det inte finns någon validering som tillämpas på cellen returneras null.

På liknande sätt kan du använda metod [**Worksheet.Validations.GetValidationInCell**](https://reference.aspose.com/cells/net/aspose.cells/validationcollection/methods/getvalidationincell) för att få validering som har tillämpats på en cell genom att ange dess rad- och kolumnindex.

{{% /alert %}}

## C# kod för att få valideringen som används på en cell

Nedan följer ett kodexempel som visar hur du får validering som har tillämpats på en cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetValidationAppliedOnCell-GetValidationAppliedOnCell.cs" >}}

## Relaterade artiklar

- [Data validering](/cells/sv/net/data-validation/)
{{< app/cells/assistant language="csharp" >}}
