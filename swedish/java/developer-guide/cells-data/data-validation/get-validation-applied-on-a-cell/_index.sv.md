---
title: Få validering som tillämpats på en cell
type: docs
weight: 80
url: /sv/java/get-validation-applied-on-a-cell/
description: Denna artikel visar hur man tillämpar validering på en cell med Java
keywords: tillämpa cellvalidering i excel med java, tillämpa validering på en cell i excel med java, tillämpa validering i excel med java, cellvalidering i excel med java, java tillämpa cellvalidering i excel, java tillämpa validering på en cell i excel, java cellvalidering i excel, java cellvalidering
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells API för att få valideringen som tillämpas på vilken cell som helst. Aspose.Cells tillhandahåller [**Cell.getValidation()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation--) metoden för detta ändamål. Om det inte finns någon validering på cellen returnerar den null. På samma sätt kan du använda [**Worksheet.getValidations().getValidationInCell(int row, int column)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) metoden för att erhålla valideringen som tillämpas på en cell genom att ange dess rad- och kolumnindex.

{{% /alert %}}

Följande ögonblicksbild visar den prov Microsoft Excel-fil som används i provkoden nedan. Cell **C1** har **decimal validering** tillämpad och kan endast ta värden **mellan 10 och 20**.

**En cell med validering**

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

Prov koden nedan hämtar valideringen som tillämpats på C1 och läser dess olika egenskaper.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

Här är konsoloutputen från provkoden utförd med den provfil som visas i ögonblicksbilden ovan.

{{< highlight java >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## Relaterade artiklar

- [Data validering](/cells/sv/java/data-validation/)
