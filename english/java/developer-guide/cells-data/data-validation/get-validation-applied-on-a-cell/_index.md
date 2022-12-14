---
title: Get Validation Applied on a Cell
type: docs
weight: 80
url: /java/get-validation-applied-on-a-cell/
description: This article show how to apply validation on a Cell with Java
keywords: apply cell validation in excel with java, apply validation on a cell in excel with java, apply validation in excel with java, cell validation in excel with java, java apply cell validation in excel, java apply validation on a cell in excel, java cell validation in excel, java cell validation
---

{{% alert color="primary" %}}

You can use Aspose.Cells API to get the validation applied to any cell. Aspose.Cells provides the [**Cell.getValidation**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation()) method for this purpose. If there is no validation on the cell, it returns null. Similarly, you can use the [**Worksheet.getValidations().getValidationInCell(int row, int column)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) method to acquire the validation applied to a cell by providing its row and column indices.

{{% /alert %}}

The following snapshot shows the sample Microsoft Excel file used in the sample code below. Cell **C1** has **decimal validation** applied and can only take values **between 10 and 20**.

**A cell with validation**

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

The sample code below gets the validation applied to C1 and reads its various properties.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

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

## Related Articles

- [Data Validation](/cells/java/data-validation/)
