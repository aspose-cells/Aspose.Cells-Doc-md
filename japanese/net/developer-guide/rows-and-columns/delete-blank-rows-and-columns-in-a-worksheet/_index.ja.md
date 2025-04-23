---
title: ワークシート内の空白の行と列を削除する
type: docs
weight: 300
url: /ja/net/delete-blank-rows-and-columns-in-a-worksheet/
---

{{% alert color="primary" %}}

ワークシートからすべての空白の行と列を削除することが可能です。たとえば、Microsoft ExcelファイルからPDFファイルを生成し、データや関連オブジェクトが含まれる行と列のみを変換したい場合に便利です。

空の行と列を削除するために以下のAspose.Cellsのメソッドを使用します:

1. 空白の行を削除するには、[**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows)メソッドを使用します。削除される空白の行については、[**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/)がtrueであるだけでなく、それらの行のいかなるセルにも見えるコメントが定義されていないこと、そしてそれらと交差するピボットテーブルがないことも必要です。
1. 空白の列を削除するには、[**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns)メソッドを使用します。

{{% /alert %}}

## 空白の行を削除するためのC#コード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

## 空白の列を削除するためのC#コード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
