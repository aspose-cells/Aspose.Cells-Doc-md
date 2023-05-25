---
title: ワークシート内の空白の行と列を削除する
type: docs
weight: 300
url: /ja/net/delete-blank-rows-and-columns-in-a-worksheet/
---
{{% alert color="primary" %}}

ワークシートからすべての空白の行と列を削除することができます。これは、たとえば、Microsoft Excel ファイルから PDF ファイルを生成し、データまたは関連オブジェクトを含む行と列のみを変換したい場合に便利です。

空の行と列を削除するには、次の Aspose.Cells メソッドを使用します。

1. 空白行を削除するには、[**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows)方法。削除される空白行については、次のことが必要なだけではないことに注意してください。[**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) true である必要がありますが、それらの行のセルに対して定義された表示可能なコメントや、範囲が交差するピボット テーブルがあってはなりません。
1. 空白の列を削除するには、[**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns)方法。

{{% /alert %}}

##  C# 空白行を削除するコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

## C# 空白列を削除するコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
