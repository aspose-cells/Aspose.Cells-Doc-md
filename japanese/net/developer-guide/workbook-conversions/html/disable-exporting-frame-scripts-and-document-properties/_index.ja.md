---
title: フレーム スクリプトとドキュメント プロパティのエクスポートを無効にする
type: docs
weight: 310
url: /ja/net/disable-exporting-frame-scripts-and-document-properties/
---
{{% alert color="primary" %}}

Aspose.Cells は、ワークブックを HTML に変換する際に、フレーム スクリプトとドキュメント プロパティをエクスポートします。 Aspose.Cells for .NET の 8.6.0 バージョンでは、オプションでフレーム スクリプトとドキュメント プロパティのエクスポートを無効にできるオプションが導入されています。エクスポートを無効にするには、HtmlSaveOptions.ExportFrameScriptsAndProperties プロパティを使用してください。

{{% /alert %}}

## **フレーム スクリプトとドキュメント プロパティのエクスポートを無効にする**

次のサンプル コードでは、フレーム スクリプトとドキュメント プロパティのエクスポートを無効にできます。ワークブックを HTML に変換すると、出力ファイルにはフレーム スクリプトとドキュメント プロパティが含まれなくなります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HtmlExportFrameScripts-1.cs" >}}
