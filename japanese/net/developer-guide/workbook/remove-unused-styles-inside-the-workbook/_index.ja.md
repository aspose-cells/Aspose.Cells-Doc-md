---
title: ワークブック内の未使用のスタイルを削除する
type: docs
weight: 340
url: /ja/net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Excelファイル内の未使用のスタイルはスペースを取るだけでなく、PDF、HTMLなどの異なる形式への変換時にパフォーマンスの問題を引き起こします。Aspose.Cellsは、ワークブック内のすべての未使用スタイルを削除するための [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) を提供しています。

{{% /alert %}}

次のコードは、[**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) の使用法を説明しています。コードは、提供されたリンクからダウンロードできる[テンプレートExcelファイル](5115520.xlsx)をロードします。このファイルには**AsposeStyle**という未使用のスタイルが含まれており、このスタイルおよびその他の未使用のスタイルは、コードの実行後に削除されます。

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}
