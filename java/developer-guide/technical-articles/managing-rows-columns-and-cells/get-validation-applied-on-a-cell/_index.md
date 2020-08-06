---
title: Get Validation Applied on a Cell
type: docs
weight: 80
url: /java/get-validation-applied-on-a-cell/
---

{{% alert color="primary" %}} 

You can use Aspose.Cells API to get the validation applied to any cell. Aspose.Cells provides the [Cell.getValidation](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#getValidation\(\)) method for this purpose. If there is no validation on the cell, it returns null. Similarly, you can use the [Worksheet.getValidations().getValidationInCell(int row, int column)](https://apireference.aspose.com/java/cells/com.aspose.cells/validationcollection#getValidationInCell\(int,%20int\)) method to acquire the validation applied to a cell by providing its row and column indices.

{{% /alert %}} 

The following snapshot shows the sample Microsoft Excel file used in the sample code below. Cell **C1** has **decimal validation** applied and can only take values **between 10 and 20**.

**A cell with validation** 

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

The sample code below gets the validation applied to C1 and reads its various properties.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}


Here is the console output from the sample code executed with the sample file shown in the snapshot above.

{{< highlight java >}}

 Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}
