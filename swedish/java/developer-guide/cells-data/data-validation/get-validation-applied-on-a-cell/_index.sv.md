---
title: Få validering tillämpad på en Cell
type: docs
weight: 80
url: /sv/java/get-validation-applied-on-a-cell/
description: Den här artikeln visar hur du tillämpar validering på en Cell med Java
keywords: apply cell validation in excel with java, apply validation on a cell in excel with java, apply validation in excel with java, cell validation in excel with java, java apply cell validation in excel, java apply validation on a cell in excel, java cell validation in excel, java cell validation
---
{{% alert color="primary" %}}

 Du kan använda Aspose.Cells API för att få valideringen tillämpad på valfri cell. Aspose.Cells tillhandahåller[**Cell.getValidation**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation() ) metod för detta ändamål. Om det inte finns någon validering på cellen, returnerar den null. På samma sätt kan du använda[**Worksheet.getValidations().getValidationInCell(int rad, int kolumn)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) metod för att förvärva valideringen som tillämpas på en cell genom att tillhandahålla dess rad- och kolumnindex.

{{% /alert %}}

 Följande ögonblicksbild visar exemplet Microsoft Excel-fil som används i exempelkoden nedan. Cell**C1** har**decimal validering** tillämpas och kan bara ta värden**mellan 10 och 20**.

**En cell med validering**

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

Exempelkoden nedan får valideringen applicerad på C1 och läser dess olika egenskaper.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

Här är konsolutgången från exempelkoden som körs med exempelfilen som visas i ögonblicksbilden ovan.

{{< highlight "java" >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## relaterade artiklar

- [Datavalidering](/cells/sv/java/data-validation/)
