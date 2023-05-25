---
title: ページ設定設定をソース ワークシートから宛先ワークシートにコピーする
type: docs
weight: 80
url: /ja/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: この記事では、C# API または .NET ライブラリ サンプル コードを使用して、ページ設定設定をソース ワークシートからターゲット ワークシートにプログラム的にコピーする方法について説明します。
keywords: copy page setup settings c#, copy page setup settings to target worksheet c#
---
##  **考えられる使用シナリオ**

新しいシートをワークブックに追加すると、そのシートにはデフォルトの *ページ設定設定* が含まれます。設定を転送する必要がある場合があります ([**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)あるワークシートから別のワークシートへ。このドキュメントでは、Aspose.Cells API を使用して、あるワークシートから別のワークシートにページ設定設定をコピーする方法について説明します。

##  **ページ設定設定をソース ワークシートから宛先ワークシートにコピーする**

次のサンプル コードは、コピー方法を示しています。*ページ設定の設定*あるワークシートから別のワークシートへ[**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy)方法。参考として、次のサンプル コードとそのコンソール出力を参照してください。

##  **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

##  **コンソール出力**

{{< highlight "java" >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
