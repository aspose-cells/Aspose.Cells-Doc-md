---
title: Få validering som tillämpats på en cell
type: docs
weight: 200
url: /sv/nodejs-cpp/get-validation-applied-on-a-cell/
description: Denna artikel visar hur man tillämpar validering på en cell med Node.js via C++.
keywords: tillämpa cellvalidering i Excel med Node.js via C++, tillämpa validering på en cell i Excel med Node.js via C++, tillämpa validering i Excel med Node.js via C++, cellvalidering i Excel med Node.js via C++, Node.js via C++ tillämpa cellvalidering i Excel, Node.js via C++ tillämpa validering på en cell i Excel, Node.js via C++ cellvalidering i Excel
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för Node.js för att hämta valideringen som tillämpats på en cell. Aspose.Cells tillhandahåller metoden [**Cell.getValidation()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidation--) för detta ändamål. Om ingen validering tillämpats på cellen returneras null.

På liknande sätt kan du använda metod [**Worksheet.validations.getValidationInCell(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/validationcollection/#getValidationInCell-number-number-) för att få validering som har tillämpats på en cell genom att ange dess rad- och kolumnindex.

{{% /alert %}}

## Node.js kod för att hämta valideringen som är tillämpad på en cell

Nedan visas exempel på kod som visar hur du hämtar validering som är tillämpad på en cell.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ReadingValidationPropertiesOfCell.js" >}}


## Relaterade artiklar

- [Data validering](/cells/sv/nodejs-cpp/data-validation/)
