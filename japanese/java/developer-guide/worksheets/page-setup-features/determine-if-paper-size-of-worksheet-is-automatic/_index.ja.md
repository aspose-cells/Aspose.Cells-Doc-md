---
title: ワークシートの用紙サイズが自動かどうかを判断する
type: docs
weight: 20
url: /ja/java/determine-if-paper-size-of-worksheet-is-automatic/
---
## **考えられる使用シナリオ**

ほとんどの場合、ワークシートの用紙サイズは自動です。自動の場合は、次のように設定されることがよくあります*手紙*.ユーザーは、必要に応じてワークシートの用紙サイズを設定することがあります。この場合、用紙サイズは自動ではありません。ワークシートの用紙サイズが自動かどうかを確認するには、[**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize)方法。

## **ワークシートの用紙サイズが自動かどうかを判断する**

以下のサンプル コードは、次の 2 つの Excel ファイルを読み込みます。

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

最初のワークシートの用紙サイズが自動かどうかを調べます。 Microsoft Excel では、このスクリーンショットに示すように、[ページ設定] ウィンドウで用紙サイズが自動かどうかを確認できます。

![todo:画像_代替_文章](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **コンソール出力**

以下は、指定されたサンプル Excel ファイルで実行されたときの上記のサンプル コードのコンソール出力です。

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
