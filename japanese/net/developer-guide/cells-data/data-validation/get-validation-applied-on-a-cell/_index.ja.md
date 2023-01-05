---
title: Cell に検証を適用する
type: docs
weight: 200
url: /ja/net/get-validation-applied-on-a-cell/
description: この記事では、C# を使用して Cell に検証を適用する方法を示します。
keywords: apply cell validation in excel with c#, apply validation on a cell in excel with c#, apply validation in excel with c#, cell validation in excel with c#, c# apply cell validation in excel, c# apply validation on a cell in excel, c# cell validation in excel, c# cell validation
---
{{% alert color="primary" %}}

Aspose.Cells を使用して、セルに適用される検証を取得できます。 Aspose.Cells は[**Cell.GetValidation()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidation)この目的のためのメソッド。セルに検証が適用されていない場合は、null が返されます。

同様に、使用できます[**Worksheet.Validations.GetValidationInCell**](https://reference.aspose.com/cells/net/aspose.cells/validationcollection/methods/getvalidationincell)行と列のインデックスを提供することにより、セルに適用される検証を取得するメソッド。

{{% /alert %}}

## Cell に適用された検証を取得するための C# コード

以下のコード サンプルは、セルに検証を適用する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetValidationAppliedOnCell-GetValidationAppliedOnCell.cs" >}}

## 関連記事

- [データ検証](/cells/ja/net/data-validation/)
