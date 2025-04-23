---
title: 書式設定ありおよびなしでセル文字列の値を取得
type: docs
weight: 240
url: /ja/nodejs-cpp/get-cell-string-value-with-and-without-formatting/
description: セル文字列の値をフォーマットなしとありの両方で取得する方法について、Aspose.Cells for Node.js via C++ APIを通じて学びます。
keywords: フォーマットあり／なしのセルの文字列値をNode.jsとC++を通じて取得します。
---

{{% alert color="primary" %}}

Aspose.Cellsは、セルの文字列値をフォーマットの有無にかかわらず取得できる[**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--)メソッドを提供します。例えば、値0.012345のセルを小数点以下2桁にフォーマットすると、Excelでは0.01と表示されます。[**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--)メソッドを用いて、0.01と0.012345の両方の値を取得できます。これは以下の列挙された値を持つ[**CellValueFormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/cellvalueformatstrategy/)型のパラメータが必要です。

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

以下のサンプルコードは[**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--)メソッドの使用例を説明しています。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-GetCellStringWithOrWithoutFormatting.js" >}}

