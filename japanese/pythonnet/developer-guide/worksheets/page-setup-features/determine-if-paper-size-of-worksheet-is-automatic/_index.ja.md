---
title: ワークシートの用紙サイズが自動かどうかを判定する
type: docs
weight: 90
url: /ja/python-net/determine-if-paper-size-of-worksheet-is-automatic/
description: この記事では、Aspose.Cells for Python via .NETのサンプルコードを使用して、ワークシートの用紙サイズが自動かどうかをプログラム的に判断する方法を説明します。
keywords: Python Excelライブラリを使って、ワークシートの用紙サイズが自動かどうかを判断します。
---

## **可能な使用シナリオ**

ワークシートの用紙サイズは大抵自動的です。自動的な場合、*レター* として設定されることがしばしばあります。時々、ユーザーは要件に応じてワークシートの用紙サイズを設定します。この場合、用紙サイズは自動的ではありません。ワークシートの用紙サイズが自動的かどうかは、[**Worksheet.page_setup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_automatic_paper_size/) プロパティを使用して確認できます。

## **ワークシートの用紙サイズが自動かどうかを判断する**

以下のサンプルコードは、次の2つのExcelファイルをロードし

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

その最初のワークシートの用紙サイズが自動かどうかを確認します。Microsoft Excelでは、このスクリーンショットに示すように、ページ設定ウィンドウで用紙サイズが自動かどうかを確認できます。

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.py" >}}

## **コンソール出力**

上記のサンプルコードを指定されたサンプルExcelファイルで実行したときのコンソール出力は次の通りです。

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
