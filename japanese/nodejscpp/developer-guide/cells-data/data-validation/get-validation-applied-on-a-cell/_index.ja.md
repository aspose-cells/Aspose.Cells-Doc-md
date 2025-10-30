---
title: セルに適用された検証を取得
type: docs
weight: 200
url: /ja/nodejs-cpp/get-validation-applied-on-a-cell/
description: この記事では、Node.jsからC++を介してセルに検証を適用する方法を紹介します。
keywords: Node.jsからC++を介してExcelのセル検証を適用する方法、Node.jsからC++を介してExcelのセルに検証を適用する方法、Node.jsからC++を介してExcelで検証を行う方法、Node.jsからC++を介してExcelのセル検証、Node.js via C++でExcelにセル検証を適用、Node.js via C++でExcelのセルに検証を適用、Node.js via C++でExcelのセル検証
---

{{% alert color="primary" %}}

Node.js用Aspose.Cellsを使用してセルに適用されている検証を取得できます。Aspose.Cellsはこの目的のために[**Cell.getValidation()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidation--)メソッドを提供しています。セルに検証が適用されていない場合はnullを返します。

同様に、[**Worksheet.validations.getValidationInCell(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/validationcollection/#getValidationInCell-number-number-)メソッドを使用して、行と列のインデックスを指定してセルに適用された検証を取得できます。

{{% /alert %}}

## Node.jsでセルに適用された検証を取得するコード例

以下のコード例は、検証をセルに取得する方法を示しています。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ReadingValidationPropertiesOfCell.js" >}}


## 関連記事

- [データの検証](/cells/ja/nodejs-cpp/data-validation/)
{{< app/cells/assistant language="nodejs-cpp" >}}
