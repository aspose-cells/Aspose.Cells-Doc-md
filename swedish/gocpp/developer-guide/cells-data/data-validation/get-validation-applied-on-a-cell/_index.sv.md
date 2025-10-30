---
title: Hämta validering tillämpad på en cell med Golang via C++
linktitle: Få validering som tillämpats på en cell
type: docs
weight: 200
url: /sv/go-cpp/get-validation-applied-on-a-cell/
description: Denna artikel visar hur man tillämpar validering på en cell med Golang via C++.
keywords: tillämpa cellvalidering i Excel med C++, tillämpa validering på en cell i Excel med C++, tillämpa validering i Excel med C++, cellvalidering i Excel med C++, C++ tillämpning av cellvalidering i Excel, C++ tillämpning av validering på en cell i Excel, C++ cellvalidering i Excel, C++ cellvalidering
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att få valideringen som tillämpas på en cell. Aspose.Cells tillhandahåller [**Cell::GetValidation()**](https://reference.aspose.com/cells/go-cpp/cell/getvalidation/) metoden för detta ändamål. Om det inte finns någon validering som tillämpas på cellen returneras null.

På liknande sätt kan du använda metod [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/go-cpp/validationcollection/getvalidationincell/) för att få validering som har tillämpats på en cell genom att ange dess rad- och kolumnindex.

{{% /alert %}}

## C++-kod för att hämta validering tillämpad på en cell

Nedan visas exempel på kod som visar hur du hämtar validering som är tillämpad på en cell.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetValidationAppliedOnACell.go" >}}
## Relaterade artiklar

- [Data validering](/cells/sv/cpp/data-validation/)
