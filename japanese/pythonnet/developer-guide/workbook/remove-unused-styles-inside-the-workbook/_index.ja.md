---
title: ワークブック内の未使用のスタイルを削除する
type: docs
weight: 340
url: /ja/python-net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Excelファイル内の未使用のスタイルは、スペースを取るだけでなく、PDFやHTMLなどに変換する際にパフォーマンスの問題を引き起こすこともあります。Aspose.Cells for Python via .NETは、ワークブック内のすべての未使用スタイルを削除するための[**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles)を提供します。

{{% /alert %}}

次のコードは、[**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles) の使用法を説明しています。コードは、提供されたリンクからダウンロードできる[テンプレートExcelファイル](5115520.xlsx)をロードします。このファイルには**AsposeStyle**という未使用のスタイルが含まれており、このスタイルおよびその他の未使用のスタイルは、コードの実行後に削除されます。

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-RemoveUnusedStyles-1.py" >}}

