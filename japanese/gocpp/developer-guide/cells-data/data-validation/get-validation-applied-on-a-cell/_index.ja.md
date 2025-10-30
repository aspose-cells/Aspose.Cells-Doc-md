---
title: GolangをC++経由でセルに適用された検証を取得
linktitle: セルに適用された検証を取得
type: docs
weight: 200
url: /ja/go-cpp/get-validation-applied-on-a-cell/
description: この記事は、C++を使用したGolangでのセルの検証の適用方法を示しています。
keywords: C++を使用してExcelにセル検証を適用、セルに検証を行う、C++でExcelのセル検証を適用、C++でExcelのセル検証、C++でExcelのセル検証を行う、C++でセルの検証をExcelに適用、C++でExcelのセル検証を行う
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、セルに適用された検証を取得できます。Aspose.Cellsはこの目的のために[**Cell::GetValidation()**](https://reference.aspose.com/cells/go-cpp/cell/getvalidation/)メソッドを提供します。セルに検証が適用されていない場合、nullを返します。

同様に、[**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/go-cpp/validationcollection/getvalidationincell/)メソッドを使用して、行と列のインデックスを指定してセルに適用された検証を取得できます。

{{% /alert %}}

## C++でセルに適用された検証を取得するコード例

以下のコード例は、検証をセルに取得する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetValidationAppliedOnACell.go" >}}
## 関連記事

- [データの検証](/cells/ja/cpp/data-validation/)
