---
title: ワークシートの用紙サイズが自動かどうかを判断する
type: docs
weight: 90
url: /ja/net/determine-if-paper-size-of-worksheet-is-automatic/
---
## **考えられる使用シナリオ**

ほとんどの場合、ワークシートの用紙サイズは自動です。自動の場合は、次のように設定されることがよくあります*手紙*.ユーザーは、必要に応じてワークシートの用紙サイズを設定することがあります。この場合、用紙サイズは自動ではありません。ワークシートの用紙サイズが自動かどうかを確認するには、[**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize)財産。

## **ワークシートの用紙サイズが自動かどうかを判断する**

以下のサンプル コードは、次の 2 つの Excel ファイルを読み込みます。

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

最初のワークシートの用紙サイズが自動かどうかを調べます。 Microsoft Excel では、このスクリーンショットに示すように、[ページ設定] ウィンドウで用紙サイズが自動かどうかを確認できます。

![todo:画像_代替_文章](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

## **コンソール出力**

以下は、指定されたサンプル Excel ファイルで実行されたときの上記のサンプル コードのコンソール出力です。

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
