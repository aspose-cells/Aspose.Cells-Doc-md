---
title: フレームスクリプトとドキュメントプロパティのエクスポートを無効にする
type: docs
weight: 310
url: /ja/net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cellsは、ワークブックをHTMLに変換する際にフレームスクリプトとドキュメントプロパティをエクスポートします。Aspose.Cells for .NETの8.6.0バージョンでは、フレームスクリプトとドキュメントプロパティのエクスポートをオプションで無効にすることができるようになりました。HtmlSaveOptions.ExportFrameScriptsAndProperties プロパティを使用して、エクスポートを無効にしてください。

{{% /alert %}}

## **フレームスクリプトとドキュメントプロパティのエクスポートを無効にする**

以下のサンプルコードを使用すると、フレームスクリプトとドキュメントプロパティのエクスポートを無効にできます。ワークブックをHTMLに変換すると、出力ファイルにフレームスクリプトとドキュメントプロパティは含まれません。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HtmlExportFrameScripts-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
