---
title: フレームスクリプトとドキュメントプロパティのエクスポートを無効にする
type: docs
weight: 310
url: /ja/python-net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、ワークブックをHTMLに変換する際にフレームスクリプトやドキュメントプロパティもエクスポートします。バージョン8.6.0では、これらのエクスポートを任意で無効にするオプションが追加されました。HtmlSaveOptions.ExportFrameScriptsAndProperties プロパティを使用してください。

{{% /alert %}}

## **フレームスクリプトとドキュメントプロパティのエクスポートを無効にする**

以下のサンプルコードを使用すると、フレームスクリプトとドキュメントプロパティのエクスポートを無効にできます。ワークブックをHTMLに変換すると、出力ファイルにフレームスクリプトとドキュメントプロパティは含まれません。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HtmlExportFrameScripts-1.py" >}}
