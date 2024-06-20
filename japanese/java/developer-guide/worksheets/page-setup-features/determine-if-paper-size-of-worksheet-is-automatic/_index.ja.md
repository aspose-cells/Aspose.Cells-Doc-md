---
title: ワークシートの用紙サイズが自動かどうかを判定する
type: docs
weight: 20
url: /ja/java/determine-if-paper-size-of-worksheet-is-automatic/
---

## **可能な使用シナリオ**

ワークシートの用紙サイズはほとんど自動です。自動の場合、*レター*として設定されることがよくあります。ユーザーがワークシートの用紙サイズを自分の要件に合わせて設定することもあります。この場合、用紙サイズは自動ではありません。[**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize) メソッドを使用して、ワークシートの用紙サイズが自動かどうかを判断することができます。

## **ワークシートの用紙サイズが自動かどうかを判断する**

以下のサンプルコードは、次の2つのExcelファイルをロードし

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

その最初のワークシートの用紙サイズが自動かどうかを確認します。Microsoft Excelでは、このスクリーンショットに示すように、ページ設定ウィンドウで用紙サイズが自動かどうかを確認できます。

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **コンソール出力**

上記のサンプルコードを指定されたサンプルExcelファイルで実行したときのコンソール出力は次の通りです。

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
