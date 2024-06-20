---
title: ワークシート内の空白の行と列を削除する
type: docs
weight: 300
url: /ja/python-net/delete-blank-rows-and-columns-in-a-worksheet/
description: Aspose.Cells for Python via .NET ライブラリを使用して、ワークシート内の空白行と列を削除する方法について説明します。
keywords: Python Excel ライブラリ、Python 空白行の削除、Python 空白列の削除、Python 空白行と列の削除、Python 空白行および列の削除
---

{{% alert color="primary" %}}

ワークシートからすべての空白の行と列を削除することが可能です。たとえば、Microsoft ExcelファイルからPDFファイルを生成し、データや関連オブジェクトが含まれる行と列のみを変換したい場合に便利です。

空の行と列を削除するために以下のAspose.Cellsのメソッドを使用します:

1. 空白の行を削除するには、[**Cells.delete_blank_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_rows)メソッドを使用します。削除される空白の行については、[**Row.is_blank**](https://reference.aspose.com/cells/python-net/aspose.cells/row/is_blank/)がtrueであるだけでなく、それらの行のいかなるセルにも見えるコメントが定義されていないこと、そしてそれらと交差するピボットテーブルがないことも必要です。
1. 空白の列を削除するには、[**Cells.delete_blank_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_columns)メソッドを使用します。

{{% /alert %}}

## 空白の行を削除するためのC#コード

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankRows-1.py" >}}

## 空白の列を削除するためのC#コード

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankColumns-1.py" >}}
