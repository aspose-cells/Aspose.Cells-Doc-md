---
title: ワークシートの用紙サイズが自動かどうかを確認する
type: docs
weight: 90
url: /ja/net/determine-if-paper-size-of-worksheet-is-automatic/
description: この記事では、C# API または .NET ライブラリ サンプル コードを使用して、ワークシートの用紙サイズがプログラム的に自動かどうかを判断する方法について説明します。
keywords: determine if paper size of worksheet automatic c#
---
##  **考えられる使用シナリオ**

ほとんどの場合、ワークシートの用紙サイズは自動で設定されます。自動の場合は*文字*に設定されることが多いです。場合によっては、ユーザーが要件に応じてワークシートの用紙サイズを設定することがあります。この場合、用紙サイズは自動設定されません。ワークシートの用紙サイズが自動かどうかは、[**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize)財産。

##  **ワークシートの用紙サイズが自動かどうかを確認する**

以下のサンプル コードは、次の 2 つの Excel ファイルを読み込みます。

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [SamplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

最初のワークシートの用紙サイズが自動かどうかを確認します。 Microsoft Excel では、このスクリーンショットに示すように、ページ設定ウィンドウで用紙サイズが自動かどうかを確認できます。

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

##  **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

##  **コンソール出力**

以下は、指定されたサンプル Excel ファイルで実行された場合の上記のサンプル コードのコンソール出力です。

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
