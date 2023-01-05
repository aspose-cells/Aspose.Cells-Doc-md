---
title: Cell に検証を適用する
type: docs
weight: 80
url: /ja/java/get-validation-applied-on-a-cell/
description: この記事では、Java を使用して Cell に検証を適用する方法を示します。
keywords: apply cell validation in excel with java, apply validation on a cell in excel with java, apply validation in excel with java, cell validation in excel with java, java apply cell validation in excel, java apply validation on a cell in excel, java cell validation in excel, java cell validation
---
{{% alert color="primary" %}}

 Aspose.Cells API を使用して、検証を任意のセルに適用できます。 Aspose.Cells は[**Cell.getValidation**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation() この目的のためのメソッド。セルに検証がない場合は、null を返します。同様に、[**Worksheet.getValidations().getValidationInCell(int 行、int 列)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) 行と列のインデックスを提供することによって、セルに適用される検証を取得するメソッド。

{{% /alert %}}

次のスナップショットは、以下のサンプル コードで使用されるサンプル Microsoft Excel ファイルを示しています。 Cell**C1**もっている**小数の検証**適用され、値のみを取ることができます**10から20の間**.

**検証のあるセル**

![todo:画像_代替_文章](get-validation-applied-on-a-cell_1.png)

以下のサンプル コードは、C1 に適用される検証を取得し、そのさまざまなプロパティを読み取ります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

上記のスナップショットに示されているサンプル ファイルで実行されたサンプル コードからのコンソール出力を次に示します。

{{< highlight "java" >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## 関連記事

- [データ検証](/cells/ja/java/data-validation/)
