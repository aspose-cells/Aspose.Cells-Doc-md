---
title: ソースワークシートからページ設定を宛先ワークシートにコピー
type: docs
weight: 80
url: /ja/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: この記事では、C# API または .NET ライブラリのサンプルコードを使用して、ソースワークシートから宛先ワークシートへのページ設定の設定をコピーする方法について説明します。
keywords: c# でページ設定の設定をコピー、c# でページ設定の設定をターゲットワークシートにコピー
---

## **可能な使用シナリオ**

新しいシートをワークブックに追加すると、デフォルトの*ページ設定の設定*が含まれます。時々、ユーザーが要件に応じてワークシートのページ設定を転送する必要があります。この場合、ページ設定は自動ではありません。Aspose.Cells API を使用して、1 つのワークシートから別のワークシートにページ設定の設定 ([**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) をコピーする方法について説明します。

## **ソースワークシートからページ設定を宛先ワークシートにコピー**

次のサンプルコードでは、1 つのワークシートから別のワークシートにページ設定の設定をコピーする方法を示しています。参照として、次のサンプルコードとそのコンソール出力をご覧ください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

## **コンソール出力**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
