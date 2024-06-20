---
title: セルに適用された検証を取得
type: docs
weight: 80
url: /ja/java/get-validation-applied-on-a-cell/
description: この記事では、Javaでセルに検証を適用する方法について説明します。
keywords: JavaでExcelでセルの検証を適用し、JavaでExcelのセルに検証を適用し、JavaでExcelで検証を適用し、ExcelでのJavaでセルの検証、JavaでExcelでセルの検証を適用、JavaでExcelでセルに検証を適用し、JavaでExcelでセルの検証を適用、Javaでセルの検証
---

{{% alert color="primary" %}}

Aspose.Cells APIを使用して、任意のセルに適用された検証を取得できます。 Aspose.Cellsはこの目的のために[**Cell.getValidation()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation--)メソッドを提供します。セルに検証がない場合はnullを返します。同様に、行と列のインデックスを指定してセルに適用された検証を取得するために[**Worksheet.getValidations().getValidationInCell(int row, int column)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int))メソッドを使用できます。

{{% /alert %}}

以下のスナップショットは、下記のサンプルコードで使用されるMicrosoft Excelファイルの例を示しています。セル** C1 **に** 10から20の間 **の値しか受け付けない**10進数の検証**が適用されています。

**検証のあるセル**

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

以下のサンプルコードは、C1に適用された検証を取得し、そのさまざまなプロパティを読み取ります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

以下は、スナップショットで示されているサンプルファイルで実行されたサンプルコードのコンソール出力です。

{{< highlight java >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## 関連記事

- [データの検証](/cells/ja/java/data-validation/)
