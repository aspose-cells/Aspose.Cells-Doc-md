---
title: ワークシートの用紙サイズが自動かどうかを判定する
type: docs
weight: 90
url: /ja/net/determine-if-paper-size-of-worksheet-is-automatic/
description: この記事では、C# API または .NET ライブラリのサンプルコードを使用して、ワークシートの用紙サイズが自動的かどうかをプログラムで判定する方法について説明します。
keywords: c# でワークシートの用紙サイズが自動的かどうかを判定
---

## **可能な使用シナリオ**

ワークシートの用紙サイズは大抵自動的です。自動的な場合、*レター* として設定されることがしばしばあります。時々、ユーザーは要件に応じてワークシートの用紙サイズを設定します。この場合、用紙サイズは自動的ではありません。ワークシートの用紙サイズが自動的かどうかは、[**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize) プロパティを使用して確認できます。

## **ワークシートの用紙サイズが自動かどうかを判断する**

以下のサンプルコードは、次の2つのExcelファイルをロードし

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

その最初のワークシートの用紙サイズが自動かどうかを確認します。Microsoft Excelでは、このスクリーンショットに示すように、ページ設定ウィンドウで用紙サイズが自動かどうかを確認できます。

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

## **コンソール出力**

上記のサンプルコードを指定されたサンプルExcelファイルで実行したときのコンソール出力は次の通りです。

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
